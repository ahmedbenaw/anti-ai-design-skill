# 05 — Mobile App AI-Design Tells & UI/Marketing Copy Tells

Research date: 2026-08-28. All claims traceable to opened sources numbered below (A# for Part A, B# for Part B).

---

# Part A — Mobile app AI-design tells

## Sources

| # | Title | Author type | Date | URL | Takeaway |
|---|---|---|---|---|---|
| A1 | "AI Design Slop: Why Every AI-Built Interface Looks the Same (And How to Fix It)" | Designer, Medium blog (Mohit Phogat) | 2026-08-07 | https://mohitphogat.medium.com/ai-design-slop-why-every-ai-built-interface-looks-the-same-and-how-to-fix-it-bf874e0b470c | Catalogs the slop palette (purple-cyan gradients, indigo-500, Inter everywhere, 3/6-col card grids) and explains the token-prediction cause; fixes via DESIGN.md |
| A2 | "How to fix the 'AI-generated' look in your frontend" | Developer, DEV Community (Alan West) | 2026-05-18 | https://dev.to/alanwest/how-to-fix-the-ai-generated-look-in-your-frontend-1ahh | Names the exact Tailwind classes of the AI look (indigo-600, rounded-2xl, shadow-lg) and the canonical section order; proposes lint rules against them |
| A3 | "How to Make AI UI Look Less Generic: 5 Fixes" | AI-design tool team blog (Jason Zhou, Superdesign) | 2026-06-21 | https://superdesign.dev/blog/how-to-make-ai-ui-look-less-generic | Tell list (Inter/Roboto, purple/indigo gradients, centered hero + single CTA, three-card icon rows, rounded everything, 0.1-opacity shadows); "generic is what one prompt does" |
| A4 | "The Dribbblisation of Design" | Product design VP, Intercom blog (Paul Adams) | 2013-09-18 | https://www.intercom.com/blog/the-dribbblisation-of-design/ | The pre-AI origin of the aesthetic: identical flat-design treatments applied to any domain, optimized for peer approval, not users |
| A5 | "Google Stitch Review (2026): What Users Actually Say" | AI-design tool team blog (Superdesign, aggregating user reviews) | 2026 (reviews Apr–Jun 2026) | https://superdesign.dev/blog/google-stitch-review | Stitch users: output "cannot shake the AI-looking design", inconsistent nav across screens, re-prompt-and-hope iteration; ranked last in a same-prompt test |
| A6 | "Why Fintech Looks the Same" | Brand/marketing agency (Brandon Pazitka, Freshly Brewed) | 2026-05-05 | https://freshlybrewed.co/insights-news/why-fintech-looks-the-same/ | Fintech cliches: purple-to-blue/teal-to-green gradients, floating geometric shapes, Circular/Inter/SF Pro, isometric 3D illustrations, three-column features; copied from Revolut/Monzo/Stripe era |
| A7 | "Mobile-App Onboarding: An Analysis of Components and Techniques" | UX research firm (Alita Kendrick, Nielsen Norman Group) | 2020-06-21 | https://www.nngroup.com/articles/mobile-app-onboarding/ | Research-based case against feature-tour carousels and deck-of-cards tutorials: "tutorials didn't improve task performance"; skip onboarding where possible |
| A8 | "I tested 4 AI tools to generate UI from the same prompt" | UX designer, Medium (Xinran Ma) | 2024-10-25 | https://medium.com/@xinranma/i-tested-4-ai-tools-to-generate-ui-from-the-same-prompt-0d2113736cce | Same-prompt comparison of Wireframe Designer, UX Pilot, Uizard, Galileo AI; all converge on similar mobile-first layouts; Uizard emits whole multi-screen sets from one prompt |
| A9 | "Why AI-Generated UI Looks Good But Often Feels Generic" | Designer, Medium (Samith Pitigala) | 2026-06-01 | https://medium.com/@cssamithpitigala/why-ai-generated-ui-looks-good-but-often-feels-generic-020a9b1b8492 | Mechanism piece: AI outputs "what is common, not what is deeply specific"; healthcare/finance/learning apps all get identical treatment; trend elements (glassmorphism, gradients, soft shadows) repeat without purpose |
| A10 | "Apple Updates App Store Guidelines With Stricter Rules for Low-Quality Apps" | Tech news (MacRumors) | 2026-06-09 | https://www.macrumors.com/2026/06/09/app-store-guidelines-low-quality-apps/ | Guideline 4.3 spam now names saturated template categories; "opportunistically creating variants of existing app categories or popular apps degrades App Store discovery" |

## Tells

### 1. Purple-blue / purple-cyan gradient everything
- **What it looks like:** Gradient hero headers, gradient buttons, gradient app icons — almost always in the indigo→violet→cyan band. A1 calls out "purple-to-cyan gradients" and "indigo-500 defaults"; A3 lists "purple or indigo gradients" as a core marker; A6 documents "gradient backgrounds (purple-to-blue or teal-to-green)" as a fintech-wide cliche.
- **Code/structure pattern:** Tailwind defaults are the fingerprint: `bg-indigo-600 hover:bg-indigo-700`, `from-purple-* to-blue-*` gradient utilities (A2). A1 traces it to indigo-500 being Tailwind's showcased primary.
- **Tools named:** Claude Code, Cursor, v0 (A1); Tailwind, shadcn/ui (A2); Google Stitch outputs described as unable to "shake the AI-looking design" (A5).
- **Sources:** A1, A2, A3, A5, A6.
- **Quotes:** "Purple-to-blue gradient hero...CTA button with `bg-indigo-600 hover:bg-indigo-700`" (A2). "For visual choices, 'most probable' means the statistical average of millions of templates" (A1).
- **Counter-evidence:** A6 shows purple gradients predate AI — they were a deliberate 2015–2018 fintech-disruptor signal (Revolut, Monzo, Stripe) that the industry then copied. A human team that shipped a purple gradient in 2019 was on-trend, not AI-assisted.

### 2. Inter / Roboto / system-default typography with no pairing
- **What it looks like:** One neutral grotesque used at every size and weight; no display face, no intentional pairing; hierarchy carried only by `font-bold`.
- **Code/structure pattern:** "Inter for everything, with the occasional `font-bold` for headings" (A2); "Inter font everywhere, in every weight" (A1).
- **Tools named:** Tailwind defaults (A2); A6 lists Circular, Inter, SF Pro as the fintech-standard set.
- **Sources:** A1, A2, A3, A6.
- **Quotes:** "Inter or Roboto typefaces without personality" (A3).
- **Counter-evidence:** Inter and SF Pro are also the deliberate choice of large, well-designed products (SF Pro is the iOS system font); font alone is a weak signal without the other tells co-occurring (implied by A6's pre-AI fintech usage).

### 3. Rounded-everything + soft-shadow card soup
- **What it looks like:** Every surface a rounded-corner card with a faint drop shadow; excessive padding; no square edges, no dividers, no density variation.
- **Code/structure pattern:** `rounded-2xl` + `shadow-lg`, "three cards in a row with excessive padding" (A2); "drop shadows at 0.1 opacity", "rounded corners on every element" (A3); "rounded corners throughout", "status pills and stat cards with green arrows" (A1).
- **Sources:** A1, A2, A3.
- **Counter-evidence:** Card-based layouts are the Material Design and iOS-widget default; rounded cards per se are universal. The tell is uniformity — identical radius/shadow on every element with no exceptions (A2's fix is a consistent-but-intentional "component vocabulary," not squarer corners).

### 4. Centered hero + three-card feature grid layout skeleton
- **What it looks like:** Centered composition, one CTA under the headline, then a 3-column (or 6-column) grid of cards, each: icon, heading, exactly two lines of text.
- **Code/structure pattern:** "Hero → features grid → social proof → pricing → FAQ → footer" as vertically stacked full-width sections (A2); "icon + heading + exactly two lines of text per card" (A1); "centered hero layouts with single CTA, three-card icon rows" (A3); "three-column feature layouts" also standard in human fintech (A6).
- **Sources:** A1, A2, A3, A6; shitfa.st (B2) confirms "three-card feature grids with identical formatting" from the copy side.
- **Quotes:** A1's fix: "Forbid six-column grids explicitly."
- **Counter-evidence:** A6 and B3 (minimaxir: "landing pages were already heavily templated prior to agents") — this skeleton was a human template convention first.

### 5. Three-slide onboarding carousel with illustrations
- **What it looks like:** Swipeable 3-screen feature-promotion deck (illustration, headline, one line of copy, page dots, Skip) before the user sees the product.
- **Code/structure pattern:** PageView/carousel + page indicator + skip button; NN/g's taxonomy calls these feature-promotion decks and "deck-of-cards" tutorials (A7).
- **Sources:** A7 (pattern and critique); A8 (AI tools emit full multi-screen sets including onboarding from one prompt).
- **Quotes:** Deck-of-cards tutorials "tend to make the interface appear more complicated than it actually is, and strains user's memory" (A7); "tutorials didn't improve task performance" (A7).
- **Counter-evidence:** This is a decade-old human pattern (NN/g criticized it in 2020, pre-generative-AI). It signals template-thinking, not necessarily AI authorship. NN/g also allows onboarding for genuinely novel interaction patterns.

### 6. Interchangeable domain treatment (fintech = healthcare = learning app)
- **What it looks like:** The same visual system regardless of product domain: a meditation app, a bank, and a project tracker share gradients, cards, ring charts, and tone.
- **Sources:** A9, A4, A1.
- **Quotes:** "A healthcare app, a finance app, a learning app, and a project management app should not all feel the same" (A9). Pre-AI version: "Whether it's social software, accounting software, a marketing site, a weather app, the same styles are applied" (A4, 2013).
- **Counter-evidence:** A4 proves the sameness disease predates AI by a decade — Dribbble peer-approval culture produced it first. AI tools trained on those shots industrialized it.

### 7. Big rounded balance card + ring/progress-chart dashboard
- **What it looks like:** Fintech/health dashboards led by one large rounded balance or stat card, green up-arrows, ring progress charts — the Dribbble-shot dashboard.
- **Sources:** A1 ("status pills and stat cards with green arrows"), A6 (fintech hero conventions), A4 (Dribbble weather-app example: beautiful, identical, non-functional).
- **Quotes:** "Things that look great but don't work well" (A4). "A screen that looks good in one static image is not the same as a product that works across different states, errors, devices" (A9).
- **Counter-evidence:** Balance-card-plus-chart is also the information architecture of genuinely good banking apps; the tell is absence of edge states (empty, error, loading) and of any data the chart could really show (A9).

### 8. Glassmorphism, neon glows, floating shapes, isometric 3D blob illustrations
- **What it looks like:** Frosted-glass panels with neon accent glows (A1), "floating geometric shapes" and "isometric illustrations and abstract 3D elements" (A6), trend elements applied without purpose (A9).
- **Sources:** A1, A6, A9.
- **Quotes:** "Common trendy elements (glassmorphism, gradients, soft shadows) repeat across outputs without strategic purpose" (A9).
- **Counter-evidence:** Each was a legitimate human trend cycle (glassmorphism ~2020–21, corporate-blob illustration ~2018–20); dating the design correctly matters before attributing to AI.

### 9. Cross-screen inconsistency (the AI-specific giveaway)
- **What it looks like:** Generated screens that individually look polished but drift: the top nav renders differently on different pages, spacing/radius vary per component, styles don't compose into a system.
- **Sources:** A5, A2 (per-component "drift" needing a component vocabulary), A8 (outputs "required additional refinement work").
- **Quotes:** "my top navigation looked a little different on different pages" (Product Hunt reviewer, in A5); "cannot just tweak a font or a background; you re-prompt and hope" (A5).
- **Counter-evidence:** None found — inconsistency-despite-polish is closer to a true AI/template fingerprint than any single visual trope, because human design systems enforce the opposite.

### 10. Template-category app clones (App Store 4.3 spam profile)
- **What it looks like:** Whole apps that are re-skins of a saturated template category — timers, wallpapers, sound effects, fortune telling — differing only in gradient and icon.
- **Sources:** A10.
- **Quotes:** Apps in saturated categories now rejected unless "meaningfully different or improved"; "opportunistically creating variants of existing app categories or popular apps degrades App Store discovery, reduces overall app quality, and harms both users and developers" (A10).
- **Counter-evidence:** A10's article notes the guideline text does not mention AI specifically — 4.3 spam predates and is broader than AI generation.

### 11. Why it happens (mechanism, for the record)
- LLMs predict the statistical average of training data dominated by templates and tutorials: "A language model predicts the most probable next token... 'most probable' means the statistical average of millions of templates" (A1); "Most AI-generated UI is based on what is common, not what is deeply specific" (A9); "Generic is what one prompt does when it has to pick taste, explore, and write code all at once" (A3). Default config files (Tailwind) dominate public code samples (A2).
- Documented fixes across A1/A2/A3: a written DESIGN.md with exact hex/font/radius decisions; capped 4–5 color palette; named font pairing; explicit bans ("no six-column grids"); custom (not extended) Tailwind palette; asymmetric layouts; lint rules failing builds on banned classes; extract a design system before generating screens.

### Tools named across Part A sources
Claude Code, Cursor, v0 (A1); Tailwind, shadcn/ui, ESLint (A2); Superdesign, Nano Banana Pro, FLUX.2, Ideogram v3, Imagen 4 Ultra, Recraft, GSAP, Motion.dev (A3); Google Stitch, Claude Design, Figma Make (A5); Wireframe Designer, UX Pilot, Uizard, Galileo AI (A8). Note: Galileo AI became Google Stitch (per search results; the Banani review title states "Galileo AI for UI Design (now Google Stitch)").

---

# Part B — UI and marketing copy tells

## Sources

| # | Title | Author type | Date | URL | Takeaway |
|---|---|---|---|---|---|
| B1 | "Wikipedia:Signs of AI writing" (WP:AISIGNS) | Wikipedia project page (WikiProject AI Cleanup), read in full via raw wikitext | live, updated Aug 2026 | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | The canonical field guide: AI vocabulary lists by model era, puffery, vague attribution, negative parallelism, rule of three, title case, boldface, em dashes, emoji headers, curly quotes, cutoff disclaimers, placeholder text |
| B2 | shitfa.st — "An archive of landing pages that all read like one AI wrote them" | Satirical catalog site | 2026 (live) | https://shitfa.st/ | Documents fake-proof patterns: unverifiable "Trusted by 5,000+ teams", first-name-only testimonials, fake logo bars, AI founder headshots, "for modern teams" hero copy, ShitScore calculator |
| B3 | "Are we in the era of AI slop landing pages?" (HN discussion) | Practitioner forum thread | 2026 | https://news.ycombinator.com/item?id=49024805 | Practitioners name tells: "Trusted by 10,000+ professionals" contradicted by traffic data, identical card layouts; counterpoint that templates predate AI |
| B4 | "Stop Sounding Like AI" | UX-writing newsletter (Sathya, Microcopy Examples) | 2025-02-27 | https://microcopyexamples.substack.com/p/stop-sounding-like-ai | Word list (Elevate, Unlock, Curate, Delight, Infused, Game-changer, Revolutionize) with human rewrites; "write how you talk" |
| B5 | "Avoid 'landing page words'" | UX-writing newsletter (Sathya, Microcopy Examples) | 2024-12-23 | https://microcopyexamples.substack.com/p/avoid-landing-page-words | Unlock/Unleash/Empower/Supercharge/Game-changer as "empty buzzwords"; replace with concrete task-level benefits |
| B6 | "Week 16: 10 phrases that scream AI" | Writer's newsletter (Tan Rosado) | 2024-10-11 | https://tanrosado.substack.com/p/week-16-10-phrases-that-scream-ai | 10-phrase list (Seamlessly integrated, In today's fast-paced world, cutting-edge, game-changer, Un- verbs); notes humans get falsely accused |
| B7 | "No One Wants to 'Get Started'" | UX writer newsletter (Natalie Sacks) | 2024-07-08 | https://nataliewritesthings.substack.com/p/no-one-wants-to-get-started | Why "Get Started" is vague and burden-framing; CTAs should name the specific action ("Open an account", "View offer") |
| B8 | "13 Call-to-Action (CTA) buttons that go beyond 'Learn More' and 'Get Started'" | Business services blog (Smith.ai) | updated 2026-05-06 | https://smith.ai/blog/13-call-to-action-cta-buttons-that-go-beyond-learn-more-and-get-started | "Learn More tells a visitor almost nothing"; outcome-named, first-person CTAs outperform |
| B9 | "Don't Write Like AI: 10 Takeaways from Wikipedia's Signs of AI Writing" | Content-marketing blog (Blake Stockton) | 2025-08-07 | https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/ | Practitioner distillation of B1: inflated symbolism, "**Scalability:** The system..." bolded bullets, em dashes, vague attribution |
| B10 | "How Users Read on the Web" | UX research (Jakob Nielsen, NN/g) | 1997-09-30 | https://www.nngroup.com/articles/how-users-read-on-the-web/ | Pre-AI baseline: promotional "marketese" measurably hurts usability (objective language +27%, concise +58%); users "detested" boastful claims |

## Word/phrase list

### Headline verbs (the "transformation" verbs)
- **Elevate, Unlock, Unleash, Unveil, Unmask, Empower, Supercharge, Revolutionize, Transform, Curate, Delight, Infuse** — B4 ("Unlock your true potential with our cutting-edge solutions" as the archetype), B5 (Unlock/Unleash/Exceed/Empower/Supercharge), B6 (item 10: "Unveil, Unlock, Unleash, Unmask (UN-) — dramatic reveal language"), A2 ("Empower," "Unlock," "Transform" as generic frontend copy).
- **Enhance, boasts, showcase, highlight (v.), underscore (v.), delve, foster, garner** — B1's cited-study AI-vocabulary box (each word backed by refs to Juzek & Ward 2025, Kobak et al. 2025, Russell et al. 2025, Kriss/NYT 2025).

### Adjectives and abstract nouns
- **Seamless/seamlessly, effortless(ly), cutting-edge, game-changer, transformative, innovative, all-in-one, world-class, next-generation** — B6 (items 1, 5, 6, 9), B4, B5 ("world-class solutions").
- **crucial, pivotal, key (adj.), robust, vibrant, rich, profound, intricate, meticulous, enduring, valuable, landscape (abstract), tapestry (abstract), testament, interplay** — B1 AI-vocabulary box; B1 also dates them by model era (2023–mid-2024 GPT-4: delve/tapestry/testament/pivotal; mid-2024–2025 GPT-4o: align with/fostering/showcasing; 2025+: emphasizing/enhance/highlighting/showcasing).
- **Puffery set:** "boasts a", "renowned", "groundbreaking", "diverse array", "nestled", "in the heart of", "rich cultural heritage", "natural beauty", "commitment to" (B1 promotional-language section; B9).

### Significance inflation (headline/sub-head filler)
- "stands as / serves as", "is a testament to", "plays a vital/pivotal/crucial role", "marks/represents a significant shift", "setting the stage for", "evolving landscape", "indelible mark", "deeply rooted", "underscores its importance" (B1 "Undue emphasis on significance" box; B9's "inflated symbolism").
- Openers: "In today's fast-paced world" (B6 item 2); "Welcome to the future of X" is the marketing-page variant of the same significance-inflation move (pattern per B2's hero-copy catalog and B1's puffery; exact phrase not itemized in either — flag as inference).

### Triads (rule of three)
- LLMs "overuse the rule of three... from 'adjective, adjective, adjective' to 'short phrase, short phrase, and short phrase'", often "to make superficial analyses appear more comprehensive" (B1, citing Russell et al., Kriss, The Economist 2026-07-30).
- UI form: three feature cards titled with abstract pairs — "Fast / Secure / Scalable" style. A1 (three-column feature grids, "icon + heading + exactly two lines"), A2 (abstract feature titles like "Seamless Integration"), B2 (three-card feature grids). The specific triad wording is the copy-side of Part A tell #4.
- Bolded-bullet triads: "**Scalability:** The system..." — a ChatGPT list convention (B9; B1 inline-header vertical lists WP:AILIST).

### CTA labels
- **"Get Started"** — vague, burden-framing: "You're telling the user that there's a bunch of things they need to do and not even sharing what they are" (B7).
- **"Learn More"** — "tells a visitor almost nothing" (B8); NN/g-style guidance echoed by both: name the action/outcome instead ("Open an account", "View offer", "Start Your Free Trial", "See Plans and Pricing") (B7, B8).
- The **"Get Started" + "Learn More" pair** as dual hero buttons is the composite tell: it's the default emitted in the hero → features → pricing skeleton (A2's canonical section order; B2's archive).
- Also flagged as AI-ish: "Ready to...?" pre-CTA question ("Ready to transform your workflow?") (B4).

### Fake-proof patterns (social proof that doesn't check out)
- **Inflated counts:** "Trusted by 5,000+ teams" / "10,000+ professionals" on recently-registered domains, contradicted by traffic data (B2, B3).
- **Unverifiable logo bars:** "fake authority logo bars with unverifiable brands" (B2).
- **Testimonial shape:** first names or initials only — "Sarah K., verified customer" (B2); AI-generated founder/customer headshots with "perfect pores and no life behind the eyes" (B2).
- **Precision theater:** "99.9% uptime"-style stats and perpetually "pending" security badges (B2).
- **Vague attribution (body-copy version):** "Industry reports", "Experts argue", "Observers have cited", "Some critics argue" without citable sources (B1 WP:AIWEASEL; B9).

### Punctuation / formatting tells
- **Em dash overuse** — used "in places where humans are more likely to use commas, parentheses, colons", "in a formulaic, pat way, often mimicking 'punched up' sales-like writing"; AI em dashes usually spaced, contrary to typographic convention (B1 WP:AIDASH).
- **Title Case Everywhere** — "In section headings, AI chatbots strongly tend to capitalize all main words" (B1 WP:AITITLECASE).
- **Emoji as formatting** — emoji prefixed to headings and bullets ("👋 Welcome...", "🎯 What I'm Working On"); "✨" before "AI-powered" is the marketing-page instance of the same habit (B1 WP:AIEMOJI documents the heading-emoji pattern; the ✨-specific pairing is not itemized in opened sources — flag as inference).
- **Boldface overuse** — "emphasize every instance of a chosen word or phrase, often in a 'key takeaways' fashion", inherited from readmes/listicles/sales pitches (B1 WP:AIBOLD).
- **Negative parallelism** — "It's not just X, it's Y" / "not X, but Y" / "no ..., no ..., just ..." (B1 WP:AIPARALLEL, citing Russell et al., Kriss, Economist; B9). Marketing form: "It's not just a [product]; it's a [metaphor]" (B4 flags exactly this template).
- **Robotic enumeration** — "Firstly, secondly, lastly" (B6); sentence-initial "Additionally," "Moreover," "Furthermore" (B1 AI-vocab; B9).
- **Curly quotes/apostrophes** where the rest of a codebase/site uses straight ones, or inconsistent mixing (B1 WP:AICURLY).
- **Leftover phrasal templates** — unfilled "[Describe the specific...]" placeholders and knowledge-cutoff disclaimers ("As of my last knowledge update...") shipping in production copy (B1 WP:AIPLACEHOLDER, WP:AICUTOFF).

## Structural copy tells

- **Canonical page skeleton:** "Hero → features grid → social proof → pricing → FAQ → footer" as vertically stacked full-width sections (A2); B3 commenters describe "cookie-cutter templates lacking differentiation" and "identical card layouts and color schemes across multiple sites."
- **Hero copy formula:** vague value proposition "for modern teams," no product demonstration, waitlist instead of product (B2).
- **Testimonial shape:** three cards, first-name-plus-initial attribution, stock/AI headshot, each testimonial restating a feature bullet in first person (B2's catalog: first-names-only + generated headshots; B3: metrics contradicted by reality).
- **FAQ shape:** SEO-bait questions "nobody typed" (B2) — the same 5 generic questions (pricing, security, cancellation, support, "is X right for me") appended to every page; B2 frames this as "SEO optimization targeting questions nobody typed."
- **Section summaries and outline-like endings:** concluding "challenges and future prospects" boilerplate and headings that contain only other headings (B1).
- **Roadmap theater:** public roadmaps with vague timeline statuses standing in for shipped functionality (B2).

## What good human copy does instead

- **Objective, specific, concise.** Nielsen's 1997 study: objective language improved usability 27%, concise text 58% vs promotional control; users "detested" marketese and "want to get the straight facts"; "credibility suffers when users clearly see that the site exaggerates" (B10).
- **Concrete benefit over abstraction:** "Our app helps you organize your tasks, saving you hours each week" instead of "Supercharge your productivity with our revolutionary app" (B5); "New flavors. No gimmicks. Just great taste." instead of "an ever-changing world of delightful flavors" (B4).
- **CTAs that name the action or outcome:** "Open an account", "Add to cart", "Browse flights" before "Book flight", "View offer" (B7); outcome-named and first-person copy ("Start my free trial") outperforms generic actions (B8).
- **Voice:** "Write how you talk—clear, engaging, and real" (B4).
- **Effort as trust signal:** "A good product has a soul... trust is built on invested effort" (elenaviter, B3); real practitioners study competitors, customize copy, hand-edit AI output rather than shipping the template (n8n_and_coffee, B3).

## High false-positive phrases (common in human copy too)

- **"Let's dive in"** — B6 explicitly flags it as "flagged as AI despite legitimate use"; B6's whole thesis is that "skilled human writers legitimately use these phrases, yet face unfair accusations."
- **Em dashes** — B1 stresses this sign is "most useful in combination with other indicators, not by itself"; per the Economist study B1 cites (2026-07-30), of contemporary models only Claude used em dashes more than professional writers — ChatGPT used them less. Professional human writers use them heavily.
- **Curly quotes** — auto-inserted by Word smart quotes, macOS/iOS system-wide, Chicago-style publishing (B1).
- **"Seamless", "cutting-edge", "game-changer", "empower"** — standard human marketing-speak for decades; B10 shows marketese was a documented human plague in 1997. B5 calls them "empty buzzwords" (a quality problem) rather than AI proof.
- **Title case** — house style for many US publications and Apple's own marketing.
- **Rule of three** — a classical rhetorical device; B1 notes negative parallelism is "common among human writers (especially in 'common misconceptions'... listicles)."
- **"Trusted by N+ customers" rows and Get Started/Learn More pairs** — human growth-marketing convention long before AI; B3's minimaxir: "Landing pages were already heavily templated prior to agents."
- **General caveat from B1 (verbatim):** "Not all text featuring these indicators is AI-generated, as the large language models... are trained on human writing"; the list is "descriptive, not prescriptive"; and AI vocabulary shifts by era — "delve" spiked in 2023–24 then "dropped off sharply in 2025," so word lists date quickly.

## Gaps

- **FlutterFlow:** the one substantive source on the "default FlutterFlow look" (flutterflowclub.substack.com) was unfetchable (robots/rate-limit). The template-look claim for FlutterFlow specifically rests on search-result titles only ("How to Make Your FlutterFlow App Stand Out & Feel More Custom"), not opened content.
- **Uizard/Figma Make specifics:** A8 covers Uizard's multi-screen output but not a detailed visual critique; the fintech-prompt Uizard test article (Mericler, Medium) returned only metadata. No opened source examined Figma Make output.
- **Glossy gradient app icons and "emoji icons" as UI iconography:** asserted in the brief but not specifically documented in any opened source; nearest support is B1's emoji-as-formatting (copy) and A1/A6 gradient culture (inference).
- **"Welcome to the future of X"** and **"✨ AI-powered"** exact strings: pattern-consistent with opened sources (B1 puffery, B1 emoji, B2 hero-copy catalog) but not verbatim itemized anywhere opened — marked as inference above.
- **5-tab bottom bars:** no opened source discusses tab-bar count as an AI tell; both Apple HIG and Material allow 3–5 tabs, so this is likely a platform convention, not a tell — treat as high false-positive risk.
- **Quantitative evidence:** apart from B10 (1997 usability) and studies cited inside B1 (Juzek & Ward, Kobak et al., Russell et al., Economist), no opened source measures how often the mobile-visual tells co-occur with actual AI authorship; most Part A evidence is practitioner observation.
- **Paywalled:** Washington Post em-dash analysis and Forbes App-Store-slop piece (403) were not readable; em-dash claims rely on B1's summary of those sources.
