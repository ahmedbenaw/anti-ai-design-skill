---
description: Scan files for AI-look tells and craft problems, explain plainly
argument-hint: [file-or-folder]
allowed-tools: Bash(python3:*), Read, Glob
---

The user wants to know whether their design reads as AI-generated.

1. Determine what to scan: use `"$ARGUMENTS"` if given; otherwise the UI files
   changed in this session; otherwise ask which folder in ONE short question.
2. Run every guard with one command:
   `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/verify_all.py <the files from step 1>`
   It prints a single verdict line. Quote that line. Do not write your own
   summary of it. A hand-written summary is where a failed guard quietly
   turns into a passing sentence.
   Then run these for the findings:
   - `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/ai_tell_scan.py <the files from step 1>`
   - `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/copy_check.py <the files from step 1>` (pages and docs)
   - `python3 "$(python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/find_brand_guard.py)"/scripts/audit_file.py <the files from step 1> --suggest`
     (only when brand distance failed; it prints replacement hex values)
3. If the line says `brand distance NOT RUN`, say this first, in plain words.
   The second guard is not installed. So the verdict is FAIL for a reason
   that has nothing to do with their design. Tell them to install
   `anti-antropik-design`, or to set `ANTI_ANTROPIK_PATH` to point at it. Then
   report the rest of the findings normally. Do not let a first-time user think
   their page failed on its merits when the checker was simply missing.
4. Report back in plain language, for a non-technical reader:
   - Start with the verify_all line exactly as printed, then one sentence
     saying what it means.
   - Then a numbered list of at most 7 findings, worst first. For each:
     what it is (no jargon), why it matters (one line), and the exact fix.
   - If there were near-proof findings (generator plumbing), say plainly:
     "this project carries its generator's fingerprints" and what they are.
   - Keep craft/accessibility flags in a separate short list, labelled
     "not AI signs — just worth fixing".
5. End with exactly one question: "Want me to fix these? (/design-fix)"
   Do not start fixing unless asked.

Never dump raw scanner output at the user. Never claim a PASS proves human
authorship — the scanner measures the AI look, not authorship.
