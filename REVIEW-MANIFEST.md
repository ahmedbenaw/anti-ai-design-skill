# Review manifest v2: everything built in this session

**TL;DR:** the skill is rebuilt, re-tested and repackaged. Ship
`anti-ai-design-style.skill` as-is. It now carries 37 files, including all
254 tagged sources and the nine ported libraries.

## What changed since v1

1. **You caught a real defect.** The v1 fixed example scored 0 on the AI-look
   scanner and still looked like Claude's design system. Warm cream, bookish
   serif, terracotta accent. The register had already named that trap as rule
   CO6. The example walked into the rule that describes it.
2. **It is now measured, not argued.** `anti-antropik-design` scored the v1
   file: background 2.74 Delta-E from a brand neutral, where 12 or more is
   required, and Georgia is an excluded typeface. NON-COMPLIANT.
3. **Two guards now, not one.** `SKILL.md` Step 3 requires the brand-distance
   scan alongside its own. Palettes are generated, not picked.
4. **Nine libraries ported natively.** GSAP, anime.js, animate.css,
   animate-ui, Lenis, PixiJS, uiverse galaxy, Leaflet with plugins, SurveyJS.
   Read from their live docs, with adopt and avoid guidance for each.
5. **Twelve library-misuse rules** added to the scanner, with their own
   selftest fixture.
6. **254-entry sources compendium** with ADOPT and AVOID tags on every source.

Three bundles:

1. `anti-ai-design-style.skill` (312 KB): **the deliverable.** 37 files.
2. `anti-ai-design-style-workspace/`: the v1 eval runs. Evidence, not skill.
3. `PLAN-anti-ai-design-style.md`: the updated plan, tasks 0 to 12.

Measured state right now:

| Check | Result |
|---|---|
| AI-tell scanner selftest | PASS (incl. new library fixture, 9 rules caught) |
| Copy-checker selftest | PASS |
| Bad example page | 52/100, FAIL (correct) |
| Fixed example page (v2) | 0/100, PASS (correct) |
| Fixed example, brand guard | **COMPLIANT, 0 violations** |
| User-facing docs vs the copy checker | PASS |
| skill-creator structure validation | Valid |
| Eval assertions, with skill (v1 run) | 18/18 |
| Eval assertions, baseline (v1 run) | 15/18 |

---

## Part 1: Inside the skill (all ship together)

| File | Size | What it is | Verdict |
|---|---|---|---|
| `SKILL.md` | 12 KB | **The skill itself.** Workflow, scoring model, refusals. 185 lines. | SHIP — this is the skill |
| `commands/design-brief.md` | 1 KB | Claude Code slash command. | SHIP — Claude Code only, optional |
| `commands/design-check.md` | 1 KB | Claude Code slash command. | SHIP — Claude Code only, optional |
| `commands/design-fix.md` | 1 KB | Claude Code slash command. | SHIP — Claude Code only, optional |
| `evals/evals.json` | 4 KB | 3 test prompts with assertions. | SHIP — rerun after any rule change |
| `examples/README.md` | 3 KB | Before/after explainer with the measured scores. | SHIP |
| `examples/fixed-example.html` | 7 KB | Same product redesigned. Scores 0 (PASS). | SHIP — regression fixture |
| `examples/slop-example.html` | 6 KB | Deliberately AI-looking page. Scores 52 (FAIL). | SHIP — regression fixture |
| `hookify/hookify.ai-copy-tells.local.md` | 790 B | Claude Code warning rule (hookify format). | SHIP — Claude Code only, optional |
| `hookify/hookify.ai-fake-proof.local.md` | 756 B | Claude Code warning rule (hookify format). | SHIP — Claude Code only, optional |
| `hookify/hookify.ai-gradient-tells.local.md` | 904 B | Claude Code warning rule (hookify format). | SHIP — Claude Code only, optional |
| `hookify/hookify.design-scan-before-done.local.md` | 647 B | Claude Code warning rule (hookify format). | SHIP — Claude Code only, optional |
| `reference/accessibility.md` | 4 KB | Exact WCAG 2.2 / COGA / BDA thresholds with criterion numbers. | SHIP |
| `reference/brand-distance.md` | 4 KB | The second guard. Why passing this skill's scanner is not the same as being distinct, the v1 defect that proved it, and how to generate palettes instead of picking them. | SHIP - read with the examples |
| `reference/fixes.md` | 5 KB | How to fix each finding, plain words + code snippets. | SHIP |
| `reference/setup-guide.md` | 4 KB | Plain-language install guide, 4 parts, ADHD-friendly format. | SHIP |
| `reference/sources-compendium.md` | 182 KB | **All 254 sources**, one entry each: context bullets, ADOPT/AVOID tags, and which rule it feeds. Ends with the master AVOID map, the ADOPT map, and contested/stale claims. | SHIP - the answer to "says who?" |
| `reference/sources.md` | 2 KB | Index of the 174 sources and three honesty caveats. | SHIP |
| `reference/tells-register.md` | 21 KB | **The verified register.** ~60 tells, each with sources, weight, era tag, false-positive note. The evidence spine. | SHIP — review this one closely |
| `reference/libraries/README.md` | 5 KB | Index for the nine ported libraries plus the one rule that governs all of them. | SHIP |
| `reference/libraries/maps-forms.md` | 80 KB | Leaflet with its categorised plugin table, and SurveyJS with its licence split spelled out. | SHIP - the two antidote libraries |
| `reference/libraries/motion.md` | 66 KB | GSAP, anime.js, animate.css, animate-ui: install, real API, adopt/avoid, reduced-motion, scanner signatures, licence facts. | SHIP |
| `reference/libraries/scroll-canvas-ui.md` | 72 KB | Lenis, PixiJS, uiverse galaxy: same structure, plus scroll-hijacking and canvas-accessibility cases. | SHIP |
| `reference/research/01-practitioners.md` | 44 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/02-academic.md` | 23 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/03-community-wiki.md` | 25 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/04-code-patterns.md` | 21 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/05-mobile-and-copy.md` | 28 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/06-accessibility.md` | 33 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/07-prior-art.md` | 26 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `reference/research/08-visual-science.md` | 31 KB | Full research dossier with source table, quotes, counter-evidence, gaps. | SHIP (bundled evidence) |
| `scripts/ai_tell_scan.py` | 21 KB | Scanner: AI-look score + craft flags. Stdlib-only Python, has --selftest. | SHIP — the core engine |
| `scripts/copy_check.py` | 11 KB | Copy checker: readability grade, long sentences, AI phrasing, fake stats. Has --selftest. | SHIP |
| `scripts/rules.json` | 25 KB | Machine-readable rules: every pattern, weight, plain-language explain + fix. | SHIP — edit this to tune |
| `scripts/__pycache__/copy_check.cpython-311.pyc` | 18 KB |  |  |
| `templates/design-brief.md` | 3 KB | The 7-question DESIGN.md template. The highest-impact piece. | SHIP |
| `templates/prompt-packs.md` | 4 KB | Copy-paste prompts for Lovable, Bolt, v0, Cursor. | SHIP |
**If you only read four files:** `SKILL.md`, `reference/brand-distance.md`
(the defect and the fix), `reference/sources-compendium.md` (every source,
tagged), and `reference/libraries/README.md` (the nine, and the one rule).

## Part 2: Test evidence (review, then keep or bin)

| File | What it is | Verdict |
|---|---|---|
| `anti-ai-design-style-workspace/benchmark.md` | With-skill vs no-skill, plus an honest "what this does not prove" section. | READ IT, then bin |
| `.../iteration-1/<eval>/with_skill/outputs/` | What Claude produced with the skill. A clinic site, a student budget screen, a de-slopped Lovable page. | Open the HTML |
| `.../iteration-1/<eval>/without_skill/outputs/` | The same three tasks without the skill. | Compare, then bin |
| `.../scan.json`, `copy.json`, `grading.json`, `timing.json` | Raw measurements per run. | Bin unless you want the numbers |

Note: these eval runs are from v1. They do not exercise the library rules or
the brand guard. Re-running them is open item 1 in the plan.

## Part 3: What to do in Claude Code

1. **Unzip the .skill into `~/.claude/skills/anti-ai-design-style/`.**
2. **Install `anti-antropik-design` alongside it.** The brand-distance guard
   is now a required step, and its palette generator is the recommended way
   to choose colours. Without it you lose half the verification.
3. **Optional, 3 minutes:** copy `hookify/*.md` into `.claude/` and
   `commands/*.md` into `.claude/commands/`, then replace `<skill-path>`.
4. **Do not rewrite the register from memory.** Change `scripts/rules.json`
   and the matching row in `reference/tells-register.md` in the same edit.
   Then run `python3 scripts/ai_tell_scan.py --selftest` and the three evals.

## Part 4: Known limits

1. **It reads code, not pixels.** A page can pass and still look bad. The
   judgment checks in `SKILL.md` cover what a script cannot.
2. **A PASS never means "human-made".** No honest tool can prove that.
3. **The register goes stale.** Eras run about 18 months. Purple gradients,
   then shadcn defaults, then the cream-and-serif escape. Version 2026.09 is
   dated on purpose.
4. **The v1 eval numbers are stale too.** They predate the library rules and
   the brand guard.
5. **The nine libraries are ported as guidance, not vendored code.** The skill
   carries their install commands, real API snippets, adopt and avoid rules,
   and misuse signatures. It does not ship their source. That is deliberate:
   a `.skill` is a documentation and script bundle, and vendoring npm packages
   into it would rot within months.
6. **Exa was never connected**, so research used web search, page fetches and
   the arXiv database. 254 sources, all opened.

## Part 5: Three things worth arguing with

1. **"Full adoption" of the animation libraries cuts against the skill's own
   thesis.** animate.css is the canonical fade-up-on-scroll library. uiverse
   galaxy is a copy-paste component gallery, which is the exact failure mode
   this skill exists to prevent. They are ported with that stated plainly, as
   a capability layer with a discipline, not as a recommendation to use them.
2. **Leaflet and SurveyJS are the two that actually matter here.** They add
   function, not motion. They are the direct cure for the strongest tell in
   the register, which is polish without depth. The other seven are optional.
3. **The measured gap between skill and baseline is still modest.** 18/18 vs
   15/18 on v1. The real wins were accessibility craft and refusing to keep
   fake testimonials. Not "the definitive guard against AI design".
