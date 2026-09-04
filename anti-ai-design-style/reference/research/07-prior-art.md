# Prior art: detectors, linters, skills, prompt fixes

Survey date: 2026-08-28. Every item below was opened and read (README, skill file, or article). Sources are numbered; the number is reused in later sections.

## Inventory

| # | Name | Type | Language | Licence | Last activity | URL | What it checks |
|---|------|------|----------|---------|---------------|-----|----------------|
| 1 | ux-skill (Laith0003) | Deterministic anti-slop linter + design engine + MCP server | Python (regex rules), JSON data | MIT | Active 2026 (v3.0) | https://github.com/Laith0003/ux-skill | 152 regex rules in 9 categories (a11y 23, content 15, layout 13, typography 10, color 9, quality 9, visual 9, motion 8, perf 4); 160 brand DESIGN.md specs; 7-axis token synthesizer |
| 2 | unslop-ui-skill (claudiusararu) | Agent skill + tells catalog | Markdown (no deps) | MIT | Active 2026 | https://github.com/claudiusararu/unslop-ui-skill | ~100 catalogued "AI design tells" (TELLS.md) with rationales + self-check list; installs into Claude Code/Cursor/Windsurf |
| 3 | impeccable (pbakaus) | Agent skill / design language | Markdown | (repo licence; open source) | Active 2026 | https://github.com/pbakaus/impeccable (skill/SKILL.src.md) | 13 absolute banned patterns, OKLCH-only color rules, contrast floors, typography/motion/copy rules, "two-altitude" slop test |
| 4 | Anthropic frontend-design skill | Agent skill (official) | Markdown | Anthropic skills repo licence | Active 2026 | https://github.com/anthropics/skills (frontend-design/SKILL.md) | Names 3 clustered AI default looks (warm-cream+serif+terracotta; near-black+acid accent; broadsheet/hairline); rules for deliberate type pairing, 4–6 named hex palette tied to subject, restrained motion |
| 5 | avoid-ai-design (funboy322) | Agent skill (audit + rewrite) | Markdown | MIT | Active 2026 | https://github.com/funboy322/avoid-ai-design | Tells across 6 categories with P0/P1/P2 severity; 5-step audit→commit-to-direction→rewrite→re-audit workflow; HTML/CSS and React/Tailwind/shadcn |
| 6 | open-design anti-ai-slop.md (nexu-io) | Rules file with exact hex banlist | Markdown | Repo licence (open) | Active 2026 | https://github.com/nexu-io/open-design/blob/main/craft/anti-ai-slop.md | "Seven cardinal sins" (P0) incl. exact banned Tailwind indigo/violet hexes, banned emoji icons, banned gradients; P1 soft tells with numeric thresholds (>12 raw hexes outside :root, accent used 6+ times) |
| 7 | design-deslop command (Dammyjay93/interface-design) | Agent slash command | Markdown | Repo licence (open) | Active 2026 | https://github.com/Dammyjay93/interface-design/blob/main/.claude/commands/design-deslop.md | Two-pass de-slop: rendered "squint test" (focal point, hierarchy, timid color, borders-as-structure) + diff-level scan (tokens, states, spacing grid) |
| 8 | design-anti-slop (prathameshagrawal) | Agent skill | Markdown | MIT | Active 2026 | https://github.com/prathameshagrawal/design-anti-slop | 25 named anti-patterns in 3 layers (visual V1–V9, structural S1–S9, conceptual C1–C7); pre-generation question mode + post-generation audit mode |
| 9 | @projectwallace/css-analyzer | CSS analytics library | TypeScript | MIT | Active (v9.9.0, 100+ releases) | https://github.com/projectwallace/css-analyzer | 150+ metrics: unique colors, font-families, font-sizes, z-indexes, shadows, specificity, complexity, uniqueness ratios |
| 10 | axe-core (Deque) | Accessibility rules engine | JavaScript | MPL-2.0 | Very active | https://github.com/dequelabs/axe-core | WCAG 2.0/2.1/2.2 A/AA/AAA + best practices incl. color-contrast; ~57% of WCAG issues automatable; a11y only, no design-quality checks |
| 11 | wcag-contrast (tmcw) | Colour-contrast micro-library | JavaScript | BSD-2-Clause | Mature/stable | https://github.com/tmcw/wcag-contrast | luminance/rgb/hex contrast ratio + score() letter grade; author himself flags WCAG-ratio limits and points to Lighthouse/axe for page-level testing |
| 12 | tinycss2 | CSS parser | Python ≥3.10, no deps | BSD-3-Clause | v1.5.1, Nov 2025 | https://pypi.org/project/tinycss2/ | CSS Syntax Level 3 tokenizer/block parser; no selector or property semantics |
| 13 | textstat | Readability metrics | Python ≥3.6 | MIT | v0.7.13, Feb 2026 | https://pypi.org/project/textstat/ | Flesch, FK grade, SMOG, Coleman-Liau, ARI, Dale-Chall, Gunning Fog + counts; multilingual variants |
| 14 | Bolt "10 prompt keywords" | Vendor prompting guide | Article | — | 2025 | https://bolt.new/blog/10-prompt-keywords-to-make-your-app-look-fire | Named-aesthetic keywords (neumorphism, glassmorphism, brutalism, claymorphism, …) as levers against generic output |
| 15 | Vercel "How to prompt v0" | Vendor prompting guide | Article | — | 2025 | https://vercel.com/blog/how-to-prompt-v0 | 3-part framework: product surface, context of use, constraints & taste ("Constraints tell v0 what not to invent") |
| 16 | Lovable prompting docs | Vendor prompting guide | Docs | — | Active | https://docs.lovable.dev/prompting/prompting-one | Context/task/guidelines/constraints structure; knowledge files as persistent design direction; atomic UI vocabulary; real content over placeholders |
| 17 | DESIGN.md × Google Stitch guide | Format guide | Article/docs | Open format | 2026 | https://designmd.app/guides/google-stitch/ | DESIGN.md sections: colors (hex), type scale, spacing scale, component patterns with concrete values, Do/Don't constraints; portable across Stitch, Claude Code, Cursor, Kiro, Windsurf |
| 18 | "Why Your AI Keeps Building the Same Purple Gradient Website" | Analysis article w/ experiments | Article | — | 2025/26 | https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website | Root-cause analysis (Tailwind indigo default → training-data median) + side-by-side prompt experiments across Claude/GPT-5/Gemini/v0 |
| 19 | AIMultiple AI image detector benchmark | Detector benchmark | Article | — | 2026 | https://aimultiple.com/ai-image-detector | 7 detectors (SightEngine, Hive, Illuminarty, …) benchmarked on photoreal images; "most perform no better than a coin toss" |
| 20 | Anthropic blog "Improving frontend design through Skills" | Vendor evidence post | Article | — | 2025/26 | https://claude.com/blog/improving-frontend-design-through-skills | Names the problem "distributional convergence"; before/after comparisons for landing page, blog, dashboard |

Also surfaced but not opened in depth (candidates for follow-up): projectwallace/stylelint-plugin and css-code-quality, stylelint-plugin-carbon-tokens and Kong design-tokens stylelint plugin (token-enforcement prior art), spencergoldade/cursor-designer, theclaymethod/unslop, GitHub topics `anti-slop` / `ai-slop-detection`, PatrickJS/awesome-cursorrules (design entries are stack-focused, not aesthetics-focused), leaked v0 system prompts (jasonkneen gist; 2-fly-4-ai/V0-system-prompt).

## Detailed notes per item

### 1. ux-skill — the most complete prior art for a *deterministic* scanner
- Architecture: `bin/ux-lint.py`, a Python regex scanner reading rules from `data/anti-patterns.json` (bash fallback). CI-safe: non-zero exit on Critical/High findings; ~200ms on a typical project. Offline, never calls an LLM, deterministic (same input → same output).
- Rule examples: Inter as display font; arbitrary oversized hero font sizes; purple→blue "default AI gradient"; centered hero with gradient background; three equal cards in a row; over-tall sticky headers; "John Doe" placeholders; generic CTAs; "celebratory AI-cheerful copy".
- Scoring: lint score 0–100; a decisions ledger (`.ux/decisions.jsonl`) only counts a run when `lint_score >= 80 AND user_accepted = true`.
- Generation side: 7-axis synthesizer (warmth, contrast, density, geometry, formality, motion, type personality) compiles briefs into fresh tokens instead of selecting templates; 160 brand DESIGN.md specs, 176 palettes, 70 type pairings, 57 motion presets ship as JSON data.
- Reusable: the rule format (pattern + evidence template + fix guidance in JSON) and the CI exit-code convention are directly imitable; the JSON manifests are MIT.
- Weaknesses: tiny adoption (~63 stars); very large surface (25 commands, 18 MCP tools, 17 IDEs) for what is at core a regex linter; regex-on-source can't see rendered output (a purple gradient built from CSS vars at runtime escapes it).

### 2. unslop-ui-skill — the best *catalog* of tells
- `TELLS.md` documents ~100 recurring AI design tells with rationales. Sample: purple→blue gradient accents; Inter/Geist everywhere; cream background `#faf8f4`; grey low-contrast body text; pill-shaped "eyebrow" badges above heroes; icon-card grids ("three lucide icons in rounded squares"); fade-up-on-scroll on every element; repetitive em-dashes in copy; predictable spacing; missing typographic hierarchy.
- Mechanism: pure constraint prose + a qualitative "self-check" section the agent runs against its own output. No scoring, no code.
- Reusable: MIT; TELLS.md is a ready-made seed list for regex/heuristic rules.
- Weakness: no automation at all; enforcement depends on the model actually re-reading the checklist.

### 3. pbakaus/impeccable — the most opinionated rules, with numeric thresholds
- 13 "absolute refuses": side-stripe borders (border-left/right >1px as accent); gradient text (`background-clip: text`); glassmorphism as default; hero-metric template; identical card grids; eyebrow on every section; 01/02/03 numbered markers as scaffolding; ghost-card (1px border + 8px+ blur shadow); border-radius ≥24px on cards (cap 12–16px); hand-drawn/doodle SVG; `repeating-linear-gradient()` stripes; "not just X, it's Y" copy.
- Quantified rules a scanner can lift directly: body contrast ≥4.5:1 (large text 3:1, placeholders 4.5:1); line length 65–75ch; type scale ratio ≥1.25; ≤3 font families; display clamp ≤6rem; letter-spacing ≥ −0.04em; tinted neutrals limited to 0.005–0.015 OKLCH chroma toward brand hue; every animation needs a `prefers-reduced-motion` alternative; z-index from a named scale, no 999/9999; no em dashes; banned buzzwords (streamline, empower, supercharge, leverage, seamless, world-class).
- Novel idea: the **two-altitude test** — first-order failure if theme+palette are guessable from the product category alone; second-order failure if the aesthetic *family* is still guessable even after anti-references. This is a judgment test no linter replicates.
- Weakness: prose-only; several rules (scene-based theme choice, "cards only when truly best affordance") are unlintable.

### 4. Anthropic frontend-design skill
- Now names three *clusters* of AI default looks, including the post-2025 correction defaults: (a) warm cream near `#F4F1EA` + high-contrast serif display + terracotta accent; (b) near-black + single acid-green/vermilion accent; (c) broadsheet layout, hairline rules, zero radius, dense columns. Key line: "All three are legitimate for some briefs, but they are defaults rather than choices, and they appear regardless of subject." (Important: the *escape* aesthetics from the purple-gradient era have themselves become tells.)
- Rules: 4–6 named hex values tied to the subject; deliberate display/body pairing; "structure is information" (numbering/dividers must encode real meaning); "sometimes less is more" on motion.
- Weakness: guidance only, no measurement; and per source 20 the evidence Anthropic publishes is before/after screenshots, not evals.

### 5. avoid-ai-design — severity model worth copying
- Six tell categories; concrete entries include: untouched shadcn `zinc`/`slate` palettes; `rounded-2xl shadow-lg` reflexes; hero+three-cards+CTA template; three-tier pricing with highlighted middle ring; four-column footers; uniform `gap-4`/`p-6`; DiceBear avatars; Lucide `Sparkles`/`ArrowRight`; "Elevate/Seamless/Powerful" copy.
- Process: scope → audit (optionally render) → *commit to one aesthetic direction* → calibrated rewrite (surgical for components, bold for standalone pages) → re-audit until P0 clear. Severity: P0 "screams AI" / P1 "obvious smell" / P2 cosmetic.
- Reusable: MIT; the P0/P1/P2 triage and the "surgical vs bold depending on blast radius" calibration.

### 6. nexu-io/open-design anti-ai-slop.md — the only source with an exact hex banlist
- P0 "seven cardinal sins" include machine-checkable specifics: banned accent hexes `#6366f1 #4f46e5 #4338ca #3730a3 #8b5cf6 #7c3aed #a855f7` (Tailwind indigo/violet/purple); banned two-stop hero gradients (purple→blue, blue→cyan, indigo→pink); banned emoji-as-icons (✨🚀🎯⚡🔥💡) in headings/buttons/lists; display headings must use `var(--font-display)` not hardcoded Inter/Roboto/system-ui; rounded card + colored left border = "the canonical AI dashboard tile"; invented metrics ("10× faster", "99.9% uptime") without source; lorem ipsum / "feature one/two/three".
- P1 numeric thresholds: >12 raw hex values outside `:root`; accent var used 6+ times per screen (cap 2); placeholder-image CDNs (unsplash.com, placehold.co); unvaried Hero→Features→Pricing→FAQ→CTA sequence. P2: decorative blob/wave SVGs; perfect symmetry.
- Reusable: the hex list, emoji list and thresholds drop straight into a Python scanner.

### 7. design-deslop (interface-design repo)
- Two-pass model that separates what needs *rendering* from what a *diff* can catch — exactly the split a scanner design must make. Pass 1 (rendered squint test): no focal point; flat hierarchy; monotone layout; timid color (fix: one accent at ~10% coverage); borders used as structure. Pass 2 (source scan): semantic tokens over generic names; missing hover/focus/active/disabled states; transitions without explicit properties, custom easing <300ms; off-grid spacing values; negative-margin/absolute-positioning hacks; hand-rolled controls instead of accessible primitives.
- Guardrails worth copying: behavior-preserving, diff-scoped, intentional bold choices are exempt, patterns ratified in a project `system.md` are exempt (an allowlist mechanism — rare in this space).

### 8. design-anti-slop (prathameshagrawal)
- 25 named anti-patterns, IDs V1–V9 / S1–S9 / C1–C7 (visual/structural/conceptual). Structural layer is its distinct contribution: canonical hero, three-box grid, logo carousel, bento grid, dashboard-sidebar, KPI card row. Conceptual: empty aspirational language, generic sections, missing functional states.
- Framing: "AI design slop is a statistical problem, not an aesthetic one" — fixes it *pre-generation* by asking four targeted questions before any code, rather than banning aesthetics post-hoc. Post-generation mode audits visual→structural→conceptual and ranks fixes by impact.
- Reusable: the ID scheme (stable rule identifiers) and the pre-/post-generation split.

### 9. projectwallace/css-analyzer
- Computes exactly the aggregate signals a slop scanner needs: unique color count and uniqueness ratio, font-family/font-size distributions, z-index inventory, shadow counts, selector complexity. JS/TS only — usable as the reference implementation to mirror in Python. Sibling repos: `css-code-quality` (weighted quality score from "quality guards" — prior art for scoring), `css-design-tokens` (extract tokens from CSS), `wallace-cli`.

### 10. axe-core / 11. wcag-contrast
- axe-core: the a11y baseline; color-contrast rule notably does NOT work under JSDOM (needs a real browser render) — a constraint for any pipeline that wants contrast checking without a browser: compute contrast yourself from parsed colors instead. ~57% of WCAG automatable; MPL-2.0.
- wcag-contrast: 4 functions, BSD-2; trivial to port (the WCAG relative-luminance formula is ~15 lines of stdlib Python — no dependency needed).

### 12. tinycss2 / 13. textstat
- tinycss2: BSD, zero-dependency, tokenizer + block parser only — sufficient for extracting declarations, hex/oklch values, font stacks, gradients; it will not resolve `var()` or selectors semantically.
- textstat: MIT, computes all the classic readability formulas; relevant to slop *copy* checks (marketing-buzzword density is better done with a plain wordlist, but grade-level uniformity is a weak AI-copy signal).

### 14–16. Vendor prompting guides (Bolt, v0, Lovable)
- Bolt: named aesthetic keywords (brutalism, claymorphism, glassmorphism, retro/vaporwave, hyper-minimalism…) as one-word levers; thesis: "precision of language" beats "clean UI".
- v0 (Vercel official): three-part prompt — product surface (exact components + data), context of use (role, time pressure, environment), constraints & taste ("Constraints tell v0 what not to invent"). They report measurable side-effects of specificity: 19s faster generation, 152 fewer LOC in their example. Use prompts for logic, Design Mode for visual tweaks.
- Lovable (official docs): layered prompt structure (context → task → guidelines → constraints); build modularly per component; put recurring design direction in **knowledge files** so "Lovable then applies your design direction to every prompt without you restating it"; use real content, not placeholders; atomic UI vocabulary (cards, badges, modals); buzzwords mapped to concrete treatments ("premium and cinematic" → layered depth, translucent surfaces, soft motion blur, dramatic contrast).

### 17. Google Stitch DESIGN.md
- An open, portable design-spec format: colors as hex swatches, typographic scale, spacing scale, component patterns *with concrete values* ("rounded-lg, py-2 px-4, bg brand-primary"), plus an explicit **Do's and Don'ts constraints section**. Stitch imports it (no file-watching); the same file works in Claude Code, Cursor, Kiro, Windsurf. Recommended practice: keep it in git. This is the emerging interchange format an anti-slop skill should emit/consume rather than inventing a new one.

### 18. prg.sh purple-gradient article — root cause + comparative evidence
- Mechanism claim: Tailwind's `bg-indigo-500` default (~2019) saturated tutorials → training data → "you're getting the median of every Tailwind CSS tutorial scraped from GitHub."
- Fixes tested with side-by-side outputs on 3 UI types across Claude, GPT-5, Gemini, v0: (1) constrain typography/color/motion/background separately; (2) reference specific aesthetics ("1970s ski lodge palette"); (3) explicit negative constraints ("Do not use Inter, Roboto… No purple gradients on white"); (4) Anthropic cookbook aesthetics XML prompt; (5) extract-then-feed descriptions of 3–5 admired reference designs; (6) senior-designer role + ask for three directions. Constrained versions were visibly more distinctive; Claude responded best to strong constraints; v0's shadcn specialization noted.

### 19. AI-image detectors for UI screenshots — negative result
- AIMultiple's 7-detector benchmark: "most perform no better than a coin toss"; systematic false negatives (AI images classed real) and false positives on authentic images; wildly inconsistent confidence. Critically, all test material was *photorealistic*; none of the detectors was evaluated on rendered UI, whose properties (flat fills, crisp vector type, exact geometry) violate the camera-noise/GAN-artifact assumptions these models rely on. Conclusion for the skill: screenshot-level "is this AI?" classification is a dead end; detect *design patterns*, not pixels.

### 20. Anthropic evidence post
- Coins the term "distributional convergence" for the phenomenon. Evidence offered is qualitative before/after screenshots (landing page, blog, dashboard), not benchmarks — honest caveat when citing it.

## Reusable building blocks for a dependency-light Python scanner

Preference order: stdlib first, then single small BSD/MIT deps.

| Block | Licence | Install | Why |
|-------|---------|---------|-----|
| `re`, `html.parser`, `colorsys`, `collections.Counter` (stdlib) | PSF | none | Regex tell-matching (the entire ux-skill linter is regex); `html.parser.HTMLParser` extracts inline styles/classes/text without bs4; `colorsys` for RGB↔HLS when clustering hues; Counter for uniqueness ratios à la css-analyzer |
| WCAG contrast, hand-ported | formula is public (WCAG 2.x) | none (~15 lines) | Avoids axe-core's browser requirement and the npm dep; tmcw/wcag-contrast (BSD-2) is the reference implementation to port |
| Hex/emoji/word banlists from sources 2, 3, 6 | MIT / open | none (data file) | Ready-made: 7 indigo/violet hexes, 6 emoji icons, buzzword list (streamline, empower, seamless, elevate…), `#faf8f4` cream, `#F4F1EA` cream, gradient-pair list |
| Numeric thresholds from sources 3, 6, 7 | MIT / open | none (config) | ≤3 font families; type ratio ≥1.25; radius cap 16px; ≤12 raw hexes outside :root; accent ≤2 uses/screen; contrast ≥4.5:1; line length 65–75ch; transitions <300ms; z-index whitelist |
| tinycss2 | BSD-3 | `pip install tinycss2` | Only if regex extraction proves too brittle for real CSS (comments, nested at-rules); zero transitive deps |
| textstat | MIT | `pip install textstat` | Optional copy-quality axis; skip if buzzword wordlist suffices (it usually does) |
| ux-skill rule format (`anti-patterns.json`: pattern + severity + evidence template + fix) | MIT | n/a (imitate) | Proven schema; keep CI convention: exit non-zero on Critical/High |
| css-analyzer metric set | MIT | n/a (imitate in Python) | Defines which aggregates matter: unique-color count, font-family count, shadow census, z-index census |
| DESIGN.md (Stitch format) | open format | n/a | Emit findings/fixes against a DESIGN.md; consume one as the project's allowlist (cf. design-deslop's `system.md` ratification idea) |

Explicitly avoid: axe-core in-process (needs browser for contrast), Node toolchains (stylelint, css-analyzer as runtime deps), any AI-image detector (source 19), BeautifulSoup/parse5 (stdlib `html.parser` covers extraction needs; bs4 is fine as an optional nicety but not needed).

## Prompt-level fixes with evidence

| Fix | Who reports it works | Source # | Caveats |
|-----|----------------------|----------|---------|
| Explicit negative constraints ("no Inter/Roboto, no purple gradients on white") | prg.sh author, with side-by-side outputs across 4 models | 18 | Bans breed *new* defaults: Anthropic's own skill now lists the cream+serif+terracotta and near-black+acid-accent "escape" looks as tells (4). Ban lists must be versioned. |
| Separate constraints per dimension (typography / color / motion / background), e.g. Anthropic cookbook aesthetics XML | prg.sh comparisons; Anthropic before/afters | 18, 20 | Anthropic's evidence is screenshots, not evals. |
| Reference-first prompting: describe 3–5 admired real designs, or name a concrete aesthetic ("1970s ski lodge") | prg.sh; Bolt (named-style keywords); Lovable (buzzword→treatment mapping) | 18, 14, 16 | Named styles (glassmorphism…) are themselves clichés if used solo — combine or specify further (14). |
| Brand/spec-first prompting via persistent files: DESIGN.md (Stitch), Lovable knowledge files, ux-skill brand specs | Stitch/DESIGN.md ecosystem; Lovable official docs; ux-skill's 160 shipped specs | 17, 16, 1 | Stitch does not watch the file — re-import after edits (17). Effectiveness depends on spec concreteness ("rounded-lg, py-2 px-4" beats "modern buttons"). |
| Specificity over adjectives: exact components + data + user context + constraints | Vercel official (19s faster, −152 LOC in their example); Lovable ("vague ideas produce vague outputs") | 15, 16 | Vercel's numbers are a single worked example, not a study. |
| Real content instead of placeholders | Lovable docs; echoed by tell-lists banning "John Doe"/lorem ipsum | 16, 1, 6 | — |
| Commit to ONE aesthetic direction before rewriting; surgical vs bold calibration by blast radius | avoid-ai-design workflow | 5 | — |
| Pre-generation interrogation (4 targeted questions before any code) rather than post-hoc bans | design-anti-slop; framing: slop is statistical, fix is upstream specificity | 8 | No quantitative evidence published. |
| Self-check / re-audit loop until P0 tells cleared | unslop-ui-skill self-check; avoid-ai-design re-audit step; impeccable two-altitude test | 2, 5, 3 | Relies on model honesty; deterministic linting (1) exists precisely because self-checks drift. |

## What nobody has built yet (gaps)

1. **A dependency-light, stdlib-first Python scanner as a standalone artifact.** ux-skill (1) proves regex linting works but buries it inside a 25-command, 18-tool platform. Nothing exists that is `pip install`-free, single-file, CI-friendly, and only scans.
2. **Rendered-output metrics without a browser.** Every tool is either source-regex (1, 6) or "look at it" prose (7's squint test). No one computes layout-level signals (symmetry, card-grid uniformity, accent-coverage %, focal-point presence) from parsed HTML+CSS statically.
3. **A versioned, dated tell registry.** The defaults drift: purple-gradient era → cream/serif/terracotta era (4). All current ban lists are snapshots with no versioning, deprecation, or "this ban has itself become a tell" mechanism.
4. **Scoring with calibration data.** ux-skill's 0–100 score and css-code-quality's guards are the only scoring attempts; neither publishes validation against human "looks AI" judgments. No labeled corpus of AI vs. human-designed UIs exists at all.
5. **An allowlist/ratification protocol.** Only design-deslop (7) exempts project-ratified patterns. Combining a scanner with a DESIGN.md-as-allowlist (17) — findings suppressed when the spec explicitly chose the pattern — is unbuilt.
6. **Cross-checking copy + visuals + structure in one pass.** Copy tells (buzzwords, em-dashes, invented metrics), visual tells (hexes, radii), and structural tells (hero+3 cards, bento) live in separate tools; no scanner unifies the three layers of source 8 into one report.
7. **Screenshot-level detection that works.** Source 19 shows photo-oriented AI-image detectors are unreliable even in-domain and untested on UI; a purpose-built "does this screenshot look AI-designed" classifier (trained on UI, not photos) does not exist — and given gap 4 (no corpus), can't yet.
8. **Evidence.** Nothing in this space — including Anthropic's official skill — publishes quantitative evals. Even a small human-rated A/B corpus would exceed the current state of the art.
