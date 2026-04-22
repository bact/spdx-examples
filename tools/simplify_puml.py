#!/usr/bin/env python3
"""
Post-process spdx3ToGraph PlantUML output:
  - Remove noisy helper objects (CreationInfo, Hash)
  - Limit DictionaryEntry objects to 1 per source+property (drop the rest)
  - Strip verbose property lines
  - Shorten URLs and IDs
  - Truncate long strings
  - Wrap in skinparams for readable diagrams
"""

import re
import sys
from collections import defaultdict

# Properties to drop entirely
DROPPED_PROPS = {
    "creationInfo",
    "specVersion",
    "software_copyrightText",
    "software_downloadLocation",
    "builtTime",
    "releaseTime",
    "description",
    "summary",
    "ai_informationAboutApplication",
    "ai_informationAboutTraining",
    "ai_limitation",
    "ai_modelDataPreprocessing",
    "ai_modelExplainability",
    "dataset_dataCollectionProcess",
    "dataset_dataPreprocessing",
    "dataset_datasetUpdateMechanism",
    "dataset_knownBias",
    "profileConformance",
    "comment",
}

# Object types to remove entirely (and all their edges/properties)
DROPPED_TYPES = {"CreationInfo", "Hash"}

# Keep at most this many DictionaryEntry objects per (source, property) pair
MAX_DICT_ENTRIES = 1

URL_REPLACEMENTS = [
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/ExternalIdentifierType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/PresenceType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/RelationshipType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/LifecycleScopeType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/ProfileIdentifierType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Core/HashAlgorithm/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Software/FileKindType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Software/SoftwarePurpose/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Software/SbomType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/AI/EnergyUnitType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/AI/SafetyRiskAssessmentType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Dataset/ConfidentialityLevelType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Dataset/DatasetAvailabilityType/", ""),
    (r"https://spdx\.org/rdf/3\.0\.[^/]*/terms/Dataset/DatasetType/", ""),
    (r"https://spdx\.org/spdxdocs/[^#\"'\n]*/Relationship/", ""),
    (r"https://spdx\.org/spdxdocs/[^#\"'\n]*#", ""),
    (r"https://spdx\.org/spdxdocs/[^\"'\n]*", lambda m: shorten_spdxdoc_id(m.group())),
    (r"https://spdx\.org/licenses/", ""),
    (r";charset=UTF-8", ""),
]

def shorten_spdxdoc_id(url):
    """Strip spdxdocs base URL and UUID suffix."""
    url = re.sub(r"-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", "", url)
    url = re.sub(r"^https://spdx\.org/spdxdocs/", "", url)
    return url

def shorten_urls(text):
    for pattern, repl in URL_REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    # Remove UUID patterns from remaining IDs
    text = re.sub(r"-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "", text)
    return text

def truncate_strings(text, max_len=45):
    """Truncate quoted string values longer than max_len chars."""
    def truncate_match(m):
        quote = m.group(1)
        content = m.group(2)
        if len(content) > max_len:
            return f'{quote}{content[:max_len]}...{quote}'
        return m.group(0)
    text = re.sub(r'(")((?:[^"\\]|\\.){' + str(max_len+1) + r',}?)(")', truncate_match, text)
    return text

def truncate_list_items(text, max_len=45):
    """Truncate items inside PlantUML list values."""
    def trunc(m):
        item = m.group(1)
        if len(item) > max_len:
            return f"'{item[:max_len]}...'"
        return m.group(0)
    return re.sub(r"'([^']{" + str(max_len+1) + r",}?)'", trunc, text)

SKINPARAMS = """
left to right direction
skinparam defaultFontSize 14
skinparam defaultFontName Arial
skinparam objectFontSize 14
skinparam objectHeaderFontSize 15
skinparam objectHeaderFontStyle bold
skinparam objectBorderColor #555555
skinparam objectBackgroundColor #FFFFF0
skinparam ArrowColor #333333
skinparam ArrowFontSize 12
skinparam packageBorderColor #888888
skinparam packageBackgroundColor #F8F8FF
skinparam dpi 96
"""

def simplify(puml_text):
    lines = puml_text.splitlines()

    # --- Pass 1: identify objects and their types ---
    obj_id_to_type = {}  # alias -> type string
    for line in lines:
        m = re.match(r'\s*object\s+"(?:(?:<b>.*?</b>|[^"\\]*)\\n)?(.*?)"\s+as\s+(\S+)', line)
        if m:
            type_str = m.group(1).strip()
            alias = m.group(2).strip()
            obj_id_to_type[alias] = type_str

    # Identify base dropped aliases (CreationInfo, Hash)
    dropped_aliases = {a for a, t in obj_id_to_type.items() if t in DROPPED_TYPES}

    # --- Pass 2: limit DictionaryEntry per (source, property) ---
    # Collect edges: SRC::PROP --> DST where DST is DictionaryEntry
    dict_edges = defaultdict(list)  # (src, prop) -> [dst aliases in order]
    for line in lines:
        m = re.match(r'\s*(\S+)::(\w+)\s+-->\s+(\S+)', line)
        if m:
            src, prop, dst = m.group(1), m.group(2), m.group(3)
            if obj_id_to_type.get(dst) == "DictionaryEntry":
                dict_edges[(src, prop)].append(dst)

    # Mark extras beyond MAX_DICT_ENTRIES as dropped
    for (src, prop), dsts in dict_edges.items():
        for dst in dsts[MAX_DICT_ENTRIES:]:
            dropped_aliases.add(dst)

    # --- Pass 3: filter lines ---
    result = []

    for line in lines:
        stripped = line.strip()

        # Handle @startuml / @enduml
        if stripped.startswith("@startuml"):
            title = re.sub(r"@startuml\s*", "", stripped).strip()
            result.append(f"@startuml {title}")
            result.append(SKINPARAMS)
            continue
        if stripped == "@enduml":
            result.append("@enduml")
            continue

        # Object declaration inside package block
        m = re.match(r'(\s*object\s+)"(.*?)"\s+as\s+(\S+)', line)
        if m:
            alias = m.group(3)
            if alias in dropped_aliases:
                continue
            label = m.group(2)
            label = shorten_urls(label)
            label = truncate_strings(label, max_len=40)
            result.append(f'{m.group(1)}"{label}" as {alias}')
            continue

        # Property line: ALIAS : key = value
        m_prop = re.match(r'\s*(\S+)\s+:\s+(\w+)\s+=\s+(.*)', line)
        if m_prop:
            alias = m_prop.group(1)
            prop = m_prop.group(2)
            val = m_prop.group(3)

            if alias in dropped_aliases:
                continue
            if prop in DROPPED_PROPS:
                continue
            if prop in ("spdxId", "simplelicensing_licenseListVersion", "name",
                        "software_packageVersion"):
                continue

            val = shorten_urls(val)
            val = truncate_strings(val)
            val = truncate_list_items(val)
            result.append(f"{m_prop.group(1)} : {prop} = {val}")
            continue

        # Edge line: ALIAS::prop --> ALIAS2 : label
        m_edge = re.match(r'\s*(\S+)::(\w+)\s+(-->|<--|<\.\.\.?|---?>)\s+(\S+)\s*(:.*)?', line)
        if m_edge:
            src = m_edge.group(1)
            prop = m_edge.group(2)
            dst = m_edge.group(4)

            if src in dropped_aliases or dst in dropped_aliases:
                continue
            if prop in DROPPED_PROPS:
                continue

            result.append(line)
            continue

        # Simple edge: ALIAS <-- ALIAS2::prop : label
        m_edge2 = re.match(r'\s*(\S+)\s+(<--|-->|<\.\.\.?)\s+(\S+)(?:::(\w+))?\s*(:.*)?', line)
        if m_edge2:
            src = m_edge2.group(1)
            dst = m_edge2.group(3)
            prop = m_edge2.group(4) or ""
            if src in dropped_aliases or dst in dropped_aliases:
                continue
            if prop in DROPPED_PROPS:
                continue
            result.append(line)
            continue

        # Package / closing brace / blank lines
        result.append(line)

    return "\n".join(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: simplify_puml.py <input.puml> [output.puml]")
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) > 2 else infile.replace(".puml", ".simplified.puml")
    with open(infile) as f:
        text = f.read()
    result = simplify(text)
    with open(outfile, "w") as f:
        f.write(result)
    print(f"Written: {outfile}")
