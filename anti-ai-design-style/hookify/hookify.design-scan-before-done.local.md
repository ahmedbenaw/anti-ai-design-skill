---
name: require-design-scan-before-done
enabled: true
event: stop
pattern: .*
---

Before finishing: did this session create or edit any UI files
(.html/.css/.jsx/.tsx/.vue/.svelte)?

If yes, verify BOTH of these actually ran, and passed:

- [ ] `python3 <skill-path>/scripts/ai_tell_scan.py <changed files>` → PASS
- [ ] `python3 <skill-path>/scripts/copy_check.py <changed pages/docs>` → PASS
- [ ] `python3 <anti-antropik-design>/scripts/audit_file.py <changed files>` → COMPLIANT
      (4 of 4 skill-generated pages failed this until it was made a gate)

If either failed, apply its "do this" lines and re-run before presenting.
Never present unscanned visual output — "it looks fine" is not a check;
everything AI makes looks fine.

If no UI files were touched this session, ignore this reminder.
