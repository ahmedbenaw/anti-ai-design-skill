# Eras of AI-design defaults, and vendor house looks

**Topic:** The current era of AI-design defaults (era 3, "the tasteful escape look"), Claude's/Anthropic's own house look, evidence for a fourth era, and the house looks of other AI vendors that generated output drifts toward.

**Sweep date:** 2026-09-05.

**Route used:** Exa MCP was **not** authorised in this session. All retrieval was done with **WebSearch + WebFetch**, plus `gh api` for files and commit history in the public `anthropics/skills` GitHub repository (WebFetch 404s on `raw.githubusercontent.com` in this environment).

**Sources actually opened** (fetched and read in full or extracted verbatim — search-result titles that were never opened are *not* listed and are *not* in the table below):

1. `anthropics/skills` → `skills/frontend-design/SKILL.md`, current HEAD (commit `41bbe19d`, 2026-09-03) — via `gh api`
2. same file at commit `2235be7c` (2026-06-09) — via `gh api`
3. same file at commit `00756142` (2025-12-04) — via `gh api`
4. `anthropics/skills` → `skills/brand-guidelines/SKILL.md` — via `gh api`
5. anthropic.com/news/claude-design-anthropic-labs
6. northeasttimes.com — "AI design tools are making every website look the same" (2026-07-31)
7. kylechayka.substack.com — "The generic style of AI web design" (2026-06-29)
8. generativelabs.com — "Why Do Claude Designs All Look the Same?" (2026-07-14)
9. wheelsupcollective.com — "We Don't Want a Beige Internet"
10. shadcn.io/design/vercel — third-party Vercel design-system reconstruction (2026-05-12)
11. news.designrush.com — OpenAI visual identity refresh (2025-02-07)
12. aichatdaily.com — "AI companies pivot to serif fonts to look more human" (2026-06-05)
13. explainx.ai — writeup of Jim Nielsen's "The AI Aesthetic" (Nielsen essay dated 2026-07-29)
14. blog.logrocket.com — "Linear design" (2025-06-07)

**Attempted and failed** (recorded so nobody re-runs them assuming they work): `newyorker.com` (blocked by fetcher), `openai.com/brand/` (403), `creativereview.co.uk` (403), `dezeen.com` (403), `blog.jim-nielsen.com/2026/ai-aesthetic/` (empty response), `nicksimson.com` (empty response), `createwith.com` Lovable Aesthetics page (empty response).

---

## Source table

| ID | Title | Type | Date | URL |
|---|---|---|---|---|
| P25 | `frontend-design` SKILL.md, current version | First-party vendor skill (Anthropic) | 2026-09-03 (commit `41bbe19d`) | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md |
| P26 | `frontend-design` SKILL.md at commit `2235be7c` | First-party vendor skill, prior revision | 2026-06-09 | https://github.com/anthropics/skills/commit/2235be7c |
| P27 | `frontend-design` SKILL.md at commit `00756142` | First-party vendor skill, original revision | 2025-12-04 (skill added 2025-11-12) | https://github.com/anthropics/skills/commit/00756142 |
| P28 | `brand-guidelines` SKILL.md | First-party vendor skill (Anthropic brand palette) | at current path since 2025-12-01; pre-move history not checked | https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md |
| P29 | "Introducing Claude Design by Anthropic Labs" | First-party product announcement | 2026-04-17 | https://www.anthropic.com/news/claude-design-anthropic-labs |
| P30 | "AI design tools are making every website look the same" (Maya Brooks) | Trade/news reporting | 2026-07-31 | https://northeasttimes.com/2026/07/31/ai-design-tools-are-making-every-website-look-the-same/ |
| P31 | "The generic style of AI web design" (Kyle Chayka) | Newsletter by a New Yorker staff writer, trailing his column | 2026-06-29 | https://kylechayka.substack.com/p/the-generic-style-of-ai-web-design |
| P32 | "Why Do Claude Designs All Look the Same?" (Bill Cava) | Agency/consultancy analysis post | 2026-07-14 | https://www.generativelabs.com/insights/why-ai-design-tools-look-the-same |
| P33 | "We Don't Want a Beige Internet" (Elise Oras) | Agency blog post | "May 27", year not stated on page | https://www.wheelsupcollective.com/post/we-dont-want-a-beige-internet |
| P34 | "Vercel Design System for React" | Third-party reconstruction of a vendor design system | 2026-05-12 | https://www.shadcn.io/design/vercel |
| P35 | "OpenAI Refreshes Its Visual Brand Identity…" (Arman Lorenzo Burias) | Design-trade news | 2025-02-07 (upd. 2025-05-01) | https://news.designrush.com/openai-refreshes-its-visual-brand-identity-with-new-logo-typeface |
| P36 | "AI companies pivot to serif fonts to look more human" (Jaeden Schafer) | Newsletter/analysis | 2026-06-05 | https://www.aichatdaily.com/ai-analysis/ai-companies-pivot-serif-fonts-look-more-human |
| P37 | "The AI Aesthetic Explained — Why AI Apps All Look Alike" | Secondary writeup of a primary essay | writeup 2026; Nielsen essay 2026-07-29 | https://www.explainx.ai/blog/ai-aesthetic-design-patterns-jim-nielsen-2026 |
| P38 | "Linear design: The SaaS design trend that's boring and bettering UI" (Daniel Schwarz) | Design-publication explainer | 2025-06-07 | https://blog.logrocket.com/ux-design/linear-design/ |
| P39 | `awesome-design-md` → `design-md/claude/DESIGN.md` | Third-party community reconstruction of Claude's visual system | undated in file | https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/claude/DESIGN.md |

---

## Source entries

### P25 — `frontend-design` SKILL.md, current version (2026-09-03)
- **Source:** Anthropic, first-party agent skill in the public `anthropics/skills` repo, commit `41bbe19d` dated 2026-09-03. https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- **Context:**
  - Names **five** clusters that "AI-generated design right now clusters around": (1) warm cream background near `#F4F1EA` with high-contrast serif display and a terracotta/warm-clay accent "often near `#D97757`"; (2) near-black with one acid-green or vermilion accent; (3) broadsheet layout, hairline rules, zero border-radius, dense columns; (4) a "SaaS-card kit" — identical rounded cards, one radius everywhere, the same soft grey shadow `rgba(0,0,0,.1)`, gradient washes as decoration; (5) "template chrome" — tracked-out ALL-CAPS eyebrows, middle-dot meta strings, `WORD — fragment` labels, tinted near-blacks `#0B0B0B` / `#111`, monospace small data labels, `→` appended to link text.
  - Anthropic itself flags `#D97757` as its own product accent and says that on a user's brief it therefore "reads as a tell". This is a vendor naming its own house colour as a contamination risk in generated output — the single most useful line in this sweep.
  - Also names three typographic tells: accenting one word in a headline, all-caps labels, and unnecessary labels above content. And motion tells: per-section fade-and-slide-up entrances, hover transitions on every card.
  - Guidance only. No measurement, no eval, no corpus — the document asserts these clusters without citing how they were established.
- **Tags:** `[AVOID: cream+serif+terracotta]` `[AVOID: SaaS-card kit]` `[AVOID: template chrome]` `[EVIDENCE-ONLY: for the dating of when Anthropic recognised each cluster]`
- **Feeds:** CO6 (tasteful-escape look); new candidates CAND-1 (SaaS-card kit), CAND-2 (template chrome), CAND-3 (Anthropic accent hue).

### P26 — `frontend-design` SKILL.md at 2026-06-09
- **Source:** Anthropic, first-party, commit `2235be7c` dated 2026-06-09. https://github.com/anthropics/skills/commit/2235be7c
- **Context:**
  - This revision is where the cluster language first appears: "AI-generated design right now clusters around three looks", listing cream `#F4F1EA` + serif + terracotta, near-black + acid accent, and broadsheet/hairline.
  - The terracotta is described generically here — **no** `#D97757` and **no** acknowledgement that it is Anthropic's own accent. That admission is added only in the 2026-09-03 revision (P25).
  - Same file already carries the "defaults rather than choices, and they appear regardless of subject" framing that the skill's CO6 rule depends on.
  - Gives a hard lower bound: by 2026-06-09 the cream/serif/terracotta look was recognised *by the vendor* as a default, in writing, in a public repo.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Era-3 start date.

### P27 — `frontend-design` SKILL.md at 2025-12-04
- **Source:** Anthropic, first-party, commit `00756142` dated 2025-12-04 (skill first added 2025-11-12, commit `e5c60158`). https://github.com/anthropics/skills/commit/00756142
- **Context:**
  - Contains **no** mention of cream, `#F4F1EA`, terracotta, or clusters. Grep for those terms returns nothing.
  - What it *does* name as generic: "overused font families (Inter, Roboto, Arial, system fonts)", "cliched color schemes (particularly purple gradients on white backgrounds)", and a warning not to converge on Space Grotesk.
  - So the same vendor document, seven months apart, moves from "purple gradients + Inter" to "cream + serif + terracotta" as the thing to avoid. This is the cleanest dated era boundary in the whole sweep, and it is first-party.
  - Caveat on interpretation: this dates when *Anthropic wrote about* each look, not when generated output actually changed. Nobody measured the output.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Era-1/2 → era-3 boundary.

### P28 — `brand-guidelines` SKILL.md (Anthropic brand palette)
- **Source:** Anthropic, first-party agent skill. Present at its current path since the 2025-12-01 folder reorganisation and unmodified since; its pre-move history at the old top-level path was not checked, so the file is older than that date. https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md
- **Context:**
  - Publishes an official palette: dark `#141413`, light `#faf9f5`, mid grey `#b0aea5`, light grey `#e8e6dc`; accents orange `#d97757`, blue `#6a9bcc`, green `#788c5d`.
  - Typography in this skill is **Poppins for headings, Lora for body**, with Arial/Georgia fallbacks — explicitly chosen because they need to be installable in a document-generation environment. These are *not* the faces used on Anthropic's own product surfaces, and this file names no proprietary face.
  - Confirms the warm-neutral family the skill's CO6 rule is chasing is real and first-party: an off-white with a yellow-green cast (`#faf9f5`, `#e8e6dc`) against a near-black that is itself warm (`#141413`, not `#000`), with a single warm-orange accent.
  - Note the two-hex discrepancy worth carrying: Anthropic's own light is `#faf9f5`, but the value the frontend-design skill uses to describe the *generated* cream is `#F4F1EA` — a slightly deeper, greyer cream. They are close but not the same colour; a distance-based detector must decide which centroid it is testing against.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: use these as the measured centroid for a colour-distance check]`
- **Feeds:** CO6 colour-distance measurement; CAND-3 accent-hue check.

### P29 — "Introducing Claude Design by Anthropic Labs"
- **Source:** Anthropic, first-party product announcement, 2026-04-17. https://www.anthropic.com/news/claude-design-anthropic-labs
- **Context:**
  - Confirms the date the propagation mechanism shipped: 2026-04-17, research preview, Claude Pro/Max/Team/Enterprise, powered by Claude Opus 4.7. Aimed explicitly at people without a design background — founders, PMs.
  - Output types named are decks, one-pagers, prototypes, designs — i.e. the artefacts the July reporting (P30) later finds looking identical.
  - The page describes a design-system onboarding that reads a team's codebase and design files so projects "use your colors, typography, and components automatically". It says nothing about what the tool does when a team has *no* design system — which is precisely the default-emission case the critics describe.
  - No hexes, no typeface names on the page. It is not a source for Anthropic's own visual specification.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Era-3 dating (mechanism), not a tell itself.

### P30 — "AI design tools are making every website look the same" (Maya Brooks, Northeast Times, 2026-07-31)
- **Source:** Maya Brooks, Culture & Trends writer, Northeast Times, original reporting, 2026-07-31. https://northeasttimes.com/2026/07/31/ai-design-tools-are-making-every-website-look-the-same/
- **Context:**
  - Carries the anecdote that anchors most subsequent commentary: designer **Matt Ström-Awn** was shown sales decks by two unconnected startup founders that had the same layout — bright opening slide, three bullets, four rectangles for the market, centred "our move" text — with only the logos differing. Both were made in Claude Design. His line: "they were generated by the same company".
  - Names the look concretely: beige/cream grounds, rusty-orange accents, large italicised-and-highlighted serif display, tracked-out subheadings, ticker-like scrolling text bars, stacks of rounded rectangle outlines sometimes with a neon glow beneath.
  - Quotes designer/writer **Celine Nguyen** on "tasteful, slightly askew primary colors" and desaturated mid-century-modern hues, and on the reversal once they became cliché: "Now I find myself instinctively repulsed by the warm tones".
  - **No measurement.** The article is entirely qualitative — designer testimony plus example sites. It cites no survey, no corpus, no counts. Its only numbers are the Claude Pro price.
- **Tags:** `[AVOID: cream+serif+terracotta]` `[AVOID: ticker bar]` `[AVOID: tracked-out subhead]` `[CONTESTED: prevalence is asserted, never counted]`
- **Feeds:** CO6; new candidates CAND-4 (news-ticker bar), CAND-5 (italic-highlighted serif display).

### P31 — "The generic style of AI web design" (Kyle Chayka, 2026-06-29)
- **Source:** Kyle Chayka, New Yorker staff writer ("Infinite Scroll" column), newsletter post 2026-06-29 trailing his column at https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet (the New Yorker URL itself could not be opened from this environment). https://kylechayka.substack.com/p/the-generic-style-of-ai-web-design
- **Context:**
  - This is the naming event for era 3 in mainstream press, by the writer who previously named "AirSpace"/"Filterworld". Dated 2026-06-29 — *after* Anthropic's own 2026-06-09 skill revision (P26), so the vendor documented it slightly before the press did.
  - Trait list matches P30 closely: beige/cream grounds, rusty-orange accents, large italicised serif, tracked-out subheads, ticker-like text bars, dashboard-ish stacks of rounded rectangles with neon glow.
  - Attributes the spread to Claude Design's default house style resembling Anthropic's own branding.
  - Again qualitative. The evidence is a set of named example sites plus the author's eye. Treat "taking over the internet" as a headline, not a finding.
- **Tags:** `[AVOID: cream+serif+terracotta]` `[CONTESTED: no prevalence data]`
- **Feeds:** CO6; era-3 naming date.

### P32 — "Why Do Claude Designs All Look the Same?" (Bill Cava, Generative Labs, 2026-07-14)
- **Source:** Bill Cava, Generative Labs, analysis post, 2026-07-14. https://www.generativelabs.com/insights/why-ai-design-tools-look-the-same
- **Context:**
  - The only source in this sweep that puts **hex values** on the observed generated look: cream `#F7F1E4`, ink `#211D18`, rusty orange `#D9622B`. Important caveat stated in the piece itself: these are **sampled by eye from artefacts**, not from any published spec or dataset. They are near, but not equal to, Anthropic's own `#faf9f5` / `#141413` / `#d97757` (P28) and near the skill's `#F4F1EA` (P25).
  - Quotes Ström-Awn again — the tool "defaults to the same aesthetic for every single person that's using it" — and quotes Claude Design guidance as saying "This default is persistent".
  - Makes a second-order claim that is directly relevant to the skill: asking for something less generic shifts output to "a different fixed palette rather than producing variety". If true, an anti-AI-design intervention that merely says "don't do cream" produces a *new* cluster, not diversity. That is exactly the CO6 trap.
  - Names v0, Lovable, Gemini and ChatGPT as vendors but attributes no specific traits to them; do not use this source for vendor house looks.
- **Tags:** `[AVOID: cream+serif+terracotta]` `[ADOPT: test that a de-slop intervention increases variance, not just moves the centroid]` `[CONTESTED: hexes are eyeballed samples]`
- **Feeds:** CO6 colour-distance; a methodology note for the skill's own evals.

### P33 — "We Don't Want a Beige Internet" (Elise Oras, Wheels Up Collective)
- **Source:** Elise Oras, Wheels Up Collective agency blog. Page shows "May 27" with **no year**; internal references (GitHub 2026 statistics) place it in 2026, but the date is unconfirmed. https://www.wheelsupcollective.com/post/we-dont-want-a-beige-internet
- **Context:**
  - Uses "beigeification of the web" as a **metaphor for sameness**, not as a description of the cream palette. Its actual trait list is era-1/era-2: purple-to-indigo hero gradient, Inter headlines, rounded cards, `bg-indigo-500` CTAs, centred hero → three-or-four feature cards → testimonials → footer.
  - Useful as a caution: "beige internet" language in 2026 commentary does **not** reliably mean the cream look. Do not treat the phrase as an era-3 citation.
  - Cites third-party numbers (a 92% figure for US developers using AI coding tools daily; 46% of new code AI-generated, attributed to GitHub 2026; 10%+ of Lovable apps shipping with security vulnerabilities). These are adoption/quality statistics, **not** measurements of visual homogeneity — they do not answer "has anyone measured the look".
  - Its causal claim — "The AI isn't designing; it's averaging" — is the standard training-distribution argument, asserted not tested.
- **Tags:** `[EVIDENCE-ONLY]` `[STALE-RISK: undated page]` `[CONTESTED: statistics are about adoption, not aesthetics]`
- **Feeds:** Era-2 traits; a terminology warning.

### P34 — "Vercel Design System for React" (shadcn.io, 2026-05-12)
- **Source:** shadcn.io, **third-party reconstruction**, dated 2026-05-12. The page describes itself as an interpretation of Vercel's design language and is not on a Vercel domain. https://www.shadcn.io/design/vercel
- **Context:**
  - Reconstructed palette is monochrome-first: ink `#171717`, canvas `#ffffff` with `#fafafa`/`#f5f5f5` soft steps, hairline `#ebebeb`, body `#4d4d4d`, mute `#888888`; a signal blue `#0070f3`; plus a set of two-stop brand gradients (`#7928ca`→`#ff0080`, `#007cf0`→`#00dfd8`, `#ff4d4d`→`#f9cb28`).
  - Typography: **Geist** for display/body/labels, **Geist Mono** for code and "technical eyebrows".
  - Radius scale: `0`, `6px`, `8px`, `100px`, `9999px` — i.e. small radii on containers, full pills for standalone CTAs.
  - Because it is a reconstruction, treat every value as approximate. It is adequate for building a "does this look like v0 output" heuristic; it is not adequate for asserting what Vercel publishes.
- **Tags:** `[AVOID: monochrome + Geist + Geist-Mono eyebrow]` `[CONTESTED: third-party reconstruction, not vendor-published]`
- **Feeds:** Vendor house look — v0/Vercel.

### P35 — OpenAI visual identity refresh (DesignRush, 2025-02-07)
- **Source:** Arman Lorenzo Burias, DesignRush news, 2025-02-07 (updated 2025-05-01). https://news.designrush.com/openai-refreshes-its-visual-brand-identity-with-new-logo-typeface
- **Context:**
  - OpenAI's first rebrand, 2025, in-house team with Studio Dumbar and Berlin type foundry ABC Dinamo. Custom typeface **OpenAI Sans** (geometric-but-rounded sans), refined blossom mark, new wordmark.
  - Palette described as greys and blues as a base with contrasting primaries; a pulsating blue disc as the key motion element representing ChatGPT's voice.
  - The important structural point for this skill: OpenAI's house look is a **cool grey-blue sans** system — the near-exact opposite axis to Anthropic's warm-cream-and-serif. Where generated output drifts cool-grey-sans with a blue signal colour, that is a different vendor's gravity well, not era-3.
  - This is design-trade reporting, not the OpenAI brand site (which returned 403 here). Typeface name and agencies are consistent across several trade outlets in search results, but only this one was opened.
- **Tags:** `[AVOID: OpenAI-Sans + grey/blue base as an unexamined default]` `[EVIDENCE-ONLY]` `[STALE-RISK: 2025 rebrand may have iterated since]`
- **Feeds:** Vendor house look — OpenAI.

### P36 — "AI companies pivot to serif fonts to look more human" (Jaeden Schafer, 2026-06-05)
- **Source:** Jaeden Schafer, AI Chat Daily, 2026-06-05. https://www.aichatdaily.com/ai-analysis/ai-companies-pivot-serif-fonts-look-more-human
- **Context:**
  - Names the coinages this skill should track: designer **Keya Vadgama** calls the shift the "**serif renaissance**"; the pejorative circulating online for it is "**tasteslop**". Neither coinage is given a dated primary link in this piece — Vadgama's Substack post is referenced without a date.
  - Names four AI companies as having moved to serif type in product surfaces or branding: Anthropic (Claude), Perplexity, Runway, Manus. This is the closest thing found to evidence that the serif half of era 3 is an *industry* pattern rather than an Anthropic one.
  - Carries the argument for *why* serif: print-trust association. One designer quoted saying Claude in particular emulates the feeling of reading print. Vadgama's counter-argument is that using serifs to signal non-threatening-ness is dishonest when the product is still an AI company.
  - Names no proprietary typefaces for any of the four companies — the only faces mentioned are generic examples (Times New Roman, Arial, Calibri, Helvetica, Comic Sans).
- **Tags:** `[AVOID: reflexive serif display]` `[EVIDENCE-ONLY]` `[CONTESTED: coinages have no dated primary source here]`
- **Feeds:** CO6 (serif half); vendor-cluster evidence beyond Anthropic.

### P37 — Jim Nielsen, "The AI Aesthetic" (essay 2026-07-29), read via explainx.ai writeup
- **Source:** Secondary writeup at explainx.ai of Jim Nielsen's essay, published 2026-07-29 at https://blog.jim-nielsen.com/2026/ai-aesthetic/ (the primary URL returned an empty response from this environment, so this entry is second-hand). https://www.explainx.ai/blog/ai-aesthetic-design-patterns-jim-nielsen-2026
- **Context:**
  - Nielsen's list of tells that mark software as AI-made is broader than palette: shimmering "thinking" text during async states; tiny sidebar icons; beige/cream with orange accents; serif type; the sparkle emoji as an AI signifier; whack-a-mole toggle patterns in settings.
  - Value to this skill: it extends era 3 from *marketing pages* into *product chrome*. The cream-and-orange tell shows up alongside behaviours (shimmer loading, sparkle icon) that a source scanner can catch far more reliably than a colour.
  - No hexes, no typeface names — the palette is described only as "beige/cream + orange".
  - Reached HN front page the day of publication, which is weak evidence of practitioner resonance and no evidence of prevalence.
- **Tags:** `[AVOID: shimmer loading text]` `[AVOID: sparkle emoji as AI signifier]` `[AVOID: cream+orange]` `[CONTESTED: read second-hand, primary not opened]`
- **Feeds:** CO6; new candidates CAND-6 (shimmer-loading), CAND-7 (sparkle-as-AI-icon).

### P38 — "Linear design" (Daniel Schwarz, LogRocket, 2025-06-07)
- **Source:** Daniel Schwarz, LogRocket Blog, 2025-06-07. https://blog.logrocket.com/ux-design/linear-design/
- **Context:**
  - **Important false friend.** This article uses "linear design" to mean *sequential, one-direction-scroll layout*, and only mentions the company Linear as having popularised it. It is not a specification of Linear-the-company's visual system.
  - Traits it does list, which overlap the thing practitioners mean by "Linear-style": dark mode (not mandatory), bold typography, complex gradients, glassmorphism, high contrast, monochrome palettes, minimal CTAs, one-dimensional scroll.
  - Names no hex values and no typefaces, and gives no start date for the trend.
  - Consequence for this sweep: **"Linear-style" is the weakest-sourced of the four vendor looks I was asked to cover.** I did not find, and did not open, any source that specifies it with values.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED: the term is used for two different things]` `[STALE-RISK: 2025]`
- **Feeds:** Vendor house look — Linear-style (weakly).

---

## Era timeline

A note on what "era" can mean here, because the whole section rests on it. Every dated boundary below is a date at which **someone wrote that a look was a default** — a vendor, a journalist, or a practitioner. **Not one of these boundaries is dated by a measurement of generated output.** No source opened in this sweep sampled generated pages over time and showed the distribution moving. Treat the timeline as a documented-discourse timeline, not a measured one.

### Era 1 — purple/indigo gradient (through roughly 2025, still cited into 2026)
- **Traits:** purple-to-indigo hero gradient, Inter for headlines, `bg-indigo-500` CTAs, rounded cards, centred hero → three/four feature cards → testimonials → footer (P33). Anthropic's own December 2025 skill names "purple gradients on white backgrounds" and Inter/Roboto/Arial as the cliché to avoid (P27).
- **Start evidence:** thin. Both P33 and P27 assert it without dating its onset; P33's causal story (Tailwind's `bg-indigo-500` in docs examples → GitHub over-representation → training median) is an argument, not data.
- **End evidence:** it does not cleanly end. P33 was still describing it as the current problem in 2026, and Lovable was still associated with purple/indigo in 2026 search results. **Era 1 persists in some tools while era 3 dominates elsewhere.** The register should not treat eras as mutually exclusive.

### Era 2 — shadcn/Tailwind neutral defaults (roughly 2024–2026, overlapping era 1)
- **Traits:** untouched `zinc`/`slate` scales, `rounded-2xl shadow-lg` reflexes, uniform gap/padding, the SaaS-card grid. Covered mainly by the existing reference file 07; in this sweep it surfaces indirectly in P33 (shadcn/ui named as a driver) and, notably, **reappears as cluster 4 in the September 2026 first-party list** (P25: "the SaaS-card kit").
- **Start/end evidence:** none dated in this sweep. That era 2's signature reappears in a September 2026 vendor list of *current* defaults is the most interesting finding here — it suggests era 2 never ended, it just stopped being the thing people wrote about.

### Era 3 — cream + serif + terracotta ("the tasteful escape", "tasteslop", the "serif renaissance")
- **Traits, from opened sources:** warm cream ground (`#F4F1EA` per P25; sampled as `#F7F1E4` per P32; Anthropic's own light is `#faf9f5` per P28); warm near-black ink (`#141413` per P28; sampled `#211D18` per P32); a terracotta/rust accent (`#D97757` per P25/P28; sampled `#D9622B` per P32); high-contrast serif display, often italicised and highlighted (P30, P31); tracked-out letter-spaced subheads (P30, P31); ticker-like scrolling text bars (P30, P31); stacks of rounded-rectangle outlines, sometimes with a neon glow beneath (P30, P31); generous whitespace and editorial layout.
- **Start evidence — this is the strongest dated chain in the sweep, and it is first-party:**
  - 2025-12-04: Anthropic's `frontend-design` skill names purple gradients and Inter as the cliché. No mention of cream, serif or terracotta anywhere in the file (P27).
  - 2026-04-17: Claude Design ships — a visual-output product aimed at non-designers, in preview for all paid tiers (P29). This is the plausible propagation mechanism, though no source measures its effect.
  - 2026-06-09: the same Anthropic skill file is rewritten to name **three** clusters, cream/serif/terracotta first among them, and to say they "appear regardless of subject" (P26).
  - 2026-06-29: Kyle Chayka publishes the same trait list in a New Yorker column and its trailing newsletter, attributing the spread to Claude Design (P31).
  - 2026-07-29: Jim Nielsen's essay extends the tells into product chrome (P37).
  - 2026-07-31: Northeast Times reports the two-identical-founder-decks anecdote from Matt Ström-Awn (P30).
  - 2026-09-03: Anthropic's skill file adds `#D97757` by name and states it is "Anthropic's own Claude-interaction accent, so on a user's brief it reads as a tell" (P25).
- **End evidence:** none. Era 3 is current as of this sweep.
- **Who named it:** Anthropic named it internally-but-publicly first (2026-06-09, P26); Chayka named it for a general audience (2026-06-29, P31); Keya Vadgama's "serif renaissance" and the pejorative "tasteslop" are in circulation by 2026-06-05 (P36) — earlier than both, but reported second-hand with no dated primary.
- **Is there measurement?** **No.** Every prevalence claim opened in this sweep is designer testimony or example-collection. P30 explicitly presents no counts. P32's hexes are eyeballed from artefacts. P33's statistics are about AI-coding adoption and security, not visual similarity. A targeted search for a corpus study of AI-generated page colour/typography turned up only adjacent work — text homogenisation studies and UI-generation benchmarks using CLIP similarity against reference screenshots — none of which measures drift toward a specific palette over time. **"Everyone says it, nobody counted it" is the honest state of the evidence.**

### Era 4 — no evidence found
I looked for it and did not find it. Stating that plainly, because it is the publishable result:

- **No source opened in this sweep shows that any tool's default output moved away from era 3.** The question asked was what tools are defaulting to *now*; the answer, on the evidence available, is still era 3.
- The strongest *contrary* evidence to a fourth era is the 2026-09-03 first-party revision (P25). It did not replace the cream cluster. It **kept** it, promoted it to first position, added its own accent hex to it, and **appended two more clusters** (SaaS-card kit; template chrome). That is era 3 fragmenting into a wider set of co-existing sub-defaults, not a succession.
- There is a visible **human counter-trend** — search results consistently surfaced 2026 trend pieces on "tactile brutalism", raw/monospace/zero-radius layouts, glitch and texture as proof-of-human-authorship. **I did not open these**, deliberately: they are trend-prediction listicles from agency and site-builder blogs about what *human designers* say they will do, which is a different claim from what *tools emit by default*. They do not belong in the source table and they are not evidence of a fourth era. If a later sweep wants them, the recurring titles were Fireart Studio's "Tactile Brutalism & Invisible Architecture", a Medium/Bootcamp piece by Ioana Adriana Teleanu, and the usual Wix/Figma/Hostinger 2026 roundups.
- One genuine caution against declaring era 4 prematurely: P32 argues that when asked to be less generic, the tool shifts "to a different fixed palette rather than producing variety". If that is right, an apparent "new era" could just be the same convergence relocated — which is precisely what era 3 was relative to era 1. Any future era-4 claim should be required to show *increased variance*, not merely a different centroid.

---

## Vendor house looks

Coverage here is uneven and I have flagged where. Only Anthropic has first-party sourcing.

### Anthropic / Claude — the best-documented house look, and the one CO6 is about
- **Palette (first-party, P28):** warm off-white `#faf9f5`, warm near-black `#141413`, warm greys `#b0aea5` and `#e8e6dc`; accents orange `#d97757`, blue `#6a9bcc`, green `#788c5d`. The whole family is warm-shifted — the "black" is a warm near-black, the "white" has a yellow-green cast.
- **Typefaces:** the only faces Anthropic names in a first-party source opened here are **Poppins (headings) and Lora (body)**, with Arial/Georgia fallbacks, in the `brand-guidelines` skill (P28) — and those are chosen for installability in document generation, not as the product's own faces. **No first-party source opened in this sweep names Anthropic's proprietary product typefaces.** One third-party reconstruction was opened (P39) and it names a display face and a UI face; that is a community reverse-engineering of rendered pages, not an Anthropic publication, and I opened no second reconstruction to test whether others agree with it. Do not put a typeface name for Anthropic into the skill on that basis. `[CONTESTED]`
- **What the generated version looks like (P25, P30, P31, P32):** cream ground, high-contrast serif display often italicised and highlighted, terracotta accent, tracked-out subheads, ticker bars, rounded-rectangle outline stacks with neon glow, generous whitespace, editorial rhythm.
- **Imitation:** widely, per P30/P31/P32 — but "widely" is testimony, not a count. The self-incriminating line from P25 is the highest-quality evidence in the sweep: the vendor states that its own accent colour appearing in a user's design reads as a tell.
- **Adjacent industry move (P36):** Perplexity, Runway and Manus also moved to serif in product/brand surfaces. So the serif half of era 3 has at least four vendors behind it; the cream-and-terracotta half is specifically Anthropic-flavoured.

### OpenAI
- **Traits (P35):** custom **OpenAI Sans** (geometric with rounded, friendly modifications; five weights plus italics), refined blossom mark, greys-and-blues base palette with contrasting primaries, a pulsating blue disc as the voice motif. Built 2025 with Studio Dumbar and ABC Dinamo.
- **Direction relative to Anthropic:** cool, grey-blue, geometric-sans — the opposite axis. Output that drifts cool-neutral-sans with a single blue signal is drifting toward this gravity well, not era 3.
- **Sourcing quality:** design-trade reporting only. `openai.com/brand/` returned 403 here, so nothing first-party was opened. `[STALE-RISK]` — the rebrand is 2025 and may have iterated.

### Google / Gemini
- **Not sourced.** I could not open a usable source. `dezeen.com` (the Neural Expressive redesign piece, 2026-05-19) returned 403. Search results describe a "Neural Expressive" design language rolled out at Google I/O 2026 (announced around 2026-05-19), described as extending Material 3 Expressive — fluid motion, vibrant colour, blue-and-white gradient home surface, a detached pill-shaped floating input, new typography, haptics — and Material 3 Expressive itself as announced May 2025, shipping on Pixel with Android 16 QPR1 around September 2025. **None of that was opened and none of it should be treated as verified.** Recorded here as a lead only.

### v0 / Vercel
- **Traits (P34, third-party reconstruction):** monochrome-first — ink `#171717` on `#ffffff` with `#fafafa`/`#f5f5f5` steps, `#ebebeb` hairlines, `#4d4d4d` body, `#888888` mute; a single signal blue `#0070f3`; a small set of two-stop brand gradients (`#7928ca`→`#ff0080`, `#007cf0`→`#00dfd8`, `#ff4d4d`→`#f9cb28`). **Geist** and **Geist Mono**, the mono used for "technical eyebrows". Radii `0 / 6 / 8 / 100 / 9999px` — small on containers, full pill on standalone CTAs.
- **Mechanism:** v0 uses shadcn/ui as its default component layer, which is why era-2 traits and this look are hard to separate.
- **Sourcing quality:** the page states it is an interpretation, not a Vercel publication. `[CONTESTED]` — good enough for a heuristic, not for an assertion.

### Lovable
- **Not sourced.** The one candidate page (a writeup of Lovable's "Aesthetics" feature, which reportedly lets users specify typography/layout/colour to escape the default) returned an empty response. Search results consistently associate Lovable output with Tailwind purple/indigo, gradient titles and boxy dashboards — i.e. **era 1 persisting into 2026** — but nothing was opened. Recorded as a lead. The existing reference file 07 already covers Lovable's prompting docs.

### "Linear-style"
- **Weakly sourced (P38).** The only opened source uses "linear design" to mean sequential single-direction layout and merely credits the company with popularising it. Traits it lists that match practitioner usage: dark mode, bold type, complex gradients, glassmorphism, high contrast, monochrome palettes, minimal CTAs. No hexes, no typefaces, no start date. `[CONTESTED]` — the term is genuinely ambiguous and the skill should either specify values from a better source or drop the label.

---

## Candidate tells

| Label | Description | Supports | Detectable? | Era | False-positive note |
|---|---|---|---|---|---|
| **CO6-a — warm-cream ground** | Page background is a warm off-white in the era-3 family | P25, P28, P30, P31, P32 | **Yes, colour-distance.** Build the centroid only from sourced hexes: `#F4F1EA` (P25), `#F7F1E4` (P32), `#faf9f5`/`#e8e6dc` (P28). Measure in a perceptual space (OKLab/CIELAB ΔE) rather than RGB. Do **not** hard-code a numeric radius until it is calibrated against a real corpus — no source gives one. | 3 | Cream is genuinely correct for bakeries, bookshops, wellness, stationery, print-adjacent brands. Also fires on any legitimate warm-paper editorial design. Advisory only. |
| **CO6-b — terracotta/clay accent** | Single warm-orange accent doing all the brand work | P25, P28, P30, P31, P32 | **Yes, hue-band distance** from `#D97757` (P25/P28) and `#D9622B` (P32). Strongest when combined with CO6-a in the same stylesheet. | 3 | Terracotta is correct for ceramics, Southwest/Mediterranean food, autumn seasonal work. `#d97757` specifically is Anthropic's — its presence in a non-Anthropic brief is the sharpest single signal available (P25 says so explicitly). |
| **CO6-c — reflexive serif display** | High-contrast serif headline chosen with no brief justification, often italicised and highlighted | P25, P30, P31, P36 | **Partially.** A regex over `font-family` can list serif faces, but "reflexive" is a judgment about the brief that no scanner can make. Italic + background-highlight on a display heading is regexable (`font-style: italic` on an `h1`/`h2` plus a `mark`/highlight background). | 3 | Serif is right for publishing, law, academia, literary and heritage brands, and for anything genuinely print-adjacent. Serif alone must never score; only serif **co-occurring** with CO6-a and CO6-b. |
| **CO6-d — subject-independence** | The cream/serif/terracotta trio appears regardless of what the product is | P25, P26, P30 | **No.** This is the actual definition of the tell (P25/P26: "defaults rather than choices, and they appear regardless of subject") and it requires knowing the brief. Any automated CO6 score is a proxy at best. | 3 | This is why CO6 must stay advisory. A scanner that flags cream+serif+terracotta on a bookshop site is wrong, and cannot know it is wrong. |
| **CAND-1 — SaaS-card kit** | Content chopped into identical rounded cards, one radius on everything, the same soft grey shadow under each, gradient washes as decoration | P25 | **Yes, and cheaply.** `rgba(0,0,0,.1)` (or near) as a repeated `box-shadow`; a single `border-radius` value used across all card-like classes; count of visually identical card components. | 2 (resurfaced in the 2026-09 list) | Card grids are correct for genuinely parallel items — product catalogues, search results. The tell is *one* radius and *one* shadow applied without hierarchy, not the card itself. |
| **CAND-2 — template chrome** | Tracked-out ALL-CAPS eyebrow above every heading; `A · B · C` middle-dot meta strings; `WORD — fragment` spaced-em-dash labels; monospace for small data labels; `→` appended to link/button text | P25, P30, P31 | **Yes, regex, high precision.** `text-transform: uppercase` + positive `letter-spacing` on an element immediately preceding a heading; ` · ` between short spans; ` — ` inside a label; a trailing `→`/`&rarr;` in anchor or button text. | 3 | Middle dots are legitimate in real bylines/metadata; `→` is legitimate in a genuine directional control. Count occurrences and flag repetition across sections, not single instances. |
| **CAND-3 — tinted near-black standing in for black** | `#0B0B0B`, `#111`, `#141413`, `#211D18` used as "black" | P25, P28, P32 | **Yes, colour-distance** from pure black with a warm/cool cast test. | 3 | This is standard good practice in a lot of competent design — pure `#000` is often worse. Very weak on its own; only meaningful as a co-occurrence multiplier with CO6-a/b. |
| **CAND-4 — news-ticker bar** | A horizontally scrolling text strip, cable-news style, with no informational reason to move | P30, P31 | **Partially.** A CSS keyframe animating `transform: translateX` on a full-width text container, or a marquee-ish utility class. Moderate precision. | 3 | Legitimate for actual live data — prices, scores, status. Flag only when the ticker content is static marketing copy. |
| **CAND-5 — italic-highlighted serif display** | One phrase in the headline set in serif italic and given a highlight background | P30, P31 | **Yes**, and it compounds with P25's separate rule against accenting a single word in a headline. | 3 | Occasionally a real editorial device. Rare enough in generated-vs-hand-built terms to be worth flagging. |
| **CAND-6 — shimmer "thinking" text** | Animated shimmer/gradient sweep over loading or async text | P37 | **Yes, regex.** A `background-clip: text` plus animated `background-position` keyframe over placeholder/loading copy. High precision. | 3 (product chrome) | Legitimate as a skeleton-loading affordance. The tell is applying it to *text content* as an AI-thinking motif. |
| **CAND-7 — sparkle emoji as AI signifier** | ✨ (or a sparkle icon) used as the mark for anything AI-powered | P37 | **Yes, trivially.** Literal codepoint scan; plus icon-name scan for `Sparkles`/`sparkle`/`wand` in Lucide/Heroicons imports. | 3 (product chrome) | Almost no false positives worth worrying about. Cheapest high-confidence tell in this sweep. |
| **CAND-8 — v0/Vercel monochrome drift** | Pure-monochrome palette with `#0070f3`-ish single signal blue, Geist + Geist Mono, mono used for eyebrows | P34 | **Yes**, colour-distance plus `font-family` scan for `Geist`/`Geist Mono`. | 2/3 | Monochrome-plus-one-signal is a legitimate and often excellent system. Only meaningful when it appears on a brief with no reason to be developer-tool-flavoured. `[CONTESTED]` — palette comes from a third-party reconstruction. |
| **CAND-9 — cool grey-blue geometric-sans drift (OpenAI gravity)** | Grey/blue base, rounded geometric sans, single blue accent | P35 | **Partially.** `OpenAI Sans` is name-detectable; the general look is not, without a calibrated centroid I do not have. | cross-era | Very high false-positive risk — this describes an enormous amount of competent enterprise UI. Do not ship as a scored rule. Note only. |

**One cross-cutting measurement caution (P32):** if a de-slop rule merely pushes output off the cream centroid, the plausible outcome is a *new* shared centroid, not variety. Any eval for these tells should measure **variance across generations**, not just distance from a banned palette. Otherwise the skill risks authoring era 4 itself.

---

## Gaps

1. **No measurement exists, and that is the headline gap.** Every era-3 prevalence claim opened here is qualitative — designer testimony, example collections, one anecdote about two decks. Nobody has sampled generated pages and counted palettes, typeface classes or layout structures over time. A targeted search surfaced only adjacent work (text-homogenisation studies; UI-generation benchmarks scoring CLIP similarity against reference screenshots) — nothing that measures aesthetic drift in generated design. If this skill built even a small dated corpus of generated pages with extracted colour/type/layout features, it would be the first quantitative evidence in the field. That is a real opportunity, not just a gap.
2. **Anthropic's proprietary typefaces are unverified.** No first-party source opened here names them. Third-party reconstructions disagree. The skill must not assert a typeface name for Anthropic on current evidence.
3. **Three vendor looks are effectively unsourced.** Google/Gemini (dezeen 403), Lovable (empty response), and "Linear-style" (only an ambiguous false-friend article). All three need a second pass, ideally with a fetcher that handles 403-ing publishers.
4. **The New Yorker column itself was never opened** — only Chayka's own newsletter trailing it. The column is the canonical citation for the naming event and should be read directly when possible.
5. **Jim Nielsen's essay was read second-hand.** The primary at `blog.jim-nielsen.com/2026/ai-aesthetic/` returned empty here. Its trait list should be verified against the original before any of CAND-6/CAND-7 ships with his attribution.
6. **"Serif renaissance" and "tasteslop" lack dated primaries.** Keya Vadgama's post is referenced without a date or URL in P36. Both coinages are useful register entries but currently rest on one secondary source.
7. **P33 is undated** (page shows "May 27", no year). Its statistics are also about AI-coding adoption, not aesthetics, and should not be cited as evidence about the look.
8. **Era boundaries are discourse dates, not output dates.** The whole timeline above records when people wrote about a look. Whether generated output actually changed on those dates is unknown, and the skill's register should say so wherever it cites an era start.
9. **No colour-distance thresholds are calibrated.** The hexes are sourced; the radius that separates "era-3 cream" from "any warm off-white" is not, and cannot be until gap 1 is closed. Shipping a guessed ΔE threshold would be inventing a number.
