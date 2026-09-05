# anti-ai-design-style

**TL;DR:** this measures how AI-generated a web or mobile design looks, then
helps you fix it. It works if you do not code. Start with
`reference/setup-guide.md`.

## Two ways to install it, and why there are two

**As a skill (start here).** Copy this folder to
`~/.claude/skills/anti-ai-design-style/`. Claude finds it on its own. Nothing
else to do.

**As a plugin (optional, adds automatic checks).** The `.claude-plugin/` and
`hooks/` folders make Claude run the scanner on every UI file it writes. They
also check the whole session before it ends.

Claude does not load skills from a plugin's root folder. So this route gives
you the hooks, the three slash commands and the scripts. The skill itself
comes from the skill install above.

Both routes read the same `scripts/`, so the two can never disagree about a
file.

## The second guard is a separate skill

Brand distance needs `anti-antropik-design` installed alongside this. Without
it, `verify_all.py` reports `brand distance NOT RUN` and the verdict is FAIL.
That is on purpose: a check that did not run must never read as a check that
passed. Install it, or set `ANTI_ANTROPIK_PATH` to point at it.

## Prove it works

```bash
python3 scripts/verify_all.py examples/fixed-example.html
```

Expect one line starting `PASS:` and ending in two fingerprints. Those tie the
verdict to the exact rules that produced it. Every script here also has a
`--selftest`.

## What it cannot do

It does not prove a design was made by a human, and nothing can. It reads
code, and with `--render` it measures a real browser. Neither detects
authorship. No published tool does that for interfaces.
