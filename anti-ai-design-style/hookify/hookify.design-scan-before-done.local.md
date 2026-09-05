---
name: require-design-scan-before-done
enabled: true
event: stop
pattern: .*
---

Before finishing: did this session create or edit any UI files
(.html/.css/.jsx/.tsx/.vue/.svelte)?

If yes, verify BOTH of these actually ran, and passed:

- [ ] `python3 <skill-path>/scripts/verify_all.py <changed files>` → a line
      starting with `PASS:` and exit code 0. It runs all three guards.
      `brand distance NOT RUN` in that line is a FAIL, not a pass.
      4 of 4 skill-generated pages passed the AI-look scan and failed the
      brand guard. That is why it is a gate and not a suggestion.

If either failed, apply its "do this" lines and re-run before presenting.
Never present unscanned visual output — "it looks fine" is not a check;
everything AI makes looks fine.

If no UI files were touched this session, ignore this reminder.
