# Plan: finish and harden `anti-ai-design-style` (v3), modelled on `anti-antropik-design`

---

# Sprint: finish v3 (added 2026-09-10)

## Context for this sprint

T0, T2, T3, T4, T5 are done and committed (`7de9c0c` back to `c11c460`). Both
selftests pass on Python 3.14, the fingerprint is `3b9aa5d25679d4e8`, and
`copy_check.py` already returns `Verdict: PASS` on all six user-facing docs. The
seven new research dossiers (`09-`..`15-`) exist and were read. What has *not*
happened is the thing that makes them count: not one new tell has reached
`rules.json`, the register, or the compendium. Everything else remaining (T6,
T8, T9, and the deferred T7) is downstream of that.

Two defects found while scoping this sprint, both read-only verified:

1. **Not ID drift — a notation collision** (corrected 2026-09-10 after checking
   every citation against both the dossiers and the compendium). The register
   does not cite compendium sources by `P`/`C`/`V` ID at all. Every one of its
   ~50 `P`/`C`/`V` citations is a reference to a **dossier tell number**:
   `P13` = `01-practitioners.md` tell T13 "Uppercase eyebrow/kicker label",
   `V20` = `08-visual-science.md` tell 20 "What the motion authorities converge
   on", `C39` = `03-community-wiki.md` tell 39 "Fabricated social proof". All 77
   citation instances were checked side by side against the source titles; the
   tell column matched every time and the source column matched none.
   `A` and `R` citations, by contrast, *are* compendium sources (`R3` = impeccable,
   `R6` = open-design anti-ai-slop.md) — so the register mixes two meanings of the
   same notation. Nothing is dangling and nothing needs re-pointing. But because
   the new sweep assigns real sources `P25–P39`, `C27–C41`, `V21–V35`, appending
   them would make the collision genuinely ambiguous. **Disambiguate first**:
   rewrite tell references in the register's own existing idiom (`M-A2`, `A-F12`
   are already hyphenated) as `P-T13`, `C-T39`, `V-T20`, document both notations
   in the legend, and add `scripts/check_citations.py` so the class of bug cannot
   return. The WCAG technique number `C39` on the reduced-motion rows is not a
   citation and must be left alone.
2. **The scanner cannot read the mobile files the new tells live in.**
   `SCAN_EXTENSIONS` (`scripts/ai_tell_scan.py:43`) has no `.dart` and no `.kt`.
   MOB1 (Compose default purples) and the Flutter half of T2/T7 cannot fail-then-pass
   a fixture until that set grows. This is a prerequisite inside T1, not a separate task.

## Mid-sprint update (2026-09-11)

T1, T6, T8, T9 are committed (`984c3dc`, `f52fad4`, `68cbfcd`). Exa was
authorized on 2026-09-11 and used to close the one gap the release left open:
the MB2 row's standing `[STALE-RISK]` said "re-verify against `expo/expo`
before each release", and the release had happened.

That re-verification found a defect, not just staleness. MB2's four literals
all survive in the tabs template, confirmed three independent ways. But the
register claimed MB2 covered the *default* template as well, and it never did
— source M36's `Feeds: MB2` was an overclaim that hid a real coverage gap.
Fixed in `cf81093`: MB4 added for the default scaffold, fixture-first, with a
permanent false-positive guard and three counter-evidence rows. Fingerprint
`08519bc72585992c` -> `b7cd873aa4831ab9`; register stays `2026.10`.

The sweep was **not** re-run through Exa. The dossiers' stated routes stand.

**T7 ran and is complete** (2026-09-11). with_skill 24/24, baseline 17/24.
All three baselines passed the AI-look guard and failed the brand guard, which
is the two-guard thesis replicating with a mechanism attached: the warm-cream
escape palette sits inside Delta-E 12 of the brand neutrals. The brand gate
was not tuned. Two blind spots recorded rather than patched: `a8` library
misuse never discriminated because no eval uses a library, and `side-tab` is
a tell another detector flags and this register has no rule for.

Remaining: **nothing planned.** All of T0-T9 are done.

## Sprint goal

Every row of the Verification table below prints its expected result, the
`.skill` is under 2 MB, and the commit exists on `main`.

## Capacity

| Who | Available | Allocation | Notes |
|---|---|---|---|
| Claude | this session | ~3 h of the plan's own estimates | T1 ~1.5 h, T6 ~0.5 h, T8 ~0.3 h, T9 ~0.3 h |
| Ben | review only | 2 items | Exa custom-connector sign-in (`https://mcp.exa.ai/mcp`); reviewing the eval viewer if T7 runs |
| **Committed** | | **T1 + T6 + T8 + T9** | ~75% of capacity — T7 left as stretch on purpose |

## Sprint backlog

| Priority | Item | State | Why |
|---|---|---|---|
| P0 | **T1** register + new tells | **Carryover, ~40%** | Dossiers written and read; compendium still 254/L76; register still `2026.09`; zero new fixtures |
| P1 | **T6** humanize + ADHD-shape | **Partially done** | `copy_check` already PASS on all six docs; missing the SKILL.md "short version" and "what v2 got wrong" blocks (neither heading exists) |
| P1 | **T8** description loop + `skill-reviewer` | Planned | Needs T6's final SKILL.md wording first |
| P1 | **T9** package, proposal, commit | Planned | `proposals/` does not exist yet; no `.skill` at repo root |
| P2 | **T7** evals iteration-2 (**stretch**) | **DONE** 2026-09-11 | `evals/evals.json` has 3 evals, none with a brand or library assertion; ~700K tokens |

## T1, step by step (the only P0)

1. **Disambiguate the P/C/V tell references first** (see the corrected finding
   above), then add `scripts/check_citations.py` with a selftest, so the append
   in step 7 cannot create a real collision.
2. **Grow `SCAN_EXTENSIONS`** to include `.dart` and `.kt`, with a selftest case
   proving a Dart file is now scanned and a clean Dart file still scores 0.
3. **Fixture first, every time.** Add the fixture line to `SLOP_FIXTURE` /
   `LIB_MISUSE_FIXTURE` (or a new `MOBILE_FIXTURE`), run `--selftest`, *watch it
   fail*, then add the regex to `rules.json`.
4. **Tells that passed their evidence bar** (from `09-`, `10-`, `12-`):
   MOB1 Compose default purple values; MOB2 Expo `"Tab One"` / `#2f95dc` /
   `chevron.left.forwardslash.chevron.right`; Tailwind default palette hexes in
   non-Tailwind mobile code (0 of 413 in the FlutterFlow control); the 49-file
   shadcn dump + `lovable-tagger`; orphaned `public/placeholder.svg`;
   `fontWeight: '600'` monoculture (weak, ratio-scored).
5. **Scaffold tells are marked as scaffold.** MOB1, MOB2, the placeholder-svg
   and the 49-file dump identify "nobody designed this", not "a model wrote
   this". Recommended and assumed unless Ben says otherwise: weight 1, and a
   literal `scaffold — never fires alone` note in the Status column, matching how
   MO5 is already marked "craft score, not AI score".
6. **Counter-evidence rows** for the non-replications, recorded not deleted:
   purple→pink 0/19, `bg-clip-text` 0/17, "Trusted by N+" 0/19, straight-down
   shadow refuted by the 49/49 FlutterFlow human control.
7. **Append** `M21–M36 K16–K42 C27–C41 P25–P39 L77–L79 V21–V35 X30–X52` to the
   compendium with source line, context bullets, ADOPT/AVOID/EVIDENCE-ONLY tag
   and Feeds line each.
8. **Update the register's source-key legend** — it lists dossiers 01–08 only
   and has no `L` category.
9. **Bump the register to `2026.10`** (chosen over `2026.09b`; every response,
   benchmark and eval that cites it must match). Record the new fingerprint.

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| `P`/`C`/`V` mean *tell* in the register but *source* in the compendium | Appending the new sweep's sources makes ~50 citations genuinely ambiguous | Rewrite tell refs as `P-T13` before appending; `check_citations.py` enforces it from then on |
| `.dart` / `.kt` not scanned | Mobile fixtures can never fail-then-pass; a "passing" selftest would be vacuous | Step 2 is a prerequisite, with its own selftest case |
| MOB2 Expo literals are stale-risk | A shipped rule fires on nothing, or on the wrong template | Register row carries `[STALE-RISK]`; re-verify against `expo/expo` before T9 packages |
| T7 is ~700K tokens | Blows the session before T9 commits | T7 stays P2; T9's commit lands first |
| Exa never authorized | Sweep provenance is contestable | Every dossier states the fallback route it used; Ben's sign-in is the only fix |
| My own prose keeps failing this skill's copy checker | Shipping docs the skill would flag | Run `copy_check.py` on every doc I touch, fix rather than exempt (this has happened four times) |

## Definition of done (replaces the generic template)

- [ ] A tool printed `PASS` — never "it looks fine"
- [ ] The proof line is quoted verbatim from `verify_all.py`, not composed
- [ ] `copy_check.py` returns `Verdict: PASS` on every user-facing file touched
- [ ] Fingerprint changed, printed, and recorded in the register
- [ ] Every new rule has a fixture, a register row, and a compendium ID
- [ ] Nothing weakened to pass; counter-evidence recorded, not deleted
- [ ] Commit on `main` (never to `~/.git`)

## Key dates

| Date | Event |
|---|---|
| 2026-09-10 | Sprint start (today) |
| after T1 | Mid-sprint check: `ai_tell_scan.py --selftest` PASS *with the new fixtures*, register at `2026.10` |
| after T9 | Sprint end: `quick_validate.py` valid, `.skill` < 2 MB, commit exists |
| after T9 | Retro: T7 runs or is formally carried to the next sprint |

---

## Context

Ben wants a definitive, measured guard against "AI-generated" web and mobile design, built with skill-creator, sourced from a fresh research sweep, and usable by vibe coders and neurodivergent users. A v2 of the skill already exists inside `anti-ai-design-review-bundle.zip` (37 files, selftests passed on Python 3.11, 254-source compendium, register 2026.09). It has never been extracted here, never run on this machine (Python 3.14), and three things were never done: evals re-run with the brand gate, nine libraries installed/vendored, hooks and commands fired in a live session.

Decisions Ben made in this session:

- `anti-antropik-design` stays read-only. It is the **model** for this skill (measured verdicts, fingerprint, fail-closed selftest, proof line) and the **second guard** it calls. Changes to it go into a proposal file, not the installed copy.
- Research plans for Exa first. Exa MCP needs authorization (claude.ai connector settings) and cannot OAuth in this session. If still unavailable at execution, fall back to WebSearch/WebFetch + alphaXiv/arXiv and say so. This overrides the Exa skill's "never fall back" line.
- Scope: all 7 handover tasks plus a deeper research sweep and a rendered-craft verification layer.

Ordering deviates from the handover on purpose: research and hook/command reformatting happen **before** the eval re-run, so the ~700K-token eval loop runs once on final rules.

## Non-negotiables (carry from handover §7, verified against the sibling skill)

- Never weaken `rules.json` or a threshold to pass. Never add a tell without a source ID in the compendium and a row in the register. TDD: fixture line in selftest first, watch it fail, then the regex.
- Never hand-pick hex values: `generate_palette.py` then `audit_file.py`.
- Never present without all scanners and a tool-printed proof line. "Verified" means a tool printed PASS, never "it looks fine".
- Never claim "proven human-made". Never edit the installed sibling copy.
- Every user-facing file: plain words, one action per step, time estimates, grade ≤ 9 via `copy_check.py`. `reference/research/` and `reference/libraries/*.md` are exempt evidence archives.
- Fail closed: if the brand guard cannot be found, the proof line prints `brand distance NOT RUN` and the verdict is FAIL.

## Key paths

| What | Path |
|---|---|
| Repo root | `<repo>/` |
| Bundle (source of the skill) | `anti-ai-design-review-bundle.zip` → members `anti-ai-design-style/`, `anti-ai-design-style-workspace/`, `anti-ai-design-style.skill` |
| Sibling skill (read-only) | `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/84e2f85e-.../5167a152-.../skills/anti-antropik-design/` — a **per-session cache path; must be located dynamically** |
| skill-creator scripts | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/{scripts,eval-viewer,agents,references}` |
| hookify plugin (format truth) | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/` (`core/config_loader.py`, `core/rule_engine.py`, `skills/writing-rules/SKILL.md`) |
| plugin-dev references | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/{command-development,hook-development,plugin-structure}` |
| Scratch | `/private/tmp/claude-501/-Users-ben-Downloads-Repos-Anti-AI-design-skill/197143f0-.../scratchpad` |

## Target layout after this build

```
anti-ai-design-style/
  SKILL.md                         (<300 lines; "short version" block; "v2 got these wrong" block)
  .claude-plugin/plugin.json       (NEW, measured tier: lets hooks.json run the real scanner)
  hooks/hooks.json                 (NEW: PostToolUse Edit|Write → scripts/hook_scan.py; Stop → proof check)
  scripts/
    ai_tell_scan.py, copy_check.py, rules.json      (existing; add fingerprint + LB8/9/11 fixtures)
    verify_all.py                  (NEW: runs all guards, prints the ONE proof line, exit 0/1)
    find_brand_guard.py            (NEW: locates anti-antropik-design; fail-closed)
    install.py                     (NEW harness: resolves <skill-path>/<anti-antropik-design>, writes hookify rules + commands into a target project's .claude/)
    render_check.py                (NEW: rendered craft via Playwright — contrast, targets, focus, reduced-motion, axe; screenshot for JD checklist)
    hook_scan.py                   (NEW: thin wrapper used by hooks.json; scans only the file just written)
  hookify/*.local.md               (5 rules, formats verified live; stop rule rewritten with conditions)
  commands/*.md                    (3 commands, frontmatter verified; plus skills/<name>/SKILL.md mirrors if plugin-dev's "legacy" note holds)
  templates/, examples/, evals/    (existing + brand and library assertions in evals.json)
  reference/
    tells-register.md              (bump to 2026.09b/2026.10 after sweep; era tags kept)
    sources-compendium.md          (new IDs appended per category; Feeds lines)
    research/09-*.md ...           (new sweep dossiers with Gaps sections)
    libraries/README.md            ("Installed versions" table on top) + vendor/README.md + vendor/{gsap-skills,pixijs-skills}/
    setup-guide.md                 ("What you will see" hook table; hookify facts; debug section)
    brand-distance.md, fixes.md, accessibility.md, sources.md
proposals/anti-antropik-design.md  (cross-reference paragraph + the three defects found)
anti-ai-design-style-workspace/iteration-2/  (+ description-loop.md)
```

## Tasks

### T0. Extract, prove on Python 3.14, fix known discrepancies (~20 min) — **DONE**

Skills: `skill-creator`, `live-state-truth`.

1. `unzip` the bundle's `anti-ai-design-style/` and `anti-ai-design-style-workspace/` into the repo root. Delete `scripts/__pycache__/`. Git-init the repo (it is untracked) and commit the extracted baseline so every later change is a diff Ben can review.
2. Run the handover Task 0 list with local paths: both `--selftest`s, `ai_tell_scan.py examples/` (slop 52 FAIL, fixed 0 PASS), `copy_check.py` on all user-facing docs, `quick_validate.py .`, `exclusion_check.py --selftest` and `audit_file.py examples/fixed-example.html` (COMPLIANT) from the sibling. Python 3.14 regressions (regex, argparse, stdlib) get fixed here, TDD style.
3. Fix discrepancies the exploration found:
   - `reference/setup-guide.md` says four hookify files; there are five.
   - `iteration-1/benchmark.md` says register 2026.08; everything else says 2026.09.
   - LB8, LB9, LB11 have no selftest fixture: add fixture lines, watch them fail, confirm regexes.
   - Student-budget `with_skill` grading passed "button ≥ 44px" on `min-height: 844px` (the phone frame). Re-grade honestly; the grader script must measure the button element.
   - `copy_check.py` loads `rules.json` inline in two places; single-source it.
4. Add a `fingerprint` (sha256 of `rules.json`, 16 hex chars, copied from `exclusion_check.py:fingerprint()` idea) printed in every scanner verdict and in `--json`.

Done when every line prints its expected result on 3.14 and the baseline commit exists.

### T1. Research sweep and register update (~2-3 h, subagents) — **CARRYOVER, ~40%** (P0; see sprint block)

Skills: `/exa:search` (orchestrator pattern, haiku subagents, `sources_reviewed` line) if authorized; else WebSearch/WebFetch + alphaXiv. Then `adversarial-verify`, `live-state-truth`.

Sweeps (one subagent each, each writes `reference/research/09-..md` .. with a source table, ≤30-word quotes, counter-evidence, and a Gaps section):

1. Mobile-app tells (thinnest area; FlutterFlow/Figma Make/SwiftUI/Compose defaults; 5-tab bar false-positive risk).
2. Code samples for Vue, React Native, Flutter, plus Cursor/Copilot/GPT-5-era web: repeat the K methodology (clone verified generated repos, count signatures) rather than trusting articles.
3. Reddit retry from this unproxied machine (r/web_design, r/webdev, r/UI_Design, r/lovable, r/vibecoding, r/ClaudeAI, r/cursor).
4. Claude's own defaults beyond the seven brand hexes; the "escape look" family; any 2026 "third era" tells.
5. Re-check of every entry in the compendium's "Stale" section (line 2868): library versions, licences, word lists, detector claims.
6. Visual/graphic science: rendered-output metrics anyone has published (Design Homogeneity Index follow-ups, layout entropy, screenshot benchmarks) to ground T4's render layer honestly.
7. Accessibility/neurodivergence updates: WCAG 2.2 errata, COGA, GOV.UK, ADHD-specific reading guidance.

Rules: each new source gets an ID in its category, source line, context bullets, ADOPT/AVOID/EVIDENCE-ONLY/CONTESTED tags, Feeds line. Read the Contested section (line 2784) before promoting anything. A rule enters `rules.json` only with 2+ independent sources or one measurement, an era tag, a register row, and a selftest fixture first. Retire or down-weight rules the sweep contradicts; never delete to pass. Bump register version and the fingerprint. Record the fallback used (Exa vs web) at the top of each dossier.

Done when: new dossiers exist with Gaps sections, compendium counts updated, register bumped, `--selftest` PASS with the new fixtures.

### T2. Libraries: install, verify API names, vendor the two skill repos (~30 min) — **DONE** (commit 2e06f47)

Skills: `live-state-truth`. Follow the handover Task 2 table verbatim (GSAP skills, uiverse galaxy README only, animejs, animate.css, animate-ui, lenis, pixijs-skills, leaflet + plugins page diff, survey-core/survey-js-ui). Work in scratch, not the repo. Confirm every API name used in `rules.json` LB rules exists in the installed version; a mismatch means fixture first, then regex. Write `reference/libraries/vendor/README.md` (commit, licence, override rule: our `motion.md`/`scroll-canvas-ui.md`/`maps-forms.md` win on conflict) and the "Installed versions" table with dates at the top of `libraries/README.md`. Keep `.skill` under ~2 MB (vendor SKILL.md files only if needed).

### T3. Harness: proof line, brand-guard locator, install script (~45 min) — **DONE**

Skills: `anti-antropik-design` patterns, `test-driven-development`.

1. `scripts/find_brand_guard.py`: search order — `$ANTI_ANTROPIK_PATH`, `~/.claude/skills/anti-antropik-design`, `~/.claude/plugins/**/anti-antropik-design`, `~/Library/Application Support/Claude/**/skills/anti-antropik-design` (newest mtime wins). Prints the path or exits 2.
2. `scripts/verify_all.py <files>`: runs `ai_tell_scan.py --json`, `copy_check.py --json`, the sibling's `audit_file.py --json --suggest`, optionally `render_check.py`; prints exactly one line `Verified: AI-look score N/100 (band), craft flags N, library misuse N, brand distance COMPLIANT|NON-COMPLIANT|NOT RUN, register YYYY.MM, fingerprint XXXX.` Exit 0 only when every guard passed. NOT RUN is a FAIL. SKILL.md, commands and hooks then quote this tool output instead of composing it.
3. `scripts/install.py [target-project]`: locates skill and sibling paths, rewrites `<skill-path>` / `<anti-antropik-design>` placeholders, copies hookify rules to `<target>/.claude/` and commands to `<target>/.claude/commands/`, prints what it did in plain words with a "what you will see next" line, `--dry-run` and `--uninstall`. This is what a non-technical user runs; the setup guide points at it.
4. Selftests for all three (known-answer, fail-closed cases asserted).

### T4. Rendered-craft verification layer (~1 h) — **DONE** (commits c11c460, 4c0d983)

Skills: `live-state-truth`; tools: Playwright (`plugin_playwright`) or chrome-devtools MCP.

`scripts/render_check.py <html>`: loads the page headless, measures computed contrast on text nodes (WCAG 2.2 1.4.3/1.4.11), target sizes (2.5.8, 44/48 on touch viewport), focus visibility on tab, `prefers-reduced-motion` emulation (animations stop), axe-core pass, and saves a screenshot for the judgment checklist JD1–JD5 in SKILL.md. Reports on the **craft axis only**. It does not claim AI detection from pixels: the compendium's stale section says no UI screenshot classifier works and no corpus exists; the skill must not contradict its own evidence. Optional dependency; `verify_all.py` prints `render: SKIPPED (playwright not installed)` and does not fail on that alone.

### T5. Claude Code layer, proven live (~45 min) — **DONE** (commits 11a08b7, 7de9c0c)

Skills: `/hookify:writing-rules` (the only hookify skill; `/hookify` is a command), `/plugin-dev:command-development`, `plugin-dev:hook-development`, `plugin-dev:plugin-validator` agent. Note plainly in the setup guide: `claude-tag-troubleshoot:config-guide` documents Slack admin settings and `debug-plugins` diagnoses the Slack-hosted container; neither checks local Claude Code. Their plain reference style is borrowed; the loading check is a live session plus `plugin-validator`.

Hookify facts to honour (from `core/`): rules live only in cwd `.claude/hookify.*.local.md`; regex-only, `re.IGNORECASE`, AND-only conditions; events `bash|file|stop|prompt|all`; `file` fires only on Edit/Write/MultiEdit (a Bash heredoc write bypasses it); `prompt` cannot block; broken rules fail open.

1. Rewrite `hookify.design-scan-before-done.local.md`: simple-form `pattern: .*` on `event: stop` maps to a `content` field that stop does not expose, so it may never fire. Use `conditions` on `transcript` matching `\.(html|css|jsx|tsx|vue|svelte)` so it fires only in UI sessions. Consider `action: block` for the stop rule (it is the one event where block is enforced).
2. Install into a scratch project with `install.py`, then trigger each of the five rules on purpose (gradient class, "Unlock the power of", "Trusted by 10,000+", `#FAF9F5` + Georgia, stop with unscanned UI edit). Record a table in `setup-guide.md` "What you will see": rule, trigger, fired yes/no, date.
3. Commands: verify frontmatter (`description`, `argument-hint`, `allowed-tools`), `$ARGUMENTS` use, and replace `<skill-path>` with `${CLAUDE_PLUGIN_ROOT}` in the plugin tier. Run `/design-check examples/slop-example.html`, `/design-fix` on a copy, `/design-brief`; enforce "at most 7 findings, plain words, one closing question".
4. Measured tier: add `.claude-plugin/plugin.json` and `hooks/hooks.json` (PostToolUse `Edit|Write` → `hook_scan.py` on the written file; Stop → check `verify_all.py` ran). Regex rules stay as the zero-install tier. Run `plugin-validator`.

### T6. Humanize and ADHD-shape every user-facing doc (~30 min) — **PARTIAL** (P1; copy_check already PASS, the two SKILL.md blocks are missing)

Skills: `/anthropic-skills:humanizer`, `/anthropic-skills:i-have-adhd`, `ruthless-editor`, then `copy_check.py`. Files: `SKILL.md`, `setup-guide.md`, `fixes.md`, `accessibility.md`, `brand-distance.md`, `sources.md`, `templates/*.md`, `examples/README.md`, `commands/*.md`, `hookify/*.md`, plus the new scripts' `--help` text. Add to SKILL.md: a "short version, if nothing else is read" block and a "what v2 got wrong" block (the 4-of-4 brand failure), copied from the sibling's pattern. Accessibility of the docs themselves: TL;DR first, numbered steps, no uppercase runs, no walls, time estimates, state restated after each step.

### T7. Evals iteration-2 with brand and library gates (~40 min, ~700K tokens) — **STRETCH** (P2; deferred by Ben)

Skills: `skill-creator` (spawn with_skill and baseline runs in one turn, `eval_metadata.json`, `timing.json`, grader per `agents/grader.md`, `aggregate_benchmark.py`, `generate_review.py --static` for Ben to review before any self-judging). Add two assertions per eval to `evals.json`: `audit_file.py → COMPLIANT`, `ai_tell_scan.py --json library_misuse == 0 or justified`. Hand-verify every fail with evidence. Write `iteration-2/benchmark.md` with a brand-distance column and "n = 1 per cell" stated. If with_skill fails the brand gate, that is the finding; do not tune the gate.

### T8. Description optimization (~20 min) — **PLANNED** (P1)

Skills: `skill-creator` `run_loop.py` with 20 trigger queries (8-10 should-trigger, 8-10 near-miss non-triggers: SQL, plain prose edits, data analysis with no UI, a brand-only request that belongs to the sibling). Review the set via `assets/eval_review.html`. Apply `best_description` only if the loop measured a gain; record in `workspace/description-loop.md`. Then `plugin-dev:skill-reviewer` agent on SKILL.md; apply what survives `adversarial-verify`.

### T9. Package, propose, deliver (~15 min) — **PLANNED** (P1)

1. Strip `__pycache__`, `.impeccable/`; `python3 -m scripts.package_skill <path>` from the skill-creator dir (copy to scratch if read-only); size < 2 MB; `quick_validate.py` valid.
2. `proposals/anti-antropik-design.md`: the cross-reference paragraph ("run `anti-ai-design-style` alongside; 4 of 4 pages passed one guard and failed the other") plus the three defects found in the sibling: `exclusion_check.js` is `STANDARD_VERSION 1.1` vs Python `2.0`; SKILL.md Files table says five palettes, there are 13; the excluded-font list exists in three places with different contents.
3. Rebuild the review bundle with the handover, plan, manifest, both workspace iterations. Commit. Update `HANDOVER-claude-code.md` status table.

## Verification (the line that proves each task)

| Task | Command | Proves done |
|---|---|---|
| T0 | `python3 scripts/ai_tell_scan.py --selftest` / `copy_check.py --selftest` on 3.14 | `SELFTEST: PASS` incl. LB8/9/11 |
| T0 | `python3 scripts/ai_tell_scan.py examples/` | slop FAIL ≥ 40, fixed PASS 0, fingerprint printed |
| T1 | `grep -c "^### " reference/sources-compendium.md`; register header | counts up, version bumped, every new rule has fixture + row + IDs |
| T2 | `head reference/libraries/README.md` | "Installed versions" table with dates; `vendor/README.md` with licences |
| T3 | `python3 scripts/verify_all.py examples/fixed-example.html` | one proof line, exit 0; with sibling hidden → `brand distance NOT RUN`, exit 1 |
| T3 | `python3 scripts/install.py --dry-run /tmp/proj` | lists resolved paths, no placeholders remain |
| T4 | `python3 scripts/render_check.py examples/slop-example.html` | craft findings with WCAG criterion numbers, screenshot saved |
| T5 | table in `setup-guide.md` | 5 rules × "fired: yes" with date; `/design-check` ≤ 7 findings + one question; `plugin-validator` clean |
| T6 | `python3 scripts/copy_check.py <all user-facing files>` | `Verdict: PASS` |
| T7 | `iteration-2/benchmark.md` | brand column present, n = 1 stated, grader evidence per fail |
| T8 | `workspace/description-loop.md` | train/test scores per iteration |
| T9 | `ls -la *.skill`; `quick_validate.py` | < 2 MB, valid; proposal file exists; commit on main |

## Skill-to-task map

| Skill / tool | Tasks |
|---|---|
| `skill-creator` | T0, T7, T8, T9 |
| `/exa:search` (fallback: WebSearch/WebFetch/alphaXiv) | T1 |
| `live-state-truth`, `adversarial-verify` | T0–T5, T7, T9 |
| `anti-antropik-design` (read-only; scripts called) | T0, T3, T7, T9 |
| `/hookify:writing-rules`, `plugin-dev:command-development`, `hook-development`, `plugin-validator` | T5 |
| `test-driven-development` | T0, T1, T3, T4 |
| `humanizer`, `i-have-adhd`, `ruthless-editor` | T6 |
| Playwright / chrome-devtools MCP | T4, T5 |

## Open risks

- Exa: if unauthorized at run time, the fallback route is slower and Reddit may still block; dossiers must state which route ran.
- Sibling path is a session cache; if it vanishes, T3's locator fails closed and T7 records `NOT RUN`, which is the honest result.
- Rendered layer depends on Playwright being installable; it is optional by design.
- n = 1 per eval cell stays; any number quoted must say so.
