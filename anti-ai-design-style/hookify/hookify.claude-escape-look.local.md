---
name: warn-claude-escape-look
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.(html|css|scss|jsx|tsx|vue|svelte|astro)$
  - field: content
    operator: regex_match
    pattern: (?i)#f[0-9a-f]f[0-9a-f]f[0-9a-f]\b|#fa[f9][0-9a-f]f[0-9a-f]|font-family:[^;]*(georgia|lora|merriweather|playfair|source serif|crimson|libre baskerville|poppins|montserrat|jost|futura)
---

**Possible drift into Claude's own design language** (warm off-white ground,
or a brand-guard excluded typeface).

Why this matters: this skill measures the generic AI look. It does NOT
measure brand distance, and its advice ("warm neutrals, editorial serif")
drifts into Anthropic's palette. Measured: 4 of 4 skill-generated pages
failed `anti-antropik-design` until that guard became a gate.

Do this: generate the palette instead of picking it:
`python3 "$(python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/find_brand_guard.py)"/scripts/generate_palette.py --hue N --temp neutral --chroma high --name X --css`
Then verify: `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/brand_distance.py <this file> --suggest`
