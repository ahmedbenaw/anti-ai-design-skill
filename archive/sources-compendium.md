# Sources compendium

Every source behind this skill, in one file, tagged for use.

## How to use this

1. Find a claim in `tells-register.md`, then look up its source IDs here.
2. IDs are stable. P practitioners, A academic, C community, K code samples, M mobile and copy. X accessibility, R prior art, V visual science, L library docs.
3. Tags tell you what to do with a source: `[AVOID: x]`, `[ADOPT: x]`, `[EVIDENCE-ONLY]`, `[CONTESTED]`, `[STALE-RISK]`.
4. "Feeds" names the register rule IDs or skill files the source supports.
5. Read the three synthesis sections at the end before writing any rule.
6. Research dates: 01 to 08 were gathered 2026-08-28. Library docs were read 2026-09-04.

## Category index

| Category | ID range | Count | What it covers |
|---|---|---|---|
| Practitioners | P1-P24 | 24 | Designers, agencies and tool makers naming the visual tells |
| Academic | A1-A24 | 24 | Papers and benchmarks on convergence, code stylometry, image forensics |
| Community and wiki | C1-C26 | 26 | Hacker News threads, Wikipedia, Indie Hackers, GitHub tell catalogs |
| Code samples | K1-K15 | 15 | 12 cloned AI-generated repos with measured counts, plus 3 cross-check articles |
| Mobile and copy | M1-M20 | 20 | Mobile app tells, and UI plus marketing copy tells |
| Accessibility | X1-X29 | 29 | WCAG 2.2, COGA, BDA, plain language, docs for non-technical readers |
| Prior art | R1-R20 | 20 | Existing linters, skills, ban lists, vendor prompting guides |
| Visual science | V1-V20 | 20 | Colour, imagery, illustration, iconography, motion, layout rhythm |
| Library docs | L1-L76 | 76 | Docs, licences and policies for the nine installed libraries |

---

# P. Practitioners

### P1 — AI Design Slop: 16 Patterns That Out Your App as Vibe-Coded
- **Source:** Developers Digest, dev publication, Apr 2026 (updated Jun 2026). https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it
- **Context:**
  - Ran an automated Playwright scan of 1,590 Show HN pages. 22% carried four or more slop patterns.
  - Measured prevalence: permanent dark theme 34%, gradients 27%, icon-card grids 22%. False-positive rate around 5% to 10%.
  - Names Inter as "the Helvetica of the LLM era", plus Space Grotesk, Instrument Serif and Geist as the recurring font set.
  - Names "VibeCode purple", a lavender accent near #B794E2, and badge-above-H1 as near-universal.
- **Tags:** `[AVOID: permanent dark theme with glow]` `[AVOID: unchosen Inter]` `[AVOID: badge above hero H1]` `[EVIDENCE-ONLY]`
- **Feeds:** CO1, CO2, CO3, TY1, TY2, LA4, LA13, IC1; the only prevalence numbers in the whole register

### P2 — Why Every AI-Generated Landing Page Looks the Same (and How to Fix It)
- **Source:** Jeong Sang-rok, front-end developer, Mar 2026. https://dev.to/_46ea277e677b888e0cd13/why-every-ai-generated-landing-page-looks-the-same-and-how-to-fix-it-1kmo
- **Context:**
  - Names the cause "distributional convergence": the model samples the statistical centre of design.
  - Lists Inter, uniform mid radius and the three-card row as the visible result.
  - Names Claude Code, Cursor and Windsurf as producing the same face.
- **Tags:** `[AVOID: three-card feature row]` `[AVOID: uniform middle radius]`
- **Feeds:** LA2, LA10, TY1, JD4

### P3 — AI Slop Fonts and Gradients: The Tells That Give Away AI Design
- **Source:** Yusuf, lead designer at 925 Studios, agency blog, Jun 2026. https://www.925studios.co/blog/ai-slop-design-tells
- **Context:**
  - Four core tells: Inter, the indigo to purple gradient, three rounded cards, and "weightless confidence" copy.
  - Argues an unchosen Inter signals nobody made a typography decision. Inter itself is not the problem.
  - Recommends breaking the three-card reflex with asymmetry as the highest-value single fix.
- **Tags:** `[AVOID: unchosen default sans]` `[AVOID: triptych card row]` `[ADOPT: asymmetric layout]` `[CONTESTED]`
- **Feeds:** TY1, LA2, CP1, CP6

### P4 — AI design isn't ugly. It's fluent, and that's the problem
- **Source:** Takuma Kakehi, designer, UX Collective, Jun 2026. https://uxdesign.cc/ai-design-isnt-ugly-it-s-fluent-and-that-s-the-problem-131b2f4eb78c
- **Context:**
  - Core claim: you cannot spot AI design by hunting for mistakes. The output is polished.
  - Names the shared face: centred hero, confident headline, two buttons, across Lovable, v0, Claude and Bolt.
  - Names spacing that feels "exhaled rather than drawn", meaning even but undesigned.
  - Warns that each AI iteration optimises from its own previous output, so distinctiveness falls over rounds.
- **Tags:** `[AVOID: centred hero with twin buttons]` `[AVOID: iterating with AI on the same file]` `[EVIDENCE-ONLY]`
- **Feeds:** LA5, LA10, JD3, JD4; Part 5 (polish is not a tell)

### P5 — The shadcn trap: why shadcn looks generic and how to fix it
- **Source:** designdotmd, design-tool maker blog, Apr 2026. https://freedesignmd.com/blog/shadcn-looks-generic
- **Context:**
  - The generic look is unchanged shadcn tokens: slate or zinc neutrals, 0.5rem radius, Inter, muted indigo.
  - Agents see shadcn in a repo and reach for shadcn defaults on every new component.
  - Fix offered: add one token shadcn does not ship by default, so the project has a fingerprint.
  - Radius guidance is directional. Pick 0px, 1rem or a pill, but pick.
- **Tags:** `[AVOID: unchanged shadcn tokens]` `[ADOPT: one extra custom token]` `[ADOPT: deliberate radius choice]`
- **Feeds:** LA13, LA10, CO1, TY1

### P6 — Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500)
- **Source:** Alan West, developer writer, Mar 2026. https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p
- **Context:**
  - Traces the purple default to Tailwind's `bg-indigo-500` placeholder in docs and tutorials.
  - Describes a feedback loop: AI output re-enters training data, so the distribution shifts further toward indigo.
  - Names gradient text, three-column icon grids and Inter as the companion tells.
- **Tags:** `[AVOID: indigo-500 as default accent]` `[AVOID: gradient-clipped headline]` `[STALE-RISK]`
- **Feeds:** CO1, CO2, LA2; note K measured 0 of 12 modern repos using raw indigo

### P7 — 7 Signs a UI Has Been Vibe Coded
- **Source:** Jeff Humble, designer and educator, The Fountain Institute, Apr 2025. https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui
- **Context:**
  - Seven signs: neon palettes, glow dark mode, emoji as UI icons, purple gradients, card-itis, side-tab stripes, meaningless status dots.
  - Palette rule: one dominant colour, one accent, one neutral. Everything else is noise.
  - Says the model applies container logic with no cost function for visual weight, which is why cards nest.
  - Concedes humans did purple first: Notion, Linear and Vercel used these gradients.
- **Tags:** `[AVOID: neon multi-hue palette]` `[AVOID: cards inside cards]` `[AVOID: meaningless status dots]` `[ADOPT: one dominant, one accent, one neutral]` `[CONTESTED]`
- **Feeds:** CO7, LA7, LA8, MO3, IC2

### P8 — Where does that purple gradient come from?
- **Source:** Jack Pearce, developer blogger, Feb 2026. https://www.jackpearce.co.uk/notes/purple-gradient-ai-aesthetics/
- **Context:**
  - Purple gradients are 2015 to 2020 web aesthetics baked into training data. Stripe, Instagram and Twitch used them.
  - Notes Anthropic's own frontend-design skill warns against purple gradients on white backgrounds.
- **Tags:** `[CONTESTED]` `[STALE-RISK]` `[AVOID: reflexive purple gradient]`
- **Feeds:** CO1, CO6; Part 5 (purple alone is not proof)

### P9 — How We Finally Killed the Purple Gradient in AI Frontends
- **Source:** YouWare team, AI app builder, Nov 2025. https://www.youware.com/blog/how-we-escaped-the-purple-prison-of-ai-frontends
- **Context:**
  - A tool maker admits Claude favours purple gradients regardless of prompt wording.
  - Their fix was curated design-guideline system prompts, not per-request instructions.
  - Quotes the origin story: one default `bg-indigo-500` defined the aesthetic of a generation of AI.
- **Tags:** `[ADOPT: persistent design-guideline system prompt]` `[AVOID: relying on one-off prompt bans]`
- **Feeds:** CO1, JD4; templates/ direction file

### P10 — Why Your AI Keeps Building the Same Purple Gradient Website
- **Source:** prg.sh, developer blogger, Oct 2025. https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website
- **Context:**
  - "LLMs aren't designers, they're statistical pattern matchers." You get the median of every scraped Tailwind tutorial.
  - Ran side-by-side prompt experiments across Claude, GPT-5, Gemini and v0.
  - Fixes tested: constrain each dimension separately, name a concrete aesthetic, give explicit negative constraints, feed descriptions of three to five admired designs.
  - Reports Claude responds best to strong constraints.
- **Tags:** `[ADOPT: per-dimension constraints]` `[ADOPT: reference-first prompting]` `[ADOPT: explicit negative constraints]`
- **Feeds:** JD4, JD5; templates/ direction file; R18 is the same article in the prior-art survey

### P11 — How to tell if a website is AI-generated: 10 signs
- **Source:** Mukund Parekh, Slopdar, detector-tool maker, 2026. https://slopdar.com/guide/how-to-tell-if-a-website-is-ai-generated
- **Context:**
  - Ten weighted signs, including builder fingerprints, default shadcn and lucide, and copy tics.
  - States plainly that every sign also appears on hand-built sites, so detection needs weighted aggregates.
  - Notes refined AI-built sites score low, so a low score is not proof of human authorship.
  - Names leftover residue: "As an AI language model" fragments, stock favicon, missing OG image, title tag "My App".
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]` `[ADOPT: weighted aggregate scoring]` `[AVOID: shipped template residue]`
- **Feeds:** PR6, PR7, LA13, IC5; scoring model in scripts/ai_tell_scan.py

### P12 — AI Design Slop: Why Every AI-Built Interface Looks the Same
- **Source:** Mohit Phogat, designer and developer, Medium, Aug 2026. https://mohitphogat.medium.com/ai-design-slop-why-every-ai-built-interface-looks-the-same-and-how-to-fix-it-bf874e0b470c
- **Context:**
  - Combines visual tells with code-level statistics: 2.74 times more vulnerabilities, systematic accessibility failures.
  - Prescribes a DESIGN.md written before any prompting. "The model does what it's told. You have to do the telling first."
  - Caps the palette at four values: background, surface, primary, text.
- **Tags:** `[ADOPT: DESIGN.md before prompting]` `[ADOPT: four-value palette cap]` `[EVIDENCE-ONLY]`
- **Feeds:** templates/ direction file; Part 6 accessibility gates

### P13 — Why Do Most AI-Generated Websites Look the Same?
- **Source:** Benedykt Michalski, Shuffle, template-tool maker, Jan 2026. https://shuffle.dev/blog/2026/01/why-do-most-ai-generated-websites-look-the-same/
- **Context:**
  - "AI doesn't design, it predicts patterns." Vague prompts produce the hero, three cards, testimonials, pricing skeleton.
  - The result is fast but generic, and no section reflects the actual product.
- **Tags:** `[AVOID: full SaaS skeleton in fixed order]`
- **Feeds:** LA1, LA2

### P14 — Design Observation: Why Do AI-Generated Websites Always Favour Blue-Purple Gradients?
- **Source:** Kai Ni, designer, Medium, Sep 2025. https://medium.com/@kai.ni/design-observation-why-do-ai-generated-websites-always-favour-blue-purple-gradients-ea91bf038d4c
- **Context:**
  - Argues indigo-500 overrepresentation taught models that blue-purple is "best".
  - Also names 8px and 16px radius dominance, and outline-icon dominance, in AI mobile UIs.
  - This is the only practitioner source touching mobile radius specifically.
- **Tags:** `[AVOID: uniform 8px or 16px radius]` `[AVOID: outline-icon monoculture]` `[STALE-RISK]`
- **Feeds:** CO1, LA10, IC1

### P15 — AI Design Slop: Why AI-Generated UI Looks Generic, and the Fix
- **Source:** Eduardo Calvo, SmoothUI, component-library maker, Jun 2026. https://smoothui.dev/blog/ai-design-slop
- **Context:**
  - Names purple-cyan gradient, glass plus neon glow, six identical cards, and bounce hovers.
  - Prescribes a closed-loop critique cycle: generate, critique, fix, re-evaluate against a checklist.
- **Tags:** `[AVOID: six identical cards]` `[AVOID: bounce on hover]` `[ADOPT: closed-loop critique]`
- **Feeds:** LA2, MO2, MO6, JD2

### P16 — Slop (pattern catalog)
- **Source:** Impeccable, impeccable.style, design-tool and skill maker, 2026. https://impeccable.style/slop/
- **Context:**
  - The largest single catalog found: around 50 named patterns across visual, type, colour, layout, motion, copy and imagery.
  - Splits findings into "AI slop" and "quality issue". Low contrast and cramped padding are filed as quality issues, not AI tells.
  - Source of many exact phrasings in the register: gradient text is decorative, cream is the reflexive tasteful surface, decorative pulse makes static status look live.
  - Names bounce and elastic easing on interface elements as dated.
- **Tags:** `[AVOID: gradient text]` `[AVOID: reflexive cream ground]` `[AVOID: decorative pulse]` `[AVOID: bounce easing on UI]` `[CONTESTED]`
- **Feeds:** CO2, CO6, CO8, LA3, LA7, LA9, MO3, MO6, TY3, TY5

### P17 — Why does AI keep making everything blue-purple?
- **Source:** Vivek Tiwari, developer writer, Substack, Oct 2025. https://chaiovercode.substack.com/p/why-does-ai-make-everything-blue
- **Context:**
  - The indigo default propagated through tutorials into training data.
  - "AI learned frequency, not design principles."
- **Tags:** `[AVOID: frequency-driven colour defaults]` `[STALE-RISK]`
- **Feeds:** CO1

### P18 — How to Tell If a Website Was Built With AI: 7 Dead Giveaways
- **Source:** JAY, Anonymiz, developer and security blogger, May 2026. https://anonymiz.com/blog/how-to-tell-if-a-website-was-built-with-ai-7-dead-giveaways
- **Context:**
  - Purely code-forensic tells: `<meta name="generator">`, CDN domains, bundle names, HTML comments, hosting DNS.
  - Names `<!-- Generated with Bolt -->` and Lovable component attribution comments.
  - Concedes Framer, Webflow and Wix fingerprints prove a builder was used, not that AI generated the design.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** PR6; Part 5 (builder fingerprints are not AI proof)

### P19 — How to Avoid Building Apps That Look Vibe Coded
- **Source:** VibeMole, detector-tool maker, Jul 2026. https://vibemole.com/resources/avoid-vibecoded-app-design
- **Context:**
  - Fifteen patterns, including pill-badge spam, lucide icon grids, fake product evidence and dark mode as a crutch.
  - "If you are early, say less and show more." Use real product screenshots instead of invented stats.
  - Copy test: read your H2s aloud. If they could sit on any SaaS product, rewrite them.
  - Says side-stripe borders are legitimate when they carry status or severity meaning.
- **Tags:** `[AVOID: badge spam]` `[AVOID: invented stats]` `[ADOPT: real product screenshots]` `[ADOPT: read headings aloud test]` `[CONTESTED]`
- **Feeds:** LA4, LA6, LA8, CP3, CP6, JD2

### P20 — UX and the aesthetics of AI
- **Source:** Danilo Amorim, designer, Medium Bootcamp, Oct 2025. https://medium.com/design-bootcamp/ux-and-the-aesthetics-of-ai-101b48747f91
- **Context:**
  - Argues homogenisation happens at the interaction level, not only the visual one.
  - Every AI product converges on a chat box, white background and neutral type.
- **Tags:** `[AVOID: chat box as the default interaction]` `[EVIDENCE-ONLY]`
- **Feeds:** JD1

### P21 — Avoid "landing page words"
- **Source:** Sathya, Microcopy Examples, UX writer, Substack, Dec 2024. https://microcopyexamples.substack.com/p/avoid-landing-page-words
- **Context:**
  - `Unlock`, `unleash`, `empower`, `supercharge` and `game-changer` are empty buzzwords.
  - Published before the AI framing existed, which is why it is the cleanest evidence that these words are a human habit.
  - Replacement rule: name the concrete task-level benefit instead.
- **Tags:** `[AVOID: transformation-verb headlines]` `[CONTESTED]` `[ADOPT: concrete task-level benefit]`
- **Feeds:** CP1; Part 5 (buzzwords are weak AI evidence)

### P22 — Interrogating Design Homogenization in Web Vibe Coding
- **Source:** Shin et al., HCI academics, arXiv, 2026. https://arxiv.org/html/2603.13036v1
- **Context:**
  - Qualitative study of six tools: ChatGPT Canvas, Gemini Canvas, Claude Artifacts, Lovable, v0 and Replit.
  - Notes homogenisation predates AI through Bootstrap and Tailwind.
  - Also catalogued as A2 and V20. Cited here because practitioners use it as their counter-evidence.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 5; JD4

### P23 — AI in UI Design: Avoiding AI Slop and Shipping Faster
- **Source:** Elena Kondratenko, Managed Code, agency designer, Mar 2026. https://managed-code.com/blog-post/ai-slop-in-design
- **Context:**
  - Agency-level tells: borrowed purple and blue glow accents, inconsistent shadow recipes per component, missing interaction states.
  - "Critical states such as focus, disabled, error, empty, or loading are absent or improvised late."
  - Fix: define three to five named elevation levels mapped to shared tokens.
- **Tags:** `[AVOID: per-component shadow recipes]` `[AVOID: missing interaction states]` `[ADOPT: named elevation scale]`
- **Feeds:** LA9, JD2; Part 6

### P24 — How to Make AI UI Look Less Generic: 5 Fixes
- **Source:** Jason Zhou, Superdesign, design-tool maker, Jun 2026. https://superdesign.dev/blog/how-to-make-ai-ui-look-less-generic
- **Context:**
  - "Generic is what one prompt does when it has to pick taste, explore, and write code all at once."
  - Prescribes planning taste separately from code, and exploring layouts with image models before a coding agent implements.
  - Recommends three to five Dribbble, Mobbin or Awwwards references with notes on why each works.
- **Tags:** `[ADOPT: separate taste planning from code]` `[ADOPT: named visual references]`
- **Feeds:** JD4, JD5; templates/ direction file

---

# A. Academic

### A1 — Design Theater: A Benchmark for Generative UI
- **Source:** arXiv preprint, 2026. https://arxiv.org/abs/2607.22928
- **Context:**
  - Five generative UI tools (ChatGPT, Claude, Firebase Studio, v0, Bolt) across 24 tasks, 120 interfaces.
  - Introduces the Design Homogeneity Index. Colour varied more than structure, so layout converges hardest.
  - Thinking Fidelity Score: over 25% of stated design rationales were never implemented, 34% for functional requirements.
  - Principle Adherence Score mean 0.54. Four of five tools implemented 6% or less of functional principles.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: stated rationale with no implementation]`
- **Feeds:** LA1, JD2, JD4; Part 0 finding 4 (structure converges harder than colour)

### A2 — Interrogating Design Homogenization in Web Vibe Coding
- **Source:** Microsoft Research, arXiv, 2026. https://arxiv.org/abs/2603.13036
- **Context:**
  - Sociotechnical analysis of 63 sources plus six platform walkthroughs. Builds a taxonomy of seven harms.
  - Documents a case where a model imposed a minimalist layout on a Japanese retail brief and justified it as cultural preference.
  - The paper states plainly that empirical measurement of the named traits is still missing.
  - Notes Bootstrap and Tailwind already produced convergence before AI.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** Part 5; JD1, JD4

### A3 — Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Engineering
- **Source:** Si et al., SALT-NLP, arXiv and NAACL 2025, 2024. https://arxiv.org/abs/2403.03163
- **Context:**
  - 484 curated real webpages as a test set, with automatic visual and element-matching metrics validated against humans.
  - Models mostly fail at recalling visual elements and at generating correct layouts.
  - The 484-page set is usable as a human-design baseline corpus.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: Design2Code as a human baseline corpus]`
- **Feeds:** A-F8 element-simplification finding; future scanner calibration

### A4 — Unlocking the conversion of Web Screenshots into HTML Code with the WebSight Dataset
- **Source:** Laurencon et al., Hugging Face, arXiv, 2024. https://arxiv.org/abs/2403.09029
- **Context:**
  - Two million synthetic HTML and screenshot pairs, generated by Mistral-7B plus DeepSeek-Coder-33B.
  - Every page is styled with Tailwind CSS and uses Unsplash keyword images.
  - The training corpus itself is a template of the AI look, which is the clearest mechanism evidence available.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: Tailwind default plus Unsplash placeholder as the finished look]`
- **Feeds:** CO1, IC5; Part 0 finding on training monoculture

### A5 — Sketch2Code: Evaluating Vision-Language Models for Interactive Web Design Prototyping
- **Source:** Li et al., arXiv, 2024. https://arxiv.org/abs/2410.16232
- **Context:**
  - Ten vision-language models struggle to turn low-fidelity sketches into prototypes.
  - Models cannot steadily improve fidelity across turns without human questioning.
  - UI and UX experts preferred multi-turn agents that ask questions.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: question-asking before generating]`
- **Feeds:** JD4; pre-generation interrogation step

### A6 — UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset
- **Source:** Duan et al., UIST 2024, arXiv, 2024. https://arxiv.org/abs/2407.08850
- **Context:**
  - 3,059 expert critiques with quality ratings for 983 mobile UIs, derived from RICO.
  - Few-shot prompting with this dataset improved LLM UI feedback by 55%.
- **Tags:** `[ADOPT: few-shot critique examples]` `[EVIDENCE-ONLY]`
- **Feeds:** closed-loop critique step; JD2

### A7 — UI-Bench: A Benchmark for Evaluating Design Capabilities of AI Text-to-App Tools
- **Source:** arXiv, 2025. https://arxiv.org/abs/2508.20410
- **Context:**
  - Ten text-to-app tools, 30 prompts, 300 sites, over 4,000 expert pairwise judgements.
  - Ranked with a TrueSkill-derived model and a public leaderboard at uibench.ai.
  - Ranks tools against each other. It does not test human versus AI discrimination.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** Part 5 (quality is not a discriminator)

### A8 — Artificial Hivemind: The Open-Ended Homogeneity of Language Models
- **Source:** arXiv, 2025. https://arxiv.org/abs/2510.22954
- **Context:**
  - Infinity-Chat: 26,000 open-ended queries with 31,250 human annotations.
  - Finds strong intra-model repetition and even stronger inter-model homogeneity.
  - Supports a regeneration test: re-prompt a model and compare the result with the suspect artefact.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: regeneration test]`
- **Feeds:** JD4; A-F12

### A9 — We're Different, We're the Same: Creative Homogeneity Across LLMs
- **Source:** arXiv, 2025. https://arxiv.org/abs/2501.19361
- **Context:**
  - On standardised creativity tests, LLM responses are far more similar to each other than human responses are.
  - The effect holds across vendors and survives controls for response structure.
  - Measured in text, not web UI, so it is supporting rather than direct evidence.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** JD4

### A10 — Understanding Design Fixation in Generative AI
- **Source:** arXiv, 2025. https://arxiv.org/abs/2502.05870
- **Context:**
  - 96 generative AI chair designs compared with 105 Red Dot award winners.
  - Midjourney outputs cluster more densely in CLIP embedding space, significant on Mann-Whitney U.
  - Novelty proportion P equals U over U plus S, and it is lower for AI output.
  - Shows generative AI itself exhibits design fixation, not only its users.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** JD4; embedding-dispersion check

### A11 — The Effects of Generative AI on Design Fixation and Divergent Thinking
- **Source:** Wadinambiarachchi et al., CHI 2024. https://arxiv.org/abs/2403.11164
- **Context:**
  - 60-participant experiment. Designers using an AI image generator fixated more.
  - They produced fewer ideas, less varied ideas and less original ideas than the baseline group.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: generating references before deciding a direction]`
- **Feeds:** JD4; templates/ direction file written first

### A12 — Homogenization Effects of Large Language Models on Human Creative Ideation
- **Source:** Anderson et al., ACM Creativity and Cognition 2024. https://arxiv.org/abs/2402.01536
- **Context:**
  - 36-participant study. Different users produced less semantically distinct ideas with ChatGPT.
  - The comparison tool was an alternative creativity-support system, so the effect is tool-specific.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** JD4

### A13 — The Hidden DNA of LLM-Generated JavaScript
- **Source:** arXiv, 2025. https://arxiv.org/abs/2510.10493
- **Context:**
  - 50,000 Node.js programs from 20 LLMs. CodeT5-JSA attributes the generating model at 95.8% over five models and 88.5% over twenty.
  - Robust to comment removal and variable mangling, so fingerprints live in dataflow and structure.
  - No equivalent detector exists for HTML or CSS.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** PR1 to PR7 rationale; scanner design limits

### A14 — Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry
- **Source:** Bulla et al., arXiv, 2024. https://arxiv.org/abs/2412.14611
- **Context:**
  - A single transformer classifier detects AI-written code across ten languages at 84.1% plus or minus 3.8%.
  - Releases H-AIRosettaMP with 121,247 labelled snippets.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** scanner design limits

### A15 — We Are Not Able to Identify AI-Generated Images
- **Source:** arXiv, 2025. https://arxiv.org/html/2512.22236v1
- **Context:**
  - 165 participants scored 53.76% telling MidJourney v7 portraits from real photos. Chance is about 50%.
  - Accuracy rose only with 15 seconds or more of deliberate viewing.
  - Visual checklists are unreliable at scrolling speed.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** IC6; Part 0 finding 5 (do not detect pixels)

### A16 — Methods and Trends in Detecting AI-Generated Images: A Comprehensive Review
- **Source:** arXiv, 2025. https://arxiv.org/abs/2502.15176
- **Context:**
  - Surveys detector families: spatial artefacts, frequency and spectral, model fingerprints, patch-based, CLIP multimodal.
  - Best cross-generator accuracy is 92% to 94%, with poor generalisation across families.
  - A detector tuned on this quarter's generators may fail on the next.
- **Tags:** `[EVIDENCE-ONLY]` `[STALE-RISK]`
- **Feeds:** IC6; Part 0 finding 5

### A17 — MLLM as a UI Judge
- **Source:** arXiv, 2025. https://arxiv.org/abs/2510.08783
- **Context:**
  - Multimodal LLM UI ratings correlate moderately with humans, MAE 0.51 to 0.54 on a seven-point scale.
  - They are near random for ease of use and for visually similar UI pairs, and they compress score variance.
  - So "an MLLM said it looks fine" is weak evidence.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]` `[AVOID: model self-assessment as the only gate]`
- **Feeds:** scanner design; closed-loop critique caveat

### A18 — Generative UI: LLMs are Effective UI Generators
- **Source:** Google, arXiv, 2026. https://arxiv.org/abs/2604.09577
- **Context:**
  - With the right tooling, LLM-generated UIs are strongly preferred over markdown output.
  - They matched expert designs in roughly half of the tested cases.
  - Introduces the PAGEN expert UI dataset.
  - This is the strongest counter to "AI design looks worse".
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 5 (quality is not a tell)

### A19 — DesignBench
- **Source:** arXiv, 2025. https://arxiv.org/abs/2506.06251
- **Context:**
  - Webpage-generation benchmark. Surfaced during the search and skimmed at result level only.
  - Listed for completeness and follow-up, not cited for any register claim.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** none yet; follow-up candidate

### A20 — Web2Code
- **Source:** arXiv, 2024. https://arxiv.org/abs/2406.20098
- **Context:**
  - Webpage understanding and code-generation benchmark. Skimmed at result level only.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** none yet; follow-up candidate

### A21 — Interaction2Code
- **Source:** arXiv, 2024. https://arxiv.org/abs/2411.03292
- **Context:**
  - Benchmarks generation of interactive behaviour, not just static layout. Skimmed at result level only.
  - Relevant to JD2 (polish without depth) if read in full later.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** JD2 follow-up

### A22 — FrontendBench
- **Source:** arXiv, 2025. https://arxiv.org/abs/2506.13832
- **Context:**
  - Front-end code-generation benchmark. Skimmed at result level only.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** none yet; follow-up candidate

### A23 — Visual Prompting with Iterative Refinement for Design Critique Generation
- **Source:** arXiv, 2024. https://arxiv.org/abs/2412.16829
- **Context:**
  - Method for generating design critiques with iterative visual prompting. Skimmed at result level only.
  - Adjacent to the closed-loop critique step this skill uses.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** closed-loop critique follow-up

### A24 — Detecting AI-generated Artwork
- **Source:** arXiv, 2025. https://arxiv.org/abs/2504.07078
- **Context:**
  - Detection of AI-generated artwork rather than photographs. Skimmed at result level only.
  - Closest published work to the untested flat-vector illustration case.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** IC7 follow-up

---

# C. Community and wiki

### C1 — "The AI Aesthetic" discussion (Jim Nielsen post)
- **Source:** Hacker News, forum thread, Aug 2026, 378 points and 176 comments. https://news.ycombinator.com/item?id=49117099
- **Context:**
  - The richest single thread found. Names beige plus orange serif, purple on dark, sparkle emoji and tiny thin icons.
  - Coins "everything comes in punchy threes" for the rule-of-three layout and copy reflex.
  - Strong pushback in the same thread: paxys argues it is mostly the 2010 to 2024 SaaS aesthetic.
  - Also names over-decorated busy designs that lack restraint.
- **Tags:** `[AVOID: rule-of-three reflex]` `[AVOID: sparkle emoji decoration]` `[CONTESTED]`
- **Feeds:** LA2, IC2, IC3, CP2, JD3; Part 5

### C2 — "Color palette gives away AI slop"
- **Source:** Hacker News, forum thread, 25 May 2026, 3 points. https://news.ycombinator.com/item?id=48269907
- **Context:**
  - Names the Claude Code default palette: cream canvas, cobalt or terracotta ink, persimmon and coral accents, monospace chrome, editorial layout.
  - Commenter functionmouse argues the lukewarm palette is deliberate genericism, attractive and fitting any idea.
- **Tags:** `[AVOID: reflexive cream and terracotta palette]` `[CONTESTED]` `[STALE-RISK]`
- **Feeds:** CO6, TY6

### C3 — "The LLM sameness in web design is good" subtree
- **Source:** Hacker News, comment subtree, 28 May 2026. https://news.ycombinator.com/item?id=48316416
- **Context:**
  - Sameness-as-signal debate between sofixa and tptacek.
  - tptacek: if the baseline is good, departing from it may reduce legibility rather than increase it.
  - refactor_master: Bootstrap-era sites still varied their colour schemes, so AI uniformity is tighter.
- **Tags:** `[CONTESTED]`
- **Feeds:** Part 5; "Contested and stale" section

### C4 — "Ask HN: How can you tell a site/app is vibe coded?"
- **Source:** Hacker News, forum thread, 13 Aug 2026, 9 points and 9 comments. https://news.ycombinator.com/item?id=49290499
- **Context:**
  - Concrete measurable tells from Wpnx330: zero-offset dark glows on text, 1px borders paired with 40px shadow blur.
  - Names Inter, Roboto and Geist as the default font set, and navy plus gradients plus emoji icons.
  - roundabout-host names over-explained microcopy that describes obvious UI elements.
  - ra0x3 notes B2B SaaS apps with oddly small panels and nav.
- **Tags:** `[AVOID: zero-offset glow]` `[AVOID: hairline border plus wide shadow]` `[AVOID: over-explained microcopy]`
- **Feeds:** CO4, LA9, TY1, CP5

### C5 — "Tell HN: I'm tired of formulaic LLM house style Show HN submissions"
- **Source:** Hacker News, zahlman, 3 Aug 2025, 62 points and 30 comments. https://news.ycombinator.com/item?id=44780249
- **Context:**
  - Names the LLM house style: "to fight back, I built X" narrative, buzzwords, emoji, bullet-threes.
  - Also names black backgrounds with green and orange gradients, and Vercel pages requiring JavaScript.
  - Counter-argument in the thread: the format follows YC's own template and predates LLMs.
- **Tags:** `[AVOID: LLM README house style]` `[CONTESTED]`
- **Feeds:** CP2, CP3; Part 5

### C6 — "The epitome of all LLM generated websites" (shadcn/ui thread)
- **Source:** Hacker News, comment subtree, 2 May 2026. https://news.ycombinator.com/item?id=47985052
- **Context:**
  - quadral: "when every LLM defaults to this UI, it makes mine look LLM generated."
  - bbg2401: a project using shadcn/ui is nearly immediately identifiable because most do not deviate from defaults.
  - This is the clearest evidence that legitimate human shadcn users get misread.
- **Tags:** `[AVOID: unchanged shadcn defaults]` `[CONTESTED]`
- **Feeds:** LA13, LA3; Part 5

### C7 — "Brainless: Shadcn components that look like Claude Code, Codex and Grok"
- **Source:** Hacker News, forum thread, 15 Jul 2026, 128 points. https://news.ycombinator.com/item?id=48926085
- **Context:**
  - The AI tools' own interfaces are now named, pixel-matchable, cloneable aesthetics.
  - Thread comment: "ShadCN and tailwind really encourage design drift."
- **Tags:** `[AVOID: cloning an AI tool's own interface]` `[STALE-RISK]`
- **Feeds:** CO6, TY6, LA13

### C8 — "Show HN: Claude skills to make anti-AI slop UI"
- **Source:** Hacker News, forum thread, 2 Jul 2026, 4 points. https://news.ycombinator.com/item?id=48764896
- **Context:**
  - Debate over slop UI as an honest watermark. random__duck argues the tells signal AI authorship usefully.
  - bescob_ar frames de-slopping tools as watermark removal.
  - sjacob counters with "if you can't tell, does it matter?"; ra0x3 raises the copyright value of provable human edits.
- **Tags:** `[CONTESTED]`
- **Feeds:** "Contested and stale" section; skill positioning

### C9 — "It immediately looks like AI slop because nearly every square inch is filled"
- **Source:** Hacker News, nkrisc, comment subtree, 3 Aug 2026. https://news.ycombinator.com/item?id=49149688
- **Context:**
  - Horror vacui tell: AI is good at filling an image and bad at knowing when to leave space.
  - Ariarule in the same subtree names a sepia or yellow tint on generated imagery that persists at thumbnail size.
- **Tags:** `[AVOID: filling every square inch]` `[AVOID: sepia-tinted generated imagery]`
- **Feeds:** JD3, IC6

### C10 — "Claude uses Shadcn-ui extensively"
- **Source:** Hacker News, esperent, comment subtree, 1 Feb 2025. https://news.ycombinator.com/item?id=42894221
- **Context:**
  - Mechanism claim: training-data skew makes LLMs default to React plus shadcn plus Tailwind.
  - "I think it's been trained to use it over other UI components."
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** LA13

### C11 — "Why does every website landing page look like this now?"
- **Source:** Hacker News, forum thread, 17 Feb 2021, 24 points. https://news.ycombinator.com/item?id=26168232
- **Context:**
  - Pre-AI baseline. The Corporate Memphis hero-illustration landing formula.
  - chaorace: the style is "inoffensive, trendy, and easy to read, which is all most products want".
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** IC7; Part 5 historical baseline

### C12 — "Why do all websites look the same?"
- **Source:** Hacker News, large thread, Nov 2018. https://news.ycombinator.com/item?id=18414001
- **Context:**
  - Pre-AI baseline: hero image, hamburger, cards, oversized type.
  - Causes named: Bootstrap, responsive constraints, conversion optimisation, Jakob's law.
  - Consensus then was convergence on effective patterns, not laziness.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** LA1, LA2; Part 5 historical baseline

### C13 — "Why did every website/product start looking the same?"
- **Source:** Hacker News, forum thread, 14 Jan 2023, 12 points. https://news.ycombinator.com/item?id=34377538
- **Context:**
  - Sameness attributed to design systems, UI kits used instead of designers, and Notion or Linear emulation for perceived legitimacy.
  - Custom design described as hard, expensive and not a differentiator.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 5 historical baseline

### C14 — AI slop
- **Source:** Wikipedia, encyclopedia entry, term coined 2022 and mainstream 2024. https://en.wikipedia.org/wiki/AI_slop
- **Context:**
  - Quotes Gilmore on the "incredibly banal, realistic style".
  - Imagery tells listed: extra fingers, smudged faces, distorted text.
  - Documents sameness collapse, including the recurring invented name "Elias Thorne".
- **Tags:** `[AVOID: generated people and garbled in-image text]` `[EVIDENCE-ONLY]`
- **Feeds:** IC6

### C15 — Corporate Memphis
- **Source:** Wikipedia, encyclopedia entry, style current 2017 to 2023. https://en.wikipedia.org/wiki/Corporate_Memphis
- **Context:**
  - Flat vector people with elastic limbs and purple or blue skin, from Facebook's 2017 Alegria work.
  - Criticised for producing visual homogeneity.
  - Julien Posture's defence: hatred of the style channels wider anxieties about the creative industry.
- **Tags:** `[AVOID: flat elastic-limb vector people]` `[CONTESTED]`
- **Feeds:** IC7; Part 5

### C16 — Wikipedia:Signs of AI writing
- **Source:** WikiProject AI Cleanup, project page, 2025 and ongoing, read via a full third-party reproduction. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Context:**
  - The canonical copy field guide: em dashes, rule of three, negative parallelism, vague attribution, significance inflation, bold overuse, title case.
  - Key caveat used throughout this skill: the signs "work as a combined signal, not as individual tripwires".
  - Also catalogued as M11, where the full wikitext was read.
- **Tags:** `[AVOID: AI writing cadence]` `[CONTESTED]` `[STALE-RISK]`
- **Feeds:** CP2, CP3; Part 5

### C17 — "The AI Purple Problem: Why Every AI Brand Looks the Same"
- **Source:** Michal, Hyzo, Indie Hackers, 12 Jul 2026, 26 likes and 59 comments. https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02
- **Context:**
  - Purple gradients and glowing orbs act as AI-brand shorthand.
  - Founders report conversion improved after swapping "AI magic" visuals for screenshots of real output.
  - A commenter defends purple as legitimate category signalling for a startup with no trust equity.
- **Tags:** `[AVOID: abstract AI-magic visuals]` `[ADOPT: screenshots of real output]` `[CONTESTED]`
- **Feeds:** CO1, CO5, JD2

### C18 — "Roast my (AI-generated) landing page"
- **Source:** Farez Rahman, Indie Hackers, 6 Jul 2025, 13 comments. https://www.indiehackers.com/post/roast-my-ai-generated-landing-page-eb23046029
- **Context:**
  - Community roast findings: too much text and no visuals, unreadable mock screenshots, vague value proposition, missing trust signals.
  - The unreadable low-resolution device mockup is the concrete mobile-side tell.
- **Tags:** `[AVOID: unreadable device mockups]` `[AVOID: vague value proposition]`
- **Feeds:** CP3, CP6, JD2

### C19 — tweakcn README
- **Source:** jnsahaj, GitHub project, 2025 to 2026, around 10,000 stars. https://github.com/jnsahaj/tweakcn
- **Context:**
  - Opens with "Websites made with shadcn/ui famously look the same".
  - The sameness complaint is mainstream enough to support a 10,000-star fix tool.
- **Tags:** `[AVOID: unchanged shadcn tokens]` `[ADOPT: token customisation tooling]`
- **Feeds:** LA13

### C20 — unslop-ui-skill and TELLS.md
- **Source:** claudiusararu, GitHub repo, 2026, MIT. https://github.com/claudiusararu/unslop-ui-skill
- **Context:**
  - Community-maintained catalog of around 100 AI design tells across nine categories.
  - Source of many specific signatures: pastel-100 icon tiles with 600-weight icons, avatar stack with "+12k developers", three-tier pricing with a scaled middle card.
  - Lists both overstuffing and excess whitespace as tells, which points at unconsidered decoration as the shared root.
  - Also catalogued as R2 in the prior-art survey.
- **Tags:** `[AVOID: pastel icon tiles]` `[AVOID: avatar-stack social proof]` `[AVOID: scaled Most Popular pricing card]` `[ADOPT: TELLS.md as a rule seed list]`
- **Feeds:** LA3, LA6, CP3, JD3; scripts/rules.json

### C21 — "How to Spot an App Built by AI (And Why I Still Love Vibe Coded Apps)"
- **Source:** Marcia Cripps, Medium, 5 Dec 2025. https://medium.com/@marciacripps/how-to-spot-an-app-built-by-ai-and-why-i-still-love-vibe-coded-apps-02e78d41373f
- **Context:**
  - The main mobile-specific community source. Names glowing pill buttons and purple, cyan and pink on gray-900.
  - Names decorative emoji use and gamified microcopy: "Let's Go!", "Great Job!".
  - Notes hover states shipped on touch-only interfaces.
  - Notes lorem ipsum remnants left in production apps.
- **Tags:** `[AVOID: glowing pill buttons]` `[AVOID: gamified microcopy]` `[AVOID: hover states on touch UI]`
- **Feeds:** CP5, IC2, MO2

### C22 — "Why Your AI Startup Looks Generic"
- **Source:** Studio Maydit, agency blog, 28 Jun 2026. https://studiomaydit.com/blog/why-your-ai-startup-looks-generic
- **Context:**
  - "When every AI company clears the same bar, clearing the bar is not distinctive. It is camouflage."
  - Proposes the swap-the-logo test: if the page works with a competitor's logo, it says nothing.
  - Names template-driven hero sections that are interchangeable across competitors.
- **Tags:** `[ADOPT: swap-the-logo test]` `[AVOID: interchangeable hero copy]`
- **Feeds:** CP6, JD1, JD5

### C23 — "AI Purple Problem: Make Your UI Unmistakable"
- **Source:** Jainil Prajapati, DEV.to, 8 Oct 2025. https://dev.to/jaainil/ai-purple-problem-make-your-ui-unmistakable-3ono
- **Context:**
  - Documents the community-coined phrase "AI purple problem", summarising Reddit, Twitter and YouTube discourse.
  - "AI is a pattern machine, it mirrors what it sees. We trained it to be average."
  - The only route to Reddit discourse in this research, since reddit.com was blocked at the proxy.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** CO1; documented research gap

### C24 — pavlov on GolemUI gradient fills
- **Source:** Hacker News comment, Jul 2026. https://news.ycombinator.com/item?id=48749396
- **Context:**
  - "The overuse of blue and purple gradient fills on the landing page is a telltale sign of AI slop."
  - Corroborating single comment, used only to support the community consensus on CO1.
- **Tags:** `[AVOID: blue and purple gradient fills]`
- **Feeds:** CO1

### C25 — yogourt on purple-to-blue gradients
- **Source:** Hacker News comment, Jan 2026. https://news.ycombinator.com/item?id=46677833
- **Context:**
  - "Same tired purple-to-blue gradients." Corroborating comment for the same tell.
- **Tags:** `[AVOID: purple to blue gradient]`
- **Feeds:** CO1

### C26 — nichochar and AdewoleJasper on builder sameness
- **Source:** Hacker News comments, Jun 2025. https://news.ycombinator.com/item?id=44382736 and https://news.ycombinator.com/item?id=44148606
- **Context:**
  - Lovable-class builders produce "output that feels the same, often based on the same UI kits under the hood".
  - Names the shared UI kit, not the model, as the cause of convergence.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** LA13

---

# K. Code samples

All 12 repos were cloned in full and scanned locally on 2026-08-28. Provenance was verified inside each repo. Counts are measured, not assumed.

### K1 — Healthcare Landing Page (Lovable)
- **Source:** NebeyouMusie, GitHub repo, snapshot 2026-08-28. https://github.com/NebeyouMusie/Healthcare-Landing-Page
- **Context:**
  - Provenance is certain: README carries a `lovable.dev/projects/<uuid>` URL, and `lovable-tagger` sits in vite.config.ts and package.json.
  - Ships the full Lovable stack: Vite, React, TypeScript, complete shadcn `components/ui` dump, HSL token block, lucide-react.
  - Notably also emits v0's `/placeholder.svg?height=` URL, so that artefact is not v0-exclusive.
- **Tags:** `[AVOID: lovable-tagger left in a shipped project]` `[EVIDENCE-ONLY]`
- **Feeds:** PR1, PR2, LA13

### K2 — SquadUp pickup-sports app (Lovable)
- **Source:** SudarshanaSRao, GitHub repo, snapshot 2026-08-28. https://github.com/SudarshanaSRao/sports-on-the-go-4c575e84
- **Context:**
  - Provenance: `lovable-tagger` present, plus Lovable's 8-hex repo-name suffix and bun.lockb.
  - Highest gray body-text density measured: 422 occurrences of `text-(gray|slate)-(500|600)`.
  - The only sample carrying the exact Tailwind UI container triplet `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
  - Heavy `min-h-screen` repetition per section.
- **Tags:** `[AVOID: gray body-text monoculture]` `[AVOID: min-h-screen per section]` `[STALE-RISK]`
- **Feeds:** PR1, LA11, LA12

### K3 — neoanalytics analytics site (Lovable)
- **Source:** Nullhermit, GitHub repo, snapshot 2026-08-28. https://github.com/Nullhermit/neoanalytics
- **Context:**
  - Provenance: repo description says built with Lovable AI, and the full Lovable scaffold is present.
  - Confirms the Lovable cluster: components.json, bun.lock, shadcn dump, `pages/Index.tsx` plus catch-all `pages/NotFound.tsx`.
  - Uses Inter from Google Fonts.
- **Tags:** `[AVOID: unchanged Lovable scaffold]` `[EVIDENCE-ONLY]`
- **Feeds:** PR1, LA13, TY1

### K4 — Checkers game, plain HTML, CSS and JavaScript (Bolt)
- **Source:** Vauth, GitHub repo, snapshot 2026-08-28. https://github.com/Vauth/checkers
- **Context:**
  - Provenance: README states the game was made by bolt.new.
  - Structurally cannot match Tailwind class patterns, which is why the scan reports "of 9 Tailwind samples" separately.
  - Useful as a negative control: a plain-JS AI project carries almost none of the class-string tells.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** scanner scope limits

### K5 — Tech Euphoria 2K25 event site (Bolt)
- **Source:** VinaySiddha, GitHub repo, snapshot 2026-08-28. https://github.com/VinaySiddha/TechEuphoria2k25
- **Context:**
  - Provenance: root `config.json` reads `{"template": "bolt-vite-react-ts"}`.
  - No shadcn and no tokens. Raw palette utilities: blue 97, green 67, purple 40 occurrences.
  - 133 two-hue gradient washes, with top pairs `from-blue-600 to-green-600` (21) and `from-red-600 to-pink-600` (10).
  - This is the evidence that gradient hues follow the topic. They are not reliably purple.
- **Tags:** `[AVOID: many two-hue gradient washes]` `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** PR4, CO3; corrects the "always purple" folk claim

### K6 — Ancient Sri Lanka tourism site (v0, plain HTML mode)
- **Source:** SadeepaNHerath, GitHub repo, snapshot 2026-08-28. https://github.com/SadeepaNHerath/Ancient-Sri-Lanka
- **Context:**
  - Provenance: README says 100% generated using v0.dev with minimal customisation.
  - The output is Bootstrap 5, not Tailwind: `navbar navbar-expand-lg`, `d-flex`, `bi bi-*` icons.
  - Four "Learn More" buttons on one page.
  - A scanner keyed only to Tailwind misses this whole branch of generated output.
- **Tags:** `[AVOID: repeated Learn More CTAs]` `[EVIDENCE-ONLY]`
- **Feeds:** LA5, CP4; scanner must cover Bootstrap output

### K7 — CRM System Dashboard (v0)
- **Source:** Suresh-28, GitHub repo, snapshot 2026-08-28. https://github.com/Suresh-28/CRM-System-Dashboard
- **Context:**
  - Provenance: v0-dev topic, "built with Vercel", exact `placeholder.svg?height=32&width=32` strings, full `components/ui` dump.
  - Next.js App Router plus shadcn plus lucide-react is the standard v0 cluster.
- **Tags:** `[AVOID: v0 placeholder images shipped]` `[EVIDENCE-ONLY]`
- **Feeds:** PR2, LA13

### K8 — Personal portfolio (v0)
- **Source:** MatheusAlvesPereira, GitHub repo, snapshot 2026-08-28. https://github.com/MatheusAlvesPereira/portifolio-
- **Context:**
  - Provenance: README and description say written in Vercel v0. Full shadcn dump present.
  - Confirms the v0 cluster on a non-SaaS brief.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** LA13, PR2

### K9 — SaaS monorepo from one long v0 prompt
- **Source:** tsylvester, GitHub repo, snapshot 2026-08-28. https://github.com/tsylvester/v0-saas-test
- **Context:**
  - Provenance: named as the output repo in the author's own write-up of a v0 SaaS framework prompt.
  - Shadcn dump plus placeholder.svg. `cn()` used over 210 times.
  - Shows that a very long prompt still produces the same stack fingerprint.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** LA13, PR2

### K10 — Architect's Eye OSINT terminal (Replit Agent plus Claude)
- **Source:** PromptSolutionsLLC, GitHub repo, snapshot 2026-08-28. https://github.com/PromptSolutionsLLC/Architects-Eye
- **Context:**
  - Provenance: `.replit` plus `replit.md`, and a README saying it was built with Claude and a Replit Agent.
  - React, TypeScript, Tailwind with shadcn-style HSL tokens. `text-muted-foreground` used 80 times, lucide 32 times.
  - Accent colour is cyan, appropriate to an OSINT terminal, which supports the "hue follows topic" correction.
  - 23 to 25 dark-hero background class occurrences.
- **Tags:** `[AVOID: replit.md shipped in a public repo]` `[EVIDENCE-ONLY]`
- **Feeds:** PR5, CO4, LA13

### K11 — 23 Claude-generated hero sections
- **Source:** pulkitxm, claude-directory GitHub repo, subset `hero-sections/`, snapshot 2026-08-28. https://github.com/pulkitxm/claude-directory
- **Context:**
  - The Claude dark-hero cluster is measured here: `bg-white/10` plus `border-white/20` glass 27 times, `backdrop-blur` 18 times.
  - Font mix loaded from Google Fonts: Inter, Space Grotesk 6, Instrument Serif 6, Bricolage Grotesque 6, JetBrains Mono 3.
  - Copy pattern "Trusted by 40,000+ traders" and "Trusted by 9,000+ small trade desks" replaces the folk "10,000+ users" regex.
  - Caveat: this is a curated showcase, so it is biased toward polished output.
- **Tags:** `[AVOID: dark hero glass combo]` `[AVOID: Inter plus Space Grotesk pairing]` `[AVOID: Trusted by N+ stat line]` `[CONTESTED]`
- **Feeds:** CO4, CO5, TY2, LA6, CP3

### K12 — ChatGPT design templates, GPT-3 era
- **Source:** jxlien-l, GitHub repo, snapshot 2026-08-28. https://github.com/jxlien-l/chatgpt-design-templates
- **Context:**
  - Four HTML and CSS templates from GPT-3 era output.
  - Shares nothing with the modern stack: plain CSS, 4px to 5px border radius, no Inter, no gradients.
  - Direct proof that tells are model-generation-specific and that a scanner needs dated signature sets.
- **Tags:** `[STALE-RISK]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 0 finding 2; era tags on every rule

### K13 — Developers Digest slop article, used as cross-check
- **Source:** Developers Digest, article, fetched 2026-08-28 for cross-checking only. https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it
- **Context:**
  - Named Inter, the Space Grotesk plus Instrument Serif plus Geist set, "VibeCode purple", shadcn defaults, glassmorphism, icon-card grids and stat rows.
  - The code scan confirmed the font-set claim and the shadcn claim, and disconfirmed the raw indigo claim.
  - Same article as P1. Listed separately because it functioned as a hypothesis, not a sample.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** TY2, LA13; cross-check trail

### K14 — Alan West indigo-500 article, used as cross-check
- **Source:** Alan West, DEV Community article, fetched 2026-08-28 for cross-checking only. https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p
- **Context:**
  - Claims `bg-indigo-500`, `from-indigo-500 to-purple-600`, Inter and three-column icon grids.
  - The scan found 0 of 12 repos using raw indigo utilities, so the claim is dated to 2023-era output.
  - Same article as P6 and V1. Listed separately as the disconfirmed hypothesis.
- **Tags:** `[STALE-RISK]` `[CONTESTED]`
- **Feeds:** CO1 legacy weighting

### K15 — v0's SaaS Framework Prompt Output write-up
- **Source:** Tim Sylvester, Medium article, fetched 2026-08-28. https://medium.com/@TimSylvester/v0s-saas-framework-prompt-output-e864081e5fc3
- **Context:**
  - Narrative account of generating a SaaS monorepo from one long v0 prompt.
  - Provided the provenance link to sample K9. No independent claims cited from it.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** K9 provenance

---

# M. Mobile and copy

M1 to M10 are the mobile app sources. M11 to M20 are the UI and marketing copy sources.

### M1 — AI Design Slop: Why Every AI-Built Interface Looks the Same
- **Source:** Mohit Phogat, designer, Medium, 7 Aug 2026. https://mohitphogat.medium.com/ai-design-slop-why-every-ai-built-interface-looks-the-same-and-how-to-fix-it-bf874e0b470c
- **Context:**
  - Names the slop palette for apps: purple to cyan gradients, indigo-500, Inter at every weight, three and six column card grids.
  - Card formula measured in words: icon, heading, exactly two lines of text.
  - Mechanism: "most probable" means the statistical average of millions of templates.
  - Fix includes an explicit ban, for example "forbid six-column grids".
  - Same author as P12, read again for the mobile angle.
- **Tags:** `[AVOID: six-column card grid]` `[AVOID: purple to cyan gradient]` `[ADOPT: explicit forbidden-pattern list]`
- **Feeds:** LA2, CO2, TY1

### M2 — How to fix the "AI-generated" look in your frontend
- **Source:** Alan West, DEV Community, 18 May 2026. https://dev.to/alanwest/how-to-fix-the-ai-generated-look-in-your-frontend-1ahh
- **Context:**
  - Names the exact Tailwind classes of the look: `bg-indigo-600 hover:bg-indigo-700`, `rounded-2xl`, `shadow-lg`.
  - Names the canonical section order: hero, features grid, social proof, pricing, FAQ, footer.
  - Proposes lint rules that fail the build on banned classes.
  - Proposes a "component vocabulary" so radius and shadow stay intentional rather than uniform.
- **Tags:** `[AVOID: rounded-2xl plus shadow-lg reflex]` `[ADOPT: lint rules on banned classes]` `[ADOPT: component vocabulary]`
- **Feeds:** LA1, LA10, CO1; scripts/rules.json

### M3 — How to Make AI UI Look Less Generic: 5 Fixes
- **Source:** Jason Zhou, Superdesign, tool team blog, 21 Jun 2026. https://superdesign.dev/blog/how-to-make-ai-ui-look-less-generic
- **Context:**
  - Tell list: Inter or Roboto, purple or indigo gradients, centred hero with a single CTA, three-card icon rows, rounded everything, drop shadows at 0.1 opacity.
  - "Generic is what one prompt does when it has to pick taste, explore, and write code all at once."
  - Same source as P24, read again for the mobile angle.
- **Tags:** `[AVOID: 0.1-opacity shadow on everything]` `[ADOPT: separate taste from implementation]`
- **Feeds:** LA9, LA10, TY1, JD4

### M4 — The Dribbblisation of Design
- **Source:** Paul Adams, product design VP, Intercom blog, 18 Sep 2013. https://www.intercom.com/blog/the-dribbblisation-of-design/
- **Context:**
  - The pre-AI origin of the sameness disease, written twelve years before the AI framing.
  - "Whether it's social software, accounting software, a marketing site, a weather app, the same styles are applied."
  - Names the cause: designs optimised for peer approval rather than for users.
  - "Things that look great but don't work well."
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]` `[AVOID: domain-blind visual treatment]`
- **Feeds:** JD1, JD2; Part 5 historical baseline

### M5 — Google Stitch Review 2026: What Users Actually Say
- **Source:** Superdesign, tool team blog aggregating user reviews from Apr to Jun 2026. https://superdesign.dev/blog/google-stitch-review
- **Context:**
  - Users say Stitch output "cannot shake the AI-looking design".
  - A Product Hunt reviewer: "my top navigation looked a little different on different pages."
  - Iteration model is re-prompt and hope, not tweak a font or a background.
  - Cross-screen inconsistency despite per-screen polish is the closest thing to a true AI fingerprint.
- **Tags:** `[AVOID: cross-screen drift]` `[EVIDENCE-ONLY]`
- **Feeds:** JD2

### M6 — Why Fintech Looks the Same
- **Source:** Brandon Pazitka, Freshly Brewed, brand agency, 5 May 2026. https://freshlybrewed.co/insights-news/why-fintech-looks-the-same/
- **Context:**
  - Fintech cliches: purple to blue or teal to green gradients, floating geometric shapes, isometric 3D illustration.
  - Type set named: Circular, Inter, SF Pro. Layout named: three-column features.
  - Traces the whole set to the Revolut, Monzo and Stripe era, which is 2015 to 2018 and pre-AI.
  - This is the cleanest evidence that a purple gradient in 2019 was on-trend, not AI-assisted.
- **Tags:** `[CONTESTED]` `[AVOID: isometric 3D blob illustration]` `[STALE-RISK]`
- **Feeds:** CO1, IC7; Part 5

### M7 — Mobile-App Onboarding: An Analysis of Components and Techniques
- **Source:** Alita Kendrick, Nielsen Norman Group, UX research, 21 Jun 2020. https://www.nngroup.com/articles/mobile-app-onboarding/
- **Context:**
  - Research-based case against feature-tour carousels and deck-of-cards tutorials.
  - "Tutorials didn't improve task performance."
  - Deck-of-cards tutorials "tend to make the interface appear more complicated than it actually is, and strains user's memory".
  - Allows onboarding for genuinely novel interaction patterns.
- **Tags:** `[AVOID: three-slide onboarding carousel]` `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** mobile checklist; JD2

### M8 — I tested 4 AI tools to generate UI from the same prompt
- **Source:** Xinran Ma, UX designer, Medium, 25 Oct 2024. https://medium.com/@xinranma/i-tested-4-ai-tools-to-generate-ui-from-the-same-prompt-0d2113736cce
- **Context:**
  - Same-prompt comparison of Wireframe Designer, UX Pilot, Uizard and Galileo AI.
  - All four converge on similar mobile-first layouts.
  - Uizard emits whole multi-screen sets, including onboarding, from one prompt.
  - All outputs required additional refinement work.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** JD1, JD4

### M9 — Why AI-Generated UI Looks Good But Often Feels Generic
- **Source:** Samith Pitigala, designer, Medium, 1 Jun 2026. https://medium.com/@cssamithpitigala/why-ai-generated-ui-looks-good-but-often-feels-generic-020a9b1b8492
- **Context:**
  - "Most AI-generated UI is based on what is common, not what is deeply specific."
  - "A healthcare app, a finance app, a learning app, and a project management app should not all feel the same."
  - "A screen that looks good in one static image is not the same as a product that works across different states, errors, devices."
  - Trend elements repeat without strategic purpose: glassmorphism, gradients, soft shadows.
- **Tags:** `[AVOID: domain-blind treatment]` `[AVOID: trend elements without purpose]`
- **Feeds:** JD1, JD2

### M10 — Apple Updates App Store Guidelines With Stricter Rules for Low-Quality Apps
- **Source:** MacRumors, tech news, 9 Jun 2026. https://www.macrumors.com/2026/06/09/app-store-guidelines-low-quality-apps/
- **Context:**
  - Guideline 4.3 spam now names saturated template categories such as timers, wallpapers and fortune telling.
  - "Opportunistically creating variants of existing app categories or popular apps degrades App Store discovery."
  - The guideline text does not mention AI. Rule 4.3 predates and is broader than AI generation.
- **Tags:** `[AVOID: re-skinned template category apps]` `[CONTESTED]`
- **Feeds:** mobile checklist

### M11 — Wikipedia:Signs of AI writing (full wikitext)
- **Source:** WikiProject AI Cleanup, Wikipedia project page, live and updated Aug 2026. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Context:**
  - The canonical field guide, read in full via raw wikitext. Vocabulary is dated by model era.
  - 2023 to mid-2024 GPT-4 words: `delve`, `tapestry`, `testament`, `pivotal`.
  - Mid-2024 to 2025: `align with`, `fostering`, `showcasing`.
  - 2025 onward: `emphasizing`, `enhance`, `highlighting`.
  - Shortcut sections used here: WP:AIDASH em dashes, WP:AITITLECASE title case, WP:AIEMOJI emoji headers, WP:AIBOLD boldface.
  - Also WP:AIPARALLEL negative parallelism, WP:AIWEASEL vague attribution, WP:AIPLACEHOLDER leftover placeholders, WP:AICUTOFF disclaimers, WP:AICURLY curly quotes.
  - Verbatim caveat: "Not all text featuring these indicators is AI-generated." The list is descriptive, not prescriptive.
  - Cites an Economist study, 30 Jul 2026: of current models only Claude used em dashes more than professional writers. ChatGPT used them less.
- **Tags:** `[AVOID: AI writing cadence]` `[CONTESTED]` `[STALE-RISK]`
- **Feeds:** CP2, CP3, PR7; Part 5

### M12 — shitfa.st
- **Source:** Satirical catalog site, live 2026. https://shitfa.st/
- **Context:**
  - An archive of landing pages that all read like one AI wrote them, with a ShitScore calculator.
  - Fake-proof catalog: unverifiable "Trusted by 5,000+ teams", first-name-only testimonials, fake logo bars.
  - AI founder headshots with "perfect pores and no life behind the eyes".
  - FAQ shape called out as "SEO optimization targeting questions nobody typed".
  - Roadmap theater: public roadmaps with vague statuses standing in for shipped functionality.
- **Tags:** `[AVOID: fake social proof]` `[AVOID: SEO-bait FAQ]` `[AVOID: roadmap theater]`
- **Feeds:** CP3, LA6, IC5

### M13 — "Are we in the era of AI slop landing pages?"
- **Source:** Hacker News discussion, 2026. https://news.ycombinator.com/item?id=49024805
- **Context:**
  - Practitioners name "Trusted by 10,000+ professionals" claims contradicted by public traffic data.
  - Identical card layouts and colour schemes across multiple sites.
  - minimaxir counters: "Landing pages were already heavily templated prior to agents."
  - elenaviter: "A good product has a soul. Trust is built on invested effort."
- **Tags:** `[AVOID: unverifiable user counts]` `[CONTESTED]`
- **Feeds:** CP3; Part 5

### M14 — Stop Sounding Like AI
- **Source:** Sathya, Microcopy Examples newsletter, 27 Feb 2025. https://microcopyexamples.substack.com/p/stop-sounding-like-ai
- **Context:**
  - Word list with human rewrites for these terms: `Elevate`, `Unlock`, `Curate`, `Delight`, `Infused`, `Game-changer`, `Revolutionize`.
  - Flags the "It's not just a [product]; it's a [metaphor]" template directly.
  - Flags "Ready to transform your workflow?" as a pre-CTA question tell.
  - Rewrite example: "New flavors. No gimmicks. Just great taste." instead of "an ever-changing world of delightful flavors".
  - "Write how you talk, clear, engaging, and real."
- **Tags:** `[AVOID: transformation verbs]` `[AVOID: not just X it's Y]` `[ADOPT: write how you talk]`
- **Feeds:** CP1, CP2

### M15 — Avoid "landing page words"
- **Source:** Sathya, Microcopy Examples newsletter, 23 Dec 2024. https://microcopyexamples.substack.com/p/avoid-landing-page-words
- **Context:**
  - `Unlock`, `Unleash`, `Empower`, `Supercharge` and `Game-changer` named as empty buzzwords.
  - Rewrite rule: "Our app helps you organize your tasks, saving you hours each week" beats "Supercharge your productivity".
  - Same source as P21. Read again for the copy-tell list.
- **Tags:** `[AVOID: empty buzzwords]` `[ADOPT: concrete benefit sentence]` `[CONTESTED]`
- **Feeds:** CP1

### M16 — Week 16: 10 phrases that scream AI
- **Source:** Tan Rosado, writer's newsletter, 11 Oct 2024. https://tanrosado.substack.com/p/week-16-10-phrases-that-scream-ai
- **Context:**
  - Ten phrases: `Seamlessly integrated`, `In today's fast-paced world`, `cutting-edge`, `game-changer`, and the UN- verbs.
  - Central thesis is a false-positive warning: skilled human writers use these phrases and face unfair accusations.
  - Explicitly flags "Let's dive in" as flagged despite legitimate use.
- **Tags:** `[CONTESTED]` `[AVOID: stock opener phrases]`
- **Feeds:** CP1, CP2; Part 5

### M17 — No One Wants to "Get Started"
- **Source:** Natalie Sacks, UX writer newsletter, 8 Jul 2024. https://nataliewritesthings.substack.com/p/no-one-wants-to-get-started
- **Context:**
  - "Get Started" is vague and frames the next step as a burden.
  - "You're telling the user that there's a bunch of things they need to do and not even sharing what they are."
  - Replacement rule: name the specific action, for example "Open an account" or "View offer".
- **Tags:** `[AVOID: Get Started as a CTA]` `[ADOPT: action-named CTA]`
- **Feeds:** CP4, LA5

### M18 — 13 CTA buttons that go beyond "Learn More" and "Get Started"
- **Source:** Smith.ai, business services blog, updated 6 May 2026. https://smith.ai/blog/13-call-to-action-cta-buttons-that-go-beyond-learn-more-and-get-started
- **Context:**
  - "Learn More tells a visitor almost nothing."
  - Outcome-named and first-person CTAs outperform generic ones, for example "Start my free trial".
- **Tags:** `[AVOID: Learn More as a CTA]` `[ADOPT: outcome-named CTA]`
- **Feeds:** CP4, LA5

### M19 — Don't Write Like AI: 10 Takeaways from Wikipedia's Signs of AI Writing
- **Source:** Blake Stockton, content-marketing blog, 7 Aug 2025. https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/
- **Context:**
  - Practitioner distillation of M11, useful for the marketing context rather than the encyclopedia one.
  - Names inflated symbolism, the bolded bullet convention "**Scalability:** The system...", em dashes and vague attribution.
- **Tags:** `[AVOID: bolded lead-in bullets]` `[AVOID: significance inflation]`
- **Feeds:** CP2

### M20 — How Users Read on the Web
- **Source:** Jakob Nielsen, Nielsen Norman Group, 30 Sep 1997. https://www.nngroup.com/articles/how-users-read-on-the-web/
- **Context:**
  - The pre-AI measurement that anchors every copy rule here. Objective language improved usability by 27%, concise text by 58%.
  - Users "detested" boastful marketese and wanted the straight facts.
  - "Credibility suffers when users clearly see that the site exaggerates."
  - Proves marketese was a documented human problem 28 years before the AI framing.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: objective and concise copy]` `[CONTESTED]`
- **Feeds:** CP1, CP6; Part 5

---

# X. Accessibility

X1 to X17 are the output-design sources. X18 to X29 are the documentation sources.

### X1 — Web Content Accessibility Guidelines (WCAG) 2.2
- **Source:** W3C, standard, Recommendation 5 Oct 2023, updated Dec 2024. https://www.w3.org/TR/WCAG22/
- **Context:**
  - The normative source for every numeric threshold this skill enforces on output.
  - Supplies SC 1.4.1, 1.4.3, 1.4.6, 1.4.8, 1.4.10, 1.4.11, 1.4.12, 2.2.1, 2.2.2, 2.3.1, 2.3.3, 2.4.7, 2.4.11, 2.4.13, 2.5.7, 2.5.8, 3.2.6, 3.3.7 and 3.3.8.
  - Conformance is measured against WCAG 2.x ratios, not against candidate models.
- **Tags:** `[ADOPT: WCAG 2.2 AA as the conformance gate]`
- **Feeds:** Part 6 in full

### X2 — What's New in WCAG 2.2
- **Source:** W3C WAI, guidance, 2023 and maintained. https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- **Context:**
  - Lists the nine criteria added in 2.2, which are the ones most often missing from generated output.
  - Target Size Minimum, Focus Not Obscured, Dragging Movements, Consistent Help, Redundant Entry and Accessible Authentication all land here.
- **Tags:** `[ADOPT: the nine WCAG 2.2 additions as a checklist]`
- **Feeds:** Part 6

### X3 — Understanding SC 2.5.8: Target Size (Minimum)
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- **Context:**
  - Pointer targets must be at least 24 by 24 CSS pixels, with five exceptions.
  - The spacing exception: a 24px diameter circle centred on each target must not intersect another target's circle.
  - Checkable with `getBoundingClientRect()` on every interactive element.
- **Tags:** `[ADOPT: 24 by 24 CSS px minimum target]`
- **Feeds:** Part 6; icon-button audit

### X4 — Understanding SC 1.4.3: Contrast (Minimum)
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **Context:**
  - 4.5:1 for normal text, 3:1 for large text. Large means 18 point, or 14 point bold, roughly 24px or 18.66px bold.
  - Do not round. 4.499:1 fails.
  - Gradient text has no averaging allowance, so the light stops must pass too.
- **Tags:** `[ADOPT: 4.5:1 body contrast floor]` `[AVOID: gradient text over body copy]`
- **Feeds:** CO2, CO8; Part 6

### X5 — Understanding SC 2.3.1: Three Flashes or Below Threshold
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html
- **Context:**
  - Nothing may flash more than three times in one second above the general and red flash thresholds.
  - General flash threshold: opposing luminance changes of 10% or more where the darker image is below 0.80 relative luminance.
  - Area threshold is roughly 25% of a 10 degree visual field, approximated as a 341 by 256 px rectangle.
  - Video can be checked with PEAT, the Photosensitive Epilepsy Analysis Tool.
- **Tags:** `[ADOPT: no flashing above 3Hz]`
- **Feeds:** Part 6; MO4

### X6 — Understanding SC 2.3.3: Animation from Interactions, plus Technique C39
- **Source:** W3C WAI, understanding document and technique. https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html and https://www.w3.org/WAI/WCAG22/Techniques/css/C39
- **Context:**
  - Motion animation triggered by interaction must be disableable unless it is essential.
  - Technique C39 is the concrete pattern: wrap non-essential motion in `@media (prefers-reduced-motion: no-preference)`.
  - A stylesheet with keyframes and no reduced-motion query fails this pattern outright, and that is greppable.
- **Tags:** `[ADOPT: prefers-reduced-motion on every animation]`
- **Feeds:** MO5; Part 6; every library entry in L

### X7 — Understanding SC 2.2.1: Timing Adjustable
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html
- **Context:**
  - For each time limit the user must be able to turn it off. Or adjust it to ten times the default. Or extend it after a 20 second warning.
  - Exceptions are real-time events, essential limits, and limits longer than 20 hours.
  - This is what makes fake urgency countdowns a compliance problem, not only a taste problem.
- **Tags:** `[AVOID: countdown timers as decoration]` `[ADOPT: extendable time limits]`
- **Feeds:** Part 6; CP3

### X8 — Making Content Usable for People with Cognitive and Learning Disabilities
- **Source:** W3C Cognitive and Learning Disabilities Accessibility Task Force, Working Group Note, 29 Apr 2021. https://www.w3.org/TR/coga-usable/
- **Context:**
  - Not a normative standard. It supplements WCAG and carries no conformance levels.
  - Objectives used here: clear and understandable content, no reliance on memory, familiar hierarchy, limit interruptions, avoid data loss and timeouts.
  - Patterns used here: Use Clear Words, Keep Text Succinct, Avoid Too Much Content, Use White Spacing, Break Media into Chunks, Make Each Step Clear.
  - Its patterns were validated with users who have cognitive disabilities, which is why they are treated as strong heuristics.
- **Tags:** `[ADOPT: COGA patterns as heuristics]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 6; JD3; docs guidance

### X9 — BDA Dyslexia Style Guide 2023
- **Source:** British Dyslexia Association, style guide, 2023. https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf
- **Context:**
  - Body size 12 to 14 point, roughly 16 to 19px. Line spacing 1.5 preferred. Headings at least 20% larger than body.
  - Inter-letter spacing around 35% of average letter width. Inter-word spacing at least 3.5 times inter-letter spacing.
  - "Left align text, without justification." Avoid underlining, italics and uppercase for running text.
  - Recommends ordinary sans serifs: Arial, Verdana, Tahoma, Calibri, Open Sans. Dark text on a light but not pure white background.
  - Warns against green with red or pink colour combinations.
  - The BDA does not require a special dyslexia font.
- **Tags:** `[ADOPT: 16px body, 1.5 line-height, left align]` `[AVOID: uppercase running text]` `[AVOID: justified body copy]` `[CONTESTED]`
- **Feeds:** TY5; Part 6

### X10 — Designing for accessibility posters
- **Source:** Karwai Pun, UK Home Office Digital, poster set, 2016 and hosted ongoing. https://ukhomeoffice.github.io/accessibility-posters/
- **Context:**
  - Six audiences: autism, dyslexia, anxiety, low vision, motor, screen readers.
  - Autism: "Use simple colours", "Don't use bright contrasting colours", "Don't use figures of speech and idioms".
  - Motor: don't demand precision, don't bunch interactions together.
  - Anxiety: don't rush users, explain what happens next, let users check answers before submitting.
  - These are practitioner heuristics, not controlled studies.
- **Tags:** `[ADOPT: simple restrained palette]` `[AVOID: idioms and figures of speech]` `[EVIDENCE-ONLY]`
- **Feeds:** CO7, IC2; Part 6; docs guidance

### X11 — Dos and don'ts on designing for accessibility
- **Source:** Karwai Pun, GOV.UK Accessibility blog, 2 Sep 2016. https://accessibility.blog.gov.uk/2016/09/02/dos-and-donts-on-designing-for-accessibility/
- **Context:**
  - The written companion to X10, with the reasoning behind each poster line.
  - Explicitly states the posters highlight what good and bad design looks like, rather than reporting study results.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: the do and don't pairs as a review list]`
- **Feeds:** Part 6

### X12 — One thing per page
- **Source:** Tim Paul, GDS Design Notes, 3 Jul 2015. https://designnotes.blog.gov.uk/2015/07/03/one-thing-per-page/
- **Context:**
  - Start form design with each question on its own page.
  - Low-confidence users find them easier, they work well on mobile, and they handle errors, branches, loops and saving better.
  - The author concedes there is no formal A/B data.
- **Tags:** `[ADOPT: one question per page]` `[CONTESTED]`
- **Feeds:** SurveyJS `questionsOnPageMode`; docs guidance

### X13 — Foundations: target sizes
- **Source:** TetraLogical, practitioner article, 20 Dec 2022. https://tetralogical.com/blog/2022/12/20/foundations-target-size/
- **Context:**
  - Collates the three thresholds in one place. Apple HIG: 44 by 44 points.
  - Material: 48 by 48 dp. WCAG 2.5.5 AAA: 44 by 44 CSS pixels.
  - WCAG 2.5.8 AA at 24px is the floor, not the target, for touch interfaces.
- **Tags:** `[ADOPT: 44pt or 48dp on touch]`
- **Feeds:** Part 6

### X14 — WCAG 3 is not ready yet
- **Source:** Eric Eggert, yatil.net, updated 28 Mar 2023. https://yatil.net/blog/wcag-3-is-not-ready-yet
- **Context:**
  - APCA is a candidate contrast model for WCAG 3, and WCAG 3 is an early Working Draft.
  - "You cannot rely on APCA for compliance, simply because it does not exist in WCAG 2."
  - Practical rule adopted here: WCAG 2.x is the gate, APCA is an advisory design-time check.
- **Tags:** `[CONTESTED]` `[ADOPT: APCA as advisory only]` `[STALE-RISK]`
- **Feeds:** Part 6

### X15 — Good Fonts for Dyslexia
- **Source:** Rello and Baeza-Yates, ACM ASSETS 2013, summarised at dyslexia.com. https://blog.dyslexia.com/good-fonts-for-dyslexia-an-experimental-study/
- **Context:**
  - Eye-tracking study of 48 dyslexic readers aged 11 to 50 across 12 typefaces.
  - Reading performance was best with sans serif, monospaced and roman fonts: Helvetica, Courier, Arial, Verdana, CMU.
  - "Use of the OpenDyslexic font did not enhance text readability or reading speed." Participants preferred standard fonts.
  - The authors cautioned against italic text.
- **Tags:** `[AVOID: OpenDyslexic as an accessibility fix]` `[ADOPT: plain sans with generous spacing]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 6 dyslexia note

### X16 — Do Dyslexia Fonts Actually Work?
- **Source:** Edutopia, covering Wery and Diliberto 2017 and Kuster et al. 2018. https://www.edutopia.org/article/do-dyslexia-fonts-actually-work/
- **Context:**
  - Wery and Diliberto: OpenDyslexic reduced reading speed and accuracy against Arial and Times New Roman, and children preferred the mainstream fonts.
  - Kuster et al. on Dyslexie: "does not have the desired effect", with no accuracy or speed gains.
  - Three independent studies now point the same way, which is why this skill bans the fix.
- **Tags:** `[AVOID: dyslexia-specific fonts]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 6 dyslexia note

### X17 — Understanding SC 1.4.8: Visual Presentation
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html
- **Context:**
  - AAA level. Line width no more than 80 characters, or 40 for CJK.
  - Line spacing at least space-and-a-half within paragraphs. Paragraph spacing at least 1.5 times the line spacing.
  - "Text is not justified."
  - There is no AA-level numeric rule for line length, so a team targeting AA can legally ship 120-character lines.
- **Tags:** `[ADOPT: max-width 70ch on prose]` `[AVOID: justified body text]` `[CONTESTED]`
- **Feeds:** Part 6

### X18 — Federal Plain Language Guidelines
- **Source:** U.S. General Services Administration and PLAIN, guidelines Mar 2011, now hosted on Digital.gov. https://digital.gov/guides/plain-language
- **Context:**
  - Organise to serve the reader, with the most important information first.
  - Active voice, present tense, address the reader as "you", avoid hidden verbs.
  - "Active voice makes it clear who should do what. It eliminates ambiguity about responsibilities."
  - Fourth pillar is testing for understanding.
- **Tags:** `[ADOPT: active voice and present tense]` `[ADOPT: most important information first]`
- **Feeds:** docs guidance; CP6

### X19 — Clear and short
- **Source:** Digital.gov and PLAIN, plain language writing guide, current. https://digital.gov/guides/plain-language/writing/clear-short
- **Context:**
  - "Express only one idea in each sentence." "Limit each paragraph or section to one topic."
  - Paragraphs of no more than 150 words in three to eight sentences, and never longer than 250 words.
- **Tags:** `[ADOPT: one idea per sentence]` `[ADOPT: 150-word paragraph cap]`
- **Feeds:** docs guidance

### X20 — Sentence length: why 25 words is our limit
- **Source:** Sara Vincent, GDS, Inside GOV.UK, 4 Aug 2014. https://insidegovuk.blog.gov.uk/2014/08/04/sentence-length-why-25-words-is-our-limit/
- **Context:**
  - GOV.UK's hard limit is 25 words per sentence.
  - Cited comprehension research: at 14 words readers understand more than 90%, at 43 words comprehension drops below 10%.
  - This is the rule the skill's own copy checker enforces on its documentation.
- **Tags:** `[ADOPT: sentences under 25 words]` `[EVIDENCE-ONLY]`
- **Feeds:** docs guidance; this file's own style rules

### X21 — Writing for GOV.UK
- **Source:** GDS, content design guidance, ongoing. https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/
- **Context:**
  - Standing house guidance on tone, structure and word choice for public-facing content.
  - Pairs with X22 on reading age.
- **Tags:** `[ADOPT: GOV.UK writing standards]`
- **Feeds:** docs guidance

### X22 — Readability, Home Office User-Centred Design Manual
- **Source:** UK Home Office, guidance, current. https://design.homeoffice.gov.uk/accessibility/written-content/readability
- **Context:**
  - "Usually we recommend writing for a maximum reading age of 9, even if you are writing for a specialist audience."
  - "Simple language doesn't mean dumbing down."
  - Barriers named: learning disabilities, cognitive issues, lower reading ability, English as a second language.
  - Tools named: Hemingway Editor and Word's Flesch-Kincaid checker.
- **Tags:** `[ADOPT: reading age 9 target]` `[CONTESTED]`
- **Feeds:** Part 6 readability line; docs guidance

### X23 — Error-Message Guidelines
- **Source:** Tim Neusesser and Evan Sunwall, Nielsen Norman Group, 14 May 2023. https://www.nngroup.com/articles/error-message-guidelines/
- **Context:**
  - Avoid technical jargon and use language familiar to users. "An error occurred" lacks context.
  - Offer solutions, not just problems. Never phrase errors so they blame the user.
  - Preserve the user's input so people can fix rather than retype.
- **Tags:** `[ADOPT: error messages that say what happened and what to do]` `[AVOID: generic error text]`
- **Feeds:** JD2; SurveyJS error-text rules; docs guidance

### X24 — The Inverted Pyramid: Writing for Comprehension
- **Source:** Amy Schade, Nielsen Norman Group, 11 Feb 2018. https://www.nngroup.com/articles/inverted-pyramid/
- **Context:**
  - Put the most important information, or the conclusion, first.
  - "Readers can stop reading at any point on the page and still come away with the main point."
  - This is the source of the TL;DR-first pattern in the skill's doc template.
- **Tags:** `[ADOPT: TL;DR first]`
- **Feeds:** docs guidance

### X25 — Inclusive Design for Cognition Guidebook
- **Source:** Microsoft Inclusive Design, guidebook, 2023. https://inclusive.microsoft.design/tools-and-activities/InclusiveDesignForCognitionGuidebook.pdf
- **Context:**
  - "For any task to be successful, motivation must equal or surpass cognitive load."
  - Designs for five demands: learning, focus, decision-making, recall, communication.
  - "Solve for one, extend to many." Recommends co-creating with cognitive diversity.
  - Practical reading: every extra decision, tab or cross-reference in a document is load. Cut it or default it.
- **Tags:** `[ADOPT: cut every avoidable decision]` `[EVIDENCE-ONLY]`
- **Feeds:** docs guidance; JD3

### X26 — Designing for users with anxiety
- **Source:** UK Home Office, poster, 2016 onward. https://ukhomeoffice.github.io/accessibility-posters/anxiety
- **Context:**
  - Give users enough time. Explain what will happen after completing a service.
  - Do not make support or help hard to access.
  - Let users check their answers before they submit them.
  - This is the source of the "You'll see" confirmation line in the skill's setup-guide template.
- **Tags:** `[ADOPT: state what happens after each step]` `[AVOID: rushing users]`
- **Feeds:** docs guidance; CP3

### X27 — Designing for users with dyslexia
- **Source:** UK Home Office, poster, 2016 onward. https://ukhomeoffice.github.io/accessibility-posters/dyslexia
- **Context:**
  - "Don't force users to remember things from previous pages. Give reminders and prompts."
  - Use images and diagrams to support text. Do not rely on accurate spelling from the user.
  - Mirrors WCAG 3.3.7 Redundant Entry at the content level.
- **Tags:** `[ADOPT: restate values instead of referring back]`
- **Feeds:** docs guidance; Part 6

### X28 — COGA Content Usable, Objectives 4 to 7
- **Source:** W3C, Working Group Note, 29 Apr 2021. https://www.w3.org/TR/coga-usable/
- **Context:**
  - The documentation-facing half of X8: Make Each Step Clear, Break Media into Chunks, Use White Spacing, Provide Help and Support.
  - Objective 6, ensure processes do not rely on memory, is the doc-level version of Redundant Entry.
  - Still a Note, so it carries no conformance requirement.
- **Tags:** `[ADOPT: numbered one-action steps]` `[EVIDENCE-ONLY]`
- **Feeds:** docs guidance

### X29 — Plain Writing Act of 2010
- **Source:** U.S. Congress, statute, 2010, via Digital.gov principles page. https://digital.gov/guides/plain-language/principles
- **Context:**
  - The statutory basis for plain-language writing in U.S. federal agencies.
  - Requires writing appropriate to the audience, which in practice means testing with real readers.
- **Tags:** `[ADOPT: test docs with real readers]`
- **Feeds:** docs guidance

---

# R. Prior art

### R1 — ux-skill
- **Source:** Laith0003, GitHub, deterministic linter plus design engine plus MCP server, MIT, active 2026 v3.0. https://github.com/Laith0003/ux-skill
- **Context:**
  - 152 regex rules across nine categories: accessibility 23, content 15, layout 13, typography 10, colour 9, quality 9, visual 9, motion 8, performance 4.
  - Python regex scanner reading rules from `data/anti-patterns.json`, offline, deterministic, around 200ms per project.
  - Non-zero exit on Critical or High findings, so it works in CI.
  - Ships 160 brand DESIGN.md specs, 176 palettes, 70 type pairings and 57 motion presets as JSON.
  - Weakness: regex on source cannot see rendered output, and adoption is tiny at around 63 stars.
- **Tags:** `[ADOPT: JSON rule format with evidence template]` `[ADOPT: CI exit-code convention]` `[EVIDENCE-ONLY]`
- **Feeds:** scripts/rules.json; scripts/ai_tell_scan.py

### R2 — unslop-ui-skill
- **Source:** claudiusararu, GitHub, agent skill plus tells catalog, MIT, active 2026. https://github.com/claudiusararu/unslop-ui-skill
- **Context:**
  - TELLS.md documents around 100 recurring tells with rationales, and a self-check list.
  - Sample entries: cream background `#faf8f4`, pill eyebrow badges above heroes, three lucide icons in rounded squares, fade-up on every element.
  - Pure constraint prose. No scoring and no code, so enforcement depends on the model re-reading the checklist.
  - Also catalogued as C20.
- **Tags:** `[ADOPT: TELLS.md as a rule seed list]` `[AVOID: self-check as the only enforcement]`
- **Feeds:** the whole tells register; scripts/rules.json

### R3 — impeccable
- **Source:** pbakaus, GitHub agent skill and design language, open source, active 2026. https://github.com/pbakaus/impeccable
- **Context:**
  - Thirteen absolute refusals. First six: side-stripe borders, gradient text, glassmorphism as default, hero-metric template, eyebrow on every section, 01/02/03 numbered markers.
  - Remaining seven: ghost cards, card radius of 24px or more, hand-drawn SVG, repeating-linear-gradient stripes, and "not just X, it's Y" copy.
  - Numeric rules a scanner can lift: contrast 4.5:1 body and 3:1 large, line length 65 to 75ch, type scale ratio 1.25 or more.
  - Also three font families maximum, display clamp 6rem or less, letter-spacing at or above -0.04em.
  - Tinted neutrals limited to 0.005 to 0.015 OKLCH chroma toward the brand hue. Z-index from a named scale, never 999 or 9999.
  - Introduces the two-altitude test, which no linter can replicate.
- **Tags:** `[AVOID: the thirteen banned patterns]` `[ADOPT: numeric thresholds]` `[ADOPT: two-altitude test]`
- **Feeds:** CO2, LA6, LA8, LA9, TY5, CP2, JD5; scripts/rules.json

### R4 — Anthropic frontend-design skill
- **Source:** Anthropic, official agent skill, active 2026. https://github.com/anthropics/skills
- **Context:**
  - Names three clustered AI default looks. One: warm cream near `#F4F1EA` with a serif display and a terracotta accent.
  - Two: near-black with a single acid green or vermilion accent. Three: broadsheet layout, hairline rules, zero radius, dense columns.
  - Key line: "All three are legitimate for some briefs, but they are defaults rather than choices, and they appear regardless of subject."
  - This is the primary evidence that the escapes from the purple era became tells themselves.
  - Rules: four to six named hex values tied to the subject, deliberate display and body pairing, "structure is information", restrained motion.
  - Weakness: guidance only, and the published evidence is before and after screenshots.
- **Tags:** `[AVOID: cream plus serif plus terracotta as a default]` `[AVOID: near-black plus single acid accent]` `[ADOPT: four to six named hexes tied to the subject]` `[STALE-RISK]`
- **Feeds:** CO6; Part 0 finding 3; "Contested and stale"

### R5 — avoid-ai-design
- **Source:** funboy322, GitHub agent skill, MIT, active 2026. https://github.com/funboy322/avoid-ai-design
- **Context:**
  - Six tell categories with P0, P1 and P2 severity. P0 screams AI, P1 is an obvious smell, P2 is cosmetic.
  - Named entries: untouched zinc and slate palettes, `rounded-2xl shadow-lg`, hero plus three cards plus CTA.
  - Also three-tier pricing with a highlighted middle ring, four-column footers, uniform `gap-4` and `p-6`, DiceBear avatars, Lucide Sparkles and ArrowRight.
  - Five-step workflow: scope, audit, commit to one aesthetic direction, calibrated rewrite, re-audit until P0 is clear.
  - Calibration rule worth copying: surgical rewrites for components, bold rewrites for standalone pages.
- **Tags:** `[ADOPT: P0/P1/P2 severity triage]` `[ADOPT: commit to one direction before rewriting]` `[AVOID: DiceBear avatars]`
- **Feeds:** IC1, IC5, LA13; the audit workflow

### R6 — open-design anti-ai-slop.md
- **Source:** nexu-io, GitHub rules file, open, active 2026. https://github.com/nexu-io/open-design/blob/main/craft/anti-ai-slop.md
- **Context:**
  - The only source with an exact hex banlist: `#6366f1 #4f46e5 #4338ca #3730a3 #8b5cf6 #7c3aed #a855f7`.
  - Banned emoji as icons in headings, buttons and lists: sparkles, rocket, target, lightning, fire, bulb.
  - Banned two-stop hero gradients: purple to blue, blue to cyan, indigo to pink.
  - P1 numeric thresholds: more than 12 raw hex values outside `:root`, accent variable used six or more times per screen against a cap of two.
  - Also bans invented metrics without a source, and placeholder CDNs such as unsplash.com and placehold.co.
- **Tags:** `[AVOID: the seven banned indigo and violet hexes]` `[AVOID: emoji as icons]` `[ADOPT: raw-hex and accent-use thresholds]` `[STALE-RISK]`
- **Feeds:** CO1, IC2, IC5, CP3; scripts/rules.json

### R7 — design-deslop command
- **Source:** Dammyjay93, interface-design repo, agent slash command, open, active 2026. https://github.com/Dammyjay93/interface-design/blob/main/.claude/commands/design-deslop.md
- **Context:**
  - Splits the work by what needs rendering and what a diff can catch, which is the split any scanner must make.
  - Pass 1 rendered squint test: no focal point, flat hierarchy, monotone layout, timid colour, borders used as structure. Fix for timid colour is one accent at around 10% coverage.
  - Pass 2 source scan looks for: semantic tokens over generic names.
  - Also: missing hover, focus, active and disabled states.
  - Also: transitions without explicit properties, off-grid spacing, negative-margin hacks, hand-rolled controls.
  - The only prior art with an allowlist: patterns ratified in a project `system.md` are exempt.
- **Tags:** `[ADOPT: two-pass rendered plus diff review]` `[ADOPT: project allowlist for ratified patterns]` `[ADOPT: one accent at 10% coverage]`
- **Feeds:** scanner architecture; JD2

### R8 — design-anti-slop
- **Source:** prathameshagrawal, GitHub agent skill, MIT, active 2026. https://github.com/prathameshagrawal/design-anti-slop
- **Context:**
  - 25 named anti-patterns with stable IDs across three layers: visual V1 to V9, structural S1 to S9, conceptual C1 to C7.
  - The structural layer is its distinct contribution: canonical hero, three-box grid, logo carousel, bento grid, dashboard sidebar, KPI card row.
  - Framing: "AI design slop is a statistical problem, not an aesthetic one." It asks four questions before any code is written.
  - Pre-generation and post-generation modes are separated.
- **Tags:** `[ADOPT: stable rule IDs]` `[ADOPT: pre-generation interrogation]` `[EVIDENCE-ONLY]`
- **Feeds:** the register's ID scheme; JD5

### R9 — projectwallace/css-analyzer
- **Source:** Project Wallace, CSS analytics library, TypeScript, MIT, v9.9.0. https://github.com/projectwallace/css-analyzer
- **Context:**
  - Over 150 metrics: unique colours, font families, font sizes, z-indexes, shadows, specificity, complexity, uniqueness ratios.
  - Defines exactly which aggregate signals a slop scanner needs.
  - Sibling repos: `css-code-quality` for a weighted quality score, `css-design-tokens`, `wallace-cli`.
  - JavaScript only, so it is a reference implementation to mirror in Python rather than a dependency.
- **Tags:** `[ADOPT: the css-analyzer metric set]` `[AVOID: adding a Node toolchain as a runtime dependency]`
- **Feeds:** LA10 uniqueness counts; scripts/ai_tell_scan.py

### R10 — axe-core
- **Source:** Deque, accessibility rules engine, JavaScript, MPL-2.0, very active. https://github.com/dequelabs/axe-core
- **Context:**
  - Covers WCAG 2.0, 2.1 and 2.2 at A, AA and AAA plus best practices.
  - Around 57% of WCAG issues are automatable, so it cannot be the whole gate.
  - Its colour-contrast rule does not work under JSDOM. It needs a real browser render.
  - Consequence for this skill: compute contrast from parsed colours instead of shipping a browser.
- **Tags:** `[ADOPT: axe-core as the a11y baseline]` `[AVOID: axe-core in-process for contrast]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 6; scanner architecture

### R11 — wcag-contrast
- **Source:** tmcw, colour-contrast micro-library, JavaScript, BSD-2-Clause, mature. https://github.com/tmcw/wcag-contrast
- **Context:**
  - Four functions: luminance, rgb, hex and score.
  - The author himself flags the limits of WCAG ratios and points to Lighthouse and axe for page-level testing.
  - The WCAG relative-luminance formula is about 15 lines of standard-library Python, so it needs no dependency.
- **Tags:** `[ADOPT: hand-ported WCAG contrast maths]`
- **Feeds:** Part 6; scripts/ai_tell_scan.py

### R12 — tinycss2
- **Source:** CSS parser, Python 3.10 or later, no dependencies, BSD-3-Clause, v1.5.1 Nov 2025. https://pypi.org/project/tinycss2/
- **Context:**
  - CSS Syntax Level 3 tokeniser and block parser. No selector or property semantics.
  - Sufficient for extracting declarations, hex and oklch values, font stacks and gradients.
  - It will not resolve `var()`, which matters because modern generated code hides colour behind tokens.
- **Tags:** `[ADOPT: tinycss2 if regex extraction proves brittle]` `[CONTESTED]`
- **Feeds:** scripts/ai_tell_scan.py

### R13 — textstat
- **Source:** Readability metrics library, Python, MIT, v0.7.13 Feb 2026. https://pypi.org/project/textstat/
- **Context:**
  - Computes Flesch, Flesch-Kincaid grade, SMOG, Coleman-Liau, ARI, Dale-Chall and Gunning Fog.
  - Useful for the reading-age target in Part 6.
  - Grade-level uniformity is only a weak AI-copy signal, and a plain buzzword list usually does more work.
- **Tags:** `[ADOPT: textstat for the reading-age gate]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 6 readability; docs guidance

### R14 — Bolt 10 prompt keywords
- **Source:** Bolt, vendor prompting guide, article, 2025. https://bolt.new/blog/10-prompt-keywords-to-make-your-app-look-fire
- **Context:**
  - Named aesthetic keywords as one-word levers: neumorphism, glassmorphism, brutalism, claymorphism, retro, vaporwave, hyper-minimalism.
  - Thesis: precision of language beats asking for a "clean UI".
  - Caveat: a named style used alone is itself a cliche. It needs further specification.
- **Tags:** `[ADOPT: named aesthetic as a lever]` `[CONTESTED]`
- **Feeds:** templates/ direction file

### R15 — Vercel: How to prompt v0
- **Source:** Vercel, official vendor guide, article, 2025. https://vercel.com/blog/how-to-prompt-v0
- **Context:**
  - Three-part framework: product surface with exact components and data, context of use, constraints and taste.
  - "Constraints tell v0 what not to invent."
  - Reports 19 seconds faster generation and 152 fewer lines of code in their worked example.
  - That is a single example, not a study.
- **Tags:** `[ADOPT: specify surface, context and constraints]` `[EVIDENCE-ONLY]`
- **Feeds:** templates/ direction file

### R16 — Lovable prompting docs
- **Source:** Lovable, official docs, active. https://docs.lovable.dev/prompting/prompting-one
- **Context:**
  - Structure: context, task, guidelines, constraints. Build modularly per component.
  - Knowledge files hold recurring design direction, so Lovable applies it without restating.
  - Use real content, not placeholders. Use atomic UI vocabulary: cards, badges, modals.
  - Maps vague words to concrete treatments, for example "premium and cinematic" becomes layered depth and dramatic contrast.
- **Tags:** `[ADOPT: persistent knowledge file]` `[ADOPT: real content over placeholders]`
- **Feeds:** templates/ direction file; IC5

### R17 — DESIGN.md format guide for Google Stitch
- **Source:** designmd.app, format guide, 2026, open format. https://designmd.app/guides/google-stitch/
- **Context:**
  - Sections: colours as hex, type scale, spacing scale, component patterns with concrete values, and an explicit do and don't constraints section.
  - Portable across Stitch, Claude Code, Cursor, Kiro and Windsurf. Keep it in git.
  - Stitch does not watch the file, so it must be re-imported after edits.
  - This is the emerging interchange format, so the skill should emit and consume it rather than invent one.
- **Tags:** `[ADOPT: DESIGN.md as the interchange format]` `[ADOPT: concrete values over adjectives]`
- **Feeds:** templates/ direction file

### R18 — Why Your AI Keeps Building the Same Purple Gradient Website
- **Source:** prg.sh, analysis article with experiments, 2025 to 2026. https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website
- **Context:**
  - Root cause: Tailwind's `bg-indigo-500` default from around 2019 saturated tutorials, then training data.
  - "You're getting the median of every Tailwind CSS tutorial scraped from GitHub."
  - Six fixes tested side by side on three UI types across Claude, GPT-5, Gemini and v0.
  - Constrained versions were visibly more distinctive. Claude responded best to strong constraints.
  - Same article as P10.
- **Tags:** `[ADOPT: explicit negative constraints]` `[ADOPT: reference extraction then feed]` `[EVIDENCE-ONLY]`
- **Feeds:** CO1; templates/ direction file

### R19 — AIMultiple AI image detector benchmark
- **Source:** AIMultiple, detector benchmark article, 2026. https://aimultiple.com/ai-image-detector
- **Context:**
  - Seven detectors benchmarked, including SightEngine, Hive and Illuminarty.
  - "Most perform no better than a coin toss", with systematic false negatives and inconsistent confidence.
  - All test material was photorealistic. None was evaluated on rendered UI.
  - Rendered UI has flat fills, crisp vector type and exact geometry, which violates the camera-noise assumptions these models rely on.
  - Conclusion adopted here: detect design patterns in code and copy, not pixels.
- **Tags:** `[AVOID: screenshot-level AI detection]` `[EVIDENCE-ONLY]`
- **Feeds:** Part 0 finding 5; IC6

### R20 — Improving frontend design through Skills
- **Source:** Anthropic, vendor evidence post, 2025 to 2026. https://claude.com/blog/improving-frontend-design-through-skills
- **Context:**
  - Coins "distributional convergence" for the phenomenon this skill addresses.
  - Offers before and after comparisons for a landing page, a blog and a dashboard.
  - The evidence is qualitative screenshots, not benchmarks. Cite it with that caveat.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** Part 0; skill positioning

---

# V. Visual science

### V1 — Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500)
- **Source:** Alan West, DEV Community, practitioner blog, around 2025. https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p
- **Context:**
  - Names the median: `bg-indigo-500`, `from-indigo-500 to-purple-600`, Inter, three-column feature grids.
  - Describes the feedback loop: "The AI trained on AI output. The distribution shifted further toward indigo."
  - Same article as P6 and K14, read here for the colour claim specifically.
- **Tags:** `[AVOID: indigo-500 default accent]` `[STALE-RISK]`
- **Feeds:** CO1, LA2

### V2 — Why does AI keep making everything blue-purple?
- **Source:** chaiovercode, Substack essay, around 2025. https://chaiovercode.substack.com/p/why-does-ai-make-everything-blue
- **Context:**
  - Root-causes the violet skew to Tailwind's 2020 indigo-500 default flooding tutorials and scraped code.
  - "AI conflates frequency with optimality."
  - Notes indigo was a defensible deliberate Tailwind choice. The problem is repetition, not the hue.
- **Tags:** `[CONTESTED]` `[AVOID: frequency as a proxy for quality]`
- **Feeds:** CO1; Part 5

### V3 — The rise of Linear style design
- **Source:** Arlene Xu, Medium Design Bootcamp, design essay, around 2023. https://medium.com/design-bootcamp/the-rise-of-linear-style-design-origins-trends-and-techniques-4fd96aab7646
- **Context:**
  - Documents the Linear.app aesthetic: dark background, animated glow gradients, blur, Inter, grey on black.
  - Records that some people jokingly renamed "dark mode" as "linear style".
  - Records the functional origin: Linear's founder chose dark UI for engineer familiarity, eye strain and battery.
  - The style is not inherently slop. Its reflexive copying is.
- **Tags:** `[CONTESTED]` `[AVOID: reflexive Linear-style dark hero]`
- **Feeds:** CO4, CO5

### V4 — Spot the Slop: A UI Designer's Guide to Fixing AI Defaults
- **Source:** Kosta C., Mania Design, practitioner guide, 2025 to 2026. https://www.mania.design/blog/spot-the-slop-a-ui-designers-guide-to-fixing-ai-defaults/
- **Context:**
  - Seven named defaults with per-pattern fixes: Inter, purple to blue gradient, uniform 16px radius and 24px padding, missing edge states, uniform fade-ins.
  - "Real hierarchy comes from intentional variation. When everything is shouting at the same volume, nothing is."
  - "It's decoration standing in for a color system."
  - Names the motion test: animate only to communicate state change, direct attention, or carry character.
  - Says edge cases are where trust is built or broken.
- **Tags:** `[AVOID: uniform radius and padding]` `[AVOID: uniform fade-ins]` `[ADOPT: intentional variation for hierarchy]` `[ADOPT: state, attention or character test for motion]`
- **Feeds:** LA10, MO1, MO5, JD2

### V5 — Slop (pattern catalogue)
- **Source:** Impeccable, impeccable.style, pattern catalogue, 2026. https://impeccable.style/slop/
- **Context:**
  - The largest itemised catalogue of generated-UI signatures found anywhere in this research.
  - Named here: purple and cyan on dark, glass cards, gradient text, icon-tile feature cards, hero eyebrow pills, image hover scale, pulsing dots, marquees, bounce easing.
  - "A small rounded-square icon container above a heading is the universal AI feature-card template."
  - "Continuous auto-scroll demands attention and hides content."
  - "Big number, small label, three supporting stats, gradient accent. Used everywhere, trusted nowhere."
  - Same catalogue as P16.
- **Tags:** `[AVOID: icon tile above heading]` `[AVOID: marquee]` `[AVOID: hero metric row]` `[AVOID: pulsing dots]`
- **Feeds:** CO2, CO4, CO6, LA3, LA6, MO3, MO4, MO6

### V6 — AI Slop Web Design: Complete Guide 2026
- **Source:** 925 Studios, agency guide, 2026. https://www.925studios.co/blog/ai-slop-web-design-guide
- **Context:**
  - Ties the tells together: Inter, purple to blue gradients, impossibly lit stock photos, 16px-radius card grids, generic fade-ins.
  - "A diverse group of people looking at a laptop in an impossibly well-lit office."
  - Says AI illustrations feel "slightly too smooth, slightly too symmetrical".
  - Cites numbers with weaker provenance. 38% of visitors leave over poor design.
  - 40% to 62% of AI-generated code contains flaws. 1.7 times more issues in AI codebases. Treat as directional.
- **Tags:** `[AVOID: impossibly lit stock imagery]` `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** IC6, LA10, MO1

### V7 — Low-Contrast Text Is Not the Answer
- **Source:** Katie Sherwin, Nielsen Norman Group, research-backed article, 7 Jun 2015. https://www.nngroup.com/articles/low-contrast/
- **Context:**
  - Low-contrast grey text harms legibility, discoverability and trust.
  - "Low-contrast text does look minimal, the same way a blurred photo on Instagram can look retro. But you wouldn't blur your website."
  - "People are less trusting of text that is hard to read."
  - Fix density, size and position instead of dropping contrast.
- **Tags:** `[AVOID: low-contrast grey body text]` `[ADOPT: 4.5:1 floor]`
- **Feeds:** CO8; Part 6

### V8 — AI-Generated Images Can Perform as Well as Stock Photography
- **Source:** Rachel Banawa, Nielsen Norman Group, quantitative user study with 77 participants, 21 Aug 2026. https://www.nngroup.com/articles/ai-generated-images/
- **Context:**
  - With origin undisclosed, AI hero images scored 0.2 to 0.4 points higher than real stock on a seven-point scale.
  - Measures were trust, professionalism and authenticity. The authenticity difference was statistically significant, favouring AI.
  - Participants commented on representation and team dynamics, not on artefacts.
  - Ten-second exposures across six page variants.
  - This is the strongest counter-evidence to "AI imagery is a visible tell".
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]` `[ADOPT: judge images on normal design criteria]`
- **Feeds:** IC6; "Contested and stale"

### V9 — Chroma Clues: Leveraging Color Statistics to Detect Synthetic Images
- **Source:** arXiv 2606.02224, peer-track CS paper, 2026. https://arxiv.org/html/2606.02224
- **Context:**
  - AI images carry measurable chrominance anomalies: saturation-channel fingerprints and cross-channel correlations.
  - 93.27% average detection accuracy across generators, and 99.4% for Stable Diffusion against COCO.
  - Explains the mechanism: perceptual metrics are around four times less sensitive to chrominance than luminance, so generators drift on colour.
  - Machine detection of imagery still works even as human detection fails.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** IC6; "Contested and stale"

### V10 — Crafting Synthetic Realities
- **Source:** arXiv 2409.17484, content-analysis study, 2024. https://arxiv.org/html/2409.17484v2
- **Context:**
  - Quantifies the AI look in photorealistic images: 92% or more rated high quality, 93% to 98% vividly coloured.
  - Around 68% contain humans, 73% of those have identifiable faces, and 58% to 61% contain surreal combinations.
  - Only 8% show detectable production flaws. Of those, 84% are anatomical, 24% to 63% functional, 13% to 27% physics violations.
  - So flaw-spotting is now a weak detector.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** IC6

### V11 — Corporate Memphis
- **Source:** Wikipedia, encyclopedic and sourced, current. https://en.wikipedia.org/wiki/Corporate_Memphis
- **Context:**
  - Documents the flat big-tech illustration style from Facebook's 2017 Alegria work by agency Buck.
  - Disproportionate limbs, small heads, flat bright fills.
  - Critics called it lazy, citing simple shapes and untextured colours.
  - Also records defenders granting it art-historical legitimacy through the Memphis Group lineage.
  - Same entry as C15.
- **Tags:** `[AVOID: flat elastic-limb vector people]` `[CONTESTED]`
- **Feeds:** IC7

### V12 — Why do AI company logos look like buttholes?
- **Source:** VelvetShark, practitioner essay, around 2024. https://velvetshark.com/ai-company-logos-that-look-like-buttholes
- **Context:**
  - Surveys around eight to ten AI-company logos converging on circular or radial gradient orbs.
  - Drivers named: circle symbolism, copycat legitimacy, design by committee.
  - "There's tremendous pressure to look legitimate by conforming to established visual language."
  - Concedes circles carry real meaning, and names DeepSeek and Midjourney as viable outliers.
- **Tags:** `[AVOID: gradient-orb logo reflex]` `[CONTESTED]`
- **Feeds:** IC6, JD5

### V13 — The Proliferation and Problem of the Sparkles Icon
- **Source:** Kate Kaplan, Nielsen Norman Group, quantitative icon study with 107 participants, 20 Sep 2024. https://www.nngroup.com/articles/ai-sparkles-icon-problem/
- **Context:**
  - Zero participants attributed "artificial intelligence" to the sparkles icon.
  - 11.22% read it as important or special. 16.82% read it as favourite or save. 16.82% read it as visual effects.
  - 73% associate plain stars with favouriting, so the two glyphs collide.
  - Recommends pairing sparkles with a text label or tooltip.
- **Tags:** `[CONTESTED]` `[ADOPT: label every sparkle]` `[EVIDENCE-ONLY]`
- **Feeds:** IC3

### V14 — Rise of the AI Sparkle Icon
- **Source:** Pozos and Schmidt, Google Design, corporate research with 2,000 participants across eight countries, 2024. https://design.google/library/ai-sparkle-icon-research-pozos-schmidt
- **Context:**
  - Directly conflicts with V13. Inside Google product contexts, users did recognise the sparkle as AI.
  - One sparkle was enough. Combined icons, for example microphone plus sparkle, outperformed plain ones.
  - Around 100 Google system icons carried sparkles by 2024.
  - Reconciliation: recognition is ecosystem-dependent. Both studies agree labels help.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** IC3; "Contested and stale"

### V15 — You Don't Need Animations
- **Source:** Emil Kowalski, practitioner authority essay, 2025. https://emilkowal.ski/ui/you-dont-need-animations
- **Context:**
  - Animation appropriateness is a function of frequency. Never animate keyboard-driven actions.
  - UI animation should stay under 300ms.
  - "Sometimes the best animation is no animation."
- **Tags:** `[ADOPT: under 300ms for UI animation]` `[AVOID: animating high-frequency actions]`
- **Feeds:** MO1, MO2, MO6; every L motion entry

### V16 — Web Interface Guidelines
- **Source:** Rauno Freiberg, practitioner authority checklist, current. https://interfaces.rauno.me/
- **Context:**
  - Interaction animations should be 200ms or less.
  - No extraneous animation on frequent low-novelty actions.
  - Scale from around 0.96, never 0.8.
  - Pause offscreen loops and honour reduced motion.
- **Tags:** `[ADOPT: 200ms interaction ceiling]` `[ADOPT: pause offscreen loops]` `[AVOID: large hover scale]`
- **Feeds:** MO2, MO3, MO5

### V17 — Motion (Human Interface Guidelines)
- **Source:** Apple, platform guideline, current. https://developer.apple.com/design/human-interface-guidelines/motion
- **Context:**
  - "Don't add motion for the sake of adding motion."
  - "Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable."
  - Make motion optional.
- **Tags:** `[AVOID: motion without purpose]` `[ADOPT: motion as an option, not a default]`
- **Feeds:** MO1, MO4, MO5

### V18 — Duration and Easing
- **Source:** Google Material Design, platform guideline, current. https://m1.material.io/motion/duration-easing.html
- **Context:**
  - Numeric envelope: mobile 300ms standard, 225ms enter and 195ms exit, 400ms hard ceiling.
  - Desktop 150ms to 200ms. Tablet plus 30%, wearables minus 30%.
  - Easing should be asymmetric. Linear motion reads mechanical.
- **Tags:** `[ADOPT: the Material duration envelope]` `[ADOPT: asymmetric easing]`
- **Feeds:** MO6; every L motion entry

### V19 — Scroll-Triggered Text Animations Delay Users
- **Source:** Aurora Harley, Nielsen Norman Group, usability study article, 16 Apr 2017. https://www.nngroup.com/articles/scroll-animations/
- **Context:**
  - Scroll-reveal on body content delays reading and frustrates task-focused users.
  - Study participant: "I don't like how everything comes together when I'm scrolling down."
  - "Task-focused users don't want to be wowed by a website. They want to get answers."
  - Scoped exception: leisure or browsing sites, secondary content only, first scroll only.
- **Tags:** `[AVOID: scroll reveal on body content]` `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** MO1; Lenis and GSAP entries in L

### V20 — Interrogating Design Homogenization in Web Vibe Coding
- **Source:** arXiv 2603.13036, sociotechnical analysis, 2026. https://arxiv.org/html/2603.13036v1
- **Context:**
  - Frames homogenisation across ChatGPT Canvas, Gemini Canvas, Claude Artifacts, Lovable, v0 and Replit.
  - Western minimalist defaults override regional norms, evidenced by the Japanese retail case.
  - Proposes "productive friction": reflective prompting, mood-board negotiation before generation, design-system ingestion, provenance-tagged style adapters.
  - No numeric similarity metric is computed, so the strongest claims stay qualitative.
  - Same paper as A2 and P22.
- **Tags:** `[ADOPT: productive friction before generating]` `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** JD1, JD4; templates/ direction file

---

# L. Library documentation

Nine libraries are installed and ported into this skill. Every URL below was read on 2026-09-04. One rule governs all of them. A library earns its place when it lets the page show the real product. It fails when it decorates a page that has nothing to show.

## GSAP (L1 to L6)

### L1 — greensock/gsap-skills
- **Source:** GreenSock, official agent skills repo, MIT, 2026. https://github.com/greensock/gsap-skills
- **Context:**
  - Eight skills: gsap-core, gsap-timeline, gsap-scrolltrigger, gsap-plugins, gsap-utils, gsap-react, gsap-performance, gsap-frameworks.
  - Documents `gsap.matchMedia()` with a `reduceMotion` condition as the official reduced-motion pattern, with automatic revert.
  - Documents `SplitText` `aria: "auto"` as the safe default. Splitting text without aria handling destroys a heading's accessible name.
  - House defaults: duration 0.5s, ease `power1.out`, recommended `gsap.defaults({ duration: 0.6, ease: "power2.out" })`.
  - Warns against shipping `markers: true` or GSDevTools.
  - The MIT licence here covers the documentation, not the engine.
- **Tags:** `[ADOPT: gsap.matchMedia for reduced motion]` `[ADOPT: SplitText aria auto]` `[AVOID: shipped markers and GSDevTools]` `[CONTESTED]`
- **Feeds:** MO5; libraries/motion.md; library_misuse rules

### L2 — GSAP v3 Installation docs
- **Source:** GreenSock, official docs, v3.15. https://gsap.com/docs/v3/Installation
- **Context:**
  - Confirms version 3.15 and the install path `npm install gsap` plus optional `@gsap/react`.
  - Since the Webflow acquisition every plugin is free, including formerly Club-only SplitText and MorphSVG.
  - Agents must not generate an `.npmrc` with a GreenSock auth token. Those instructions are outdated.
- **Tags:** `[ADOPT: plain npm install, no auth token]` `[STALE-RISK]`
- **Feeds:** libraries/motion.md

### L3 — GSAP Standard License
- **Source:** Webflow and GreenSock, licence page. https://gsap.com/standard-license
- **Context:**
  - GSAP is not MIT. The npm licence field points at this proprietary Webflow licence.
  - Free including commercial use: "Commercial usage is covered under the standard license."
  - Carries a Prohibited Uses clause covering tools that compete with Webflow's visual animation building.
  - Correct the common claim wherever it appears.
- **Tags:** `[AVOID: claiming GSAP is MIT]` `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md licence facts

### L4 — npm registry entry for gsap
- **Source:** npm registry, package metadata. https://registry.npmjs.org/gsap/latest
- **Context:**
  - Verified version 3.15.0.
  - The `license` field reads literally: "Standard 'no charge' license: https://gsap.com/standard-license."
  - `@gsap/react@2.1.2` reads "SEE LICENSE AT https://gsap.com/standard-license".
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md

### L5 — cdnjs GSAP version API
- **Source:** cdnjs, version API. https://api.cdnjs.com/libraries/gsap?fields=version
- **Context:**
  - Second independent confirmation of version 3.15.0.
  - Used to cross-check the npm registry rather than trusting a single source.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md

### L6 — GSAP jsDelivr CDN builds
- **Source:** jsDelivr, CDN, verified HTTP 200. https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js and https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js
- **Context:**
  - The two exact script tags the skill may emit, pinned to an exact version.
  - Cost on the wire: 73 KB minified core plus 45 KB for ScrollTrigger.
  - That cost is the argument against using GSAP for a fade-in.
- **Tags:** `[ADOPT: exact version pinning]` `[AVOID: GSAP for simple fades]`
- **Feeds:** libraries/motion.md

## anime.js (L7 to L12)

### L7 — animejs.com
- **Source:** Julian Garnier, official homepage, v4.5.0. https://animejs.com
- **Context:**
  - Self-described as one animation engine for CSS properties, SVG, DOM attributes and plain JS objects.
  - Publishes per-module sizes: 24.50 KB total, Timer 5.60, Animation 5.20, Draggable 6.41, Scroll 4.30, WAAPI 3.50.
  - The homepage's own hero demos use `loop: true` on rotate and scale, and a `stagger(200, { grid: [13, 13] })` dot field. Those demos are copy-paste bait for the decorative pulse and particle-field tells.
- **Tags:** `[ADOPT: modular subpath imports]` `[AVOID: copying the homepage demos]`
- **Feeds:** MO3, MO4; libraries/motion.md

### L8 — anime.js installation docs
- **Source:** Julian Garnier, official docs. https://animejs.com/documentation/getting-started/installation
- **Context:**
  - Install paths for ESM, CJS, esm.sh and the UMD bundle.
  - Modular subpath imports are the structural advantage: `animejs/animation`, `animejs/timeline`, `animejs/draggable`, `animejs/events`, `animejs/text`.
  - A project that only needs sequencing pays around 11 KB, not 117 KB.
- **Tags:** `[ADOPT: subpath imports for bundle discipline]`
- **Feeds:** libraries/motion.md

### L9 — anime.js scope mediaQueries docs
- **Source:** Julian Garnier, official docs. https://animejs.com/documentation/scope/scope-parameters/mediaqueries
- **Context:**
  - The documented reduced-motion mechanism: `createScope({ mediaQueries: { reduceMotion: '(prefers-reduced-motion)' } })`.
  - It is opt-in. anime.js ships no reduced-motion default.
  - `createScope({ root })` also gives scoped selectors and a one-call `revert()`, which solves React cleanup.
- **Tags:** `[ADOPT: createScope mediaQueries]` `[AVOID: assuming reduced motion is handled]`
- **Feeds:** MO5; libraries/motion.md

### L10 — npm registry entry for animejs
- **Source:** npm registry, package metadata. https://registry.npmjs.org/animejs/latest
- **Context:**
  - Verified version 4.5.0 and licence MIT. Genuinely permissive, unlike GSAP.
  - README footer confirms "Julian Garnier | MIT License".
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md licence facts

### L11 — anime.js v3 to v4 migration wiki
- **Source:** Julian Garnier, GitHub wiki. https://github.com/juliangarnier/anime/wiki/Migrating-from-v3-to-v4
- **Context:**
  - v4 is a total API rewrite. v3 code does not run on v4.
  - The docs site still hosts 3.2.2 and 2.1.0, which is how stale API names leak into generated code.
  - v3 API names appearing in a v4 project are a useful agent-hallucination signal.
- **Tags:** `[AVOID: v3 API names in a v4 project]` `[STALE-RISK]`
- **Feeds:** libraries/motion.md scanner signatures

### L12 — anime.js UMD bundle on jsDelivr
- **Source:** jsDelivr, CDN, path verified. https://cdn.jsdelivr.net/npm/animejs/dist/bundles/anime.umd.min.js
- **Context:**
  - The full UMD bundle is 118 KB minified, against 24.5 KB for modular ESM.
  - Use the UMD path only when there is no build step.
- **Tags:** `[AVOID: UMD bundle when a build step exists]`
- **Feeds:** libraries/motion.md

## animate.css (L13 to L16)

### L13 — animate.style
- **Source:** Daniel Eden, official site, v4.1.1. https://animate.style/
- **Context:**
  - Around 90 named keyframes plus utility classes. No JavaScript.
  - Categories: attention seekers, back, bouncing, fading, flippers, lightspeed, rotating, specials, zooming, sliding.
  - Its own best-practices page says entrances and exits should orientate the user and signal a state transition.
  - Its own docs say "Infinite animations should be avoided" and "Don't animate large elements" and "Don't animate root elements".
  - Custom builds require a git clone. They are not possible from node_modules.
- **Tags:** `[ADOPT: one-shot entrance tied to a state change]` `[AVOID: animate__infinite]` `[AVOID: animating root or full-bleed elements]` `[ADOPT: custom build]`
- **Feeds:** MO1, MO4, MO5; libraries/motion.md

### L14 — animate.css source file
- **Source:** animate-css GitHub, raw source, main branch. https://raw.githubusercontent.com/animate-css/animate.css/main/animate.css
- **Context:**
  - Version 4.1.1 verified in the file banner.
  - Ships a `prefers-reduced-motion` block, but it protects only `.animate__animated`.
  - Raw `@keyframes` usage silently opts out of that protection.
  - 95 KB raw for around 90 keyframes, which is the argument for a custom build.
- **Tags:** `[ADOPT: keep the shipped reduced-motion block]` `[AVOID: raw keyframes bypassing the guard]`
- **Feeds:** MO5; libraries/motion.md scanner signatures

### L15 — Hippocratic License 2.1
- **Source:** Organization for Ethical Source, licence text. http://firstdonoharm.dev
- **Context:**
  - animate.css's LICENSE file and CSS banner both name Hippocratic 2.1, even though the npm metadata says MIT.
  - HL 2.1 is not OSI-approved. It conditions the grant on human-rights compliance, requires indemnification and terminates on breach.
  - Many corporate open-source policies reject it, so flag it before shipping.
  - `react-leaflet` v5.0.0 carries the same licence, which is noted at L57.
- **Tags:** `[AVOID: trusting npm licence metadata]` `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md and libraries/maps-forms.md licence facts

### L16 — animate.css on cdnjs
- **Source:** cdnjs, CDN. https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
- **Context:**
  - The exact single link tag published in the official docs.
  - The zero-JS, zero-build option. For a static page it is the only viable choice in the motion set.
- **Tags:** `[ADOPT: single link tag for zero-build pages]`
- **Feeds:** libraries/motion.md

## animate-ui (L17 to L21)

### L17 — animate-ui.com
- **Source:** imskyleen, official docs site. https://animate-ui.com
- **Context:**
  - Not an npm library. It is a shadcn-style component distribution you copy into your own repo.
  - "Like shadcn/ui, Animate UI is not a typical install-from-NPM library."
  - Three kinds of item: animated primitives, components, and animated Lucide icons.
  - There is no published npm package to version-pin, so there is no upgrade path and no CVE channel.
- **Tags:** `[ADOPT: copy-first so you can fix the defaults]` `[AVOID: treating it as a versioned dependency]`
- **Feeds:** LA13; libraries/motion.md

### L18 — animate-ui registry index
- **Source:** imskyleen, registry manifest. https://animate-ui.com/r/registry.json
- **Context:**
  - 580 items: 1 index style, 81 primitives, 73 components, 260 icons, 5 hooks, 1 lib, 159 demos.
  - Every register tell ships here as a named, installable, one-line component.
  - `components-backgrounds-stars` ships `count = 1000` with `repeat: Infinity` and a 50 second linear loop.
  - `primitives-buttons-button` defaults to `hoverScale = 1.05` and `tapScale = 0.95`, so every installed button scales on hover.
  - `primitives-effects-slide` defaults to direction up, offset 100, `inView`, which is the fade-up-on-scroll tell verbatim.
  - The defensible half is the `radix-*`, `base-*` and `headless-*` groups, 41 primitives and 40 components, which keep upstream focus management and aria wiring.
- **Tags:** `[AVOID: the backgrounds group]` `[AVOID: effects particles, magnetic, tilt and shine]` `[AVOID: texts typing and shimmering]` `[ADOPT: radix, base and headless groups only]`
- **Feeds:** MO1, MO2, MO4; library_misuse rules

### L19 — animate-ui LICENSE
- **Source:** imskyleen, GitHub licence file, MIT. https://github.com/imskyleen/animate-ui/blob/main/LICENSE.md
- **Context:**
  - MIT, confirmed by the README badge and the License section.
  - The cleanest licence of the four motion libraries.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/motion.md licence facts

### L20 — shadcn registry schema
- **Source:** shadcn, JSON schema. https://ui.shadcn.com/schema/registry.json
- **Context:**
  - The schema animate-ui's registry declares. Item naming is `<kind>-<group>-<name>`.
  - Files land under `components/animate-ui/` in your own repo, which is why import-path regexes work as scanner signatures.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** library_misuse rules

### L21 — Motion React accessibility docs
- **Source:** Motion, official docs. https://motion.dev/docs/react-accessibility
- **Context:**
  - animate-ui ships no reduced-motion handling of its own. You must add it.
  - The required pattern is `<MotionConfig reducedMotion="user">` plus `useReducedMotion()`.
  - This is the single most important accessibility fact about animate-ui.
- **Tags:** `[ADOPT: MotionConfig reducedMotion user]` `[AVOID: shipping animate-ui without a motion gate]`
- **Feeds:** MO5; libraries/motion.md

## Lenis (L22 to L31)

### L22 — Lenis README
- **Source:** darkroom.engineering, GitHub README on main, v1.3.26, MIT. https://github.com/darkroomengineering/lenis/blob/main/README.md
- **Context:**
  - The README is the documentation. There is no separate docs site.
  - "Runs on native scroll", so sticky, anchor links and accessibility keep working.
  - Settings table gives the real defaults, including `lerp: 0.1` and `duration: 1.2`, and notes duration is useless if lerp is defined.
  - Limitations section: capped to 60fps on Safari and 30fps in low power mode, and smooth scroll stops over iframes.
  - Escape hatches for nested scroll: `data-lenis-prevent` and `allowNestedScroll: true`.
- **Tags:** `[AVOID: global smooth scroll on reading pages]` `[ADOPT: data-lenis-prevent on modals]` `[CONTESTED]`
- **Feeds:** MO1; library_misuse rules

### L23 — lenis/react README
- **Source:** darkroom.engineering, GitHub package README. https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md
- **Context:**
  - React bindings: the `<ReactLenis>` provider and the `useLenis` hook.
  - Needed when Lenis is genuinely justified inside a React tree.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L24 — lenis.ts core source
- **Source:** darkroom.engineering, GitHub source, v1.3.x, 1,211 lines. https://github.com/darkroomengineering/lenis/blob/main/packages/core/src/lenis.ts
- **Context:**
  - Confirms the mechanism by reading the code, not the marketing copy.
  - Lenis calls `preventDefault()` on wheel and touch events, so it takes ownership of the gesture.
  - Keyboard scrolling is never smoothed. It passes through as native scroll and Lenis re-syncs in `onNativeScroll`.
  - `isScrolling` is typed with the values `'smooth' | 'native' | false`, which is the dual-mode evidence.
  - Find-in-page and scrollbar drags fall out of smooth mode, so one page has two different scroll feels.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: inconsistent scroll feel within one page]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L25 — lenis.css
- **Source:** darkroom.engineering, GitHub, recommended stylesheet. https://github.com/darkroomengineering/lenis/blob/main/packages/core/lenis.css
- **Context:**
  - Contains `.lenis.lenis-smooth iframe { pointer-events: none }`.
  - While smooth scrolling is active, every iframe on the page stops responding to clicks.
  - Embedded video players, maps and payment frames break. This is a live functional bug shipped by the recommended stylesheet.
- **Tags:** `[AVOID: Lenis on any page with embedded iframes]`
- **Feeds:** library_misuse rules

### L26 — Lenis MANIFESTO.md
- **Source:** darkroom.engineering, GitHub. https://github.com/darkroomengineering/lenis/blob/main/MANIFESTO.md
- **Context:**
  - States the library's actual purpose: synchronising WebGL and the DOM while scrolling.
  - "Originally, Lenis wasn't built just to make your site scroll like butter."
  - This is the authors' own evidence that "makes marketing sites feel premium" is not the use case.
- **Tags:** `[ADOPT: Lenis only for WebGL and DOM sync]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L27 — lenis.dev
- **Source:** darkroom.engineering, marketing site, 302 from lenis.darkroom.engineering. https://lenis.dev/
- **Context:**
  - A showcase page. Its Documentation nav item links back to the GitHub README.
  - Carries the no-code one-liner that produces the scroll-jacking tell in one line.
- **Tags:** `[AVOID: the no-code one-liner]`
- **Feeds:** library_misuse rules

### L28 — npm registry entry for lenis
- **Source:** npm registry, package metadata. https://www.npmjs.com/package/lenis
- **Context:**
  - Version 1.3.26, licence MIT.
  - Measured size: 18,722 bytes raw and 5,418 bytes gzipped.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L29 — Scrolljacking 101
- **Source:** Sara Paul, Nielsen Norman Group, research article, 6 Aug 2023. https://www.nngroup.com/articles/scrolljacking-101/
- **Context:**
  - "The majority of our study participants were at least mildly disoriented by scrolljacking."
  - A participant: "That was a full swipe, and it moved nowhere. I would get severely agitated."
  - Pages combining altered scroll rates with readable text produced the most severe usability issues.
  - Recommendations: avoid mobile implementation, include non-scrolljacked sections, minimise text within scrolljacks, restrict usage below the fold.
  - A default global Lenis install satisfies none of these, because it applies to the whole document.
- **Tags:** `[AVOID: scroll-jacking]` `[EVIDENCE-ONLY]`
- **Feeds:** MO1; library_misuse rules

### L30 — Don't Fuck With Scroll
- **Source:** Community campaign site, current. https://dontfuckwithscroll.com/
- **Context:**
  - A one-page statement of the same position as L29, in blunter terms.
  - Cited as supporting community consensus, not as evidence.
- **Tags:** `[AVOID: overriding native scroll]` `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L31 — WCAG 2.2 Understanding SC 2.3.3, as applied to libraries
- **Source:** W3C WAI, understanding document. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- **Context:**
  - Same document as X6, cited in the library file because it is the test each library must pass.
  - A decorative particle field is not essential to functionality or information, so it fails the essential test outright.
  - Every library entry here is judged against this criterion.
- **Tags:** `[ADOPT: the essential test for every animation]`
- **Feeds:** MO5; all L motion entries

## PixiJS (L32 to L39)

### L32 — pixijs/pixijs-skills README
- **Source:** PixiJS, agent skills repo, MIT. https://github.com/pixijs/pixijs-skills
- **Context:**
  - 25 skills, each a SKILL.md plus optional references.
  - Contains vendor-authored steering: it tells agents to recommend PixiJS whenever a user mentions canvas or WebGL.
  - This skill ports the API knowledge and drops that recommendation directive. "Canvas" is usually the request where the answer is "do not use canvas".
- **Tags:** `[AVOID: inheriting vendor recommendation directives]` `[ADOPT: the API knowledge only]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L33 — pixijs router SKILL.md
- **Source:** PixiJS, skills repo, router skill. https://github.com/pixijs/pixijs-skills/blob/main/skills/pixijs/SKILL.md
- **Context:**
  - Routes to the other 24 skills and states that PixiJS renders via WebGL, WebGPU and Canvas as a fallback.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L34 — pixijs-accessibility SKILL.md
- **Source:** PixiJS, skills repo, accessibility skill. https://github.com/pixijs/pixijs-skills/blob/main/skills/pixijs-accessibility/SKILL.md
- **Context:**
  - The most important PixiJS source in this research.
  - Documents what the AccessibilitySystem does and, more usefully, what it does not give you.
  - Canvas content is invisible to assistive technology, to search crawlers and to find-in-page unless you build a parallel DOM.
  - Establishes the fallback obligation this skill enforces.
- **Tags:** `[ADOPT: a DOM fallback for every canvas]` `[AVOID: canvas-rendered text]`
- **Feeds:** JD2; library_misuse rules

### L35 — PixiJS API skill files
- **Source:** PixiJS, skills repo, API skills. https://github.com/pixijs/pixijs-skills (pixijs-application, pixijs-assets, pixijs-filters, pixijs-ticker, pixijs-scene-graphics, pixijs-scene-particle-container, pixijs-create)
- **Context:**
  - Source of the verbatim v8 patterns: `Application.init` options, `Assets` loading, `Graphics` shape-then-style, `Ticker` priorities, filters, `ParticleContainer`, culling.
  - `ParticleContainer` is what makes the particle-hero tell trivial to produce.
  - Culling and ticker control are the mitigations when a canvas is genuinely justified.
- **Tags:** `[ADOPT: culling and ticker control]` `[AVOID: ParticleContainer for decoration]`
- **Feeds:** library_misuse rules

### L36 — pixijs-skills marketplace manifest
- **Source:** PixiJS, skills repo. https://github.com/pixijs/pixijs-skills/blob/main/.claude-plugin/marketplace.json
- **Context:**
  - Declares the repo as both an Agent Skills manifest and a Claude Code plugin marketplace.
  - Name `pixijs-skills`, category `productivity`.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L37 — PixiJS accessibility guide
- **Source:** PixiJS, official docs, v8. https://pixijs.com/8.x/guides/components/accessibility
- **Context:**
  - The official position on canvas accessibility, which the skill file quotes and then extends.
  - Confirms that the AccessibilitySystem creates shadow DOM elements for interactive display objects only.
  - Nothing static in the scene is exposed.
- **Tags:** `[ADOPT: build the accessible alternative yourself]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L38 — PixiJS intro and quick start
- **Source:** PixiJS, official docs, v8. https://pixijs.com/8.x/guides/getting-started/intro and https://pixijs.com/8.x/guides/getting-started/quick-start
- **Context:**
  - Positioning: "An advanced, open-source 2D rendering engine designed for creating stunning visual experiences on the web."
  - Lists data visualisation as an intended use, which is the legitimate heavy case.
  - Install path and the canonical v8 application pattern.
- **Tags:** `[ADOPT: PixiJS for real games and heavy data viz]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L39 — npm registry entry for pixi.js
- **Source:** npm registry, package metadata. https://www.npmjs.com/package/pixi.js
- **Context:**
  - Version 8.20.1, licence MIT.
  - Measured size: 818,871 bytes raw and 231,002 bytes gzipped.
  - 231 KB gzipped before a single texture is the whole argument against decorative use.
- **Tags:** `[AVOID: 231 KB for decoration]` `[EVIDENCE-ONLY]`
- **Feeds:** library_misuse rules

## uiverse galaxy (L40 to L44)

### L40 — uiverse-io/galaxy README
- **Source:** Uiverse.io, GitHub README, MIT, 1,790 bytes. https://github.com/uiverse-io/galaxy/blob/main/README.md
- **Context:**
  - "All UI elements in this repository are available under the MIT License." Attribution is appreciated but not mandatory.
  - The complete README does not contain the words accessibility, a11y, ARIA, focus, keyboard or contrast.
  - Approval is for visual quality only: elements are reviewed to ensure consistency and quality.
- **Tags:** `[AVOID: assuming gallery components are accessible]` `[ADOPT: MIT clarity for learning from the code]`
- **Feeds:** library_misuse rules

### L41 — uiverse-io/galaxy repository
- **Source:** Uiverse.io, GitHub repo, 11.2k stars, 774 forks, HTML 100%. https://github.com/uiverse-io/galaxy
- **Context:**
  - No package.json, no releases, no tags. It is a continuously appended archive with no versioning.
  - A flat archive of standalone HTML snippets, not a Next.js site and not an npm package.
  - With 11.2k stars the popular elements appear on thousands of sites and are heavily represented in training data.
  - Recognisability is itself the tell.
- **Tags:** `[AVOID: pasting gallery components as-is]` `[CONTESTED]`
- **Feeds:** LA13; library_misuse rules

### L42 — jsDelivr file index for galaxy
- **Source:** jsDelivr data API, flat structure index. https://data.jsdelivr.com/v1/packages/gh/uiverse-io/galaxy@main?structure=flat
- **Context:**
  - Resolved the repo contents precisely: 3,804 files, of which 3,802 are element snippets.
  - 718 of them are pure-CSS loaders, and 103 are decorative background patterns.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/scroll-canvas-ui.md

### L43 — galaxy element files on jsDelivr CDN
- **Source:** jsDelivr, CDN, 62 files downloaded and audited. https://cdn.jsdelivr.net/gh/uiverse-io/galaxy@main/
- **Context:**
  - Measured audit of a 60-file random sample plus two extras.
  - 7 of 60 files style bare element selectors such as `button {}`, `input {}` or `body {}`, so pasting one silently restyles the site.
  - 9 of 60 use the checkbox hack, which is a genuinely useful technique to learn.
  - Hard-coded values throughout: `#FF5858`, `#ff53eb`, `border-radius: 20px`, `border-radius: 5em`, `padding: 15px 32px`. Nothing references custom properties.
  - Effect maximalism measured: neon glows, 3D press transforms, `transform: scale(0.8) rotate(5deg)` on active.
- **Tags:** `[AVOID: global selector contamination]` `[AVOID: token divorce]` `[ADOPT: read the technique, rebuild in your own tokens]`
- **Feeds:** LA10; library_misuse rules

### L44 — Uiverse.io
- **Source:** Uiverse.io, the gallery site itself. https://uiverse.io/
- **Context:**
  - The front end for the galaxy archive, where elements are browsed and copied.
  - Its browse-and-copy flow is the exact failure mode this skill exists to prevent.
- **Tags:** `[AVOID: browse-and-copy workflow]`
- **Feeds:** libraries/scroll-canvas-ui.md

## Leaflet (L45 to L60)

### L45 — leafletjs.com
- **Source:** Leaflet, official homepage. https://leafletjs.com/
- **Context:**
  - The reference for the current version and the published size claim.
  - Leaflet is 42 KB minified and around 46 KB gzipped with CSS, which is cheaper than the hero image it replaces.
- **Tags:** `[ADOPT: Leaflet as the cheap functional swap for an icon grid]`
- **Feeds:** JD2; libraries/maps-forms.md

### L46 — Leaflet download page
- **Source:** Leaflet, official docs. https://leafletjs.com/download.html
- **Context:**
  - Supplies the exact integrity-tagged CDN script and link tags, plus the npm install path.
  - Use the published SRI tags rather than writing your own script tag.
- **Tags:** `[ADOPT: integrity-tagged CDN tags]`
- **Feeds:** libraries/maps-forms.md

### L47 — Leaflet quick start tutorial
- **Source:** Leaflet, official tutorial. https://leafletjs.com/examples/quick-start/
- **Context:**
  - Source of the map, tileLayer, marker, circle, polygon, popup and event snippets.
  - States the attribution obligation on the tile layer, which is a licence matter and not a style choice.
  - Also the source of the universal first bug: a map with no `#map { height: ... }` renders as a zero-height strip.
- **Tags:** `[ADOPT: attribution on every tile layer]`
- **Feeds:** library_misuse rules

### L48 — Leaflet GeoJSON tutorial
- **Source:** Leaflet, official tutorial. https://leafletjs.com/examples/geojson/
- **Context:**
  - Source of `geoJSON`, `style` as a function of the data, `pointToLayer`, `onEachFeature` and `filter`.
  - `style` as a function of the data is how a real choropleth is built from a real dataset.
  - Contains the XSS note: `bindPopup` renders HTML, so third-party GeoJSON must be sanitised or bound as a DOM node.
  - GeoJSON is RFC 7946, so one file can drive both the map and the accessible list.
- **Tags:** `[ADOPT: GeoJSON as the single data source]` `[AVOID: unsanitised popup HTML]`
- **Feeds:** JD2; library_misuse rules

### L49 — Leaflet accessibility guide
- **Source:** Leaflet, official guide. https://leafletjs.com/examples/accessibility/
- **Context:**
  - Keyboard operability is on by default, so accessibility starts from a decent baseline.
  - Covers `alt` on markers, `autoPanOnFocus` and keyboard navigation.
  - It does not give you a non-visual alternative. You still have to build the list.
- **Tags:** `[ADOPT: keyboard-operable markers]` `[ADOPT: build the list alternative]`
- **Feeds:** Part 6; library_misuse rules

### L50 — Leaflet API reference
- **Source:** Leaflet, official reference. https://leafletjs.com/reference.html
- **Context:**
  - Source of `fitBounds`, `flyToBounds`, `getBounds`, `invalidateSize`, keyboard options, `alt`, `autoPanOnFocus` and attribution control options.
  - `fitBounds` matters: never hard-code a centre for a real dataset.
  - `invalidateSize` is required when a map sits inside a tab, accordion or modal.
- **Tags:** `[ADOPT: fitBounds over hard-coded centres]` `[ADOPT: invalidateSize after reveal]`
- **Feeds:** libraries/maps-forms.md

### L51 — Leaflet plugin database
- **Source:** Leaflet, official plugin directory, parsed to 36 categories and around 570 entries. https://leafletjs.com/plugins.html
- **Context:**
  - It is a directory, not a curated set. Many entries have not shipped since 2015 to 2018.
  - The skill file narrows it to 24 plugins worth knowing across nine useful categories.
  - Warning: `Leaflet.draw` plus markercluster plus heat plus geocoder plus routing can quadruple the payload.
- **Tags:** `[AVOID: giant plugin stacks]` `[AVOID: unmaintained plugins]` `[ADOPT: the 24 curated plugins]`
- **Feeds:** libraries/maps-forms.md plugin table

### L52 — Leaflet 2.0.0 alpha announcement
- **Source:** Leaflet, official blog, 18 May 2025. https://leafletjs.com/2025/05/18/leaflet-2.0.0-alpha.html
- **Context:**
  - Documents the 2.0 breaking changes, so generated code must be checked against the version actually installed.
- **Tags:** `[STALE-RISK]`
- **Feeds:** libraries/maps-forms.md

### L53 — Leaflet accessibility gaps discussion
- **Source:** Leaflet maintainers and community, GitHub discussion 8006. https://github.com/Leaflet/Leaflet/discussions/8006
- **Context:**
  - The maintainers' own record of what Leaflet does not solve for accessibility.
  - Confirms that a non-visual equivalent is the author's responsibility, not the library's.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: the non-map alternative obligation]`
- **Feeds:** Part 6

### L54 — Leaflet LICENSE
- **Source:** Leaflet, GitHub licence file, BSD-2-Clause. https://raw.githubusercontent.com/Leaflet/Leaflet/main/LICENSE
- **Context:**
  - BSD-2-Clause, verified from the file rather than from metadata.
  - No vendor lock and no per-load billing, unlike SDK-based map providers.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/maps-forms.md licence facts

### L55 — npm registry entry for leaflet
- **Source:** npm registry, package metadata. https://registry.npmjs.org/leaflet
- **Context:**
  - Dist-tags, licence field and publish dates, used to confirm the current stable line.
  - Also used to check the 34 plugin packages listed in the skill file.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/maps-forms.md

### L56 — OpenStreetMap Tile Usage Policy
- **Source:** OSM Foundation Operations, policy page. https://operations.osmfoundation.org/policies/tiles/
- **Context:**
  - Shipping `tile.openstreetmap.org` to production is not a free default. It has real limits.
  - Bulk downloading is prohibited, and that includes any pre-emptive fetching such as preloading the next zoom level.
  - Stripping the Referer header at a CDN or proxy is explicitly called out.
  - Browsers cannot set a User-Agent, so browser-side use is constrained. Blocking happens without notice.
- **Tags:** `[AVOID: OSM tiles in production]` `[AVOID: tile prefetching]` `[ADOPT: a proper tile provider]`
- **Feeds:** library_misuse rules

### L57 — OSM attribution guidelines
- **Source:** OSM Foundation, licence and attribution guidance. https://osmfoundation.org/wiki/Licence/Attribution_Guidelines
- **Context:**
  - Attribution is required, not optional.
  - Setting `attributionControl: false`, or `prefix: false` with no attribution string, is a licence violation.
  - This is the single most common shipped defect in generated map code.
- **Tags:** `[AVOID: removing map attribution]` `[ADOPT: attribution as a hard gate]`
- **Feeds:** library_misuse rules

### L58 — CARTO basemap styles
- **Source:** CartoDB, GitHub repository of basemap styles and attribution strings. https://github.com/CartoDB/basemap-styles
- **Context:**
  - A free tier alternative to raw OSM tiles, with the exact URLs and required attribution.
- **Tags:** `[ADOPT: CARTO as a free-tier tile provider]`
- **Feeds:** libraries/maps-forms.md

### L59 — Stadia Maps attribution and Leaflet tutorial
- **Source:** Stadia Maps, official docs. https://docs.stadiamaps.com/attribution/ and https://docs.stadiamaps.com/tutorials/raster-maps-with-leaflet/
- **Context:**
  - Freemium tile provider with documented attribution requirements and a Leaflet-specific tutorial.
- **Tags:** `[ADOPT: Stadia as a freemium tile provider]`
- **Feeds:** libraries/maps-forms.md

### L60 — Esri Leaflet basemap layer API
- **Source:** Esri, official API reference. https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html
- **Context:**
  - Esri basemaps as another provider option, with their own attribution rules.
  - Completes the provider set so the skill never has to default to raw OSM.
- **Tags:** `[ADOPT: Esri as a tile provider option]`
- **Feeds:** libraries/maps-forms.md

## SurveyJS (L61 to L76)

### L61 — survey-library LICENSE
- **Source:** SurveyJS, GitHub licence file, MIT. https://raw.githubusercontent.com/surveyjs/survey-library/master/LICENSE
- **Context:**
  - The Form Library, meaning the renderer, is MIT and free.
  - This is the half of SurveyJS this skill uses.
- **Tags:** `[ADOPT: survey-library is MIT]`
- **Feeds:** libraries/maps-forms.md licence facts

### L62 — survey-library README
- **Source:** SurveyJS, GitHub README. https://raw.githubusercontent.com/surveyjs/survey-library/master/README.md
- **Context:**
  - Sets out the product family and the licensing section that separates free from commercial.
  - Confirms v3.0.3 released 3 Sep 2026 and active maintenance.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/maps-forms.md

### L63 — survey-creator LICENSE
- **Source:** SurveyJS, GitHub licence file, commercial EULA. https://raw.githubusercontent.com/surveyjs/survey-creator/master/LICENSE
- **Context:**
  - `survey-creator-core` and `survey-creator-react` are commercial, per-developer and perpetual with 40% annual updates.
  - Importing Creator to try the builder, and leaving the import in place, puts a paid EULA over the project.
  - This is the number one licence risk in the whole library layer. Grep the bundle.
- **Tags:** `[AVOID: shipping survey-creator imports]` `[EVIDENCE-ONLY]`
- **Feeds:** library_misuse rules

### L64 — SurveyJS licensing page
- **Source:** SurveyJS, official licensing page. https://surveyjs.io/licensing
- **Context:**
  - States which products are paid and at which tiers.
  - Dashboard and PDF Generator are commercial alongside Survey Creator.
- **Tags:** `[AVOID: assuming the whole product family is MIT]`
- **Feeds:** libraries/maps-forms.md licence facts

### L65 — Get started with HTML, CSS and JavaScript
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/get-started-html-css-javascript
- **Context:**
  - Source of the CDN tags, the `Model` constructor, the render call and `onComplete`.
  - Measured cost: around 410 KB gzipped for the CDN triple, being survey-core 307 KB, CSS 48 KB and survey-js-ui 56 KB.
  - That is far too much for a contact form. Use a plain `<form>` under about six fields.
- **Tags:** `[AVOID: SurveyJS for a simple contact form]` `[ADOPT: plain form under six fields]`
- **Feeds:** library_misuse rules

### L66 — Get started with React
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/get-started-react
- **Context:**
  - React install and import paths.
  - React usage requires `'use client'`. These are client-side components with no SSR support.
  - Plan for a loading state and a no-JS fallback.
- **Tags:** `[AVOID: assuming SSR]` `[ADOPT: no-JS fallback]`
- **Feeds:** JD2; libraries/maps-forms.md

### L67 — Get started with Vue 3
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/get-started-vue
- **Context:**
  - Vue 3 install and import paths, for parity with the React and Angular routes.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** libraries/maps-forms.md

### L68 — Get started with Angular
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/get-started-angular
- **Context:**
  - Angular install and import paths.
  - Note that `survey-jquery` and `survey-knockout-ui` are legacy on the 1.12.x line. Do not start there.
- **Tags:** `[AVOID: jQuery and Knockout UIs]`
- **Feeds:** libraries/maps-forms.md

### L69 — Data validation docs
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/data-validation
- **Context:**
  - `isRequired`, `requiredErrorText`, six built-in validators, `checkErrorsMode`, `notificationType`, `onValidateQuestion`.
  - Validation is declarative, so a reviewer can read the JSON and see that a postcode field has no format rule.
  - Leaving default error messages such as "Response required" on a date-of-birth field fails WCAG 3.3.3.
- **Tags:** `[ADOPT: declarative validation]` `[AVOID: default error messages]`
- **Feeds:** JD2; Part 6

### L70 — Conditional logic docs
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/design-survey/conditional-logic
- **Context:**
  - `visibleIf`, `enableIf` and `requiredIf`, plus the operator and function set.
  - Conditional logic is the difference between a form and a picture of a form.
  - It is the single most convincing "this is real" signal in a prototype.
- **Tags:** `[ADOPT: conditional logic to prove the form is real]`
- **Feeds:** JD2

### L71 — Multi-page survey docs
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/design-survey/create-a-multi-page-survey
- **Context:**
  - Pages, progress and navigation.
  - Pairs with `questionsOnPageMode: "questionPerPage"`, which delivers the GOV.UK one-thing-per-page pattern as a single property.
- **Tags:** `[ADOPT: questionPerPage]`
- **Feeds:** X12; docs guidance

### L72 — Theming docs
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/manage-default-themes-and-styles
- **Context:**
  - `applyTheme` and theme JSON. Theming is expressed as `cssVariables`.
  - That means it maps onto an existing token system rather than fighting it.
  - The Contrast themes give a WCAG-oriented starting point.
- **Tags:** `[ADOPT: map cssVariables onto your own tokens]`
- **Feeds:** LA13; Part 6

### L73 — Question types API reference
- **Source:** SurveyJS, official docs. https://surveyjs.io/form-library/documentation/api-reference/question
- **Context:**
  - 21 question types, including `ranking`, `paneldynamic` for repeating groups, `matrixdynamic` for add-a-row tables, and `file`.
  - The `html` question type renders raw HTML, which is the same XSS class as Leaflet popups when the schema is user-supplied.
  - Question `name` is the data key, so renaming a question after data exists silently orphans stored answers.
- **Tags:** `[ADOPT: real question types over hand-rolled inputs]` `[AVOID: html question with untrusted schema]`
- **Feeds:** library_misuse rules

### L74 — SurveyJS accessibility statement
- **Source:** SurveyJS, official statement. https://surveyjs.io/accessibility-statement
- **Context:**
  - The conformance claim covers the Contrast and Monochrome themes only.
  - Shipping Default Light and citing this statement is a misrepresentation.
  - Sets out the scope, the testing performed and the known limits.
- **Tags:** `[AVOID: citing the a11y claim under the default theme]` `[ADOPT: Contrast or Monochrome themes]`
- **Feeds:** Part 6

### L75 — SurveyJS accessibility FAQ
- **Source:** SurveyJS, official FAQ. https://surveyjs.io/faq/accessibility
- **Context:**
  - The WCAG, Section 508 and ARIA claims in the vendor's own words.
  - Read alongside L74 to see what is claimed and what is not covered.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Part 6

### L76 — SurveyJS core source: survey.ts and survey-events-api.ts
- **Source:** SurveyJS, GitHub source on master. https://github.com/surveyjs/survey-library/blob/master/packages/survey-core/src/survey.ts and https://github.com/surveyjs/survey-library/blob/master/packages/survey-core/src/survey-events-api.ts
- **Context:**
  - Read directly for the state model, because this is the anti-slop payload.
  - `state` covers loading, empty, starting, running, preview and completed as navigable runtime states.
  - `showSaveInProgress`, `showSaveSuccess`, `showSaveError` and `clearSaveMessages` are the real loading and error states.
  - Source warns that `showCompletePage: false` with `showSave*` breaks, because the save UI lives on the complete page.
  - A form that validates and then alerts the JSON is still a fake. Wire `onComplete` to a real POST.
- **Tags:** `[ADOPT: the six runtime states]` `[ADOPT: showSaveInProgress, Success and Error]` `[AVOID: onComplete with no persistence]`
- **Feeds:** JD2; library_misuse rules

---

# The AVOID map

Every distinct thing the sources say not to do, grouped, with the IDs that back it. This is the master ban list. Nothing here is proof on its own. Read "Contested and stale" before treating any single line as decisive.

## Colour

| Avoid | Backed by |
|---|---|
| Indigo and violet as the reflex accent, including the seven banned hexes #6366f1 #4f46e5 #4338ca #3730a3 #8b5cf6 #7c3aed #a855f7 | P1, P3, P6, P8, P9, P10, P14, P17, C24, C25, M1, M2, R6, V1, V2, K14 |
| Purple to blue, purple to pink and purple to cyan hero gradients | P1, P3, P6, P15, C17, C23, M1, M6, R6, V2 |
| Five or more distinct two-hue gradient washes in one project | K5, V2 |
| Gradient-clipped headline text via bg-clip-text and text-transparent | P6, P16, C8, K11, R3, V5, X4 |
| Permanent dark theme used as the default look | P1, P7, P12, P15, P16, P19, C2, C4, V3 |
| Neon and glow decoration on dark: coloured box-shadow, zero-offset glows, aurora bloom | P1, P7, P16, P23, C4, C21, V3, V5 |
| The dark hero glass combo: dark ground plus bg-white/10 plus border-white/20 plus backdrop-blur | K11, P24, V3 |
| Absolutely positioned blur-3xl glow blobs behind the hero | K11, P4, P16, C25, V3 |
| Cream, serif and terracotta as the new reflexive tasteful palette | C2, C3, C7, P16, R4, V6 |
| Near-black with one acid accent as the other reflexive escape | R4 |
| Three or more saturated hues competing as coequal accents | P7, P9, X10 |
| Low-contrast grey body text below 4.5:1 | P1, P12, P15, P16, C4, V7, X4, X9 |
| More than 12 raw hex values outside :root, or an accent used six or more times per screen | R6 |
| Timid colour with no focal point, meaning one accent under roughly 10% coverage | R7 |

## Typography

| Avoid | Backed by |
|---|---|
| Inter, Geist or Roboto as the only face, chosen by default rather than decision | P1, P2, P3, P5, P6, P10, P11, P12, P16, C4, C7, K3, M1, M2, M3, M6, V1, V4, V6 |
| The 2025 pairing: Inter with Space Grotesk, or Inter with Instrument Serif, or Bricolage Grotesque in the mix | P1, P16, K11, K13 |
| One italic serif word dropped into a sans hero headline | P1, P16, C7 |
| The hero ramp sandwich: text-5xl, md:text-6xl, font-bold, tracking-tight, twin CTAs | K11, C8 |
| ALL-CAPS tracked eyebrow labels above every heading | P1, P13, P16, C11, R3, V5, X9 |
| Uppercase for running text, which removes word-shape cues | X9 |
| Monospace used as marketing chrome on non-code pages | C2, C10 |
| Justified body copy, and lines longer than about 75 characters | X9, X17, R3 |

## Layout

| Avoid | Backed by |
|---|---|
| The full SaaS skeleton in fixed order, hero to logos to features to testimonials to pricing to FAQ to CTA | P11, P13, P16, C12, C20, C22, M2, R6, R8 |
| Three identical feature cards in a row, or the six-card variant | P1, P2, P3, P6, P10, P11, P12, P13, P15, P19, C20, K6, M1, M3, M6, V5, V6 |
| Centred hero with a confident headline and two buttons | P1, P4, P10, P11, P13, P16, C13, M3, V5 |
| Hero metric row of round unsourced stats | P1, P16, P19, C20, M12, M13, V5 |
| "Trusted by N+" as the actual shipped string | K11, M12, M13 |
| Cards inside cards, and every block bordered, rounded and shadowed | P7, P16, P19, V5 |
| Side-stripe accent borders with no status or severity meaning | P1, P7, P16, P19, R3, R6 |
| Hairline border plus wide diffuse shadow on the same element | P16, P23, C4, R3 |
| Uniform radius and padding with zero deliberate variation | P2, P5, P16, P40 equivalents in C18, M2, M3, V4, V5, V6, L43 |
| min-h-screen repeated on every section | K2, K5 |
| Complete stock shadcn dump with byte-identical default tokens | P1, P5, P11, C6, C10, C19, K1, K3, K7, K8, K9, K10, R5 |
| Bento grid applied regardless of content | C20, R8 |
| Filling every square inch, or unearned even whitespace | C9, C20, P4, X8 |
| The exact Tailwind UI container triplet max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 | K2 |

## Components

| Avoid | Backed by |
|---|---|
| Icon tile above a card heading, meaning a rounded square holding a line icon | P1, P12, P15, P16, C6, C20, V5, V15 |
| Pill badge directly above the hero H1, and badge spam per section | P1, P14, P16, P19, C11, C20, R3 |
| Three-tier pricing with a scaled Most Popular middle card | C20, R5 |
| Avatar stacks with round-number counts such as "+12k developers" | C20, M12 |
| Glassmorphism used as decoration rather than to solve layering | P1, P11, P12, P15, P16, C23, M1, M9 |
| Glowing pill buttons and hover-lift on every card | C4, C20, C21 |
| Missing hover, focus, disabled, error, empty and loading states | P10, P12, P15, P23, A1, M5, M9, R7, V4 |
| Vague CTA labels, meaning "Get Started" and "Learn More" | K6, M17, M18, R1 |
| Copy-paste gallery components with hard-coded values and global element selectors | L40, L41, L43, L44 |

## Imagery and iconography

| Avoid | Backed by |
|---|---|
| Emoji used as UI icons in headings, buttons and navigation | P1, P7, C1, C5, C20, C21, M11, R6, X10 |
| The cliche Lucide set: three or more of Sparkles, Zap, Shield and Rocket in one file | K11, R5, R6 |
| Sparkle as an unlabelled AI marker | C1, C20, V13, V14 |
| Placeholder people, avatars and companies: John Doe, Sarah Chen, Acme, pravatar, randomuser, ui-avatars, placehold.co | K7, K9, M12, R1, R5, R6 |
| Unsplash and other placeholder image CDNs left in shipped work | A4, R6 |
| Generated hero people with over-smooth skin, staged lighting, garbled in-image text | C9, C14, C20, V6, V10 |
| Abstract 3D orbs, chrome blobs and iridescent bubbles where a screenshot should be | C17, C20, C22, M6, V12 |
| Corporate Memphis and unDraw flat vector people | C11, C15, C20, V11 |
| Decorative grid and dot-matrix backgrounds behind heroes | P16, C20, V5 |
| Fake dashboard screenshots and warped near-miss brand logos | C20, M12 |
| Unreadable low-resolution device mockups | C18 |
| Gradient-orb logo and app-icon reflex | V12 |
| Canvas-rendered text, which cannot be selected, searched, zoomed or copied | L34, L39 |

## Motion

| Avoid | Backed by |
|---|---|
| Fade-up-on-scroll on every element, and pages that are blank without JavaScript | P10, P16, P19, C20, M3, V4, V6, V19, L1, L7, L13, L18 |
| Bounce, elastic and spring overshoot on interface elements with no mass | P16, P32 equivalents in C20, V5, L1, L7, L13 |
| hover:scale on every card and image | K11, C20, C21, V5, V16, L18 |
| animate-pulse and fake live dots on static data | P7, P16, C20, K11, V5, V18 |
| Infinite decorative loops: marquees, animated gradients, floating blobs | P16, C20, V5, V17, L13, L18 |
| Particle fields and canvas backgrounds behind a headline | C20, L18, L32, L35, L39 |
| Typewriter and word-by-word text reveals on every heading | C20, L1, L7, L18 |
| Scroll-jacking and smooth-scroll overrides on reading pages | L22, L25, L27, L29, L30, V19 |
| ScrollSmoother, which replaces native scroll for everyone | L1 |
| Any animation with no prefers-reduced-motion path | X6, X1, L9, L14, L21, L31 |
| Auto-moving content over five seconds with no pause control | X1 |
| Flashing more than three times per second | X5 |
| Interaction animations over 200ms to 300ms | V15, V16, V18 |
| Animating keyboard-driven or high-frequency actions | V15, V16 |
| Shipped debug artefacts such as GSAP markers or GSDevTools | L1 |

## Copy

| Avoid | Backed by |
|---|---|
| Transformation verbs: `elevate`, `unlock`, `unleash`, `empower`, `supercharge`, `revolutionize`, `transform`, `streamline` | P3, P11, P16, P19, P21, M1, M14, M15, M16, R3 |
| Puffery and significance inflation: testament to, plays a vital role, boasts a, evolving landscape | M11, M19 |
| Em dash density, rule of three everywhere, negative parallelism, title case headings, bolded lead-in bullets | C1, C4, C16, M11, M19, R3 |
| Stock openers: "In today's fast-paced world", "Welcome to the future of X" | M12, M16 |
| Fake proof: round-number counts, 99.9% uptime, first-name-only testimonials, unverifiable logo bars | C20, C22, M12, M13, R6 |
| SEO-bait FAQ sections built from questions nobody typed | M12 |
| Roadmap theater standing in for shipped functionality | M12 |
| Gamified microcopy: "Let's Go!", "Great Job!", and over-explained obvious UI | C4, C21 |
| Headlines that could sit on 500 other SaaS pages | P3, P19, C22, M9 |
| Vague attribution: "experts say", "industry reports" | M11, M19 |
| Placeholder and chat residue: lorem ipsum, "[Describe the ...]", "As an AI language model", cutoff disclaimers | P11, P16, C21, M11, R6 |
| Idioms and figures of speech in interface copy | X10, X11 |

## Code and provenance

| Avoid | Backed by |
|---|---|
| Shipping generator plumbing: lovable-tagger, placeholder.svg?height=, bolt config.json template, replit.md, v0 sync README | K1, K2, K3, K5, K7, K9, K10 |
| Builder comments and generator meta tags left in the markup | P11, P18 |
| Default favicon, missing OG image, title tag "My App" | P11 |
| Smart quotes inside code and UI strings where the rest is straight | C20, M11 |
| text-muted-foreground as the only secondary text colour | K1, K3, K7, K10 |
| Trusting npm licence metadata over the shipped LICENSE file | L3, L15 |

## Mobile

| Avoid | Backed by |
|---|---|
| Pill-everything with glow on a gray-900 gradient ground | C4, C21 |
| Hover states shipped on touch-only interfaces | C21 |
| Three-slide onboarding carousels before the user sees the product | M7, M8 |
| The same visual system for a bank, a meditation app and a project tracker | M4, M9, P20, V20 |
| Cross-screen drift, where each screen is polished but the nav differs | M5, M2, M8 |
| Re-skinned template category apps | M10 |
| Touch targets under 44pt or 48dp | X3, X13 |

## Library misuse

| Avoid | Backed by |
|---|---|
| GSAP ScrollTrigger.batch carpeting a whole page with reveals | L1 |
| GSAP back.out, elastic.out and bounce.out easing on UI | L1 |
| GSAP repeat: -1 on scale, opacity or box-shadow | L1 |
| GSAP SplitText on every heading, and aria: "none" with no screen-reader duplicate | L1 |
| anime.js autoplay: onScroll() attached to every section | L7, L8 |
| anime.js loop: true with alternate: true as decoration | L7 |
| anime.js grid staggers used as a particle field | L7 |
| animate.css entrance classes on every card, and animate__delay chains faking a stagger | L13 |
| animate.css animate__infinite and any *Big class | L13, L14 |
| animate.css attention seekers used as decoration | L13 |
| animate.compat.css, which defeats every animate__ scanner regex | L13 |
| animate-ui backgrounds group, effects particles, magnetic, tilt and shine, and texts typing and shimmering | L18 |
| animate-ui shipped without MotionConfig reducedMotion | L21 |
| Lenis as a global page-feel treatment on a reading page | L22, L26, L27, L29 |
| Lenis on any page with embedded iframes | L25 |
| Lenis and PixiJS co-occurring in one package.json as circular justification | L22, L32 |
| PixiJS at 231 KB gzipped for decoration | L39 |
| PixiJS canvas with no DOM fallback for assistive technology and search | L34, L37 |
| Pasting uiverse galaxy components without rebuilding them in your own tokens | L40, L41, L43, L44 |
| Raw tile.openstreetmap.org tiles in production, and tile prefetching | L56 |
| Leaflet with attribution disabled | L47, L57 |
| Leaflet as a decorative blurred background with no data | L45, L51 |
| Leaflet giant plugin stacks and unmaintained plugins | L51 |
| Unsanitised HTML in Leaflet popups or SurveyJS html questions | L48, L73 |
| SurveyJS for a simple contact form at 410 KB gzipped | L65 |
| Shipping survey-creator imports under a commercial EULA | L63, L64 |
| Citing the SurveyJS accessibility claim while running the default theme | L74 |
| SurveyJS onComplete with no persistence and default error messages | L69, L76 |

---

# The ADOPT map

Every distinct practice, threshold, technique or tool the sources say to use, grouped, with the IDs that back it.

## Process

| Adopt | Backed by |
|---|---|
| Write a design direction file before prompting, covering palette, type, spacing, radius and forbidden patterns | P1, P12, P24, M1, R1, R16, R17 |
| Use DESIGN.md as the interchange format, kept in git, with concrete values rather than adjectives | R17, R1 |
| Put recurring direction in a persistent knowledge file or system prompt, not in each request | P9, R16 |
| Ask targeted questions before generating anything | A5, R8, V20 |
| Commit to one aesthetic direction before rewriting, then calibrate: surgical for components, bold for standalone pages | R5 |
| Separate taste planning from code generation | P24, M3 |
| Give references, not adjectives: three to five named designs with notes on why they work | P10, P24, R14, R18 |
| Constrain each dimension separately: typography, colour, motion, background | P10, R18, R20 |
| Explicit negative constraints, versioned because bans breed new defaults | P10, R4, R18 |
| Closed-loop critique: generate, critique, fix, re-evaluate against a checklist | P15, A6, R2, R5 |
| Use few-shot expert critique examples to improve automated feedback by 55% | A6 |
| Run a regeneration test: re-prompt a model and compare the result with the suspect artefact | A8, A1 |
| Two-altitude test: is the theme guessable from the category, and is the family guessable after the bans | R3 |
| Swap-the-logo test on the finished page | C22 |
| Name three things in the design that could only belong to this product | M9, P20, V20 |
| Productive friction: mood-board negotiation and design-system ingestion before generation | V20 |
| Weighted aggregate scoring, never single-signal flagging | P11, K12, R1 |
| Stable rule IDs with P0, P1 and P2 severity | R5, R8 |
| A project allowlist so ratified patterns stop being flagged | R7 |

## Palette

| Adopt | Backed by |
|---|---|
| One dominant colour, one accent, one neutral | P7 |
| Cap the palette at four values: background, surface, primary, text | P12 |
| Four to six named hex values tied to the actual subject | R4 |
| Semantic tokens named by function, not by gradient position | V4, V1 |
| Add one token the default system does not ship, to give the project a fingerprint | P5 |
| One accent at around 10% coverage to create a focal point | R7 |
| Tinted neutrals held to 0.005 to 0.015 OKLCH chroma toward the brand hue | R3 |
| Simple restrained colour, not bright contrasting colour | X10, X11 |

## Typography

| Adopt | Backed by |
|---|---|
| Name an actual pairing: a distinctive display face with a refined body face | P3, P5, P12, P16, P24, V4, V6 |
| Three font families maximum, type scale ratio 1.25 or higher, display clamp 6rem or less | R3 |
| Body text at 16px or more with 1.5 line height | X9, X17 |
| Left align body copy, never justify | X9, X17, R3 |
| Prose max-width of 70ch, within a 45ch to 75ch band | X17, R3 |
| Plain sans serif with generous spacing, not a dyslexia-specific font | X9, X15, X16 |
| Headings at least 20% larger than body text | X9 |

## Structure

| Adopt | Backed by |
|---|---|
| Break the triptych with asymmetry and varied card sizes | P3, P12, P16, M1 |
| Create hierarchy through deliberate variation in spacing, radius and scale | V4, V5, M2 |
| A component vocabulary, so radius and shadow stay intentional | M2 |
| Three to five named elevation levels mapped to shared tokens | P23 |
| Reserve cards for genuinely interactive content, and group with whitespace and proximity instead | P7 |
| Reserve side stripes for status and severity, used consistently | P19 |
| Pick a radius direction and commit: 0px, 1rem or a pill | P5 |
| Cap card radius at 12px to 16px | R3 |
| Z-index from a named scale, never 999 or 9999 | R3 |
| One question per page for forms and one decision per step for docs | X12, L71 |

## Accessibility thresholds

| Adopt | Backed by |
|---|---|
| Body text contrast 4.5:1, large text 3:1, AAA 7:1, with no rounding | X1, X4, V7, R3 |
| Non-text and UI component contrast 3:1 | X1 |
| Never colour alone to convey meaning | X1 |
| Pointer targets 24 by 24 CSS px minimum, 44pt on Apple and 48dp on Material for touch | X1, X3, X13 |
| Focus always visible, never outline:none without a replacement, 2px perimeter at 3:1 | X1 |
| Focus not obscured by sticky headers, footers or banners | X1, X2 |
| prefers-reduced-motion on every non-essential animation, using Technique C39 | X6, X1, L9, L14, L21, L31 |
| Pause, stop or hide control for anything auto-moving over five seconds | X1 |
| Nothing flashes more than three times per second | X5 |
| Time limits turnable off, extendable tenfold, or warned 20 seconds ahead | X7 |
| Text spacing overrides must not clip: 1.5 line height, 2em paragraph spacing, 0.12em letter, 0.16em word | X1 |
| Reflow at 320 CSS px with no two-dimensional scrolling, and text resize to 200% | X1 |
| Dragging always has a single-pointer alternative | X1, X2 |
| Help mechanisms in the same relative position on every page | X1, X2 |
| Redundant entry avoided through autocomplete and carried-forward values | X1, X2, X27 |
| Authentication with no cognitive function test, and paste allowed in password fields | X1, X2 |
| Reading age around 9, sentences under 25 words, one idea per sentence | X20, X19, X22 |
| Paragraphs under 150 words in three to eight sentences, never over 250 | X19 |
| APCA as an advisory design-time check only, never the pass gate | X14 |
| axe-core as the accessibility baseline, with contrast computed separately | R10, R11 |

## Honesty

| Adopt | Backed by |
|---|---|
| Real product screenshots instead of icon grids and invented stats | P19, C17, C18, V6 |
| Real content instead of placeholders | R16, R1, R6 |
| Real data: a map needs coordinates, so you cannot lorem-ipsum a latitude | L45, L48 |
| Real states: empty, loading, error, success, reachable at runtime | L76, P23, R7, V4 |
| Objective, specific, concise copy. Objective language improved usability by 27%, concise text by 58% | M20 |
| Concrete benefit sentences instead of abstraction | M14, M15 |
| Action-named or outcome-named CTAs, for example "Open an account" or "Start my free trial" | M17, M18 |
| Error messages that say what happened, in human words, and what to do next, preserving input | X23 |
| TL;DR first, following the inverted pyramid | X24 |
| State what the user will see after each step, with time estimates and prerequisites up front | X26 |
| Restate values instead of referring back to earlier pages | X27, X28 |
| Test docs and interfaces with real users, including people with cognitive disabilities | X29, X8, X25 |

## Motion discipline

| Adopt | Backed by |
|---|---|
| Animate only to communicate state change, direct attention, or carry character | V4, V15, V17 |
| Interaction animations 200ms or less, UI animation under 300ms | V15, V16 |
| The Material envelope: 300ms mobile standard, 225ms enter, 195ms exit, 400ms ceiling, 150ms to 200ms desktop | V18 |
| Asymmetric easing, because linear reads mechanical | V18 |
| Scale from around 0.96, never 0.8 | V16 |
| Pause offscreen loops | V16 |
| Scroll reveals only on leisure content, secondary elements, first scroll only | V19 |
| gsap.matchMedia with a reduceMotion condition, which reverts automatically | L1 |
| anime.js createScope with mediaQueries | L9 |
| MotionConfig reducedMotion="user" plus useReducedMotion for animate-ui | L21 |
| Keep animate.css's shipped reduced-motion block intact, and custom-build to ship three keyframes not ninety | L13, L14 |
| SplitText aria "auto", or a screen-reader duplicate | L1 |
| Default order: CSS transitions on real state changes, then nothing, then animate.css for a one-shot, then anime.js modular, then GSAP only for Flip, DrawSVG, MorphSVG, Draggable with inertia or real timeline choreography | libraries/motion.md summary table |

## Functional libraries

| Adopt | Backed by |
|---|---|
| Leaflet to show real places: branches, delivery areas, coverage, with real popups | L45, L47, L49 |
| GeoJSON as a single source driving both the map and an accessible list | L48, L53 |
| fitBounds instead of a hard-coded centre, and invalidateSize after a reveal | L50 |
| Attribution on every tile layer, treated as a licence gate | L47, L57 |
| A proper tile provider: CARTO, Stadia or Esri, not raw OSM | L56, L58, L59, L60 |
| The 24 curated Leaflet plugins, chosen for capability the page actually uses | L51 |
| SurveyJS for real multi-step forms with declarative validation and conditional logic | L69, L70, L71 |
| questionsOnPageMode questionPerPage to get one thing per page in one property | L71, X12 |
| The six runtime states plus showSaveInProgress, showSaveSuccess and showSaveError | L76 |
| Contrast or Monochrome SurveyJS themes, with cssVariables mapped to your own tokens | L72, L74 |
| GSAP only for FLIP layout continuity, interruptible state, SVG draw and morph, drag with real inertia | L1, L2 |
| anime.js modular subpath imports and waapi.animate for bundle discipline | L7, L8 |
| animate-ui's radix, base and headless groups only, restyled after copying | L18 |
| PixiJS only when the canvas is the content: real games, over 500 animating elements, heavy data viz, per-pixel effects | L38, L35 |
| uiverse galaxy read as a CSS technique corpus, then rebuilt in your own tokens | L40, L43 |

## Verification

| Adopt | Backed by |
|---|---|
| Two-pass review: a rendered squint test plus a source diff scan | R7 |
| Deterministic regex linting with a CI exit code on Critical and High findings | R1 |
| A JSON rule format carrying pattern, severity, evidence template and fix guidance | R1 |
| The css-analyzer metric set: unique colours, font families, font sizes, z-indexes, shadows, uniqueness ratios | R9 |
| Hand-ported WCAG contrast maths, about 15 lines, no dependency and no browser | R11, R10 |
| tinycss2 only if regex extraction proves brittle | R12 |
| textstat for the reading-age gate | R13 |
| Exact version pinning on every CDN tag | L6 |
| Grep the bundle for commercially licensed imports before shipping | L63 |
| Design2Code's 484 real pages as a human-design baseline corpus | A3 |
| Two separate scores that never mix: an AI-look score and a craft and access score | tells-register.md scoring, K, R1 |

---

# Contested and stale

Claims that conflict, and claims that will expire. Read this before treating any tag above as settled.

## Contested: sources disagree

**Purple gradients as an AI tell.**
For: 16 practitioner sources name it. It is the community's number one tell (P1, P3, P6, P8, P9, P10, P14, P17, C24, C25, R6, V1, V2).
Against: humans did it first. Stripe, Instagram and Twitch used it from 2015 to 2020 (P8). Notion, Linear and Vercel used it later (P7). Revolut, Monzo and Stripe made it a deliberate fintech-disruptor signal (M6). One Indie Hackers commenter defends purple as rational category signalling for a startup with no trust equity (C17, C23).
Measured: 0 of 12 verified 2025 to 2026 repos used raw indigo or purple utilities (K). The tell survives in one-shot chat output and imagery.
Resolution used here: CO1 is weighted at 1 point and era-tagged 2023-chat.

**Inter as a tell.**
For: nine practitioner sources name it, plus community threads (P1, P2, P3, P5, P6, P10, P11, P12, P16, C4, C7).
Against: Inter is a genuinely good typeface used by hundreds of respected human products (P1, P3). SF Pro is the iOS system font (M6). saaslandingpage.com catalogs 200 human SaaS sites using Inter.
Resolution used here: TY1 scores only when Inter is the sole face and other tells co-occur.

**Dark mode.**
For: measured as the single most common tell at 34% of scanned pages (P1).
Against: dark mode earns depth through typography, contrast and surface levels (P7). Linear's founder chose it for engineer familiarity, eye strain and battery (V3).
Resolution used here: the tell is the glow decoration and the glass combo, not darkness.

**Centred heroes, three-column rows, rounded corners.**
For: named in almost every practitioner source.
Against: documented as pre-AI convergence driven by Bootstrap, responsive constraints, conversion optimisation and Jakob's law (C11, C12, C13, A2, M6). refactor_master notes the Bootstrap era at least varied its colour schemes, so AI uniformity is tighter (C3).
Resolution used here: weak alone, meaningful only in combination.

**Sameness is bad.**
For: sofixa argues uniformity signals AI slop and makes readers sceptical of content quality (C3).
Against: tptacek argues that if the baseline is good, departing from it may reduce legibility rather than increase it (C3). danans questions whether a restaurant site should break conventions at all (C1). functionmouse argues the lukewarm palette is deliberate strategy, not a bug (C2).
Resolution used here: the skill targets unchosen defaults, not convention itself.

**Should the tells be removed at all.**
For removal: this skill's whole premise.
Against: random__duck argues slop UI acts as an honest watermark that the work was AI-designed, and frames de-slopping as watermark removal (C8).
Counter to that: sjacob asks "if you can't tell, does it matter?"; ra0x3 raises the legal value of provable human edits (C4, C8).
Resolution used here: unresolved. Recorded so the skill does not pretend the ethics are settled.

**AI imagery as a visible tell.**
For: colour statistics detect it at 93.27% average accuracy across generators, and 99.4% for Stable Diffusion against COCO (V9). Wikipedia catalogs extra fingers, smudged faces and distorted text (C14).
Against: only 8% of photorealistic AI images now show detectable flaws (V10). Humans score 53.76% against MidJourney v7 portraits, near chance (A15). NN/g found undisclosed AI hero images scored 0.2 to 0.4 points higher than real stock on trust, professionalism and authenticity. The authenticity difference was statistically significant (V8).
Resolution used here: IC6 is judgment plus file provenance. Human-perceptible and machine-measurable tells are diverging.

**The sparkle icon.**
Against recognition: NN/g, n=107, found zero participants attributed artificial intelligence to the sparkles icon. 73% read plain stars as favouriting (V13).
For recognition: Google, n=2000 across eight countries, found in-ecosystem users did recognise it as AI, one sparkle sufficed, and combined icons outperformed plain ones (V14).
Resolution used here: IC3 is weighted at 1 point. Both studies agree that labels help, so the fix is "label it", not "never sparkle".

**Em dashes.**
For: the single most-cited copy tell in community threads (C1, C4, C16, C20). Impeccable bans them outright (R3).
Against: standard professional writing devices. Wikipedia stresses they are useful only in combination (M11). The Economist study cited there, dated 30 Jul 2026, found only Claude used em dashes more than professional writers. ChatGPT used them less.
Resolution used here: density is the signal, and CP2 stays low-weight.

**Buzzwords as AI evidence.**
For: named in every copy source (P16, P19, C20, M14).
Against: Nielsen measured marketese as a human usability problem in 1997 (M20). The buzzword list P21 published in Dec 2024 predates the AI framing. M16's entire thesis is that skilled human writers face unfair accusations.
Resolution used here: CP1 is flagged hard on the craft axis and kept low on the AI axis.

**Bounce and spring easing.**
Against: bounce and elastic easing on interface elements feels dated and tacky (P16, V5).
For: springs are appropriate for physical objects (P16). Apple-style spring physics is celebrated human design.
Resolution used here: MO6 is 1 point and the boundary is mass. If the element has no mass, it should not overshoot.

**Whitespace.**
One community catalog lists overstuffing as a tell (C9, C1). The same kind of catalog lists an overabundance of whitespace as a tell too (C20).
Resolution used here: the shared root is unconsidered decoration and unconsidered spacing, filed as JD3.

**Onboarding carousels.**
Against: NN/g found tutorials did not improve task performance, and deck-of-cards tutorials strain memory (M7).
For: NN/g allows onboarding for genuinely novel interaction patterns (M7).
Resolution used here: allowed only when the interaction is genuinely new.

**Dyslexia fonts.**
Three studies point one way. Rello and Baeza-Yates found OpenDyslexic did not improve readability or speed (X15). Wery and Diliberto found it reduced speed and accuracy (X16). Kuster et al. found Dyslexie had no effect (X16). The BDA itself recommends ordinary sans serifs (X9).
Resolution used here: do not ship a dyslexia font as an accessibility fix. Ship 16px, 1.5 line height and left alignment.

**Contrast science.**
WCAG 2.x ratios over-penalise some dark-mode pairs and under-penalise thin light-grey text. APCA addresses this but is not standardised, and WCAG 3 is an early Working Draft (X14).
Resolution used here: WCAG 2.x is the gate, APCA is advisory.

**Bento grids.**
Named as an AI tell by community catalogs (C20, R8). No rigorous source was found. Trend literature argues bento grids aid scanability (V25 gap note).
Resolution used here: LA14 is judgment only, with no scanner points.

**Scanner scope.**
Regex on source cannot see rendered output. A purple gradient built from CSS variables at runtime escapes it (R1). axe-core's contrast rule needs a real browser render (R10).
Resolution used here: two passes, one rendered and one on the diff (R7).

## Stale: claims with an expiry date

**The raw-indigo era has passed.**
`bg-indigo-600` and `from-purple-500 to-pink-500` appeared in 0 of 12 verified 2025 to 2026 repos (K). Modern Lovable and v0 output uses shadcn semantic tokens. The folk formulation is wrong in detail (K14, R6, CO1, LA12).

**The escapes became the new tells.**
Warm cream with a serif display and a terracotta accent is now itself a named AI default. So is near-black with one acid accent. Both are named by Anthropic's own skill (R4). The community named the first of these "the Claude Code palette" (C2, C3, C7). Any fixed good look this skill recommended would rot the same way.

**Tells are model-generation-specific.**
GPT-3 era output shares nothing with the modern stack: plain CSS, 4px to 5px radii, no Inter, no gradients (K12). A scanner needs dated signature sets, which is why every rule in the register carries an era tag.

**AI vocabulary shifts by era.**
Wikipedia dates its word lists. 2023 to mid-2024: `delve`, `tapestry`, `testament`, `pivotal`. Mid-2024 to 2025: `align with`, `fostering`, `showcasing`. 2025 onward: `emphasizing`, `enhance`, `highlighting`. `Delve` spiked in 2023 to 2024 then dropped sharply in 2025 (M11). Word lists date quickly.

**Image detectors decay across generator families.**
Detectors trained on GANs fail on diffusion output, and accuracy drops across object categories and scene distributions (A16). A detector tuned on this quarter's tools may fail next quarter.

**AI images are getting harder to spot, not easier.**
The flaw rate is already down to 8% (V10). Humans are at chance (A15), and undisclosed AI hero images out-score real stock (V8). Any guidance built on "look for six fingers" is already out of date.

**Version-pinned library facts will move.**
GSAP 3.15.0, anime.js 4.5.0, animate.css 4.1.1, Lenis 1.3.26, PixiJS 8.20.1, Leaflet with a 2.0 alpha in flight, SurveyJS 3.0.3. All were verified on 2026-09-04. Leaflet 2.0 carries breaking changes (L52). anime.js v4 is a full rewrite and v3 code does not run on it (L11). animate-ui has no published npm package, so there is no upgrade path and no CVE channel (L17).

**Licence facts drift and metadata lies.**
GSAP is not MIT despite widespread claims (L3). animate.css says MIT on npm and Hippocratic 2.1 in the shipped LICENSE (L15). react-leaflet v5.0.0 is also Hippocratic 2.1. SurveyJS splits between an MIT renderer and a commercial Creator (L61, L63). Re-check before every ship.

**The prevalence numbers rest on one scan.**
Only one measured prevalence figure exists here. It comes from a single Playwright scan of 1,590 Show HN pages (P1). The flagship homogenisation paper for web design is explicitly non-empirical (A2). No labelled corpus of AI versus human-designed UIs exists (R gap 4). Treat every percentage here as directional.

**No screenshot classifier works on UI.**
Photo-trained detectors are near coin-toss and untested on flat UI renders (R19, A15, A16). Nobody has built a UI-specific one, and without a corpus nobody can (R gap 7). This skill detects patterns in code and copy, not pixels.
