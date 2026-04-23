# SPDX 3 to Diagram

Generate a graphical diagram (SVG + 8K PNG) from an SPDX 3.0 JSON file.

## Prerequisites

Install once:
```bash
brew install plantuml librsvg

# Clone and patch spdx3ToGraph
git clone https://github.com/maxhbr/spdx3ToGraph.git /tmp/spdx3ToGraph
# Patch to skip unknown properties instead of crashing:
sed -i '' 's/raise KeyError(f"Unknown property .*/import logging; logging.warning(f"Skipping unknown property '"'"'{key}'"'"'")/' \
  /tmp/spdx3ToGraph/spdx3_to_graph/spdx30.py
brew install graphviz
cd /tmp/spdx3ToGraph && \
  CFLAGS="-I$(brew --prefix graphviz)/include" \
  LDFLAGS="-L$(brew --prefix graphviz)/lib" \
  poetry install
```

## Pipeline

For each SPDX 3.0 JSON file `INPUT.spdx3.json`:

### Step 1 — Generate raw PlantUML
```bash
cd /tmp/spdx3ToGraph
CFLAGS="-I$(brew --prefix graphviz)/include" \
LDFLAGS="-L$(brew --prefix graphviz)/lib" \
poetry run python -m spdx3_to_graph INPUT.spdx3.json
# Output: INPUT.spdx3.json.puml (next to input file)
```

### Step 2 — Simplify PlantUML
```bash
python3 tools/simplify_puml.py INPUT.spdx3.json.puml OUTPUT.simplified.puml
```

The `tools/simplify_puml.py` script:
- Removes `CreationInfo` and `Hash` objects (visual clutter)
- Limits `DictionaryEntry` objects to **1 per source+property** (keep just one metric/hyperparameter to illustrate the pattern)
- Drops verbose text properties (`description`, `summary`, `/AI/informationAboutApplication`, `/AI/limitation`, etc.)
- Strips full SPDX RDF vocabulary URLs (e.g. `https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/` → empty, leaving just `contains`)
- Strips spdxdocs namespace prefix from element IDs
- Removes UUID suffixes from IDs
- Truncates quoted strings to 45 chars
- Adds `left to right direction` and skin parameters for readability

### Step 3 — Render to SVG
```bash
plantuml -tsvg OUTPUT.simplified.puml
# Output: OUTPUT.simplified.svg
```

### Step 4 — Convert SVG to high-res PNG (2-step for quality)
```bash
# SVG → PNG at 7680px wide; height follows the diagram's natural aspect ratio.
# Do NOT specify -h: combining -w and -h without -a distorts; with -a it shrinks
# diagrams whose natural height exceeds 4320px (portrait layouts lose resolution).
rsvg-convert -w 7680 OUTPUT.simplified.svg -o EXAMPLE_DIR/exampleNN.spdx3.png
```

> Do NOT use `plantuml -tpng` directly — the resolution will be too low.
> Always go SVG → PNG via `rsvg-convert`.
> Do NOT add `-h`: it either distorts (without `-a`) or caps resolution for tall diagrams (with `-a`).
> The `left to right direction` directive in the PlantUML skinparams (set by
> `simplify_puml.py`) is the primary driver of horizontal layout — diagrams
> flow left-to-right, producing wide canvases naturally.
> Custom `.puml` files must also include `left to right direction`.

## For complex examples (many files or elements)

When an example has >30 elements or many `/Software/File` objects that make the
auto-generated layout unreadable, write a **custom PlantUML** file manually:

- Reference: `ai/example01/spdx3.0/simplehtr-example.spdx3.puml`
- Reference: `ai/example02/spdx3.0/sbom.spdx3.puml`

Custom PUMLs use the same skin parameters and `left to right direction`.
Keep only key elements and relationships; collapse file lists into packages where
possible. DictionaryEntry objects: keep at most 1–2 per property.

## Output locations

| Example | PNG path |
|---------|----------|
| `ai/example01` | `ai/example01/example01.spdx3.png` |
| `ai/example02` | `ai/example02/example02.spdx3.png` |
| `ai/exampleNN` | `ai/exampleNN/exampleNN.spdx3.png` |
| `dataset/exampleNN` | `dataset/exampleNN/exampleNN.spdx3.png` |

## Files to commit

- `*.spdx3.png` — final diagram images
- `tools/simplify_puml.py` — simplification script
- Custom `.puml` files (for examples written manually)

Do NOT commit `.json.puml` (auto-generated), `.simplified.puml`, or `.simplified.svg`.
