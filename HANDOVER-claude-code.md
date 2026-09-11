# Handover to Claude Code: finish building `anti-ai-design-style`

Written 2026-09-04 for a Claude Code session. Read top to bottom once. Then
work the numbered tasks in order. Every task names the skill to invoke, the
exact command, and the line that proves it is done.

**TL;DR for a human reader (Ben):** the skill exists, is packaged, and passes
its own checks. Three things are not done. First, the evals have not been
re-run with the brand guard turned on. Second, the nine libraries are not
installed, and the two that ship as Claude skills are not vendored. Third,
the hooks and slash commands have never fired in a real Claude Code session.
Those three are why this handover exists.

---

## 0. The one fact that changes how you build

**4 of 4 pages the skill generated passed its own AI-look scanner. All four
landed on Claude's brand palette anyway.** Measured with
`anti-antropik-design/scripts/audit_file.py`:

```
examples/fixed-example.html v1   FAIL #F5F1E8 (2.74 dE from brand, needs >=12), georgia   NON-COMPLIANT (2)
clinic-landing-page/with_skill   FAIL #F3F5F2                                              NON-COMPLIANT (1)
student-budget-app-screen        FAIL #B9B6AC #F1F1EA #FBFBF7                              NON-COMPLIANT (3)
deslop-lovable-page              FAIL #FBFBF9, georgia, source serif 4                     NON-COMPLIANT (4)
```

Why it happens: "escape generic AI" and "escape the cream editorial look"
both push toward warm off-white, bookish serif, terracotta. That corner IS
Claude's design language. The register already names it (rule CO6). The
skill walked into its own rule.

What was done about it (all in the packaged skill now):

- `SKILL.md` Step 3: "The second guard is not optional", runs `audit_file.py`.
- `templates/design-brief.md` section 4: palettes are generated with
  `generate_palette.py`, then named. Never hand-picked. Never list extended
  with the excluded typefaces and "no geometric sans over bookish serif".
- `commands/design-check.md` and `commands/design-fix.md`: run all three
  scanners; before/after line includes brand distance.
- `hookify/hookify.design-scan-before-done.local.md`: COMPLIANT checkbox.
- `hookify/hookify.claude-escape-look.local.md` (new): fires on a warm
  off-white hex or an excluded `font-family`.
- `reference/brand-distance.md`: the full story with the numbers.

What was NOT done: the evals were never re-run with the gate in place. The
18/18 benchmark is an AI-look and craft number only. **Do not quote it as
proof the skill avoids Claude's brand.** Task 1 below fixes that.

---

## 1. What exists, where

| Path | What | State |
|---|---|---|
| `/home/claude/anti-ai-design-style/` | the skill, 37 files | packaged, selftests PASS |
| `/home/claude/anti-ai-design-style.skill` | zip of the above, ~312 KB | ship candidate |
| `/home/claude/anti-ai-design-style-workspace/iteration-1/` | v1 eval runs, `benchmark.md`, per-run `scan.json` `copy.json` `grading.json` `timing.json` | evidence; pre-gate |
| `/home/claude/PLAN-anti-ai-design-style.md` | build plan v2, tasks 0 to 12, skill-to-task map | current |
| `/home/claude/REVIEW-MANIFEST.md` | every file with a SHIP or BIN verdict | current |
| `/home/claude/anti-ai-design-review-bundle.zip` | all of the above | rebuilt with this handover |
| `/root/work/anti-ai-design/research/01-08*.md` | raw research dossiers (also bundled under `reference/research/`) | evidence |
| `/root/work/anti-ai-design/libs/01-03*.md` | raw library notes (ported into `reference/libraries/`) | evidence |
| `<anti-antropik-design>` | sibling skill; scripts `audit_file.py`, `generate_palette.py`, `exclusion_check.py` | installed copy is a read-only cache |

Inside the skill:

```
SKILL.md                              workflow, two scores + library misuse, proof line, refusals
scripts/ai_tell_scan.py               AI-look scanner; --selftest, --json, --max-ai (default 20)
scripts/copy_check.py                 copy tells + Flesch-Kincaid grade gate; --selftest
scripts/rules.json                    register 2026.09: provenance PR1-7, code tells, copy tells, craft CR1-6, library_misuse LB1-12, bands
reference/tells-register.md           every rule, its era tag, weight, source IDs
reference/sources-compendium.md       254 sources, context bullets, ADOPT/AVOID tags, master maps, contested/stale
reference/sources.md + research/      the dossiers behind the compendium
reference/brand-distance.md           the second guard
reference/fixes.md                    one "do this" per rule
reference/accessibility.md            the floors with standard numbers
reference/setup-guide.md              install steps for non-technical users
reference/libraries/README.md         the one rule, nine-library table, licence facts
reference/libraries/motion.md         GSAP, anime.js, animate.css, animate-ui
reference/libraries/scroll-canvas-ui.md   Lenis, PixiJS, uiverse galaxy
reference/libraries/maps-forms.md     Leaflet + plugins, SurveyJS
templates/design-brief.md             Step 1 brief; palette generated then named
templates/prompt-packs.md             Lovable / Bolt / v0 / Cursor blocks
examples/slop-example.html            scores 52, FAIL (fixture)
examples/fixed-example.html           v2, Kiln palette, scores 0, COMPLIANT (fixture)
examples/README.md                    v1 to v2 story
commands/design-brief.md, design-check.md, design-fix.md
hookify/*.local.md                    5 rules (gradient tells, copy tells, fake proof, scan-before-done, claude-escape-look)
evals/evals.json                      3 evals with assertions
```

Current measured state (re-verify in Task 0, do not trust this table):

| Check | Result |
|---|---|
| `ai_tell_scan.py --selftest` | PASS: slop 51, 19 tells, 2 craft; clean 0; library fixture 9 rules |
| `copy_check.py --selftest` | PASS |
| `examples/slop-example.html` | 52/100 FAIL (correct) |
| `examples/fixed-example.html` | 0/100 PASS, brand COMPLIANT |
| quick_validate | valid |
| evals with_skill / baseline | 18/18 vs 15/18, **pre-gate**, brand 0/3 |

---

## 2. Design decisions you must not undo

1. **Measured, not judged.** A scanner that scores AI-tell density. Not a
   fifth ban list. Ben chose this explicitly.
2. **Two axes never mixed.** AI-look score (0-19 distinct, 20-39 leaning
   generic, 40+ reads as AI) and craft/accessibility flags. Plus library
   misuse in its own section. Plus brand distance from the sibling skill.
3. **Tiered evidence.** Provenance artifacts (lovable-tagger,
   `placeholder.svg?height=`, bolt `config.json`, `replit.md`, generator
   comments, chat residue) are near-proof at 15 points. Everything else is
   co-occurrence scored. No single non-provenance tell crosses a band alone.
4. **Era-tagged, dated register** (v2026.09). Tells drift about every 18
   months: purple → shadcn defaults → cream/serif/terracotta escape look.
   Raw purple classes: 0 of 12 modern AI repos. Structure converges harder
   than colour (Design Homogeneity Index). Sparkle-icon evidence conflicts.
5. **No rule from memory.** A rule enters `rules.json` only with a source ID
   in the compendium and a row in the register. Never delete a rule to pass.
6. **Accessibility floors with standard numbers.** WCAG 2.2 1.4.3 (4.5:1),
   1.4.11 (3:1), 2.5.8 (24px; 44pt/48dp touch), 2.3.3 reduced motion, 2.2.2,
   2.3.1, 2.4.7 focus, 1.4.8 (≤75ch, never justified). BDA: 16px, 1.5 line
   height, left aligned. Copy at about grade 9, 25-word sentences. APCA is
   advisory only. Dyslexia fonts do not work; do not recommend them.
7. **Honesty is a design material.** No invented people, stats, logos,
   testimonials. The skill refuses to help fake proof evade its own rules.
8. **Library discipline in one line.** "A library earns its place when it
   lets the page show the real product. It fails when it decorates a page
   that has nothing to show." Leaflet and SurveyJS are the antidote for JD2,
   polish without depth. They add function, not motion.
9. **Readability exemption is explicit.** `reference/research/` and
   `reference/libraries/*.md` are evidence archives and are exempt from the
   grade-9 gate. Everything a user reads is not exempt.
10. **The audience.** Vibe coders, non-technical, neurodivergent. Plain
    words, one action per step, one question at a time, time estimates,
    say what they will see next. That is a requirement on every doc and on
    every command's output, not a tone preference.

---

## 3. Skills to invoke, per task

| Skill | Invoke for | Notes |
|---|---|---|
| `skill-creator` | Tasks 0, 1, 6, 7 | eval loop (`with_skill` vs `without_skill`), `quick_validate.py`, `package_skill.py`, `run_loop.py` |
| `/exa:search` | Task 5 | **Was never connected in the Cowork session.** Check first: Settings → Plugins → Exa → Connect [Likely]. If still absent, fall back to WebSearch/WebFetch + arXiv/alphaXiv as before |
| `live-state-truth` | every task | run the script, read the live doc, never assert from memory |
| `adversarial-verify` | Tasks 1, 2, 4, 7 | attack each claim after building it |
| `/humanizer` | Task 6 | on every user-facing `.md` (not research/ or libraries/) |
| `/i-have-adhd` | Task 6 | shape docs: action first, numbered, restate state, one thing per step |
| `/hookify:hookify`, `/hookify:writing-rules` | Task 3 | verify the five rules load and fire; fix format if the plugin rejects them |
| `/plugin-dev:command-development` | Task 3 | verify frontmatter (description, argument-hint, allowed-tools) and behaviour of the three commands |
| `/claude-tag-troubleshoot:debug-plugins` | Task 3 | confirm the skill, hookify rules and commands are actually loaded in the session; diagnose if not |
| `anti-antropik-design` | Tasks 1, 2, 7 | `audit_file.py --suggest`, `generate_palette.py`, `exclusion_check.py --selftest` |

The `superpowers` plugin is active in Claude Code. `brainstorming` is not
needed; the design is settled. `test-driven-development` applies to any
change in `ai_tell_scan.py` or `copy_check.py`: add a fixture line to the
selftest first, watch it fail, then add the rule.

---

## 4. Tasks, in order

### Task 0: Prove the current state (10 minutes)

Skills: `skill-creator`, `live-state-truth`, `anti-antropik-design`.

```
cd /home/claude/anti-ai-design-style
python3 scripts/ai_tell_scan.py --selftest          # SELFTEST: PASS
python3 scripts/copy_check.py --selftest             # PASS
python3 scripts/ai_tell_scan.py examples/            # slop FAIL 52, fixed PASS 0
python3 <anti-antropik-design>/scripts/exclusion_check.py --selftest
python3 <anti-antropik-design>/scripts/audit_file.py examples/fixed-example.html   # COMPLIANT
python3 scripts/copy_check.py SKILL.md reference/setup-guide.md reference/fixes.md \
  reference/accessibility.md reference/brand-distance.md reference/sources.md \
  reference/sources-compendium.md templates/*.md examples/README.md commands/*.md   # PASS
python3 /mnt/skills/examples/skill-creator/scripts/quick_validate.py .
```

Note: `package_skill.py` fails when run from `/mnt/skills` (read-only,
module import). Copy skill-creator to `/tmp/sc` and run
`cd /tmp/sc && python3 -m scripts.package_skill /home/claude/anti-ai-design-style`.

Done when: every line above prints its expected result. If any does not,
stop and fix before anything else.

### Task 1: Re-run the evals against v2, with the brand gate (about 40 min, ~700K tokens)

Skills: `skill-creator`, `adversarial-verify`, `anti-antropik-design`.

1. Run all three evals in `evals/evals.json`, `with_skill` and
   `without_skill`, as in iteration 1. Put them in
   `anti-ai-design-style-workspace/iteration-2/`.
2. Grade with the existing assertions AND add one assertion per eval:
   `audit_file.py <output> → COMPLIANT`. Add it to `evals.json` so it stays.
3. Add one assertion per eval: `ai_tell_scan.py --json` reports
   `library misuse 0` (or lists real, justified uses).
4. Grade honestly. In iteration 1 the grading script produced false fails
   (a "FAQ" word check; a `height:` vs `min-height:` check). Hand-verify each
   fail with evidence in `grading.json`. Keep genuine baseline fails
   (`John Doe`, `Sarah Chen`, `Jane Smith`; `10K+`, `99.9%`, `Trusted by 10,000`).
5. Rewrite `benchmark.md` for iteration 2 with a brand-distance column.
   If with_skill fails the brand gate again, that is the finding. Report it.
   Do not tune the gate down.

Done when: `iteration-2/benchmark.md` exists with a brand column and n=1
per cell stated plainly.

### Task 2: Install the nine libraries and vendor the two skill repos (30 min)

Skills: `live-state-truth`, `anti-antropik-design` (nothing else).

Ben's words: "after installing all of the following libraries of porting its
skills fully and nativeized inside the our skill itself". Current state: the
port is **docs-derived guidance**, written from live docs. It is not vendored
skill files. Two of the nine ship as Claude skills; those must be vendored
verbatim, with licence, so the port is literal, not paraphrased.

| # | Library | Install command (Ben's, verbatim) | What "ported" means here |
|---|---|---|---|
| 1 | GSAP | `https://github.com/greensock/gsap-skills` | clone; copy its `SKILL.md` and any `references/` into `reference/libraries/vendor/gsap-skills/`; keep LICENSE. Note: GSAP itself is NOT MIT (Webflow standard no-charge licence) |
| 2 | uiverse galaxy | `https://github.com/uiverse-io/galaxy` | clone; do NOT vendor components (that is the failure mode); vendor README/licence only; keep our "study, then rebuild in own tokens" rule |
| 3 | anime.js | `npm i animejs` | install in a `/tmp/libcheck` project; confirm the `onScroll`, `loop`, `autoplay` API names used in `rules.json` LB rules exist in the installed version; record version |
| 4 | animate.css | `https://github.com/animate-css/animate.css` | `npm i animate.css`; confirm `animate__infinite` and the reduced-motion block exist in the installed CSS; record version |
| 5 | animate-ui | `https://github.com/imskyleen/animate-ui` | clone; confirm no reduced-motion default; record commit |
| 6 | Lenis | `https://github.com/darkroomengineering/lenis` | `npm i lenis`; confirm `new Lenis(` signature; record version |
| 7 | PixiJS skills | `npx skills add https://github.com/pixijs/pixijs-skills` or `/plugin marketplace add pixijs/pixijs-skills` | vendor the skill files verbatim into `reference/libraries/vendor/pixijs-skills/` with licence |
| 8 | Leaflet + plugins | `npm i leaflet`; plugin list from `https://leafletjs.com/plugins.html` | confirm `L.tileLayer` and attribution behaviour; re-fetch the plugins page and diff against the categorised table in `maps-forms.md` |
| 9 | SurveyJS | `https://github.com/surveyjs/survey-library` | `npm i survey-core survey-js-ui`; confirm the renderer vs Creator licence split against the installed package.json files |

Then:

1. Add a `reference/libraries/vendor/README.md`: what is vendored, from
   which commit, under which licence. State one rule there: our own
   `motion.md`, `scroll-canvas-ui.md` and `maps-forms.md` override the
   vendored guidance wherever they conflict. Vendored skills teach the tells.
2. Add L-entries to the compendium for anything the installed versions
   contradicted. Bump nothing without a source.
3. If an installed API name differs from a `rules.json` regex, fix the regex
   AND add a selftest fixture line first (TDD).
4. Repackage (Task 7). Check the `.skill` stays under about 2 MB; if
   vendoring pushes it over, vendor SKILL.md files only, not assets.

Done when: `reference/libraries/vendor/` exists with licences, and a
"Installed versions" table with dates sits at the top of
`reference/libraries/README.md`.

### Task 3: Prove the Claude Code layer works in a live session (20 min)

Skills: `/hookify:hookify`, `/hookify:writing-rules`,
`/plugin-dev:command-development`, `/claude-tag-troubleshoot:debug-plugins`.

None of this was testable from Cowork. It has never fired.

1. Install the skill into a scratch project per `reference/setup-guide.md`
   Parts 3 and 4 (copy `hookify/*.local.md` to `.claude/`, copy `commands/*.md`
   to `.claude/commands/`).
2. Run `/claude-tag-troubleshoot:debug-plugins`. Confirm the skill, the five
   hookify rules, and three commands are loaded. If the skill name says
   "config-guide" anywhere in the docs, replace with `debug-plugins` (Ben's
   latest instruction).
3. Trigger each hook on purpose: write a file with
   `bg-gradient-to-r from-indigo-500`; write "Unlock the power of"; write
   "Trusted by 10,000+"; write `#FAF9F5` and `font-family: Georgia`; then try
   to stop with a UI file edited and no scan. Each must fire with its plain
   language message. Record what actually fired in
   `reference/setup-guide.md` under a new "What you will see" subsection.
4. Run `/design-check examples/slop-example.html`, `/design-fix` on a copy,
   `/design-brief`. Confirm the output follows the "at most 7 findings, plain
   words, one question at the end" rules. Fix the command text if the model
   drifts.
5. If hookify's format has changed (`event:`, `conditions:`, `regex_match`),
   use `/hookify:writing-rules` and update all five files.

Done when: a short table in `setup-guide.md` lists each hook, the trigger
used, and "fired: yes" with the date.

### Task 4: Description optimisation and skill review (15 min)

Skills: `skill-creator` (`run_loop.py`), `plugin-dev:skill-reviewer` agent,
`adversarial-verify`.

1. Run skill-creator's description optimisation loop with the trigger set
   in `evals/evals.json` plus at least five near-miss prompts that should
   NOT trigger (plain text edit, SQL, a data analysis with no UI).
2. Run the `skill-reviewer` agent on `SKILL.md`. Apply what survives
   `adversarial-verify`.

Done when: description changed only if the loop measured a gain; the
measurement is in `anti-ai-design-style-workspace/description-loop.md`.

### Task 5: Research gaps (optional, 30 min, only if Exa connects)

Skills: `/exa:search`, `live-state-truth`, `adversarial-verify`.

Known thin areas, in order. Reddit was blocked during the sweep. Mobile-app
tells: the M section is 20 entries and mostly practitioner. Vue, React
Native and Flutter code samples: the K section is React and plain HTML only.
Claude's own "tasteful" defaults beyond the seven brand hexes.

Each new source gets: an ID in its category, source line, context bullets,
`[ADOPT]`/`[AVOID]`/`[EVIDENCE-ONLY]`/`[CONTESTED]` tags, and a Feeds line.
Nothing enters `rules.json` from a single article.

### Task 6: Humanize and ADHD-shape every user-facing doc (20 min)

Skills: `/humanizer`, `/i-have-adhd`, then `copy_check.py`.

Files: `SKILL.md`, `reference/setup-guide.md`, `fixes.md`,
`accessibility.md`, `brand-distance.md`, `sources.md`, `templates/*.md`,
`examples/README.md`, `commands/*.md`, `hookify/*.md`. NOT `research/`, NOT
`libraries/*.md` (stated exemption).

1. `/humanizer` pass. Watch for the copy checker's own banned list; the
   docs quote bad phrases in backticks on purpose, keep the backticks.
2. `/i-have-adhd` pass: every section opens with the action; state is
   restated after each step; nothing over 25 words per sentence.
3. `copy_check.py` on every file above. PASS required.

Done when: all listed files PASS and the diff is reviewable by Ben.

### Task 7: Repackage, cross-reference, deliver (10 min)

Skills: `skill-creator`, `propose_skills` (Cowork) or the equivalent.

1. Remove stray dirs (`scripts/__pycache__/`, any `.impeccable/`).
2. `cd /tmp/sc && python3 -m scripts.package_skill /home/claude/anti-ai-design-style`.
3. Rebuild `anti-ai-design-review-bundle.zip` with this handover, the plan,
   the manifest, both iterations of the workspace.
4. **Cross-reference in the sibling skill.** The installed
   `anti-antropik-design` copy is a read-only cache. Do not edit it. Propose
   an update instead, via `propose_skills` in Cowork or a PR if it lives in
   a repo. Add one paragraph to its SKILL.md: "For distance from generic AI
   output, run `anti-ai-design-style` alongside. The two guards see different
   failures. 4 of 4 pages passed one and failed the other."
5. Deliver the `.skill`, the bundle, and the iteration-2 benchmark.

---

## 5. Every source, categorised (pointer, not a copy)

All 254 entries live in `reference/sources-compendium.md`. Each has: Source,
Context bullets, Tags, Feeds. Do not duplicate them here; edit them there.

| Category | IDs | Count | Covers |
|---|---|---|---|
| Practitioners | P1-P24 | 24 | designers, agencies, tool makers naming visual tells |
| Academic | A1-A24 | 24 | convergence, Design Homogeneity Index, code stylometry, image forensics, UI benchmarks |
| Community and wiki | C1-C26 | 26 | HN, Wikipedia, Indie Hackers, GitHub tell catalogs, tweakcn, unslop-ui |
| Code samples | K1-K15 | 15 | 12 cloned AI repos with counts + 3 cross-checks |
| Mobile and copy | M1-M20 | 20 | mobile tells, UI and marketing copy tells |
| Accessibility | X1-X29 | 29 | WCAG 2.2, COGA, BDA, plain language, GOV.UK |
| Prior art | R1-R20 | 20 | existing linters, skills, ban lists, vendor prompting guides |
| Visual science | V1-V20 | 20 | colour, imagery, illustration, icons, motion, rhythm |
| Library docs | L1-L76 | 76 | docs, licences, policies for the nine libraries |

Three synthesis sections sit at the end of the compendium. Those are the
ones that matter for building.

- **The AVOID map** (line ~2432): colour, typography, layout, components,
  imagery and iconography, motion, copy, code and provenance, mobile,
  library misuse. Every row cites IDs. This is the master ban list.
- **The ADOPT map** (line ~2614): process, palette, typography, structure,
  accessibility thresholds, honesty, motion discipline, functional libraries,
  verification.
- **Contested and stale** (line ~2780). Purple gradients: 16 sources for,
  measured 0/12 repos, humans did it first. Sparkle icons: NN/g vs Google.
  Cream/serif escape look: now itself a tell. Dyslexia fonts: do not work.
  APCA: advisory. Photo-trained AI detectors: fail on UI. Plus every claim
  with an expiry date.

Rule for anything new: read the contested section before promoting any
single source to a rule.

---

## 6. Everything missed or left open, in one list

**Status as of 2026-09-11.** Closed items keep their number so older notes still
line up.

| # | Item | Status |
|---|---|---|
| 1 | Evals re-run with the brand gate | **Closed** (aee812a). Iteration 2: with_skill 24/24, baseline 17/24, n = 1 per cell. All three baselines passed the AI-look guard and failed the brand guard. The gate was not tuned. |
| 2 | Nine libraries installed, gsap-skills and pixijs-skills vendored | **Closed** (commit 2e06f47). |
| 3 | Hookify rules and slash commands fired live | **Closed** (11a08b7, 7de9c0c). Four of the five had never fired; they bound to a field the event does not provide. |
| 4 | `config-guide` is Slack-only; use `debug-plugins` | **Closed.** Both are named plainly in the setup guide as not checking local Claude Code. |
| 5 | Description optimisation loop | **Run, and it measured nothing.** Every query scored a trigger rate of 0.0, both sides. The harness needs a tool call to detect and got none. No change applied. See `anti-ai-design-style-workspace/description-loop.md`. |
| 6 | Exa never connected | **Closed 2026-09-11** by Ben. Used once since, for the MB2 re-verification that produced MB4. The 2026-09 sweep was **not** re-run, and every dossier's stated route stands. |
| 7 | No Vue, React Native or Flutter samples; mobile tells thin | **Closed.** 27 new K entries, 24 cloned generated repos and a 413-file human-built control. Four mobile rules now ship: MB1, MB2, MB3 and MB4. |
| 8 | Register expires around 2028-03 | **Open by design.** "Keeping this register alive" now lives at the end of the register, with the steps. |
| 9 | Cross-reference from `anti-antropik-design` back to this skill | **Written, not applied.** `proposals/anti-antropik-design.md`. The installed copy stays read-only. |
| 10 | n=1 per eval cell | **Open, and stated.** Iteration 2's benchmark says it in the header and again in `benchmark.json` metadata. Still has to be said wherever a number is quoted. |
| 11 | `scripts/__pycache__/` in the tree | **Closed.** Stripped before packaging; the `.skill` is 0.63 MB. |
| 12 | Grader agents hit a 429 in iteration 1 | **Sidestepped.** Iteration 2 graded the mechanical assertions with a script (`workspace/tools/grade.py`) and the judgment ones by reading, so no grader agents were spawned. The 429 risk returns if anyone goes back to agent grading. |

New since the handover was written:

13. The register cited two different things with the same spelling. `P13` meant
    a research finding; `R3` meant a source. `scripts/check_citations.py` now
    fails if either kind stops resolving. 146 citations resolve.
14. `.dart` and `.kt` were not scanned at all, so no mobile rule could have
    fired. They are now, and rules can be scoped by file type.
15. Seven candidate tells did not replicate and are recorded as counter-evidence
    in the register, including the straight-down shadow. A human-built control
    hit it 49/49.
16. A `[STALE-RISK]` row said "re-verify before each release" and the release
    happened without it. Worse, the register claimed MB2 covered two Expo
    scaffolds and it only ever covered one. Source M36's `Feeds: MB2` was an
    overclaim, and that is what hid the gap. MB4 closes it. The maintenance
    checklist now has an eighth step: re-check the `[STALE-RISK]` rows.
17. The two guards are close to orthogonal, and now there is a mechanism. Every
    baseline brand failure in iteration 2 was a warm cream inside Delta-E 12 of
    the brand neutrals. The cream-editorial escape from the AI look lands inside
    the brand violation zone. A page can satisfy one guard by failing the other.
18. `side-tab` is **measured and refuted**, not an open gap. 2 of 12
    verified-generated repos carry one, and 9 of the 12 instances are in a
    single repo's admin dashboard. MB3 cleared at 5 of 12. No rule; a
    counter-evidence row in the register and the full method in
    `research/16-side-tab-tailwind.md`. The page that raised it was a
    hand-authored fixture with no Lovable provenance marker, so its three
    side-tabs record a belief rather than a measurement. Bare Inter remains a
    deliberate difference, since TY2 is a pairing rule. A flat type scale
    needs computed sizes and belongs in `render_check.py`. Note the correction
    in `cross-tool-findings.md`. The first write-up used design-hook messages
    and was wrong. All six iteration-2 artifacts are clean under the other
    tool's own detector.
19. `a8` library misuse scored 0 in all six iteration-2 runs and never
    discriminated. No eval uses an animation or map library. A fourth eval
    would give the assertion something to score.

## 7. Non-negotiables for whoever picks this up

- Never weaken `rules.json` or a threshold to make a scan pass.
- Never add a tell from memory. Source ID in the compendium first.
- Never hand-pick a hex value. `generate_palette.py`, then `audit_file.py`.
- Never present a page without all three scanners and the proof line:
  `PASS: AI-look 0/100 (distinct), craft flags 0, library misuse 0, copy
  grade 4.6, brand distance COMPLIANT, rendered PASS | register 2026.10,
  rules 6b7abae241e662e5, brand rules 5697117fa1b27195 (installed)`
  Quote what `verify_all.py` printed. Never compose the line by hand.
- Never claim "proven human-made". The scanner measures the AI look.
- Never edit the installed `anti-antropik-design` copy. Propose instead.
- Write for a non-technical, possibly neurodivergent reader in every file
  a user opens. One action per step. Plain words. Time estimates.
