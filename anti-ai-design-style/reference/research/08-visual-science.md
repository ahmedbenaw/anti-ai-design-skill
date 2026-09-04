# Visual-science sources on AI-design tells

Research pass on the visual side of AI-generated web/mobile design: colour, imagery, illustration, iconography, motion, layout rhythm. 18 web searches run (including domain-restricted passes on nngroup.com, smashingmagazine.com, arxiv.org); 20 sources opened and read in full via WebFetch. Every tell below traces to at least one opened source (# in the table).

## Sources

| # | Title | Author / Org | Type | Date | URL | Takeaway |
|---|-------|--------------|------|------|-----|----------|
| 1 | Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500) | Alan West / DEV Community | Practitioner blog | ~2025 | https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p | LLMs reproduce the statistical median of Tailwind-era landing pages: `bg-indigo-500`, `from-indigo-500 to-purple-600`, Inter, 3-column feature grids; feedback loop as AI output re-enters training data. |
| 2 | Why does AI keep making everything blue-purple? | chaiovercode / Substack | Practitioner essay | ~2025 | https://chaiovercode.substack.com/p/why-does-ai-make-everything-blue | Root-causes the violet skew to Tailwind's 2020 indigo-500 default flooding tutorials/scraped code; "AI conflates frequency with optimality." |
| 3 | The rise of Linear style design | Arlene Xu / Medium (Design Bootcamp) | Design essay + tutorial | ~2023 | https://medium.com/design-bootcamp/the-rise-of-linear-style-design-origins-trends-and-techniques-4fd96aab7646 | Documents the Linear.app aesthetic (dark bg, animated glow gradients, blur, Inter) and its copying across SaaS; "dark mode" jokingly renamed "linear style." |
| 4 | Spot the Slop: A UI Designer's Guide to Fixing AI Defaults | Mania Design (Kosta C.) | Practitioner guide | 2025–26 | https://www.mania.design/blog/spot-the-slop-a-ui-designers-guide-to-fixing-ai-defaults/ | Seven named AI-default patterns (Inter, purple-blue gradient, uniform 16px radius / 24px padding, missing edge states, uniform fade-ins) with per-pattern fixes. |
| 5 | Slop (pattern catalogue) | Impeccable (impeccable.style) | Pattern catalogue | 2026 | https://impeccable.style/slop/ | Largest itemised catalogue of generated-UI signatures: purple/cyan-on-dark, glass cards, gradient text, icon-tile feature cards, hero eyebrow pills, image hover scale, pulsing dots, marquees, bounce easing. |
| 6 | AI Slop Web Design: Complete Guide (2026) | 925 Studios | Agency guide | 2026 | https://www.925studios.co/blog/ai-slop-web-design-guide | Ties tells together (Inter, purple-blue gradients, impossibly-lit stock photos, 16px-radius card grids, generic fade-ins) and cites conversion/quality numbers. |
| 7 | Low-Contrast Text Is Not the Answer | Katie Sherwin / NN/g | Research-backed article | 2015-06-07 | https://www.nngroup.com/articles/low-contrast/ | Low-contrast grey text harms legibility, discoverability, trust; cites WCAG 1.4.3. |
| 8 | AI-Generated Images Can Perform as Well as Stock Photography | Rachel Banawa / NN/g | Quant user study (n=77) | 2026-08-21 | https://www.nngroup.com/articles/ai-generated-images/ | Counter-evidence: with origin unknown, AI hero images scored slightly HIGHER on trust/professionalism than real stock; users noticed representation, not artifacts. |
| 9 | Chroma Clues: Leveraging Color Statistics to Detect Synthetic Images | arXiv 2606.02224 | Peer-track CS paper | 2026 | https://arxiv.org/html/2606.02224 | AI images carry measurable chrominance anomalies (saturation-channel fingerprints, cross-channel correlations); 93.27% avg detection accuracy, 99.4% on SD-vs-COCO. |
| 10 | Crafting Synthetic Realities: Visual Realism and Misinformation Potential of Photorealistic AI Images | arXiv 2409.17484 | Content-analysis study | 2024 | https://arxiv.org/html/2409.17484v2 | Quantifies the "AI look": 92%+ high image quality, 93–98% vivid colour, staged pro lighting, shallow DoF; only 8% show detectable flaws (of those, 84% anatomical). |
| 11 | Corporate Memphis | Wikipedia | Encyclopedic (sourced) | current | https://en.wikipedia.org/wiki/Corporate_Memphis | Documents the flat big-tech illustration style (Facebook "Alegria", 2017, agency Buck): disproportionate limbs, small heads, flat brights; criticism as "lazy". |
| 12 | Why do AI company logos look like buttholes? | VelvetShark | Practitioner essay | ~2024 | https://velvetshark.com/ai-company-logos-that-look-like-buttholes | ~8–10 AI-company logos converge on circular/radial gradient orbs; drivers: circle symbolism, copycat legitimacy, design-by-committee. |
| 13 | The Proliferation and Problem of the ✨ Sparkles ✨ Icon | Kate Kaplan / NN/g | Quant icon study (n=107) | 2024-09-20 | https://www.nngroup.com/articles/ai-sparkles-icon-problem/ | Sparkle icon is ambiguous: 0 participants read it as "AI"; only 11.22% associated it with special info; confused with star/favourite (73% read stars as favourite). |
| 14 | Rise of the AI Sparkle Icon | Pozos & Schmidt / Google Design | Corporate research (n=2000, 8 countries) | 2024 | https://design.google/library/ai-sparkle-icon-research-pozos-schmidt | Counter-evidence: in Google-product contexts users DO recognise sparkle as AI; one sparkle suffices; ~100 Google system icons carried sparkles by 2024. |
| 15 | You Don't Need Animations | Emil Kowalski | Practitioner authority essay | 2025 | https://emilkowal.ski/ui/you-dont-need-animations | Animation appropriateness = f(frequency): never animate keyboard-driven actions; UI animation < 300ms; "sometimes the best animation is no animation." |
| 16 | Web Interface Guidelines | Rauno Freiberg | Practitioner authority checklist | current | https://interfaces.rauno.me/ | Interaction animations ≤ 200ms; no extraneous animation on frequent low-novelty actions; scale from ~0.96 not 0.8; pause offscreen loops; honour reduced motion. |
| 17 | Motion (Human Interface Guidelines) | Apple | Platform guideline | current | https://developer.apple.com/design/human-interface-guidelines/motion (read via mirrored text) | "Don't add motion for the sake of adding motion"; gratuitous animation distracts and can cause discomfort; make motion optional. |
| 18 | Duration & Easing (Material Design) | Google Material | Platform guideline | current (M1 doc; M3 equivalent JS-gated) | https://m1.material.io/motion/duration-easing.html | Numeric envelope: mobile 300ms standard (225 in / 195 out, max 400ms), desktop 150–200ms; asymmetric easing; linear motion reads mechanical. |
| 19 | Scroll-Triggered Text Animations Delay Users | Aurora Harley / NN/g | Usability-study article | 2017-04-16 | https://www.nngroup.com/articles/scroll-animations/ | Scroll-reveal on body content delays reading and frustrates task-focused users; if used, secondary content only, first scroll only. |
| 20 | Interrogating Design Homogenization in Web Vibe Coding | arXiv 2603.13036 | Sociotechnical analysis (63 sources + 6 platform walkthroughs) | 2026 | https://arxiv.org/html/2603.13036v1 | Frames homogenisation across ChatGPT Canvas, Gemini Canvas, Claude Artifacts, Lovable, v0, Replit; Western minimalist defaults override regional norms; proposes "productive friction." |

## Tells by topic

### Colour

**1. AI purple / violet-indigo default accent**
- What it looks like: indigo-to-violet primary buttons, links, and accents on white or near-black; hue band roughly 240–280°.
- Measurable signal: presence of Tailwind classes `bg-indigo-500` (#6366F1, hue ≈ 239°), `text-indigo-600`, `violet-500` (#8B5CF6, hue ≈ 258°); hue histogram of accent colours concentrated in ~240–290°; % of generated pages whose primary CTA falls in that band.
- Sources: #1, #2, #5, #6, #20.
- Quote: "AI conflates frequency with optimality" (#2); "Purple/violet gradients and cyan-on-dark are the most recognizable tells of AI-generated UIs" (#5).
- Counter-evidence: none of the opened sources defends violet per se; #2 notes indigo was a deliberate, defensible Tailwind design choice — the problem is repetition, not the hue.

**2. Purple-to-blue gradient (hero, CTA, headings)**
- What it looks like: linear gradient sweeping indigo→purple (sometimes →pink) across hero backgrounds, buttons, or clipped into headline text.
- Measurable signal: count of `linear-gradient(...)` declarations whose stops span hues 220–300°; Tailwind `from-indigo-500 to-purple-600` / `from-purple-* to-pink-*` class counts; gradient-text via `background-clip: text`.
- Sources: #1, #4, #5, #6.
- Quote: "It's decoration standing in for a color system" (#4); "Gradient text is decorative rather than meaningful. A common AI tell, especially on headings" (#5).
- Counter-evidence: gradients are core to legitimate systems (e.g. Linear's own brand, #3); the tell is unmotivated gradients, not gradients as such.

**3. "Linear-style" dark mode with glowing gradients / aurora backgrounds**
- What it looks like: near-black page, blurred multi-colour gradient blobs ("aurora"/mesh) glowing behind content, grid lines, micro-motion, Inter in grey-on-black.
- Measurable signal: dark base (<#111) + ≥1 large blurred radial/angular gradient layer (`filter: blur(40px+)` on a positioned gradient div); coloured `box-shadow` glows on dark.
- Sources: #3, #5.
- Quote: some jokingly suggested renaming "dark mode" as "linear style" (#3); "Dark backgrounds with colored box-shadow glows are the default 'cool' look of AI-generated UIs" (#5).
- Counter-evidence: #3 records functional origins — Linear's founder chose dark UI for engineer familiarity, eye strain, battery; the style is not inherently slop, only its reflexive copying.

**4. Oversaturation / uniformly vivid colour**
- What it looks like: everything maximally colourful; no muted or neutral passages; AI imagery in particular near-universally vivid.
- Measurable signal: 93–98% of photorealistic AI images are vividly coloured (#10); AI-generated images carry statistically detectable saturation-channel fingerprints — 99.4% classifier accuracy for SD vs COCO (#9); mean HSV saturation of page imagery/accents vs human-made baselines.
- Sources: #9, #10.
- Quote: "Perturbations in the luminance components have an effect... around magnitude 4 stronger than... the chrominance components" (#9 — why generators get colour statistics wrong).
- Counter-evidence: #10 notes high polish makes images MORE convincing to lay viewers, not less; vividness reads as "professional."

**5. Low-contrast grey body text**
- What it looks like: light-grey paragraphs on white (or dim grey on black), especially secondary copy; standard on AI-generated marketing pages via `text-gray-400/500`.
- Measurable signal: WCAG contrast ratio below 4.5:1 for body text (SC 1.4.3, cited in #7); count of text nodes under threshold.
- Sources: #7 (the authority), #5 (grey-on-black Linear-style body copy noted in #3).
- Quote: "Low-contrast text does look minimal, the same way a blurred photo on Instagram can look retro. But you wouldn't blur your website" (#7); "People are less trusting of text that is hard to read" (#7).
- Counter-evidence: none found; NN/g position predates AI and is broadly accepted.

**6. Cream/beige "tasteful" background (the counter-slop slop)**
- What it looks like: warm off-white (#FAF7F2-ish) page ground adopted reflexively when models try to avoid looking like AI.
- Measurable signal: page background in a narrow warm-cream band paired with a serif display face.
- Sources: #5.
- Quote: "A warm cream or beige page background has become the default 'tasteful' AI surface, reached for by reflex" (#5).
- Counter-evidence: warm neutrals are also a hallmark of deliberate editorial design; only diagnostic in combination with other tells.

### Imagery

**7. Over-polished "AI stock photo" look (smooth skin, staged lighting, shallow DoF)**
- What it looks like: hero photos with professional theatrical lighting (Rembrandt-style shadows), impossibly clean offices, glossy symmetric faces, cinematic bokeh.
- Measurable signal: from #10's content analysis of photorealistic AI images: 92%+ rated high image quality, 93–98% vivid colour, ~68% contain humans, 73% of those with identifiable faces, 58–61% contain surreal combinations; from #9: chrominance/cross-channel statistics separable from natural photos at 93.27% average accuracy across DALL-E 2/3, Midjourney 5/6, SD 1.5, SDXL, Firefly.
- Sources: #9, #10, #6, #8.
- Quote: "diverse group of people looking at a laptop in an impossibly well-lit office" (#6); AI illustrations feel "slightly too smooth, slightly too symmetrical" (#6).
- Counter-evidence: #8 (NN/g, n=77, 2026) — when origin was undisclosed, AI-generated consulting-site hero images scored 0.2–0.4 points HIGHER (7-pt scale) on trust/professionalism/authenticity than real stock; participants commented on diversity and team dynamics, not artifacts. The "tell" is increasingly invisible to users at 10-second exposure.

**8. Generation flaws: garbled text, anatomy, physics**
- What it looks like: melted lettering on signage, wrong finger counts, impossible reflections/object pairings.
- Measurable signal: only 8% of photorealistic AI images showed detectable production flaws; of flawed ones, 84% anatomical implausibility, 24–63% functional distortion, 13–27% physics violations (#10).
- Sources: #10, #8 (NN/g recommends inspecting "anatomy, text, hands, reflections").
- Quote: photorealistic AIGIs show "high surrealism and professional aesthetic styling, lacking discernible watermarks" (#10).
- Counter-evidence: the 8% figure itself — obvious flaws are now the exception, so flaw-spotting is a weak detector.

**9. Gradient-orb AI logos and app icons**
- What it looks like: circular/radial mark, soft organic curves, central aperture, rainbow or violet gradient — the "AI company hexagon-flower/orb."
- Measurable signal: radial symmetry + gradient fill + circular silhouette; #12 surveys ~8–10 major AI-company logos converging on this scheme (OpenAI, DeepMind, Claude et al.; DeepSeek/Midjourney as outliers).
- Sources: #12.
- Quote: "there's tremendous pressure to look legitimate by conforming to established visual language" (#12).
- Counter-evidence: #12 concedes circles carry real meaning ("wholeness, completion, infinity") and convergence partly reflects sound symbolism, not only laziness.

### Illustration

**10. Corporate Memphis / Alegria flat people**
- What it looks like: flat cartoon humans with elongated limbs, tiny heads, solid bright fills (purples/blues), abstract joyful poses; sometimes isometric.
- Measurable signal: no numeric metric in sources; ubiquity documented qualitatively (Facebook's Alegria 2017 → industry-wide).
- Sources: #11, #6.
- Quote: critics called it lazy, citing "simple shapes [and] untextured colours" (#11); it makes startups "look friendly, approachable, and concerned with human-level interaction" (Claire L. Evans, via #11).
- Counter-evidence: #11 records defenders — scholars granting it "art-historical legitimacy" (Memphis Group lineage) and illustrators defending its craft; criticism partly reflects industry anxiety, not aesthetics.

**11. Interchangeable open-source illustration packs (unDraw et al.) and AI amplification**
- What it looks like: the same violet-accented unDraw-style SVG scenes across unrelated startups; AI tools regurgitate the style because it saturates training data.
- Measurable signal: none found; unDraw's own single-accent-colour parameterisation (site default is violet) is itself the mechanism.
- Sources: #6 ("AI-generated illustrations" as placeholder tell), #11 (style economics: cheap, scalable, low-skill), #20 (homogenisation framing).
- Quote: style choices let companies appear as "established tech companies" at low cost (#11, paraphrase of documented rationale).
- Counter-evidence: free illustration democratised decent visuals for teams with zero budget (implicit in #11's cost rationale).
- Gap: no opened source specifically audits unDraw ubiquity — noted in Gaps.

**12. Glossy 3D blob/clay renders**
- What it looks like: soft-shaded 3D blobs, clay-like mascots, glass spheres floating in heroes.
- Measurable signal: none found in opened sources.
- Sources: only obliquely via #5 (glassmorphism-as-decoration) and #12 (orb aesthetics). Weakly sourced — see Gaps.

### Iconography

**13. Sparkle ✨ as universal AI marker**
- What it looks like: four-point sparkle glyph (usually violet/gradient) on every AI feature, button, and menu item.
- Measurable signal: NN/g quant study n=107: 0 participants attributed "artificial intelligence" to the sparkles icon; 11.22% read it as "important/special"; 16.82% each read "favourite/save" or "visual effects"; 73% read plain stars as favouriting (#13). Google: ~100 Google system icons incorporated the sparkle by 2024; studies n=2000 across 8 countries (#14).
- Sources: #13, #14.
- Quote: "No one attributed the concept of 'artificial intelligence' to the icon" (#13).
- Counter-evidence: #14 directly conflicts — inside Google product contexts users did recognise sparkle=AI, one sparkle sufficed, and combined icons (mic+sparkle) outperformed plain ones. Reconciliation: recognition is context- and ecosystem-dependent; standalone ambiguity remains (both agree labels help).

**14. Emoji as UI icons**
- What it looks like: raw emoji (🚀 💡 ⚡ ✨) standing in for designed icons in feature cards and nav.
- Measurable signal: count of emoji codepoints inside heading/button/list elements.
- Sources: #13 (sparkles emoji origin of the icon), #5 (icon-tile feature-card template it typically fills). No opened source condemns emoji-as-icon in general — see Gaps.

**15. Default icon sets, uniform icon tiles, inconsistent stroke weight**
- What it looks like: lucide/heroicons defaults inside small rounded-square tinted containers above every card heading; mixed filled/outline weights when sets are mixed.
- Measurable signal: "icon container above a heading" repetition count per page (#5); same icon-set fingerprint (24px grid, 1.5–2px stroke) across all AI-tool output.
- Sources: #5, #1 ("three-column feature grids with icons" as the median layout).
- Quote: "A small rounded-square icon container above a heading is the universal AI feature-card template" (#5).
- Counter-evidence: consistent open-source icon sets are an accessibility/coherence win; the tell is the container-above-heading template, not the sets.

### Motion

**16. Fade-up-on-scroll on every element**
- What it looks like: each section/heading/card translates up and fades in as it enters viewport, sitewide.
- Measurable signal: % of top-level elements wired to IntersectionObserver/AOS-style reveal; NN/g flags any scroll-triggered animation on primary text content; repetition on every scroll pass (vs first-view-only) (#19).
- Sources: #19, #4 ("uniform fade-ins without character or purpose"), #6 ("generic fade-in animations on every element").
- Quote: "I don't like how everything comes together when I'm scrolling down" (study participant, #19); "Task-focused users don't want to be wowed by a website — they want to get answers" (#19).
- Counter-evidence: #19 itself allows scroll animation for leisure/browsing sites, on secondary content, first scroll only — a scoped exception, not a blanket ban.

**17. hover:scale cards and image zoom-on-hover**
- What it looks like: whole cards/images grow (`hover:scale-105`) or rotate on pointer-over.
- Measurable signal: `transform: scale(...)` in hover rules; Rauno's calibration — scale proportional to element size (buttons ~0.96, never 0.8) (#16).
- Sources: #5, #16, #15.
- Quote: "Scaling or rotating an image on hover is a recurring generated-UI signature" (#5).
- Counter-evidence: #15/#16 endorse subtle press/hover scale on low-frequency marketing surfaces; the tell is magnitude + ubiquity.

**18. Floating/bouncing decorative elements & bounce easing**
- What it looks like: infinitely looping float/bob keyframes on hero blobs and badges; elastic/bounce easing on UI transitions; pulsing "live" status dots on static data.
- Measurable signal: infinite-iteration keyframe animations running while offscreen (#16 says pause them); `cubic-bezier` overshoot/elastic curves (#5); pulse animation on non-updating data (#5).
- Sources: #5, #16, #17.
- Quote: "Bounce and elastic easing on interface elements feels dated and tacky" (#5); "Decorative pulse makes static status look live. Animate only when data is changing" (#5).

**19. Gradient animations, typing effects, particle backgrounds, marquee logo rows**
- What it looks like: hue-shifting hero gradients, typewriter headlines, canvas particle fields, auto-scrolling logo strips.
- Measurable signal: auto-scrolling marquee present (#5); animated background layers competing with content; particle canvas elements. Typing effects and particles specifically were NOT named by any opened source — inferred only from adjacent guidance; see Gaps.
- Sources: #5 (marquee), #3 (animated gradients as Linear-style core), #17 (gratuitous-motion principle covers all four).
- Quote: "Continuous auto-scroll demands attention and hides content" (#5); "Don't add motion for the sake of adding motion" (#17).

**20. What the motion authorities converge on (intentional vs decorative)**
- The rule set, with numbers: interaction animations ≤ 200ms (Rauno, #16) / < 300ms (Kowalski, #15); Material envelope 150–200ms desktop, 300ms mobile standard, 400ms hard ceiling, asymmetric easing, linear = mechanical (#18); frequency governs appropriateness — never animate keyboard-initiated or high-frequency actions (#15, #16); motion must communicate state change, direct attention, or carry character (#4's formulation), otherwise cut it (#15, #17); always honour `prefers-reduced-motion` (#16, #17).
- Quotes: "sometimes the best animation is no animation" (#15); "Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable" (#17); "Animation duration should not be more than 200ms for interactions to feel immediate" (#16).

### Layout rhythm

**21. Uniform radius/padding — "everything at the same volume"**
- What it looks like: identical 16px border-radius and 24px padding on every card, button, input; monotone spacing scale with no rhythm.
- Measurable signal: variance of border-radius and padding values across components ≈ 0; single spacing token reused everywhere (#4, #5, #6).
- Sources: #4, #5, #6.
- Quote: "Real hierarchy comes from intentional variation... when everything is shouting at the same volume" (#4); "Same spacing value everywhere. No rhythm, no variation" (#5).
- Counter-evidence: design systems legitimately standardise radii/spacing; the tell is absence of any deliberate deviation for hierarchy.

**22. Everything is a card / identical card grids**
- What it looks like: icon + heading + two lines of text in same-sized cards, repeated in 3-column grids for features, testimonials, pricing, blog; sometimes cards nested inside cards.
- Measurable signal: count of visually identical card components per page; nesting depth of card-styled containers >1 (#5).
- Sources: #5, #1, #6.
- Quote: "Same-sized cards with icon + heading + text repeated endlessly. The default AI homepage layout" (#5).

**23. Centred hero, oversized headline, eyebrow pill, symmetric everything**
- What it looks like: centre-aligned full-viewport hero; tiny uppercase letter-spaced pill label; display-size full-sentence headline; two centred CTAs; then symmetric alternating sections.
- Measurable signal: hero headline consumes most of viewport height (#5); presence of eyebrow-pill pattern; text-align:center on all top-level sections.
- Sources: #5, #6 ("Oversized hero sections with vague headlines like 'Build the future'"), #1 (predictable CTA placement).
- Quote: "Tiny uppercase letter-spaced label immediately above oversized headline is the default AI SaaS hero" (#5).

**24. Hero metric row / stat tiles**
- What it looks like: big number, small label, three supporting stats with gradient accent, regardless of whether numbers are real.
- Measurable signal: 3–4 stat tiles in hero or first section.
- Sources: #5.
- Quote: "Big number, small label, three supporting stats, gradient accent. Used everywhere, trusted nowhere" (#5).

**25. Bento grids**
- What it looks like: Apple-style mixed-size rounded tiles packing features into one mosaic; now a default "premium" section in generated landing pages.
- Measurable signal: none found in opened sources; search surfaced only trend-promotion pieces (Medium bento-box, Galaxy UX), no rigorous critique — see Gaps.
- Sources: (search-level only; no opened source. Closest opened evidence: #5's identical-card-grid and nested-card tells cover degenerate bentos.)
- Counter-evidence: trend literature argues bento grids genuinely aid scanability/modularity.

**26. Homogenisation itself as the meta-tell (platform-level)**
- What it looks like: outputs of ChatGPT Canvas, Gemini Canvas, Claude Artifacts, Lovable, v0 and Replit converging on one Western-minimalist template regardless of brief or culture.
- Measurable signal: #20 is qualitative (63-source review + 6 platform walkthroughs), no similarity metric; documents a case where a model imposed a minimalist layout on a Japanese retail site and "justified a minimalist layout as a cultural preference," overriding local high-density norms.
- Sources: #20, #1, #2.
- Quote: "The AI trained on AI output. The distribution shifted further toward indigo" (#1, feedback-loop mechanism).
- Counter-evidence: none of the opened sources quantifies convergence with a hard similarity score — the strongest claims remain qualitative.

## Quantitative evidence found

- Tailwind indigo-500 = #6366F1 (hue ≈ 239°); named gradient `from-indigo-500 to-purple-600` as the canonical AI gradient (#1). Hue values computed from the hex codes the source names.
- AI-image colour statistics: 93.27% average cross-generator detection accuracy from colour features alone; 99.4% accuracy from saturation-channel fingerprints (SD vs COCO); LPIPS ~4x less sensitive to chrominance than luminance, explaining systematic colour drift (#9).
- Photorealistic AI-image content analysis: ~68% contain humans; 73% of those with identifiable faces; >10% depict celebrities/politicians; 92%+ high image quality; 93–98% vividly coloured; 58–61% contain surreal combinations; only 8% show detectable flaws — of flawed images, 84% anatomical implausibility, 24–63% functional distortion, 13–27% physics violations (#10).
- NN/g AI-vs-stock imagery study: n=77, 10-second exposures, 6 page variants; AI images +0.2–0.4 points on 7-point trust/professionalism/authenticity scales; authenticity difference statistically significant (favouring AI) (#8).
- Sparkle icon: n=107; 0% attributed AI; 11.22% "important/special"; 16.82% "favourite/save"; 16.82% "visual effects"; 73% associate plain stars with favouriting (#13). Google: n=2000 across 8 countries; ~100 Google system icons with sparkle by 2024 (#14).
- Motion numbers: ≤200ms interaction animations (#16); <300ms UI animations (#15); Material: 300ms mobile standard, 225ms enter / 195ms exit, 400ms max, 150–200ms desktop, tablet +30%, wearables −30% (#18).
- WCAG 1.4.3 minimum contrast (4.5:1 body text) as the low-contrast threshold reference (#7).
- 925 Studios (agency-cited, weaker provenance): 38% of visitors leave over poor design/content; 40–62% of AI-generated code contains security/design flaws; 1.7x more issues in AI codebases (#6). Treat as directional, not rigorous.
- Homogenisation study scope: 63 sources reviewed, 6 vibe-coding platforms walked through (#20) — but no numeric similarity metric.

## Recommended alternatives from the sources

- **Colour**: build a semantic colour system — name tokens by function (primary-action, warning, success), not by gradient position; supply explicit hex codes or a reference design system in prompts instead of accepting model defaults (#1, #4). Keep body text ≥ 4.5:1; fix density/size/position rather than dropping contrast (#7).
- **Imagery**: evaluate AI images individually against normal design criteria; audit representation; inspect anatomy, text, hands, reflections; know the tool's training-data policy (#8). Prefer real product screenshots and real team photos over any stock, AI or not (#6).
- **Illustration/branding**: differentiate rather than conform — the orb-logo convergence is a legitimacy reflex, and outliers (DeepSeek, Midjourney) show divergence is viable (#12).
- **Iconography**: use sparkles only for established conventions (image editing), genuinely special items, or AI features as a transitional marker — and always pair with a text label/tooltip (#13); combined icons (function-icon + sparkle) outperform standalone marks (#14).
- **Motion**: animate only to communicate state change, direct attention, or carry character (#4); cut animation on frequent and keyboard-initiated actions (#15, #16); keep interactions ≤200–300ms with asymmetric ease-out (#15, #16, #18); scroll-reveals only on leisure content, secondary elements, first scroll (#19); honour reduced-motion and pause offscreen loops (#16, #17).
- **Layout/typography**: pick a display face with personality over Inter-by-default (Linear/Stripe cited as authored counterexamples) (#4, #6); create hierarchy through intentional variation in spacing, radius, and scale (#4, #5); design empty/loading/error states — "these edge cases are where trust is built or broken" (#4); use progressive disclosure instead of showing everything at once (#4).
- **Process-level**: "productive friction" — reflective prompting, mood-board negotiation before generation, design-system ingestion ("contextual anchoring"), and provenance-tagged style adapters to stop training-data collapse (#20); specify constraints explicitly in prompts (fonts, hexes, layout references) (#1).

## Gaps

1. **No hard quantitative measurement of UI homogenisation.** The best available study (#20) is qualitative; no opened source computes hue-histogram shares, layout-similarity scores, or font-frequency counts across a corpus of AI-generated sites. The proposed metrics above (hue share in 240–290°, gradient-declaration counts, radius/padding variance, % scroll-revealed elements) are operationalisations suggested by the sources' claims, not published measurements.
2. **Bento grids**: only trend-promotion literature surfaced; no rigorous critique or usage statistics were opened. The "bento = AI tell" claim is currently community folklore.
3. **3D clay/blob renders and gradient-orb app icons** (as distinct from company logos): no substantive dedicated source found; covered only obliquely (#5, #12).
4. **unDraw specifically**: its ubiquity is asserted everywhere but audited nowhere; no source with counts of unDraw deployments was found.
5. **Typing effects and particle backgrounds**: named in the task but not by any opened source; they fall under gratuitous-motion principles (#17) rather than documented AI-specific tells.
6. **Emoji-as-icons**: no authority piece condemning the practice was found; NN/g and Google cover only the sparkle case.
7. **Smashing Magazine**: domain-restricted search returned AI-interface pattern articles (e.g. "Design Patterns For AI Interfaces", "Digital Design In The AI Era") but none squarely on visual tells of AI-generated design; none opened as a core source.
8. **Conflicting evidence on detectability**: #8 and #10 suggest the imagery tells are weakening (8% flaw rate; AI images out-scoring stock on trust), while #9 shows machine-detectable colour statistics persist. Human-perceptible and machine-measurable tells are diverging — worth flagging in any guidance built on this file.
