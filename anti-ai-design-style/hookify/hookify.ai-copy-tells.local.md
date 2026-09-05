---
name: warn-ai-copy-tells
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.(html|jsx|tsx|vue|svelte|md|mdx)$
  - field: content
    operator: regex_match
    pattern: (?i)(elevate your|unlock the|seamless(ly)?|supercharge|game.chang|in today's fast-paced|it'?s not just|revolutioni[sz]e your)
---

**AI-sounding copy detected** (register rules CP1/CP2).

Why this matters: this phrasing fits 500 other products, which is exactly
the problem — readers skim past it, and it reads as machine-written.

Do this instead: state the specific thing the product does, in words you
would say to a customer. "Saves you re-typing invoices" beats `streamlines
your workflow`.

Then check: `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/copy_check.py <this file>`
