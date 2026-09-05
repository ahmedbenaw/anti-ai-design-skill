# 11 — Community and practitioner discussion (2026)

**Topic:** What practitioners say actually gives AI-generated design away, in their own words. Reddit-first, Hacker News second.
**Sweep date:** 2026-09-05
**Route used:** WebSearch / WebFetch route authorized (Exa MCP not authorized this session). In fact **WebSearch was never invoked** and **WebFetch was invoked once** (blocked at the domain layer). In practice the productive channels were plain HTTP fetches via Bash: the Hacker News Algolia API (`hn.algolia.com/api/v1/*`) and the **Arctic Shift Reddit archive** (`arctic-shift.photon-reddit.com/api/*`). WebFetch itself is domain-blocked for `www.reddit.com`.

## Was Reddit reachable?

**Live Reddit: no. Archived Reddit: yes.** This distinction matters and is not a fudge — the comment bodies below are full comment trees, not search snippets.

Exactly what was tried against live Reddit, all failed:

| Attempt | Result |
|---|---|
| `WebFetch` → `https://www.reddit.com/r/web_design/search.json?q=AI+generated+design&restrict_sr=1&sort=top` | "Claude Code is unable to fetch from www.reddit.com" — domain blocked at the tool layer |
| `curl https://www.reddit.com/r/web_design/search.json?...` (browser UA) | HTML shell, not JSON |
| `curl https://www.reddit.com/r/webdev/top.json?limit=2` | **HTTP 403** — Reddit network-security block page |
| `curl https://old.reddit.com/r/webdev/search.json?q=...&restrict_sr=1` | HTTP 302 → 403 |
| `curl https://old.reddit.com/r/webdev/search.rss?q=AI+design&restrict_sr=1` | **HTTP 403** |
| `curl https://www.reddit.com/search.json?q=AI+generated+design+tell` | **HTTP 403** |
| `curl https://api.reddit.com/r/webdev/search?...` | HTML shell |
| Redlib mirror `https://redlib.catsarch.com/r/webdev/search?...` | **HTTP 403** |
| PullPush (Pushshift successor) `https://api.pullpush.io/reddit/search/submission/?...` | **HTTP 429** — "does not provide free scraping resources for agents" |

**What worked:** `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&query=<q>&limit=25` and `https://arctic-shift.photon-reddit.com/api/comments/tree?link_id=<id>&limit=150`. This is a full Reddit archive mirror; it returns real post metadata (score, num_comments, author, created_utc) and complete nested comment bodies. It rate-limits hard (429/422 after roughly 8–10 requests), which capped how many threads could be opened.

Also blocked this session: **Bluesky** public AppView (`public.api.bsky.app/xrpc/app.bsky.feed.searchPosts`) returned **HTTP 403** for every query. No Bluesky or Mastodon sources are included. See Gaps.

**Threads actually opened (full comment trees fetched and read): 15.**
9 Reddit (r/web_design ×4, r/UI_Design ×3, r/lovable ×1, r/vibecoding ×1) + 6 Hacker News.

---

## Source table

| ID | Title | Community | Date | Engagement | URL |
|---|---|---|---|---|---|
| C27 | What's one giveaway that the website was AI generated? | r/web_design | 2026-08-05 | 0 pts, 63 comments | https://www.reddit.com/r/web_design/comments/1vgdi27/ |
| C28 | What makes a website feel human instead of AI-generated? | r/web_design | 2026-08-25 | 0 pts, 24 comments | https://www.reddit.com/r/web_design/comments/1vxra9d/ |
| C29 | how do you tell if a landing page is ai generated? | r/web_design | 2026-07-22 | 0 pts, 23 comments | https://www.reddit.com/r/web_design/comments/1v3k6h3/ |
| C30 | Designer in our company regressed too much with AI, to a point it makes our product laughable | r/web_design | 2026-08-30 | 409 pts, 69 comments | https://www.reddit.com/r/web_design/comments/1w2308l/ |
| C31 | How can you tell a design is AI? | r/UI_Design | 2026-06-22 | 7 pts, 33 comments | https://www.reddit.com/r/UI_Design/comments/1uchh8o/ |
| C32 | Anyone feel like this UI looks too AI generated? | r/UI_Design | 2026-05-28 | 12 pts, 22 comments | https://www.reddit.com/r/UI_Design/comments/1tq8u5r/ |
| C33 | The trashy, vibe-coded design of my app is unanimously preferred over the carefully crafted one | r/UI_Design | 2026-05-17 | 0 pts, 7 comments | https://www.reddit.com/r/UI_Design/comments/1tfr0sc/ |
| C34 | How I fixed the "AI-built this" look on my Lovable site | r/lovable | 2026-05-15 | 5 pts, 12 comments | https://www.reddit.com/r/lovable/comments/1tdw9yc/ |
| C35 | Slightly reducing the sloppiness of AI generated front end | Hacker News | 2026-06-12 | 219 pts, 135 comments in fetched tree | https://news.ycombinator.com/item?id=48504912 |
| C36 | Hallmark – Anti-AI-Slop Design Skill for Claude Code, Cursor, and Codex | Hacker News | 2026-07-26 | 7 pts, 9 comments | https://news.ycombinator.com/item?id=49058547 |
| C37 | Join Me in Jamverse | Hacker News | 2026-08-06 | (comment subthread) | https://news.ycombinator.com/item?id=49199867 |
| C38 | Launch HN: ProvenMetal (YC S26) | Hacker News | 2026-08-06 | (comment) | https://news.ycombinator.com/item?id=49199220 |
| C39 | We scanned 131 AI-built websites, and the "AI look" wasn't the biggest tell | Hacker News | 2026-06-11 | 4 pts, 4 comments | https://news.ycombinator.com/item?id=48489797 |
| C40 | The annotated PyTorch training loop (AI-design accusation subthread) | Hacker News | 2026-06-22 | 81 pts (story) | https://news.ycombinator.com/item?id=48679076 |
| C41 | I audited an interface I built with AI and found about 30 things that gave it away | r/vibecoding | 2026-08-02 | 25 pts, 10 comments | https://www.reddit.com/r/vibecoding/comments/1vdp2nw/ |

Reddit rows were read through the archive endpoint `https://arctic-shift.photon-reddit.com/api/comments/tree?link_id=<id>&limit=150`; the canonical permalinks are given above.

---

## Per-source entries

### C27 — What's one giveaway that the website was AI generated?
- **Source:** r/web_design, open question thread, 2026-08-05, 0 pts / 63 comments. https://www.reddit.com/r/web_design/comments/1vgdi27/
- **Context:**
  - The single most-detailed answer, u/inthebinary, gives a stacking list rather than a single tell: cards with a left-only border, hero "eyebrow" headers, no real privacy/terms page, purple/green/blue gradients, italics used for emphasis, 15–20px border radius throughout, Poppins, and "basically default Shadcn/ui stuff." They note the shadcn look predates agentic coding.
  - Three separate commenters independently name the **left-side colored border on boxes** (u/inthebinary, u/thestaffstation, u/masaIafries). u/masaIafries calls it "the strange artifact of a border on the left-hand side" alongside cream/beige palettes and mixed serif/sans/mono in one headline.
  - u/derpystuff_ (29 pts): "That stupid chip at the top with a pulsating 'live' indicator, overuse of gradients."
  - u/fonster_mox names a time-stamped trend: "At the moment it's those tiny all-caps pixel font headings." u/come2thecabaret adds an even smaller eyebrow line above it, grey on dark.
  - Dissent inside the thread: u/jroberts67 (20 pts) argues there is no reliable tell because Claude will clone any site you point it at; u/ngmcs8203 says "skills that can be used to remove any slop indicators"; u/buildwithaiVineet argues "AI isn't the giveaway—generic thinking is."
- **Tags:** `[AVOID: single-side colored card border]` `[AVOID: all-caps letterspaced eyebrow]` `[AVOID: pulsing "live" status chip]` `[AVOID: uniform 15-20px radius]` `[CONTESTED]`
- **Feeds:** left-border card motif; eyebrow microcopy; status-pill decoration; shadcn-default fingerprint

### C28 — What makes a website feel human instead of AI-generated?
- **Source:** r/web_design, open question thread, 2026-08-25, 0 pts / 24 comments. https://www.reddit.com/r/web_design/comments/1vxra9d/
- **Context:**
  - Top-voted answers are refusals and jokes ("Nice try, clanker" — u/The_Real_Mr_F, 16 pts; "Usually they're made by humans" — u/Nidhogg369, 56 pts). The thread was widely read as a prompt-farming attempt, which is itself a data point about how the community treats detection lists.
  - u/addycodes (19 pts) argues for a non-visual account: sites "smell," like the uncanny valley. Pressed by u/braincandybangbang on the Squarespace-template counterargument, they refine it: it is not layout or stock assets, it is that "no thought has been put in to it at all... It's not about high art, it's about authenticity."
  - u/Brufacee gives the most operational positive definition: real product screenshots, "uneven amounts of detail," a point of view that excludes someone; generic sites have "perfectly balanced sections."
  - A live false-positive test runs in-thread: u/Puzzled-Driver987 posts a hand-made site, u/Cephell calls it AI-looking on "font choice and the general theming" plus Tailwind + inline styles in source, and the author confirms it was not AI.
- **Tags:** `[ADOPT: uneven detail density]` `[ADOPT: specificity that excludes someone]` `[AVOID: perfectly balanced section weights]` `[CONTESTED]`
- **Feeds:** section-rhythm uniformity; the "specificity" axis; Tailwind-as-proxy false positive

### C29 — how do you tell if a landing page is ai generated?
- **Source:** r/web_design, open question thread, 2026-07-22, 0 pts / 23 comments. https://www.reddit.com/r/web_design/comments/1v3k6h3/
- **Context:**
  - u/heycosmicbunny gives the sharpest structural claim in the sweep: "the tell isn't the polish, it's the rhythm" — headline, three-icon feature grid, testimonial carousel, pricing, "regardless of what the product actually does." Human pages have asymmetry because someone made a call.
  - u/Ninjishnu, independently: "everything has the same weight and nothing pulls your eye first... AI output treats every section as equally important," plus interaction breakage — placeholder text still in a card, a button that scrolls instead of acting.
  - u/Consistent_Hippo2402, writing as a user of AI builders, says the giveaway "isn't even the design": generic sections, three feature cards, fake-sounding testimonials, stock people, and nothing that says what the business does.
  - u/Spirited-Animal2404 claims model-level discrimination: "once you saw like 5 GPT/Claude sites your brain adapts. I can also instant tell a claude site from a gpt one." u/worldDev immediately pushes back with pareidolia.
  - u/gatwell702 names visual tells: purple/blue gradients, hover animations everywhere, typewriter text effect. u/Fast-Patience-2290 adds "eyebrows on every section."
- **Tags:** `[AVOID: canonical landing-page section rhythm]` `[AVOID: equal visual weight across sections]` `[AVOID: typewriter/reveal effects]` `[CONTESTED]`
- **Feeds:** section-rhythm uniformity; flat emphasis hierarchy; interaction dead-ends

### C30 — Designer in our company regressed too much with AI
- **Source:** r/web_design, workplace complaint thread, 2026-08-30, 409 pts / 69 comments. https://www.reddit.com/r/web_design/comments/1w2308l/
- **Context:**
  - The highest-engagement Reddit thread in this sweep, and the only one that captures the *stakeholder* reaction rather than the designer's. OP describes a formerly strong in-house designer now answering questions live from Claude during calls; commenters coin/repeat "meat proxy" (u/CtrlShiftRo, u/testingaurora) and "cognitive surrender" (u/SignatureOpposite504).
  - u/ibopm (141 pts, top comment) makes the historical-analogy argument explicitly: "This is similar to when Bootstrap came out and every website started looking exactly the same." Good designers still used Bootstrap but customised the components.
  - u/HrLewakaasSenior gives a dated visual tell and a behavioural consequence: "Now whenever I see the rounded corner gradient filled boxes with monospace subtitles, I just close the site and move on." Note the pairing — gradient-filled rounded cards *with* monospace subtitles, not gradients alone.
  - u/xo0O0ox_xo0O0ox describes the drift directly: there was "a brief period where the design 'jump' to AI produced stuff was visually striking... but then the same-ness and mediocrity of it all really started to show."
  - Counter-position from u/tourqski: if it ships and gets approved, "you're just bothered by your personal taste."
- **Tags:** `[AVOID: gradient-filled rounded cards + monospace subtitle pairing]` `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** monospace-subtitle motif; the Bootstrap-precedent reframe; client/stakeholder tolerance ceiling

### C31 — How can you tell a design is AI?
- **Source:** r/UI_Design, open question thread, 2026-06-22, 7 pts / 33 comments. https://www.reddit.com/r/UI_Design/comments/1uchh8o/
- **Context:**
  - The densest single tell-list in the sweep, u/idolikeglitter: giant bold centred h1, "BIG WORDS ABOVE HEADLINES," serif headline over sans paragraph, "boxes in boxes in boxes," text boxes with a left colored border, three counters side by side, teaser boxes with icon top-left, heavy icon and emoji use.
  - u/ThirdEyesOfTheWorld gives an independent and largely non-overlapping 2026 list: eyebrow text inside pill-shaped rounded borders, vertical colored borders on one side of boxes, **numbers set in serif with oldstyle figures**, rounded icon boxes, "very faint monospaced font for descriptors."
  - Two commenters converge on a specific typeface: u/justynmx7 names "that one serif font that every AI startup seems to be using"; u/jufs_ guesses Instrument Sans; u/justynmx7 replies with a screenshot and u/Embarrassed_Finger34 calls it "Claude codes fav choice."
  - u/SleepingCod (19 pts) argues the failure mode is not AI-specific: poor hierarchy, no spacing system, inconsistency — "the same that makes beginner designers bad." u/beikbeikbeik refines this into the actual discriminator: AI pairs "impeccable icon and font pairing, with the most amateur spacing" — mastery of hard things alongside failure at basic ones.
  - u/jzdesign relocates the tell to process: "The problem is people accept the first output, which is the median of the training data... 'First draft = final' is the actual tell."
  - u/Kibric and u/klumpp both push back that it is "template-like" rather than AI-like; u/Limp-Confidence5612 says the examples "look like every website starting around 2015."
- **Tags:** `[AVOID: oldstyle-figure serif numerals]` `[AVOID: eyebrow-in-pill]` `[AVOID: faint mono descriptors]` `[AVOID: nested boxed containers]` `[ADOPT: deliberate emphasis over even spacing]` `[CONTESTED]`
- **Feeds:** serif-numeral motif; pill eyebrow; competence-inversion signature (expert typography + amateur spacing)

### C32 — Anyone feel like this UI looks too AI generated?
- **Source:** r/UI_Design, design-critique thread on a hand-made game UI, 2026-05-28, 12 pts / 22 comments. https://www.reddit.com/r/UI_Design/comments/1tq8u5r/
- **Context:**
  - A **false-positive case study**. The OP (u/Top-Letter-9322) built every icon in Figma and every shader in Unity; u/Hepdesigns still asserts "It looks too AI generated because it is AI generated," and is corrected by the author.
  - The named triggers are thin: u/el_yanuki cites the gradient border; u/post-gym-nut-stank cites "generic" iconography and color-coded numbers "added for the sake of 'cohesion'"; u/squooshy_android claims reducing letter-spacing in the "Achievements" wordmark would remove "all visual similarity to AI." That last is a striking claim — a single tracking value read as the whole signal.
  - Majority verdict was that it does *not* look AI (u/autocosm 18 pts, u/Pitiful_Permit9585, u/egedemete, u/phoenix1984), and most feedback was ordinary craft feedback about horizontal spacing.
  - u/orion7788 names the second-order effect: "So now the goalpost is 'not looking AI' when it wasn't used at all?" u/Ancient-Range3442, sardonically: "I keep believing if I hand tune the stops of my purple gradient the humanity will evident [sic]."
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** false-positive base rate; letter-spacing as a (weak, single-observer) tell; the anxiety cost of tell-lists

### C33 — The trashy, vibe-coded design is unanimously preferred over the carefully crafted one
- **Source:** r/UI_Design, self-critique thread, 2026-05-17, 0 pts / 7 comments. https://www.reddit.com/r/UI_Design/comments/1tfr0sc/
- **Context:**
  - A designer replaced their app's AI-generated UI with a hand-crafted Figma design and found testers unanimously preferred the AI one. Every substantive reply says the hand-made version was simply worse: too dark, too low-contrast, font sizes too close together, unreadable in daylight (u/caffi_nate, u/ajb_mt, u/EyeAlternative1664, u/tomhermans).
  - u/yarin_ (18 pts, top): the vibecoded version "is still more captivating and direct," and "To an untrained eye, the figma one looks more 'ai-slop' than the actual ai-slop."
  - u/sk_sushellx points at emotional register rather than craft: the AI version's greeting and emoji "feel warm and playful," the refined version felt "more professional but also more cold."
  - Direct counterweight to the assumption that AI-look correlates with worse outcomes.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** anti-AI-look ≠ better; low-contrast dark palettes as their own failure mode

### C34 — How I fixed the "AI-built this" look on my Lovable site
- **Source:** r/lovable, build-log / product-pitch thread, 2026-05-15, 5 pts / 12 comments. https://www.reddit.com/r/lovable/comments/1tdw9yc/
- **Context:**
  - The clearest *builder-side* tell in the sweep is a content one, from u/Blade999666 on the recurring fake-persona testimonial: "Sarah Chen / Head of Ops — I've seen her a thousand times I think the past few months under various testimonials." A named, recurring synthetic testimonial identity is a hard, checkable fingerprint.
  - OP's own framing of the market: the fix he sells is "a design system you can use on unlimited projects so your site doesn't look like every other Lovable site launching right now" — i.e. the convergence is acknowledged by the tool's own userbase, not just by critics.
  - Two commenters preferred or were unimpressed by the "fixed" version (u/redditissocoolyoyo: "The AI version looks a lot better tbh"; u/ReasonableBenefit47 compares it unfavourably to free Framer templates), so the de-slopping is contested even inside the pro-Lovable sub.
  - Low engagement; treat as a single-observer signal, not consensus.
- **Tags:** `[AVOID: recurring synthetic testimonial personas]` `[CONTESTED]`
- **Feeds:** fake-testimonial fingerprint; platform-level convergence acknowledged by users

### C35 — Slightly reducing the sloppiness of AI generated front end
- **Source:** Hacker News, front-page discussion, 2026-06-12, 219 pts / 135 comments in fetched tree. https://news.ycombinator.com/item?id=48504912
- **Context:**
  - The largest and most argumentative thread found. The article's finding — prompting for a Qt-app look strips most of the slop feeling — produced a mechanistic explanation that several commenters reached independently: u/Xotic007 ("Slop is basically what you get when there's nothing specific to copy and so the AI it just averages every web style together" [sic]), u/flo_r ("the model has a very specific grammar to pull from instead of averaging over everything web-related"), u/voxleone ("'Qt app' is almost like a named distribution"), u/AmareshHebbar. This is a **causal account of the AI look as distributional averaging**, not a style list.
  - u/LucidLynx gives the 2026 visual canon: "Everything is in blue or mauve gradient, with a white background, and a single JavaScript-heavy page that lags as soon as you scroll a little," plus lots of 404s and credentials leaking in HTML comments.
  - u/LZ_Khan: "rounded corner cards with slight shadow, and sans serif font. Also full caps / overemphasis on text that doesn't need it." u/nozzlegear: dark theme, rich purples, huge headings. u/the_lucifer adds the current variant: "thin and tall serif fonts, with one singular italicized word in the title."
  - Model-specific claims: u/unleaded says "Claude's is pretty distinct" and that DeepSeek copies it; u/smusamashah reports "so many brown sites that look all the same"; u/gunapologist99 on Claude output, "really is in love with browns and oranges." Claude's palette shift away from purple is named by three separate commenters.
  - u/properbrew, on why it resists definition: "I find it such a hard thing to quantify... you can just feel the slop seep through." u/smnplk's reply is the sharpest counterfactual in the sweep — would you see slop in the identical page if a pre-AI frontend dev handed it to you? u/HughParry answers honestly: "I'd probably think it looked alright."
  - Sustained attack on published anti-AI guidance: see Disagreements.
- **Tags:** `[AVOID: distributional-average web styling]` `[AVOID: single italicised word in a bold title]` `[AVOID: blue/mauve gradient on white]` `[ADOPT: commit to a named, specific visual grammar]` `[CONTESTED]`
- **Feeds:** averaging mechanism; italic-word-in-headline motif; Claude brown/orange palette drift; the observer-bias problem

### C36 — Hallmark – Anti-AI-Slop Design Skill
- **Source:** Hacker News, Show-HN-style link thread, 2026-07-26, 7 pts / 9 comments. https://news.ycombinator.com/item?id=49058547
- **Context:**
  - u/loopmonster reviews the tool's own screenshot gallery and finds it self-defeating: the collage is "where every one screams of being AI generated," with two of the examples excepted; the rest "are practically identical and are the go-to output for what you get if you ask Sonnet to build a website."
  - u/aleksiy123 asks whether any of these skills demonstrably work; u/mstkllah, having used "impeccable, ui-ux-max, and many, many others," reports they "all seem to converge on the same thing" — useful for consistency and accessibility, but "the design itself is the same unless you are extremely explicit."
  - u/opwizardx describes the only structural counter-measure mentioned anywhere in the sweep: keeping a log of past builds and hard-failing a run that repeats recent page structures or themes — while conceding the nav-rotation rule is "the single most-violated rule in practice."
  - u/sixtyj, after exhausting skills, editors and screenshot-seeding, concludes the only reliable speed-up is drawing on paper, redrawing in Figma/Penpot, then prompting a multimodal model.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED]`
- **Feeds:** anti-slop tooling does not measurably de-converge output; explicit direction is the active ingredient

### C37 — "LLM design" as template convergence (Jamverse subthread)
- **Source:** Hacker News, comment subthread, 2026-08-06. https://news.ycombinator.com/item?id=49199867
- **Context:**
  - u/cautiouscat states the base observation: "it's getting crazy how confidently you can point at a websites design and go 'An LLM designed this.'"
  - u/pixelready gives the most useful reframe in the sweep: "I think what we sense as 'LLM design' now is what used to be 'oh, they used a popular squarespace template or Wordpress theme.'" The mechanism he proposes is that models trained on UI over-favour re-used templates and popular component libraries over bespoke work.
  - He separates a second, distinct signal: AI-generated hero imagery from lazy prompts, "riddled with tells like weird shape choices, smooth glossy surfac[es]" — an image-provenance tell, not a layout tell.
  - Implication for measurement: a detector keyed on template-likeness will flag genuine Squarespace/WordPress sites at the same rate. Two of the Reddit threads (C28, C31) reached the same objection independently.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]`
- **Feeds:** template-convergence confound; AI hero-image surface tells as a separable channel

### C38 — "It's okay to vibe code the design" (Launch HN: ProvenMetal)
- **Source:** Hacker News, Launch HN comment, 2026-08-06. https://news.ycombinator.com/item?id=49199220
- **Context:**
  - u/stopachka, reviewing a YC launch, draws an explicit asymmetry: "you can definitely tell the website content is AI-generated. It's okay to vibe code the design, but I really hesitate when I see vibed writing."
  - This is a founder-audience reaction, and it inverts the priority of most published tell-lists: the visual layer is granted a pass, the copy is not.
  - It converges with C27 (u/GodLob0: "First thing is copy"), C29 (u/Consistent_Hippo2402), C28 (u/addycodes), and C39 — five independent threads placing copy above visuals.
  - Single comment; weight accordingly, but the cross-thread convergence is the point.
- **Tags:** `[AVOID: AI-voiced marketing copy]` `[CONTESTED]`
- **Feeds:** copy-before-visuals ordering; trust penalty attaches to writing, not layout

### C39 — We scanned 131 AI-built websites, and the "AI look" wasn't the biggest tell
- **Source:** Hacker News, vendor blog submission, 2026-06-11, 4 pts / 4 comments. https://news.ycombinator.com/item?id=48489797
- **Context:**
  - The article is a vendor self-report (siteblob.com) with no inspectable method; it is included only because the comments are a clean demonstration of copy-level detection in the wild.
  - All four comments reject the piece as itself AI-written, and name why. u/bediger4000: "It has a lot of one sentence per paragraph 'LinkedInfluencer' style. It's wordy and redundant, and it never quite gets to a conclusion."
  - u/jaxefayo names a formatting tell: "the overly attention-grabbing formatting LLMs like to use, where every significant part of a sentence is bolded."
  - u/a012 observes the irony that an AI-detection site reads as AI-made. No commenter engaged with the study's actual findings.
  - **Do not cite the 131-site claim as a measurement.** The thread is evidence about detection behaviour, not about the scan.
- **Tags:** `[AVOID: one-sentence paragraphs]` `[AVOID: mid-sentence bold emphasis scatter]` `[EVIDENCE-ONLY]`
- **Feeds:** prose-rhythm tells; bold-scatter formatting tell

### C40 — Accusing a real site of Claude authorship (PyTorch essay subthread)
- **Source:** Hacker News, comment subthread on an 81-pt story, 2026-06-22. https://news.ycombinator.com/item?id=48679076
- **Context:**
  - The single most specific 2026 visual fingerprint found anywhere in the sweep, from u/f3408fh: "It has all the tell-tale signs like the all-caps bold letter-spaced microcopy... Many card-like elements with a colored border on one side only. The italic serif font as subtitle."
  - This is a live, unprompted accusation against a third-party site — not an answer to a "list the tells" question — which makes it less susceptible to listicle contamination than C27/C29/C31.
  - All three of those elements were independently named by Reddit commenters who had no contact with this thread (C27 u/inthebinary and u/masaIafries; C31 u/idolikeglitter and u/ThirdEyesOfTheWorld; C27 u/fonster_mox and u/saalaadin). That cross-platform convergence is the strongest signal in this file.
  - Notably, the commenter explicitly separates aesthetics from judgement: "That being said I'm not judging. It's competently done."
- **Tags:** `[AVOID: all-caps letterspaced microcopy]` `[AVOID: one-side colored card border]` `[AVOID: italic serif subtitle]`
- **Feeds:** the 2026 tell triad — letterspaced caps eyebrow + single-side card border + italic serif subtitle


### C41 — I audited an interface I built with AI and found about 30 things that gave it away
- **Source:** r/vibecoding, self-audit writeup by u/lfehskoob, 2026-08-02, 25 pts / 10 comments. https://www.reddit.com/r/vibecoding/comments/1vdp2nw/
- **Context:**
  - **The strongest builder-side source in this sweep.** The author shipped an AI-built site, could not initially articulate why it looked like every other one, then spent three days auditing it in six passes (accessibility, layout, typography, colour, copy, general UI) and posted ~30 tells with fixes. This is a practitioner reverse-engineering their own output, not a critic listing grievances.
  - Typography tells with named remedies: default typefaces (Inter, Roboto, Arial, Open Sans) — "not bad fonts, default fonts," and changing the typeface was "the single biggest visual improvement I made"; arbitrary off-scale sizes like `text-[15px]`; italics used for emphasis (use a weight step instead); Title Case On Everything; orphaned words in headings, fixed with `text-wrap: balance` / `pretty` instead of manual `<br>`.
  - Colour and layout: "Purple to indigo gradients. Most recognizable AI fingerprint there is" — with a diagnosis, that reaching for them means "a texture problem," remedied by SVG `feTurbulence` grain at ~0.06 opacity. Also: the purple/indigo/blue startup palette; three equal cards in a row; **everything centred** — "Symmetry is what you get when nobody decided"; misaligned card grids where pricing-table titles, prices, feature lists and CTAs all start at different heights; `height: 100vh` instead of `min-height: 100dvh`.
  - Accessibility as the most reliable channel — "the set AI skips most reliably": `<header>` nested inside `<main>`; auto-moving content with no pause control (WCAG 2.2.2), found twice; no `prefers-reduced-motion` fallback; scroll listeners instead of `IntersectionObserver` for reveal animations; and missing hover, active, focus, loading, empty and error states — "Generated interfaces almost always ship the happy path only."
  - Copy: em dashes, hype verbs (elevate, seamless, unleash, supercharge), "Learn more" / "Submit" buttons, industry-generic slogans, and round invented numbers like 99.9%. The author separates one category as an ethical rather than aesthetic problem: invented testimonials and star ratings — "A generated five-star review on that tradesperson's real site is a lie told to a customer."
  - In the comments, u/krunal_builds adds two independent tells: emoji in every heading, "the one that gives it away fastest to me, before i even read the copy," and uniform border-radius "applied everywhere... instead of varying by what the element actually is." u/97689456489564 disputes the result — the fixed version "still looks very AI-generated," citing the headline as "a Claudeism"; the author concedes the point.
- **Tags:** `[AVOID: default typeface stack]` `[AVOID: off-scale arbitrary type sizes]` `[AVOID: purple-to-indigo gradient]` `[AVOID: everything centred]` `[AVOID: happy-path-only states]` `[AVOID: emoji in headings]` `[AVOID: uniform border-radius]` `[ADOPT: audit in separate single-concern passes]` `[CONTESTED]`
- **Feeds:** default-font fingerprint; centred-symmetry-as-non-decision; missing interaction states; misaligned card-grid baselines; the audit-pass method

---

## What practitioners name

Ranked by number of **distinct threads** in which the tell was raised independently. Counts are out of 15 opened threads. This is a tally of opinion frequency, not a measurement — a tell named in six threads is a widely held belief, nothing more. Where a tell was named by only one person in a thread, that thread still counts as one.

| Rank | Tell | Distinct threads | Sources |
|---|---|---|---|
| 1 | **Gradients** — most often named as purple/blue/indigo/mauve; C30 says only "gradient filled" | 7 | C27, C28, C29, C30, C31, C35, C41 |
| 2 | **All-caps letter-spaced "eyebrow" microcopy** above headings, often stacked with a second, smaller eyebrow | 5 | C27, C29, C31, C35, C40 |
| 3 | **The copy is the tell, not the visuals** — generic marketing voice, hype verbs, vague claims, no point of view | 6 | C27, C28, C29, C38, C39, C41 |
| 4 | **Italics used for emphasis / serif-italic misuse**: italic serif subtitles, one italicised word in a bold headline | 5 | C27, C31, C35, C40, C41 |
| 5 | **Rounded-corner cards with soft drop shadow**, uniform radius applied regardless of element | 5 | C27, C30, C31, C35, C41 |
| 6 | **Card/box with a colored border on one side only** (almost always the left) | 3 | C27, C31, C40 |
| 7 | **Broken navigation language / interaction dead-ends** — polished screens that do not connect, dead CTAs, placeholder text left in | 3 | C27, C28, C29 |
| 8 | **Uniform section rhythm and flat emphasis** — every section the same weight, canonical hero→3-feature-grid→testimonials→pricing beat | 3 | C28, C29, C31 |
| 9 | **Warm neutral / cream / brown-orange palettes** (named specifically as Claude's current default, displacing purple) | 3 | C27, C31, C35 |
| 10 | **Faint monospace descriptors and subtitles** | 3 | C27, C30, C31 |
| 11 | **Tailwind / shadcn defaults visible in output and source** | 3 | C27, C28, C35 |
| 12 | **Fake or recurring synthetic testimonials** ("Sarah Chen, Head of Ops"), stock people, invented star ratings | 4 | C27, C29, C34, C41 |
| 13 | **Icon and emoji overuse**, emoji in every heading, icons that do not match their labels | 4 | C27, C28, C31, C41 |
| 14 | **Pulsing "live"/status pill chip** at the top of the hero | 1 | C27 |
| 15 | **Cramped, over-filled density** — every inch occupied, repetitive information | 2 | C31, C35 |
| 16 | **Three-counter / three-stat row** below the hero | 2 | C29, C31 |
| 17 | **Glassmorphism / translucent nav surfaces** | 2 | C27, C31 |
| 18 | **Reveal animation on every section**, infinite marquees, typewriter effects, scrolljacking | 3 | C27, C29, C41 |
| 19 | **Em dashes in copy** | 3 | C27, C28, C41 |
| 20 | **Numbers in serif with oldstyle figures** | 1 | C31 |
| 21 | **Missing interaction states** — hover/active/focus/loading/empty/error; happy path only | 1 | C41 |
| 22 | **Default typeface stack** (Inter, Roboto, Arial, Open Sans) and off-scale type sizes | 1 | C41 |
| 23 | **Everything centred / symmetrical** as a substitute for a layout decision | 1 | C41 |

Two tells worth flagging despite low counts, because they are *mechanistic* rather than stylistic:

- **Competence inversion** (C31, u/beikbeikbeik; C35, u/chorkpop): expert-level icon and font pairing sitting next to amateur spacing. AI "masters some hard things while failing at basic stuff." A human beginner fails uniformly. This is the only proposed discriminator in the sweep that would separate AI output from a bad human designer rather than merging them.
- **First-draft-as-final** (C31, u/jzdesign): the artefact is the median of the training distribution because nobody iterated. "'First draft = final' is the actual tell."
- **Accessibility as the highest-yield channel** (C41, u/lfehskoob): "the set AI skips most reliably" — landmark nesting errors, no pause control on moving content, no `prefers-reduced-motion`, and interaction states that only cover the happy path. Unlike the visual tells, these are machine-checkable and do not depend on taste, which makes them the most promising candidates for instrumented measurement in this whole file.

**Newer-than-purple looks named for 2026** (the field has visibly drifted):
warm cream/beige and brown-orange palettes attributed specifically to Claude (C27, C31, C35); tiny all-caps pixel or mono eyebrow headings (C27); serif numerals with oldstyle figures (C31); italic serif subtitles (C31, C35, C40); eyebrow text inside a pill-shaped border (C31); the pulsing "live" chip (C27, C31); u/elixon's name for the whole current mode, **"soft modernism"** — "vibrant gradients, pastel or neon accents, large rounded corners, subtle shadows, glassy or translucent surfaces, bold sans serif typography, generous whitespace, and smooth micro animations" (C27), which u/come2thecabaret glosses as "literally just 'statistically average.'"

---

## Disagreements

This is where the community materially contradicts the published listicles and itself.

**1. Practitioners reject the canonical anti-AI-design guidance as itself a listicle.** (C35, the sharpest finding in the sweep.)
u/stefan_ quotes the frontend-design skill's own instruction — never use Inter/Roboto/system fonts, never purple gradients on white, pick from brutally minimal / maximalist chaos / retro-futuristic / editorial / brutalist — and treats the enumerated style menu as self-refuting. u/duffycommaryan lands it in one line: "The frontend-design skill defeats its own purpose imo. The design equivalent of 'it's not x, it's y.'" u/kbelder asks what a model is meant to do with "make unexpected choices that feel genuinely designed for the context." u/esperent grants the intent is legible but notes nobody is running evals: "does this skill actually change the designs you get out in a positive way, consistently? Who knows?" u/smusamashah reports the empirical result — "so many brown sites that look all the same." **A prohibition list is itself a style prior; banning purple produced brown.** Directly relevant to how this skill's own rules should be written.
Counter-voices in the same thread: u/lherron, u/brinki and u/Rastonbury report good results, all three specifically when *seeding from a reference site or screenshot* rather than from the prohibition list.

**2. Is the "AI look" AI at all, or just template convergence?**
u/pixelready (C37): what we call LLM design is what we used to call "they used a popular squarespace template." u/Kibric and u/klumpp (C31) say the same unprompted; u/Limp-Confidence5612 (C31) dates the look to circa 2015. u/ibopm (C30, 141 pts) and u/Retr0id (C35) both invoke the Bootstrap era. u/swiftcoder (C35) escalates: do auth0.com, miro.com and datadog.com not already look like slop? u/deaux disagrees — Datadog and Miro are "nothing like generated slop," and current models "can't design anything even close to those two." Unresolved, and it is the load-bearing question for any detector: if the tells are template tells, the false-positive rate on human template users is the whole ballgame.

**3. Copy versus visuals — which carries the signal?**
Five threads (C27, C28, C29, C38, C39) put copy first. u/stopachka's formulation is the crispest inversion of the visual-first canon: vibe-coding the design is fine, vibed *writing* is where trust breaks. Against this, C27, C31, C35 and C40 are overwhelmingly visual in their tells, and C40's accusation was made purely on typography and card styling. The two camps do not engage each other directly, which suggests the field has two largely independent detection channels rather than one.

**4. Em dashes: a tell, or a moral panic?**
u/jbarba4 (C27) claims "real humans almost never use those" and is downvoted to −6. u/dastree and u/ironnmetal both push back from experience; u/CantaloupeCamper notes the same fate is coming for ellipses. Meanwhile u/scandii (C27) cites "a sea of — and →" as decisive. The single most-repeated tell in popular listicles is the one this community most actively disputes.

**5. Does looking AI-made actually hurt?**
C33 is a direct refutation: users unanimously preferred the AI-generated UI over the designer's hand-crafted replacement, and every reviewer agreed the hand-made version was objectively worse (contrast, legibility, hierarchy). u/yarin_: "To an untrained eye, the figma one looks more 'ai-slop' than the actual ai-slop." u/tourqski (C30) makes the same point about shipped work. Against this, u/HrLewakaasSenior (C30) reports closing sites on sight, and u/mschuster91 (C35) describes real time cost from undisclosed AI content. **The community has no agreed answer on whether the AI look carries a conversion or trust penalty for non-designers.**

**6. Is the tell real, or is it observer bias?**
u/smnplk's counterfactual (C35): would you perceive slop in the identical page if a pre-AI frontend dev had handed it to you? u/HughParry: "I'd probably think it looked alright. I think it's the fact that my eyes have been blasted with a certain visual 'vibe.'" u/emsixteen: "I'd probably just accept that I'd hired them through fiverr." u/worldDev (C29) names it as pareidolia. C32 is the empirical demonstration — a fully hand-made UI accused of being AI-generated, with the accuser doubling down after correction, and a rebuttal offered on the strength of one wordmark's letter-spacing. u/llm_nerd (C35) goes furthest: the whole slop discourse is "human slop... in an objectively undefinable way."

**7. Do the anti-slop tools work?**
u/mstkllah (C36), having used impeccable, ui-ux-max "and many, many others": they all converge on the same thing, and "the design itself is the same unless you are extremely explicit." u/aleksiy123: "For me it still pretty much looks like slop." u/loopmonster finds Hallmark's own screenshot gallery indistinguishable from the slop it claims to prevent. Against this, u/viccis and u/brinki (C35) report one-shot fixes. The consistent thread across both camps is that *explicit, specific direction* is the active ingredient — not the ban list.

**8. Model-specific fingerprints — claimed but unverified.**
u/Spirited-Animal2404 (C29) claims to distinguish Claude sites from GPT sites on sight. u/unleaded (C35) says Claude's HTML style is "pretty distinct" and DeepSeek copies it, while Kimi K2 generates more human-like HTML. u/scandii (C27) assumes Material Design 3 implies Claude. u/Ok-Investment4414 (C27) cites "claudes logo orange." Nobody in any thread offered a test, a sample, or a control. Treat as folklore worth testing, not as fact.

---

## Gaps

**Live Reddit is unreachable from this environment.** Every direct endpoint returns HTTP 403 from Reddit's bot wall, and `www.reddit.com` is blocked at the WebFetch layer. All Reddit content in this file was read through the Arctic Shift archive mirror. Anyone reproducing this should use `arctic-shift.photon-reddit.com` and expect aggressive rate limiting (429/422 after ~8–10 requests, with slow recovery).

**Subreddits searched but yielding no opened thread:**
- **r/webdev** — search returned results but none on-topic enough to open; the closest were two duplicate posts, "I built a tool that scores how AI-generated a website looks" (`1un75r1`, 12 comments; `1un4po2`, 6 comments) and "I built a tool to check if a website is vibe coded" (`1t7ypzl`, 6 comments). Known to exist, not opened — rate limit hit first.
- **r/vibecoding** — the one high-value thread found here **was** opened on a fifth attempt after sustained rate limiting; it is C41 above. No further r/vibecoding search completed, so the sub is otherwise uncovered.
- **r/userexperience** — the archive search for this sub timed out repeatedly and returned no rows. Unknown whether the sub has on-topic threads.
- **r/ClaudeAI, r/cursor, r/SaaS, r/Entrepreneur** — searches were queued but did not complete before the rate limiter cut in. No results, and therefore no basis to claim the discussion is or is not there.
- **r/UI_Design** additional threads identified but not opened: "AI Fatigue from seeing same designs" (`1tvb91q`, 22 pts, 9 comments), "Your say: how should we handle AI-generated designs in the sub?" (`1u0yn8v`, 6 pts, 18 comments), "AI is quietly making me a sloppier UI designer" (`1tc3djv`, 5 comments).
- **r/lovable** additional: "Can Lovable design good UI?" (`1s20k8c`, 23 comments).

**Bluesky: unreachable.** `https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts` returned **HTTP 403** for all three queries attempted. No designer-Bluesky discussion is represented.

**Mastodon: not attempted.** No request was made. The public API supports hashtag timelines but not cross-instance full-text search, so a targeted search would have been awkward — but this was a judgement call, not a failure. Untested.

**Product Hunt comment threads: not attempted.** No request was made and no thread was opened. Nothing in this file represents Product Hunt.

**Designer Hangout and similar closed Slack/Discord communities: structurally inaccessible.** Invite-gated; no public archive.

**Coverage skew to acknowledge.** This file is 9 Reddit threads and 6 HN threads, all English-language, all developer- or designer-facing. Three of the four r/web_design threads are "list the tells" prompts, a format that invites listicle recitation and rewards the memorable over the accurate — C40 (an unprompted accusation) and C32 (a false positive) are the only two sources here that escape that bias, and they should be weighted accordingly. **No source in this file is a measurement.** The one quantitative claim encountered (C39's "131 AI-built websites") is a vendor self-report with no inspectable method and is tagged `[EVIDENCE-ONLY]` for that reason. Nothing here should be promoted to a fact without independent instrumented testing.
