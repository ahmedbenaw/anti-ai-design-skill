# The tells register

**What this file is.** Every "AI design tell" this skill acts on, with the evidence
behind it. Nothing in the skill's rules or scanner exists without an entry here.
Register version: **2026.09** (dated on purpose: tells drift; see "Why this
register is dated" at the end).

**How to read an entry.**

- **Detect**: how the tell can be caught:
  `[provenance]` = generator plumbing in the files; one hit is near-proof.
  `[scanner]` = a script can pattern-match it; scores points, never proof alone.
  `[judgment]` = needs eyes; the skill's checklists cover it, the scanner can't.
- **Weight**: points the scanner gives (see scoring at the end).
- **Era**: when this tell is/was current. `2023-chat` (early ChatGPT output),
  `2024+` (shadcn/v0/Lovable era), `2025+escape` (the "tasteful" looks models
  fled to after purple was called out), `evergreen`.
- **FP risk**: false-positive risk: how often good human work has it too.
- **Verified / Weak**: Verified = 2+ independent sources, or one measured
  study. Weak = single-source or contested; low weight, never decisive.

Source keys: P=01-practitioners, A=02-academic, C=03-community-wiki,
K=04-code-patterns (measured on 12 verified AI-generated repos),
M=05-mobile-and-copy, X=06-accessibility, R=07-prior-art, V=08-visual-science.
Full citations with URLs live in `sources.md`.

---

## Part 0 — What the evidence actually says (read this first)

Five findings that shape every rule below:

1. **No single tell is proof.** Every practitioner source that measured anything
   says signals only work in combination (P11, C16, K). The scanner therefore
   scores co-occurrence and density, and only provenance artifacts are treated
   as conclusive alone.
2. **The folk wisdom is partly stale.** Raw `bg-indigo-600` / purple→pink
   gradient classes appeared in **0 of 12** verified 2025-26 AI repos (K).
   Modern Lovable/v0 output uses shadcn semantic tokens. The purple cliché
   survives in one-shot chat output, imagery, and older code. Rules are
   era-tagged for this reason.
3. **The escapes became tells.** Two looks are now named AI defaults.
   One is warm cream plus serif plus terracotta. The other is near-black plus
   a single acid accent. Anthropic's own frontend-design skill names both (R4).
   C2 and C3 call the first one "the Claude Code palette".
   Any fixed "good look" this skill recommended would rot the same way.
   So it recommends a process: brief, generate, measure, fix. Not a look.
   This was not theoretical. Version 1 of `examples/fixed-example.html` scored
   0 on this skill's scanner and NON-COMPLIANT on the brand-distance one.
   See `brand-distance.md`.
4. **Structure converges harder than colour.** The one direct academic
   measurement (Design Theater's Design Homogeneity Index, A1) found layout
   converges more than palette. Section-skeleton and card-grid checks deserve
   their weight.
5. **Screenshot "AI detectors" don't work on UI.** Photo-trained detectors are
   near coin-toss and untested on flat UI renders (R19, A15/A16). This skill
   detects *patterns in code and copy*, not pixels.

---

## Part 1 — Provenance artifacts `[provenance]` — near-proof, 15 pts each

These are generator plumbing. Humans don't write them. Measured in K on real repos.

| ID | Tell | Signature | Era | FP risk | Status |
|---|---|---|---|---|---|
| PR1 | Lovable scaffold | `lovable-tagger`/`componentTagger` in vite config or package.json; README URL `lovable.dev/projects/<uuid>`; repo name ending `-xxxxxxxx` (8 hex) | 2024+ | ~zero | Verified (K: 3/3 Lovable samples) |
| PR2 | v0 placeholder images | `/placeholder.svg?height=N&width=N`, `placeholder-user.jpg` | 2024+ | ~zero | Verified (K: 3/12, incl. one Lovable repo) |
| PR3 | v0 sync README | "Automatically synced with your v0.dev deployments" / "Built with v0" | 2024+ | ~zero | Verified mechanism (K, docs; owners often rewrite it) |
| PR4 | Bolt template config | root `config.json` with `"template": "bolt-..."` | 2024+ | ~zero | Verified (K) |
| PR5 | Replit Agent files | `replit.md` (Agent memory file); `.replit` alone only means Replit hosting | 2024+ | low | Verified (K) |
| PR6 | Builder comments/meta | `<!-- Generated with Bolt -->`, Lovable attribution comments, `<meta name="generator">` | 2024+ | low | Verified (P18, P11) |
| PR7 | Chat residue | "As an AI language model…", knowledge-cutoff disclaimers, unfilled `[Describe the …]` placeholders shipped in copy | evergreen | ~zero | Verified (P11, M-B1) |

## Part 2 — Code and visual tells `[scanner]`

### 2a. Colour

| ID | Tell | Signature | Weight | Era | FP risk | Status |
|---|---|---|---|---|---|---|
| CO1 | Legacy AI purple/indigo accents | `bg-indigo-(500\|600)`, `violet-500`, hexes `#6366f1 #4f46e5 #4338ca #3730a3 #8b5cf6 #7c3aed #a855f7` (nexu-io banlist, R6) | 1 | 2023-chat | medium — humans used these for a decade (P8) | Verified as *legacy*: 16 practitioner sources name it (P) but **0/12 modern repos** (K). Low weight is deliberate. |
| CO2 | Gradient-clipped headline text | `bg-clip-text` + `text-transparent` (usually with `bg-gradient-to-r`) | 4 | 2024+ | low — rare in hand-written code | Verified (K: 4/12; P16, C8, V2; impeccable bans it outright R3) |
| CO3 | Many two-hue gradient washes | ≥5 distinct `from-*-N to-*-N` pairs in one project — hue-agnostic; the hues follow the topic | 4 | 2024+ | low at that count | Verified (K: 133 occurrences in one Bolt repo; folk "always purple" corrected) |
| CO4 | Dark hero + glass combo | dark bg (`bg-(gray-900\|slate-950\|zinc-950\|black)`) + `bg-white/10` + `border-white/20` + `backdrop-blur` in one element | 4 | 2024+ | low as 3-way co-occurrence | Verified (K: Claude-cluster, 27 occ; P24, V3) |
| CO5 | Glow blobs | absolutely-positioned `rounded-full` + `blur-3xl` (or `filter: blur(40px+)`) decorative divs | 3 | 2024+ | near-zero | Verified (K: 3/12 but ~0 FP; P4, V3) |
| CO6 | "Tasteful cream" escape look | warm cream ground `#faf8f4`/`#f4f1ea` band + serif display + terracotta/coral accent, as a *combination* | 2 | 2025+escape | medium — real editorial design uses warm neutrals | Verified (R4 names it an AI default cluster; C2, C3, P8-cream; weight kept low, judgment confirms) |
| CO7 | Neon multi-hue at full saturation | 3+ saturated accent hues competing as coequals | 2 | evergreen | medium | Verified (P7, P9; also an accessibility harm, X: "Don't use bright contrasting colours") |
| CO8 | Low-contrast grey body text | computed contrast < 4.5:1 on body text (`text-gray-400` on white, `#888` on dark) | craft score, not AI score | evergreen | high — humans do it constantly | Verified harm (V7, X SC 1.4.3) but **filed as a craft/access failure, not an AI tell** (P16 explicitly classifies it "quality issue") |

### 2b. Typography

| ID | Tell | Signature | Weight | Era | FP risk | Status |
|---|---|---|---|---|---|---|
| TY1 | Unchosen default sans | Inter (or Geist/Roboto) as the only face, from Google Fonts or framework default, no pairing | 2 | evergreen | high — Inter is a fine human choice | Verified as *default-ness* signal (9 practitioner sources P; C4/C7). Scores only when it is the sole face AND other tells co-occur. |
| TY2 | The 2025 "slop pairing" | Inter + Space Grotesk, or Inter + Instrument Serif (Google Fonts imports together); Bricolage Grotesque in the mix | 2 | 2025+escape | medium | Verified (K: measured in Claude cluster; P11-fonts) |
| TY3 | Italic-serif accent word in a sans hero | `<span class="font-serif italic">` inside the H1 | 2 | 2025+escape | medium — was a human editorial trend first | Verified (P12, P16) |
| TY4 | Oversized hero ramp sandwich | `text-(4\|5)xl` + responsive `md:text-(5\|6\|7)xl` + `font-bold` + `tracking-tight` — scored only with twin CTAs (CP1) | 3 (as sandwich) | 2024+ | medium alone, low as full sandwich | Verified (K: 6/12; C8) |
| TY5 | ALL-CAPS tracked eyebrow above headings | `uppercase tracking-wide(st)` micro-label over every H1/H2 | 2 | 2024+ | medium — real editorial device | Verified (P13, C11, V23). Also an accessibility harm for dyslexic readers (X: BDA bans uppercase running text). |
| TY6 | Monospace as marketing chrome | mono eyebrows/labels on non-code marketing pages | 1 | 2025+escape | medium | Weak-to-verified (C10, C2 only) |

### 2c. Layout and components

| ID | Tell | Signature | Weight | Era | FP risk | Status |
|---|---|---|---|---|---|---|
| LA1 | The full SaaS skeleton | section ids/order hero → logos → features → how-it-works → testimonials → stats → pricing → FAQ → CTA; ≥3 of `id="(features\|pricing\|testimonials\|faq)"` | 3 | evergreen | medium — human playbook too | Verified (P18, C12, M-A2; structure converges hardest, A1) |
| LA2 | Identical-card feature grid | `grid-cols-3` (or 3×2) of same-shaped cards, each icon-tile + title + two lines | 2 | evergreen | high alone — Bootstrap-era human pattern (C12/C15) | Verified in combination (10 practitioner sources P; K: 8/12) |
| LA3 | Icon tile above heading | `w-10 h-10 rounded-lg bg-<hue>-100` (or `bg-primary/10`) wrapping a Lucide icon, centered above card titles | 3 | 2024+ | low-medium | Verified ("the universal AI feature-card template", P17/V15; C6) |
| LA4 | Pill badge above the hero H1 | rounded-full bordered chip ("New ✨ v2.0 →") directly over the headline; badge spam per section | 2 | 2024+ | medium — Linear/Vercel human convention | Verified (P14, C11, R3 bans eyebrow-per-section) |
| LA5 | Twin hero CTAs | "Get Started" + "Learn More" as sibling buttons | 2 | evergreen | medium | Verified (K: both-in-hero 2/12; M-B7/B8 on why the labels are bad anyway) |
| LA6 | Hero metric row of round stats | 3-4 stat tiles: big number, small label ("10K+ users · 99.9% uptime") | 2 | evergreen | low when numbers are round and unsourced | Verified (P20, V24, C39-copy; K corrected the regex: "Trusted by N+" formula is the real string) |
| LA7 | Cards inside cards / everything a card | card-styled containers nested >1 deep; every block bordered+rounded+shadowed | 2 | evergreen | medium | Verified (P21, V22) |
| LA8 | Side-stripe accent borders | `border-l-4 border-<accent>` on cards/callouts without semantic meaning | 3 | 2024+ | low without status semantics | Verified ("almost as reliable as em-dashes", P22; R3, R6 call it the canonical AI dashboard tile) |
| LA9 | Hairline border + big soft shadow together | `border border-gray-200` + `shadow-(lg\|xl)` on the same element ("ghost card") | 2 | 2024+ | medium | Verified (P25, C4-glow variant, R3) |
| LA10 | Uniform radius/padding monotony | near-zero variance of radius and padding across all components; same `py-16`/`gap-4` at every level | judgment + 1 | evergreen | medium — design systems standardize legitimately | Verified (P40, V21, C18); scanner counts distinct values, judgment decides |
| LA11 | min-h-screen on every section | `min-h-screen` count > 3 | 2 | 2024+ | low at that count | Verified (K: 16-36 occ in AI repos vs once in human code) |
| LA12 | Tailwind-UI container fossil | exact `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` | 1 | 2023-chat | medium | Verified as *legacy* (K: 1/12 now — folk wisdom outdated) |
| LA13 | Unchanged shadcn defaults | complete stock `components/ui` dump + token block byte-matching defaults (`--radius: 0.5rem`, stock zinc/slate HSL scale) | 6 | 2024+ | medium — humans run `npx shadcn add` too | Verified (K: 8/12; C19: "famously look the same", 10k-star tweakcn exists to fix it). Below flag-threshold alone by design. |
| LA14 | Bento grid reflex | bento mosaic applied regardless of content | judgment | 2025+ | high | **Weak** — community folklore; no rigorous source (V25 gap). Judgment-only, no scanner points. |

### 2d. Iconography and imagery

| ID | Tell | Signature | Weight | Era | FP risk | Status |
|---|---|---|---|---|---|---|
| IC1 | The cliché Lucide set | ≥3 of `Sparkles Zap Shield Rocket` imported in one file, esp. with a feature grid | 3 | 2024+ | low as a set | Verified (K: names in 8/12; R5) |
| IC2 | Emoji as UI icons | ✨🚀🎯⚡🔥💡 in headings/buttons/nav (not body prose) | 2 | evergreen | medium — Notion-style docs use emoji legitimately | Verified (P27, C31, R6 banlist). Also an access harm: screen readers announce "sparkles rocket" (X). |
| IC3 | Sparkle = AI marker | ✨ glyph or sparkle icon on AI features | 1 | 2024+ | medium | **Contested**: NN/g n=107 found 0% read it as AI; Google n=2000 found in-ecosystem users do (V13 vs V14). Low weight; the fix is "label it", not "never sparkle". |
| IC4 | Decorative grid/dot background | faint graph-paper or dot-matrix pattern behind heroes | 1 | 2024+ | medium — Vercel/Linear human trend | Verified but amplified-human (P26) |
| IC5 | Placeholder people and avatars | `i.pravatar.cc`, `randomuser.me`, `ui-avatars.com`, `placehold.co`, "John Doe"/"Sarah Chen"/"Acme" | 4 shipped / 1 in mockups | evergreen | low on a production site | Verified (K: 4/12; M-B2 testimonial shape; R6) |
| IC6 | AI-generated hero imagery | over-smooth skin, staged lighting, garbled in-image text, warped near-miss logos | judgment | evergreen | rising — only 8% of AI images now show visible flaws (V10) | Verified but **weakening**: NN/g found undisclosed AI images out-scored real stock on trust (V8). Machine colour-stats detection works (93%+, V9) but needs tooling this skill doesn't ship. Judgment + provenance of image files. |
| IC7 | Corporate Memphis / unDraw blobs | flat elastic-limb vector people, single violet accent | 1 | evergreen | high — pre-AI human cliché (C15) | Verified as amplified-human; ubiquity asserted, never audited (V gap) |

### 2e. Motion

| ID | Tell | Signature | Weight | Era | FP risk | Status |
|---|---|---|---|---|---|---|
| MO1 | Fade-up-on-scroll everywhere | reveal wiring (`opacity-0 translate-y-*` + observer, AOS) on most top-level sections; page blank without JS | 3 | 2024+ | medium — human marketing sites do it too | Verified (P33, V16; NN/g: delays and frustrates task-focused users V19) |
| MO2 | hover:scale everywhere | `hover:scale-105` + `transition` on cards/images sitewide | 1 | 2024+ | high | Verified (K: 6/12) but heavy human use; density signal only |
| MO3 | Pulse on static things | `animate-pulse` outside skeleton/loading components; fake "live" dots | 2 | 2024+ | low once skeletons excluded | Verified (P29, K: 7/12, V18) |
| MO4 | Marquees, typing effects, particles, animated gradients | infinite logo marquee; typewriter hero; canvas particles; hue-shifting bg | 2 (marquee/animated-gradient) / judgment (typing, particles) | 2024+ | medium | Marquee + animated gradient verified (P33, V19-quote, V3); typing/particles are **inference only** (V gap) — judgment |
| MO5 | No reduced-motion path | keyframe/transition animations present, zero `prefers-reduced-motion` query | craft score | evergreen | n/a — it's just a defect | Verified requirement (X SC 2.3.3/C39, V20-authorities). Craft score, not AI score. |
| MO6 | Bounce/elastic easing on UI | spring overshoot on interface elements (not physical objects) | 1 | 2024+ | medium — celebrated in Apple-style physics | Verified but contested boundary (P32, V18 vs human spring praise) |

## Part 3 — Copy tells `[scanner]` on strings, `[judgment]` on voice

The word lists live in `scripts/rules.json` (grouped, weighted). Highlights:

| ID | Tell | Examples | Weight | FP risk | Status |
|---|---|---|---|---|---|
| CP1 | Transformation-verb headlines | Elevate, Unlock, Unleash, Empower, Supercharge, Revolutionize, Transform, Streamline | 1 per distinct word, cap 4 | **high** — human marketese since before AI (M-B10 documented it in 1997) | Verified as *bad copy*; only weak AI evidence. Kept low-weight on the AI axis, flagged hard on the craft axis. |
| CP2 | AI-cadence set | em-dash density, "It's not just X, it's Y", rule-of-three everywhere, "in today's fast-paced world", Title Case Headings, bold-lead-in bullets | 1-2 | medium-high — all human rhetorical devices; density is the signal | Verified (Wikipedia Signs of AI writing, M-B1: "combined signal, not individual tripwires"; note only *Claude* out-em-dashes professional writers per the Economist study cited there) |
| CP3 | Fake-proof package | "Trusted by [N]+", 99.9% uptime, first-name-only testimonials, unverifiable logo bars, the same 5 FAQ questions | 1 each, +2 if 3+ co-occur | low on a day-one product | Verified (M-B2/B3; K corrected the exact strings) |
| CP4 | Vague CTAs | "Get Started", "Learn More" | 1 | high | Verified as weak-copy (M-B7/B8); AI-evidence only via co-occurrence (LA5) |
| CP5 | Gamified microcopy | "Let's Go!", "Great Job!" toasts, over-explained obvious UI | 1 | medium | Weak-to-verified (C41, one Medium source M) |
| CP6 | Interchangeable-product test | could this H2 sit on 500 other SaaS pages? swap-the-logo test | judgment | — | Verified as the practitioner consensus test (P34-quote, C22) |

## Part 4 — Judgment-only tells (checklists, never the scanner)

- **JD1: Domain-blindness.** A meditation app, a bank and a dev tool getting the
  same treatment. The single most-agreed tell across files (M-A9, P4, V26). Test:
  name three things in the design that could ONLY belong to this product.
- **JD2: Polish without depth.** Beautiful surface, missing hover/focus/error/
  empty/loading states, dead links, forms without validation. Academically
  measured: >25% of stated rationales never implemented (A1 "design theater");
  cross-screen inconsistency is the closest thing to a true AI fingerprint (M-A5).
- **JD3: Horror vacui / unearned evenness.** Every inch filled, or spacing so
  uniform it feels "exhaled rather than drawn" (C17, P40). Note the community
  lists BOTH overstuffing and over-whitespace: the shared root is unconsidered
  decoration.
- **JD4: Convergent revision loop.** Each AI iteration drags the design toward
  the median; distinctiveness falls as you re-prompt (P41, A-F12). Countermeasure
  is process: lock a direction file first (see `templates/`).
- **JD5: The two-altitude test** (from impeccable, R3). First-order fail: theme
  guessable from product category alone. Second-order fail: the aesthetic family
  is guessable even after you banned the defaults.

## Part 5 — NOT tells (do not flag these as AI)

Verified false-positive traps: flagging these embarrasses the skill:

- Inter itself, purple itself, dark mode itself, rounded corners themselves,
  centered heroes, 3-column layouts: all pre-AI human patterns (P-false-positives,
  C-historical baseline, Design Homogenization study A2). The tell is always
  *unchosen defaults in combination*.
- The Next.js/Vercel/Supabase stack: most popular human indie stack too (P37).
- Em-dashes, kickers, rule of three, Title Case in isolation: professional
  writing devices (M-B1 caveats).
- Craft defects (low contrast, tiny text, missing states): filed on the craft
  axis; humans produce them constantly (P16 classification).
- Polish/fluency itself: AI design is not ugly; you cannot spot it by hunting
  mistakes (P4).
- "Built with a website builder" fingerprints (Framer/Webflow meta): proves a
  builder, not AI (P18).

## Part 6 — Accessibility thresholds enforced on OUTPUT (craft axis)

Exact, sourced, machine-checkable (X file has full citations):

- Body text contrast ≥ 4.5:1; large text ≥ 3:1 (WCAG 2.2 SC 1.4.3 AA). AAA: 7:1.
- Non-text/UI contrast ≥ 3:1 (SC 1.4.11).
- Touch/click targets ≥ 24×24 CSS px (SC 2.5.8 AA); aim 44pt (Apple) / 48dp (Material) on touch.
- Every animation wrapped for `prefers-reduced-motion` (SC 2.3.3 / technique C39).
- Auto-moving content >5s needs pause/stop (SC 2.2.2). Nothing flashes >3×/s (SC 2.3.1).
- Focus visible, never `outline: none` without replacement (SC 2.4.7/2.4.13).
- Prose max-width ≤ 75ch (aim 45-75); line-height ≥ 1.5; never justified; body ≥ 16px (BDA + SC 1.4.8).
- No colour-only meaning (SC 1.4.1). No uppercase running text (BDA).
- Readability: docs and UI copy at ≈ grade 9 or lower (GOV.UK guidance).
- **Do not ship OpenDyslexic/dyslexia fonts as a fix**: three studies found no
  benefit or worse performance; plain sans + 16px + 1.5 line-height + left-align
  is the evidence-backed setup (X evidence-status).
- APCA is advisory only, not a compliance gate (WCAG 3 not ready; X).

## Scoring (implemented in `scripts/ai_tell_scan.py`)

Two separate scores, never mixed:

- **AI-look score** (0-100): provenance hits 15 each; scanner tells per weights
  above; co-occurrence bonuses (full hero sandwich, glass combo, fake-proof
  package). Bands: 0-19 distinct · 20-39 leaning generic · 40+ reads as AI.
  No Tier-2/3 signal can cross a band alone: by design (K's key rule).
- **Craft/access score** (0-100, higher is better): contrast, targets, reduced
  motion, focus, line length, readability, states present. A page can be
  distinctly designed and still fail craft: and vice versa.

## Why this register is dated

The purple era gave way to the shadcn-token era, which is giving way to the
cream-editorial escape era. Each shift took about 18 months (K, R4, R-gap3).
Every ban list in the wild is an undated snapshot. This one carries a version
and era tags, so future updates can retire tells. CO1 and LA12 are already
retired, kept at 1 point as legacy signals. When updating: re-run the K methodology (clone
verified generated repos, count), don't trust articles alone.
