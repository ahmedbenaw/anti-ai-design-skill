#!/bin/bash
# Capture the mechanical evidence for one run directory, to disk, so grading
# never depends on something scrolling past in a terminal.
set -u
ROOT="/Users/ben/Downloads/Repos/Anti-AI-design skill"
BG=$(python3 "$ROOT/anti-ai-design-style/scripts/find_brand_guard.py")
PY="$ROOT/.venv-render/bin/python3"
run="$1"   # e.g. .../clinic-landing-page/with_skill
html=$(find "$run/outputs" -name "*.html" ! -name "input.html" | head -1)
[ -z "$html" ] && { echo "  no html in $run"; exit 0; }
"$PY" "$ROOT/anti-ai-design-style-workspace/tools/measure_run.py" "$html" > "$run/measured.json" 2>&1
"$PY" "$BG/scripts/audit_file.py" "$html" > "$run/brand_audit.txt" 2>&1
"$PY" "$ROOT/anti-ai-design-style/scripts/ai_tell_scan.py" "$html" > "$run/scan.txt" 2>&1
echo "  captured $(basename "$(dirname "$run")")/$(basename "$run")"
