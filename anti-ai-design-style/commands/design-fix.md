---
description: Fix every finding from the design scan, then prove it with a rescan
argument-hint: [file-or-folder]
allowed-tools: Bash(python3:*), Read, Edit, Write, Glob
---

The user wants the AI-look findings fixed, not just listed.

1. If no scan ran this session, run `/design-check` logic first.
2. Before changing anything, check for a `DESIGN.md` (or design brief) in the
   project. If none exists, ask the user the 3 fastest brief questions from
   `<skill-path>/templates/design-brief.md`. They are: who is it for; three
   things only this product could show; the feeling in their words. Write
   their answers into a new `DESIGN.md`. Do not invent answers for them.
3. Fix every finding using `<skill-path>/reference/fixes.md`, in this order:
   provenance residue → copy tells → colour/type tells → layout tells →
   motion tells → craft flags. Respect the DESIGN.md at every step.
   Never delete or weaken the scanner's rules to make it pass.
4. Re-run all three scanners (AI-look, copy, brand distance). If any still
   FAIL, fix and re-run. Stop after 3 rounds and report what remains and why.
5. Show the user before/after in one line each. Example:
   "AI-look score: 52 to 8. Craft flags: 3 to 0. Brand distance: NON-COMPLIANT to COMPLIANT."
   Then list the 3 biggest changes you made, in plain words. They can veto
   any of them.

Preserve the user's content and functionality exactly — this command
restyles and rewrites presentation, it never changes what the product does.
