---
name: warn-ai-gradient-tells
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.(html|css|scss|jsx|tsx|js|ts|vue|svelte|astro)$
  - field: content
    operator: regex_match
    pattern: bg-clip-text[^"']*text-transparent|blur-3xl|from-(purple|indigo|violet)-\d00\s+to-(pink|purple|blue)-\d00
---

**AI-look pattern detected** (gradient headline text, glow blob, or the
classic AI gradient).

Why this matters: these are the surest AI tells in the register (rules
CO2/CO5/CO1). Gradient text also breaks contrast checks for low-vision
users.

Do this instead:
- Headline: solid text colour; use size/weight for emphasis
- Glow blobs: delete the blurred decorative divs
- Gradient: use the accent colour named in the project's DESIGN.md

Then run: `python3 <skill-path>/scripts/ai_tell_scan.py <this file>`
