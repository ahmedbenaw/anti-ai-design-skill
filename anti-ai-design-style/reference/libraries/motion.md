# Animation libraries — porting notes for the anti-AI-slop design skill

Research date: 2026-09-04. Everything below was read from the live docs/source at the URLs
given; API names and code are quoted, not reconstructed from memory.

Two framing rules that apply to all four and should survive the port:

1. **The register's tells are not bugs in these libraries — they are the libraries' most
   discoverable features.** Every one of the four ships a first-class, one-line API for
   fade-up-on-scroll, hover-scale, infinite pulse, marquee, and particle backgrounds. The
   default path through each library's own docs/homepage lands on the tell. Guidance must
   name the specific API, not just say "use animation tastefully".
2. **Only one of the four ships reduced-motion by default** (animate.css, and even then only
   for its own `.animate__animated` class). GSAP and anime.js give you an opt-in mechanism;
   animate-ui gives you nothing and you must add it yourself.

---

# GSAP

## What it is / licence / current version

- **What:** JavaScript animation engine (tweens, timelines, plugins) for DOM, SVG, canvas and
  arbitrary JS objects. Framework-agnostic. Powers Webflow Interactions — per the official
  skill: *"GSAP powers **Webflow Interactions**. Code generated or run by Webflow's interaction
  system is GSAP-based."* (`skills/gsap-core/SKILL.md`)
- **Version: 3.15.0** — verified on `https://registry.npmjs.org/gsap/latest` and
  `https://api.cdnjs.com/libraries/gsap?fields=version`; `https://gsap.com/docs/v3/Installation`
  also shows v3.15.
- **LICENCE — correct the common claim. GSAP is NOT MIT.** The npm `license` field for
  `gsap@3.15.0` is literally:
  `"Standard 'no charge' license: https://gsap.com/standard-license."`
  `@gsap/react@2.1.2` reads `"SEE LICENSE AT https://gsap.com/standard-license"`.
  `https://gsap.com/standard-license` is a **proprietary Webflow licence**, not OSI open source.
  It is free including commercial use — *"Can I really use GSAP in commercial projects without
  paying anything? Yes, really! Commercial usage is covered under the standard license."* — but
  it carries a **Prohibited Uses** clause: you may not use GSAP in *"tools that allow users to
  build visual animations without code that encourages, induces, or materially assists in
  creating a solution that competes with Webflow's visual animation building capabilities"*, may
  not reverse engineer for competitive products, and may not remove proprietary notices.
- **What *is* MIT:** the *skills repo* `greensock/gsap-skills` — `LICENSE` reads
  `MIT License / Copyright (c) 2026 GreenSock`, and each `SKILL.md` frontmatter says
  `license: MIT`. That is the licence on the *documentation*, not on the engine. Do not
  propagate "GSAP is MIT" from the SKILL.md frontmatter.
- **What genuinely changed under Webflow:** every plugin is now free. From
  `skills/gsap-plugins/SKILL.md`: *"Every GSAP plugin is **free**, including for commercial use.
  Since Webflow's acquisition of GSAP, Club GSAP is no longer a paid tier and **no plugin
  requires a membership, license key, or auth token** — this includes formerly Club-only plugins
  (**SplitText**, **MorphSVG**, etc.)."* and *"❌ Do **not** generate an `.npmrc` with a GreenSock
  auth token, suggest the private `npm.greensock.com` registry, or tell users to sign up for
  Club GSAP to access a plugin. Those instructions are outdated."*

Official agent skills repo: `https://github.com/greensock/gsap-skills` —
8 skills: `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-utils`,
`gsap-react`, `gsap-performance`, `gsap-frameworks`.

## Install

```bash
npm install gsap            # everything, all plugins included
npm install @gsap/react     # useGSAP() hook, React only
```

CDN (verified HTTP 200):

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js"></script>
```

The skills themselves (agent-side, optional):

```bash
npx skills add https://github.com/greensock/gsap-skills
# Claude Code: /plugin marketplace add greensock/gsap-skills
```

## Core API

All snippets below are copied from the official `SKILL.md` files or `gsap.com/docs/v3`.

**1 — the four tween methods (`gsap-core`)**

```javascript
gsap.to(targets, vars);              // animate from current state to vars
gsap.from(targets, vars);            // animate from vars to current state (entrances)
gsap.fromTo(targets, fromVars, toVars); // explicit start and end
gsap.set(targets, vars);             // apply immediately (duration 0)
```

**2 — transform aliases + `autoAlpha` + directional rotation (`gsap-core`)**

```javascript
gsap.to(".box", { x: 100, rotation: "360_cw", duration: 1 });
gsap.to(".fade", { autoAlpha: 0, duration: 0.5, clearProps: "visibility" });
gsap.to(svgEl, { rotation: 90, svgOrigin: "100 100" });
```
`autoAlpha` also sets `visibility: hidden` at 0, so faded-out elements stop eating clicks —
this is the accessibility-relevant one. `x/y/scale/rotation/xPercent/yPercent/skewX/skewY`
are the transform aliases; the docs say prefer them over raw `transform` strings and over
`width/height/top/left`.

**3 — timeline with position parameter (`gsap-timeline`)**

```javascript
const tl = gsap.timeline({ defaults: { duration: 0.5, ease: "power2.out" } });
tl.to(".a", { x: 100 }, 0)          // absolute: at 0s
  .to(".b", { y: 50 }, "+=0.5")     // 0.5s after previous end
  .to(".c", { opacity: 0 }, "<")    // same start as previous
  .to(".d", { scale: 2 }, "<0.2");  // 0.2s after previous start
```

**4 — ScrollTrigger, scrub vs toggleActions (`gsap-scrolltrigger`)**

```javascript
gsap.to(".box", {
  x: 500,
  scrollTrigger: {
    trigger: ".box",
    start: "top center",   // "triggerPosition viewportPosition"
    end: "bottom center",
    toggleActions: "play reverse play reverse" // onEnter onLeave onEnterBack onLeaveBack
  }
});
```
Docs: *"✅ Use **scrub** for scroll-linked progress or **toggleActions** for discrete
play/reverse; do not use both on the same trigger."* and *"If both exist, **scrub** wins."*

**5 — `ScrollTrigger.batch()` (`gsap-scrolltrigger`)** — the single highest-slop-risk API here

```javascript
ScrollTrigger.batch(".box", {
  onEnter: (elements, triggers) => {
    gsap.to(elements, { opacity: 1, y: 0, stagger: 0.15 });
  },
  onLeave: (elements, triggers) => {
    gsap.to(elements, { opacity: 0, y: 100 });
  },
  start: "top 80%",
  end: "bottom 20%"
});
```

**6 — Flip (`gsap-plugins`)** — the genuinely valuable one

```javascript
gsap.registerPlugin(Flip);
const state = Flip.getState(".item");
// change DOM (reorder, add/remove, change classes)
Flip.from(state, { duration: 0.5, ease: "power2.inOut" });
```
Vars: `absolute`, `nested`, `scale` (default `true`), `simple`, `duration`, `ease`.

**7 — Draggable + Inertia (`gsap-plugins`)**

```javascript
gsap.registerPlugin(Draggable, InertiaPlugin);
Draggable.create(".box", { type: "x,y", bounds: "#container", inertia: true });
Draggable.create(".knob", { type: "rotation" });
```
`type`: `"x" | "y" | "x,y" | "rotation" | "scroll"`. Callbacks `onDragStart/onDrag/onDragEnd`,
`onThrowUpdate/onThrowComplete`.

**8 — DrawSVG (`gsap-plugins`)** — SVG line drawing, value is a *visible segment*, not a range over time

```javascript
gsap.registerPlugin(DrawSVGPlugin);
gsap.from("#path", { duration: 1, drawSVG: 0 });                     // draw in
gsap.fromTo("#path", { drawSVG: "0% 0%" }, { drawSVG: "0% 100%", duration: 1 });
gsap.to("#path", { duration: 1, drawSVG: "20% 80%" });               // gaps at both ends
```
Requires a visible `stroke` + `stroke-width` or nothing renders.

**9 — SplitText with `autoSplit` + `onSplit` (`gsap-plugins`)**

```javascript
gsap.registerPlugin(SplitText);
SplitText.create(".split", {
  type: "lines",
  autoSplit: true,
  onSplit(self) {
    return gsap.from(self.lines, { y: 100, opacity: 0, stagger: 0.05, duration: 0.5 });
  }
});
```
`onSplit()` is v3.13.0+; returning the tween lets SplitText revert and time-sync it on re-split.

**10 — `gsap.quickTo()` for high-frequency updates (`gsap-performance`)**

```javascript
let xTo = gsap.quickTo("#id", "x", { duration: 0.4, ease: "power3" }),
    yTo = gsap.quickTo("#id", "y", { duration: 0.4, ease: "power3" });
document.querySelector("#container").addEventListener("mousemove", (e) => {
  xTo(e.pageX);
  yTo(e.pageY);
});
```

**11 — React (`gsap-react`)**

```javascript
import { useGSAP } from "@gsap/react";
gsap.registerPlugin(useGSAP);

useGSAP(() => {
  gsap.to(".box", { x: 100 });
}, { scope: containerRef });   // cleanup + revert on unmount is automatic
```

## ADOPT — what GSAP earns its place for

- **FLIP layout transitions.** `Flip.getState()` → mutate DOM → `Flip.from()`. This is the one
  thing that is genuinely hard to hand-roll and that reads as *not* AI-generated: a list
  reordering, a card expanding into a detail view, a grid→list toggle where every item travels
  from its real old box to its real new box. Nothing about it is decorative.
- **Interruptible, reversible state.** Store the tween/timeline and `.pause()/.reverse()/
  .progress()/.kill()`. A menu that reverses mid-open instead of queueing is the difference
  between "designed" and "generated".
- **Physical continuity via Draggable + InertiaPlugin.** Real throw/flick with `bounds` and
  `edgeResistance`, or `InertiaPlugin.track(el, "x")` then `gsap.to(obj, { inertia: { x: "auto" } })`
  to glide to a stop from the *actual* current velocity. Continuity of momentum from the user's
  own gesture is not something a generic effect library gives you.
- **SVG line drawing (DrawSVG) and shape morphing (MorphSVG).** Diagram-building, signature
  strokes, icon-to-icon morphs, route tracing on a map. Data- and content-driven, not decorative.
- **MotionPath** for moving an object along a real route.
- **Timeline choreography** — sequencing an actual multi-step transition (modal enters, backdrop
  dims, focus moves) with labels and the position parameter, instead of a pile of CSS delays.
- **`gsap.matchMedia()`** — the only clean way in this library to make an animation set
  breakpoint- and preference-conditional *and* self-reverting.
- **`gsap.quickTo()`** for continuous pointer-driven values without allocating a tween per frame.

## AVOID — how GSAP produces the AI-slop tells

| GSAP feature | Register tell |
|---|---|
| `ScrollTrigger.batch(".card", { onEnter: els => gsap.to(els, { opacity: 1, y: 0, stagger: 0.15 }) })` | **fade-up-on-scroll on every element.** This is the canonical generator. The docs present batch as *"Good alternative to IntersectionObserver"*, and one call carpets an entire page. |
| `gsap.from(".section", { opacity: 0, y: 40, scrollTrigger: ... })` repeated per section | fade-up-on-scroll everywhere; `from()` is marketed in `gsap-core` as *"good for entrances"*, which is exactly the trap. |
| `ease: "back.out(1.7)"`, `"elastic.out(1, 0.3)"`, `"bounce.out"`, `CustomBounce`, `CustomWiggle` | **bounce easing.** `back.out(1.7)` is the documented example value and shows up verbatim in generated code. Overshoot on a UI element that has no mass is the giveaway. |
| `repeat: -1` (+ `yoyo: true`) on `scale`/`opacity`/`boxShadow` | **decorative pulse.** Also burns a rAF forever. |
| `xPercent: -100, repeat: -1, ease: "none"` on a duplicated track | **marquee.** |
| `Physics2DPlugin` / `PhysicsPropsPlugin` on many small elements | **particle background.** |
| `pin: true` + `scrub` on every section; `containerAnimation` fake-horizontal-scroll for ordinary content | scrolljacking. Legitimate for a deliberate scrollytelling piece; slop when applied to a marketing page's feature list. |
| `ScrollSmoother` | replaces native scroll for everyone. Breaks scroll anchoring, browser find-in-page position, and users' expected scroll velocity. Never on content sites. |
| `SplitText` char-stagger on every heading | text that reassembles itself on every h2 is a 2024-25 AI-page signature. Reserve for one hero. |
| `ScrambleTextPlugin` | glitch-text decoration; almost never earns its place. |
| `gsap.to(".btn", { scale: 1.05 })` on mouseenter | **hover:scale everywhere.** GSAP doesn't push this, but generated code reaches for it. |
| `markers: true` left in | not a slop tell, but a shipped-debug tell. Docs: *"❌ Leave **markers: true** in production."* |
| `GSDevTools` shipped | docs: *"❌ Ship GSDevTools or development-only plugins to production."* |

## Accessibility

**The documented pattern is `gsap.matchMedia()` (3.11+).** Verbatim from `gsap-core/SKILL.md`:

```javascript
let mm = gsap.matchMedia();

mm.add(
  {
    isDesktop: "(min-width: 800px)",
    isMobile: "(max-width: 799px)",
    reduceMotion: "(prefers-reduced-motion: reduce)"
  },
  (context) => {
    const { isDesktop, reduceMotion } = context.conditions;
    gsap.to(".box", {
      rotation: isDesktop ? 360 : 180,
      duration: reduceMotion ? 0 : 2  // skip animation when user prefers reduced motion
    });
    return () => { /* optional cleanup when no condition matches */ };
  }
);
```

Docs notes to carry over verbatim:
- *"when it stops matching, all animations and ScrollTriggers created in that run are **reverted
  automatically**."*
- *"Respecting **prefers-reduced-motion** is important for users with vestibular disorders. Use
  `duration: 0` or skip the animation when `reduceMotion` is true."*
- *"Do not nest **gsap.context()** inside matchMedia — matchMedia creates a context internally;
  use **mm.revert()** only."*
- `gsap.matchMediaRefresh()` re-runs all matching handlers immediately (e.g. after an in-app
  reduced-motion toggle).
- `mm.add(query, handler, containerRef)` — third arg scopes selector text.

**SplitText has a real a11y setting** (`gsap-plugins/SKILL.md`), `aria`:
`"auto"` (default) *"adds `aria-label` on the split element and `aria-hidden` on line/word/char
elements so screen readers read the label"*; `"hidden"` hides all from readers; `"none"` leaves
aria unchanged — *"Use `"none"` plus a screen-reader-only duplicate if nested links/semantics
must be exposed."* **Splitting text without `aria` handling destroys the accessible name of the
heading.** Default is safe; `aria: "none"` without a SR duplicate is a defect.

Timing guidance from the docs: `gsap.defaults({ duration: 0.6, ease: "power2.out" })` is the
official house default; `duration` default is 0.5s and default ease is `"power1.out"`.

## Scanner signatures — GSAP misuse

```
# fade-up-on-scroll carpet
ScrollTrigger\.batch\s*\(                       # any batch() at all → inspect
gsap\.(from|fromTo)\s*\([^)]*\bscrollTrigger\b  # count occurrences; >3 in one file = carpet
opacity:\s*0[^}]*\by:\s*\d{2,}                  # the y:30..100 + opacity:0 pair
(?s)scrollTrigger[^}]*stagger                   # scroll-triggered stagger

# bounce / overshoot easing
ease:\s*["'](back|elastic|bounce)[.(]
CustomBounce|CustomWiggle

# decorative pulse / marquee
repeat:\s*-1                                    # any infinite tween → justify or remove
repeat:\s*-1[^}]*\byoyo:\s*true
xPercent:\s*-?100[^}]*repeat:\s*-1

# scrolljacking
ScrollSmoother                                  # any use on a content site
pin:\s*true                                     # count; >1 per page = inspect
containerAnimation

# hover scale
(mouseenter|onMouseEnter)[\s\S]{0,120}gsap\.to[^}]*scale:\s*1\.0[1-9]

# text decoration
SplitText\.create[^)]*type:\s*["'][^"']*chars   # char split → is it one hero or every heading?
ScrambleTextPlugin|scrambleText:

# missing reduced-motion: gsap.* present but no matchMedia anywhere in the project
gsap\.(to|from|fromTo|timeline)\(   AND NOT   gsap\.matchMedia\(|prefers-reduced-motion

# shipped debug
markers:\s*true
GSDevTools

# licence trap / outdated install
npm\.greensock\.com|@greensock:registry|GSAP_TOKEN|\.npmrc.*greensock
```

## Gotchas

- **Licence, not MIT.** See above. If the product is a no-code visual animation builder, GSAP's
  Prohibited Uses clause is a real blocker; flag it rather than assuming permissive.
- **Bundle size.** `gsap.min.js` 72.9 KB min (not gzipped), `ScrollTrigger.min.js` 44.6 KB,
  `Draggable.min.js` 35.8 KB, `Flip.min.js` 25.5 KB, `MotionPathPlugin.min.js` 22.0 KB,
  `MorphSVGPlugin.min.js` 21.2 KB, `SplitText.min.js` 7.7 KB, `DrawSVGPlugin.min.js` 4.4 KB.
  (jsDelivr file sizes for 3.15.0.) core + ScrollTrigger is ~117 KB min before gzip — that is a
  lot to pay for a fade-up.
- **`registerPlugin` is mandatory with bundlers.** Docs: *"we still recommend registering plugins
  so that build tools don't drop them during tree shaking."* React: register at module top level,
  *"do not register inside a component that re-renders"*, and `useGSAP` itself must be registered.
- **React StrictMode / double-invoked effects.** `useGSAP()` reverts its `gsap.context()` on
  cleanup, so the second invocation re-runs from a clean state. Plain `useEffect(() => { gsap.to(...) })`
  with no cleanup double-applies and leaks. Docs: *"❌ Skip cleanup; always revert context or kill
  tweens/ScrollTriggers in the effect return."* Pattern when `useGSAP` isn't available:
  ```javascript
  useEffect(() => {
    const ctx = gsap.context(() => { gsap.to(".box", { x: 100 }); }, containerRef);
    return () => ctx.revert();
  }, []);
  ```
- **Unscoped selectors in components.** Docs: *"❌ Target by **selector without a scope**"* — a
  bare `".card"` inside a component animates every `.card` on the page.
- **`contextSafe` for handlers created after setup.** Animations created inside a click handler
  are outside the context and never get reverted; wrap with `contextSafe()` and remove the
  listener in the returned cleanup.
- **SSR.** *"❌ Run GSAP or ScrollTrigger during SSR; keep all usage inside client-only lifecycle."*
- **ScrollTrigger placement.** *"❌ Put ScrollTrigger on a **child tween** when it's part of a
  timeline"* — put it on the timeline. *"ScrollTriggers should only exist on top-level animations."*
- **`ScrollTrigger.refresh()`** after fonts/images/dynamic content; resize is auto-handled
  (debounced 200 ms), content changes are not. Create triggers top-to-bottom or set
  `refreshPriority`.
- **`immediateRender`.** `from()`/`fromTo()` apply their start values immediately; stacking two
  on the same property needs `immediateRender: false` on the later one or it won't be visible.
- **SPA cleanup:** `ScrollTrigger.getAll().forEach(t => t.kill())` on route change.
- **`svgOrigin` and `transformOrigin` are mutually exclusive.**

---

# anime.js

## What it is / licence / current version

- **What:** Lightweight, modular JS animation engine. Self-described on `animejs.com`:
  *"All-in-one animation engine. A fast and flexible JavaScript library to animate the web."*
  Covers CSS properties, SVG, DOM attributes and plain JS objects.
- **Version 4.5.0**, **licence MIT**, homepage `https://animejs.com` — verified on
  `https://registry.npmjs.org/animejs/latest`. README footer: *"© Julian Garnier | MIT License"*.
  Genuinely permissive, unlike GSAP.
- **v4 is a total API rewrite; v3 code does not run on v4.** Docs site still hosts 3.2.2 and 2.1.0.

## Install

```bash
npm install animejs
```

```javascript
import { animate } from 'animejs';           // ESM
const { animate } = require('animejs');      // CJS
import { animate } from 'https://esm.sh/animejs';  // ESM CDN
```

```html
<script src="https://cdn.jsdelivr.net/npm/animejs/dist/bundles/anime.umd.min.js"></script>
<script>
  const { animate } = anime;
</script>
```
(`https://animejs.com/documentation/getting-started/installation`. UMD bundle path verified on
jsDelivr: `dist/bundles/anime.umd.min.js`, 118 KB minified for the full bundle.)

**Modular subpath imports** — this is anime.js's structural advantage; use them:

```javascript
import { animate }        from 'animejs/animation';
import { createTimeline } from 'animejs/timeline';
import { createDraggable }from 'animejs/draggable';
import { onScroll }       from 'animejs/events';
import { splitText }      from 'animejs/text';    // since v4.2.0
```
Homepage-published per-module sizes: **total 24.50 KB**; Timer 5.60, Animation +5.20,
Timeline +0.55, Animatable +0.40, Draggable +6.41, Scroll +4.30, Scope +0.22, SVG 0.35,
Stagger +0.48, Spring 0.52, WAAPI 3.50 KB.

## Core API (v4)

**1 — `animate()` with per-property keyframes and per-property params**

```javascript
import { animate, stagger, splitText } from 'animejs';
const { chars } = splitText('h2', { words: false, chars: true });
animate(chars, {
  y: [
    { to: '-2.75rem', ease: 'outExpo', duration: 600 },
    { to: 0, ease: 'outBounce', duration: 800, delay: 100 }
  ],
  rotate: { from: '-1turn', delay: 0 },
  delay: stagger(50),
  ease: 'inOutCirc',
  loopDelay: 1000,
  loop: true
});
```

**2 — `createTimeline()` with labels and relative positions**

```javascript
import { createTimeline } from 'animejs';
const tl = createTimeline({ defaults: { duration: 750 } });
tl.label('start')
  .add('.square',   { x: '15rem' }, 500)
  .add('.circle',   { x: '15rem' }, 'start')
  .add('.triangle', { x: '15rem', rotate: '1turn' }, '<-=500');
```
Timeline surface: `.add(target, params, position)`, `.add(timerParams, position)`,
`.sync(timelineB, position)`, `.call(fn, position)`, `.label(name, position)`.

**3 — `stagger()` — time, value, and grid staggering**

```javascript
import { animate, stagger } from 'animejs';
animate('.square', {
  x: '17rem',
  scale: stagger([1, .1]),   // value stagger
  delay: stagger(100),       // time stagger
});
```
Stagger params: `start, from, reversed, ease, grid, axis, modifier, use, total, jitter`.

**4 — Scroll Observer: `onScroll()` passed as `autoplay`**

```javascript
import { onScroll, animate } from 'animejs';
animate(targets, { x: 100, autoplay: onScroll(parameters) });
```

```javascript
animate('.square', {
  x: 100,
  autoplay: onScroll({
    container: '.container',
    target: '.section',
    axis: 'y',
    enter: 'bottom top',
    leave: 'top bottom',
    sync: true,            // synchronisation mode
    onEnter: () => {}, onLeave: () => {}, onUpdate: () => {},
  })
});
```
`sync` accepts `true` (scrub to scroll), a `0..1` smoothing value, an ease, or a space-separated
method-name list. Default `'play pause'`. Documented forms:
`{ sync: 'play' }` · `{ sync: 'play pause' }` · `{ sync: 'play pause reverse reset' }`
(= `enterForward leaveForward enterBackward leaveBackward`).

**5 — SVG line drawing**

```javascript
import { animate, svg, stagger } from 'animejs';
animate(svg.createDrawable('.line'), {
  draw: ['0 0', '0 1', '1 1'],
  ease: 'inOutQuad',
  duration: 2000,
  delay: stagger(100),
  loop: true
});
```
Also `svg.morphTo('.shape-b')` as a `d` value, and `svg.createMotionPath('.circuit')` spread
into the params: `animate('.car', { ...createMotionPath('.circuit') })`.

**6 — `splitText()` (v4.1.0+)**

```javascript
import { createTimeline, stagger, splitText } from 'animejs';
const { words, chars } = splitText('p', {
  words: { wrap: 'clip' },
  chars: true,
});
createTimeline({ loop: true, defaults: { ease: 'inOut(3)', duration: 650 } })
  .add(words, { y: [$el => +$el.dataset.line % 2 ? '100%' : '-100%', '0%'] }, stagger(125))
  .add(chars, { y: $el => +$el.dataset.line % 2 ? '100%' : '-100%' }, stagger(10, { from: 'random' }))
  .init();
```
Settings: `lines, words, chars, debug, includeSpaces, accessible`; split params `class, wrap, clone`.

**7 — `createDraggable()`**

```javascript
import { createDraggable } from 'animejs';
createDraggable('.square');
createDraggable('.circle', {
  releaseEase: createSpring({ stiffness: 120, damping: 6 })
});
```
Settings include `trigger, container, containerPadding, containerFriction,
releaseContainerFriction, releaseMass, releaseStiffness, releaseDamping, velocityMultiplier,
minVelocity, maxVelocity, releaseEase, dragSpeed, dragThreshold, scrollThreshold, scrollSpeed,
cursor`; axes params `x, y, snap, modifier, mapTo`; methods `disable() enable() setX() setY()
animateInView() scrollInView() stop() reset() revert() refresh()`.

**8 — `createScope()` — root scoping, media queries, registered methods**

```javascript
import { animate, createScope, spring, createDraggable } from 'animejs';

scope.current = createScope({ root }).add(self => {
  animate('.logo', { scale: [ { to: 1.25, ease: 'inOut(3)', duration: 200 },
                              { to: 1, ease: spring({ bounce: .7 }) } ],
                     loop: true, loopDelay: 250 });
  self.add('rotateLogo', (i) => {
    animate('.logo', { rotate: i * 360, ease: 'out(4)', duration: 1500 });
  });
});
// later, outside the effect:
scope.current.methods.rotateLogo(3);
```

**9 — `waapi.animate()` — the 3 KB Web Animations API path**

```javascript
import { waapi } from 'animejs';
const animation = waapi.animate(targets, parameters);
```
Docs: *"Anime.js provides a more lightweight (3KB) version of the `animate()` method (10KB)
powered by the Web Animation API… The WAAPI version has less features overall, but covers most
of the basic API."*

**10 — utilities**

`utils.$()`, `.get()`, `.set()`, `.cleanInlineStyles()`, `.remove()`, `.sync()`, `.keepTime()`,
`.random()`, `.createSeededRandom()`, `.randomPick()`, `.shuffle()`, `.round()`, `.clamp()`,
`.snap()`, `.wrap()`, `.mapRange()`, `.lerp()`, `.damp()`, `.degToRad()`, `.radToDeg()` —
chainable.

## v3 → v4 API differences (verify against these; do not emit v3 names)

Source: `https://github.com/juliangarnier/anime/wiki/Migrating-from-v3-to-v4`.

| v3 | v4 |
|---|---|
| `import anime from 'animejs'` | `import { animate } from 'animejs'` |
| `anime({ targets: 'div', ... })` | `animate('div', { ... })` |
| `anime.timeline()` | `createTimeline()` |
| `easing:` | `ease:` |
| `easeOutQuad` | `outQuad` (the `ease` prefix is gone) |
| default easing `easeOutElastic` | default `'out(2)'` |
| `'spring(1, 80, 10, 0)'` | `createSpring({ mass: 1, stiffness: 80, damping: 10, velocity: 0 })` |
| `endDelay` | `loopDelay` |
| `value` (in property objects) | `to` |
| `direction: 'reverse'` | `reversed: true` |
| `direction: 'alternate'` | `alternate: true` |
| `loop: 1` = 1 iteration | `loop: 1` = repeat once = **2 iterations** |
| `update / begin / complete / change` | `onUpdate / onBegin / onComplete / onRender` |
| `loopBegin` / `loopComplete` | `onLoop` |
| `anime.path()` | `svg.createMotionPath()` |
| `anime.setDashoffset()` | `svg.createDrawable()` |
| `anime.random/get/set` | `utils.random/get/set` |
| `animation.remove()` | `utils.remove()` |
| `anime.suspendWhenDocumentHidden` | `engine.pauseOnDocumentHidden` |
| `anime.running` | removed |

## ADOPT — what anime.js earns its place for

- **Bundle discipline.** Modular subpath imports mean a project that only needs sequencing pays
  ~11 KB (Timer + Animation), not 117 KB. When the animation budget is small and real, this is
  the right pick over GSAP.
- **`waapi.animate()`** — hands work to the browser's own compositor-driven Web Animations API
  for the common cases at 3 KB. This is the most performance-honest option across all four libs.
- **Data-driven motion.** `animate()` targets plain JS objects, so you can tween a value and
  render it yourself — counters, gauges, chart transitions, map camera state.
- **SVG toolset that is content, not decoration.** `svg.createDrawable()` (draw a diagram or a
  route in), `svg.morphTo()` (icon state change), `svg.createMotionPath()`.
- **`createDraggable()` with spring release.** Full physical drag/flick/snap with
  `releaseEase: createSpring({...})`, `containerFriction`, `snap`, `scrollInView()`. Real
  continuity from a real gesture.
- **`Layout` API** (`record()` / `animate()` / `update()`, `enterFrom` / `leaveTo` / `swapAt`,
  `layout id`) — anime.js's FLIP equivalent, for DOM-order changes, enter/exit, swap-parent and
  modal transitions.
- **`createScope({ root })`** — scoped selectors + one-call `revert()`. Solves the React cleanup
  problem cleanly.
- **`createScope({ mediaQueries })`** — the reduced-motion mechanism, see below.

## AVOID — how anime.js produces the AI-slop tells

| anime.js feature | Register tell |
|---|---|
| `autoplay: onScroll()` attached to every section/card | **fade-up-on-scroll on every element.** The Scroll Observer is anime.js's headline feature and its one-line `autoplay:` form makes carpeting trivially cheap. |
| `delay: stagger(100)` over a card grid combined with `onScroll` | staggered fade-up carpet. |
| `loop: true, alternate: true` on `scale` / `opacity` | **decorative pulse.** The homepage's own hero examples use `loop: true` on `rotate` and on `scale` keyframes — copy-paste bait. |
| `createSpring({ bounce: .7 })`, `ease: 'outBounce'`, `ease: 'outElastic'` | **bounce easing.** `spring({ bounce: .7 })` appears in the official React getting-started example. |
| `x: '-100%'` + `loop: true` + `ease: 'linear'` on a duplicated track | **marquee.** |
| `stagger(200, { grid: [13, 13], from: 'center' })` on a dot field | **particle / decorative grid background.** This is literally the homepage's own demo. |
| `scrambleText` (v4 `animejs/text`) | glitch-text decoration. |
| `splitText()` + `stagger(10, { from: 'random' })` on every heading | text that reassembles itself; reserve for one hero at most. |
| `sync: true` scroll-scrubbing on ordinary page content | scrolljacking-adjacent; motion that only exists because the user scrolled. |
| `utils.random()` driving position/rotation on many elements | pseudo-particle decoration. |

## Accessibility

**The documented pattern is `createScope({ mediaQueries })`.** Verbatim from
`https://animejs.com/documentation/scope/scope-parameters/mediaqueries`:

```javascript
import { createScope, animate } from 'animejs';

createScope({
  mediaQueries: {
    isSmall: '(max-width: 100px)',
    isMedium: '(min-width: 101px) and (max-width: 200px)',
    isLarge: '(min-width: 201px)',
    reduceMotion: '(prefers-reduced-motion)',
  }
})
.add(self => {
  const { isSmall, isMedium, isLarge, reduceMotion } = self.matches;
  utils.set('.square', { scale: isMedium ? .75 : isLarge ? 1 : .5 });
  animate('.square', {
    x: isSmall ? 0 : ['-35vw', '35vw'],
    y: isSmall ? ['-40vh', '40vh'] : 0,
    rotate: 360,
    loop: true,
    alternate: true,
    duration: reduceMotion ? 0 : isSmall ? 750 : 1250
  });
});
```
Docs: *"Defines the media queries to match for conditionally refreshing the Scope when one of
their matches state changes. Media queries matching states are accessible via the scope
`matches` property."* The scope re-runs when a query's match state flips, so a user toggling
Reduce Motion at OS level takes effect live.

Note the exact query string the docs use: `'(prefers-reduced-motion)'` — the bare feature query,
which matches `reduce`. `'(prefers-reduced-motion: reduce)'` is equivalent and clearer; either
is acceptable in a scanner.

**`splitText` ships real a11y** (`textsplitter-settings/accessible`, since 4.1.0):
*"Creates an accessible cloned element that preserves the structure of the original split
element."* — `splitText(target, { accessible: true })`, **Default `true`**. So
`accessible: false` in generated code is an accessibility regression and should be flagged.

**Engine-level:** `engine.pauseOnDocumentHidden` (v4 replacement for
`anime.suspendWhenDocumentHidden`) stops animations while the tab is backgrounded — set it
rather than letting infinite loops run off-screen.

## Scanner signatures — anime.js misuse

```
# fade-up-on-scroll carpet
autoplay:\s*onScroll\(                     # count; >2 per file = carpet
onScroll\([^)]*sync:\s*true                # scroll-scrubbed content
(?s)onScroll\([\s\S]{0,200}stagger\(

# decorative pulse / marquee / particles
loop:\s*true[^}]*alternate:\s*true
loop:\s*true                               # any infinite loop → justify
ease:\s*['"]linear['"][\s\S]{0,120}loop:\s*true
stagger\([^)]*grid:\s*\[
utils\.random\(|randomPick\(|createSeededRandom\(

# bounce easing
createSpring\(|spring\(\s*\{[^}]*bounce
ease:\s*['"](out|in|inOut)(Bounce|Elastic|Back)['"]

# text decoration
scrambleText
splitText\([^)]*chars:\s*true              # is it one hero or every heading?
splitText\([^)]*accessible:\s*false        # HARD FAIL: default is true

# missing reduced-motion: animate( present anywhere, no mediaQueries anywhere
\banimate\(|createTimeline\(   AND NOT   prefers-reduced-motion|mediaQueries

# v3 API leaking into a v4 project (agent hallucination signal)
\banime\(\s*\{                             # v3 call form
targets:\s*['"]                            # v3 targets key
easing:\s*['"]ease(In|Out|InOut)           # v3 easing names
anime\.timeline\(|anime\.random\(|anime\.path\(|anime\.setDashoffset\(
endDelay:|direction:\s*['"](reverse|alternate)['"]
\b(begin|complete|update):\s*(function|\()  # v3 callbacks without on- prefix

# debug left in
onScroll\([^)]*debug:\s*true
splitText\([^)]*debug:\s*true
```

## Gotchas

- **v3 vs v4 is the biggest practical risk.** Model-generated anime.js code overwhelmingly emits
  v3 (`anime({ targets: ... , easing: 'easeOutQuad' })`). On v4 that throws or silently does
  nothing. Treat any v3 token in a project with `animejs@4` as a hard error.
- **`loop: 1` changed meaning** between v3 (1 iteration) and v4 (repeat once = 2 iterations).
  Silent off-by-one.
- **React cleanup.** The documented pattern is `createScope({ root })` inside `useEffect` with
  `return () => scope.current.revert()`. Without `revert()`, StrictMode's double-invoke leaves
  duplicate animations and inline styles on the node. `utils.cleanInlineStyles()` exists for the
  residue.
- **`revert()` vs `cancel()` vs `reset()`.** `revert()` restores original inline styles;
  `cancel()` just stops. Use `revert()` in teardown.
- **SSR:** `animate()` touches the DOM; keep it client-side, same as GSAP.
- **`vector-effect="non-scaling-stroke"` + `createDrawable` is slow.** Docs: *"Animating an
  element with the `vector-effect` attribute/styles set to `non-scaling-stroke` can be slow since
  the scale factor value for the path must be recalculated on every tick."*
- **The full UMD bundle is 118 KB minified.** Only the modular ESM path gets you the advertised
  24.5 KB. A `<script src=".../anime.umd.min.js">` tag buys the whole engine.
- **`waapi.animate()` is not feature-equivalent** — the docs mark JS-only features with a `(JS)`
  badge and WAAPI-only with `(WAAPI)`, and list API differences (`iterations`, `direction`,
  `easing`, `finished`, `convertEase()`). Don't assume a JS-version snippet works under `waapi`.

---

# animate.css

## What it is / licence / current version

- **What:** A pure-CSS library of ~90 named `@keyframes` plus utility classes. Self-described on
  `https://animate.style/`: *"Animate.css is a library of ready-to-use, cross-browser animations
  for use in your web projects. Great for emphasis, home pages, sliders, and attention-guiding
  hints."* No JavaScript. Categories: attention seekers, back, bouncing, fading, flippers,
  lightspeed, rotating, specials, zooming, sliding.
- **Version 4.1.1** — verified in the file banner of
  `https://raw.githubusercontent.com/animate-css/animate.css/main/animate.css` and on
  `https://animate.style/`.
- **LICENCE — trap.** The npm `license` field says `MIT`, but the shipped `LICENSE` file and the
  CSS banner both say:
  `Licensed under the Hippocratic License 2.1 - http://firstdonoharm.dev`
  and `LICENSE` opens `Animate.css Copyright 2021 Daniel Eden ("Licensor") / Hippocratic License
  Version Number: 2.1.` **HL 2.1 is not an OSI-approved open-source licence** — it conditions the
  grant on compliance with "Human Rights Principles and Human Rights Laws", requires
  indemnification of the licensor, and terminates automatically on breach. Many corporate OSS
  policies reject it outright. Flag this; don't repeat the npm metadata's "MIT".

## Install

```shell
npm install animate.css --save
```
```shell
yarn add animate.css
```
```javascript
import 'animate.css';
```
```html
<head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
  />
</head>
```
(All four copied verbatim from `https://animate.style/`.)

## Core API

**1 — basic usage**

```html
<h1 class="animate__animated animate__bounce">An animated element</h1>
```
Every animation class needs `animate__animated` alongside it, and the `animate__` prefix is
mandatory in v4.

**2 — the CSS custom properties (v4+)**

```css
:root {
  --animate-duration: 1s;
  --animate-delay: 1s;
  --animate-repeat: 1;
}
```
```css
/* This only changes this particular animation duration */
.animate__animated.animate__bounce { --animate-duration: 2s; }
/* This changes all the animations globally */
:root { --animate-duration: 800ms; --animate-delay: 0.9s; }
```

**3 — runtime speed control**

```javascript
// All animations will take twice the time to accomplish
document.documentElement.style.setProperty('--animate-duration', '2s');
// All animations will take half the time to accomplish
document.documentElement.style.setProperty('--animate-duration', '.5s');
```

**4 — utility classes**

```html
<div class="animate__animated animate__bounce animate__delay-2s">Example</div>
<div class="animate__animated animate__bounce animate__faster">Example</div>
<div class="animate__animated animate__bounce animate__repeat-2">Example</div>
```
Delays `animate__delay-2s` … `animate__delay-5s` (multiples of `--animate-delay`).
Speeds `animate__slow` (2s), `animate__slower` (3s), `animate__fast` (800ms),
`animate__faster` (500ms). Repeats `animate__repeat-1|2|3` and `animate__infinite`
(**`animate__infinite` ignores `--animate-repeat`**).

**5 — using the raw `@keyframes` without the helper classes**

```css
.my-element {
  display: inline-block;
  margin: 0 0.5rem;
  animation: bounce;        /* referring directly to the animation's @keyframe declaration */
  animation-duration: 2s;   /* don't forget to set a duration! */
}
```
Docs warning: *"Be aware that some animations are dependent on the `animation-timing` property
set on the animation's class. Changing or not declaring it might lead to unexpected results."*
**Accessibility consequence: this path bypasses the library's reduced-motion block entirely.**

**6 — driving it from JS + `animationend`**

```javascript
const element = document.querySelector('.my-element');
element.classList.add('animate__animated', 'animate__bounceOutLeft');
element.addEventListener('animationend', () => {
  // do something
});
```

**7 — the official self-cleaning helper**

```javascript
const animateCSS = (element, animation, prefix = 'animate__') =>
  new Promise((resolve, reject) => {
    const animationName = `${prefix}${animation}`;
    const node = document.querySelector(element);
    node.classList.add(`${prefix}animated`, animationName);
    function handleAnimationEnd(event) {
      event.stopPropagation();
      node.classList.remove(`${prefix}animated`, animationName);
      resolve('Animation ended');
    }
    node.addEventListener('animationend', handleAnimationEnd, {once: true});
  });

animateCSS('.my-element', 'bounce');
```

## ADOPT — what animate.css earns its place for

Narrow, but real:

- **One-off, event-driven emphasis after a user action.** A field that `animate__headShake`s on a
  failed submit; a toast that `animate__fadeInUp`s once when it appears and `animate__fadeOutDown`s
  when dismissed. Entrances/exits tied to an actual state change are what the docs themselves
  endorse: *"Entrances and exit animations should be used to orientate what is happening in the
  interface, clearly signaling that it's transitioning into a new state."*
- **Zero-JS, zero-build.** One `<link>`. For a static page or an email-adjacent context where you
  cannot ship 70 KB of JS, this is the only option in this list.
- **The class-add / `animationend` / class-remove pattern** as a general primitive — the
  `animateCSS()` helper above is a decent way to run *any* one-shot CSS animation and clean up
  after itself, even with your own keyframes.
- **Custom builds.** `git clone` → edit `./source/animate.css` → delete the `@import`s you don't
  want → `npm start`. Shipping 3 keyframes instead of 90 is the difference between acceptable and
  indefensible. Docs: *"Custom builds are not possible from a node_modules folder as we don't ship
  the building tools in the npm module."*

## AVOID — how animate.css produces the AI-slop tells

The library's *own* best-practices page names most of these. Quote it back.

| Class / feature | Register tell |
|---|---|
| `animate__fadeInUp` (+ `fadeIn`, `fadeInDown`, `slideInUp`, `zoomIn`, `backInUp`) applied to every card / section / list item | **fade-up-on-scroll on every element.** The most common animate.css slop pattern by a wide margin, usually with an IntersectionObserver adding the class. |
| `animate__delay-1s … animate__delay-5s` chained down a list to fake a stagger | the same carpet, hand-rolled. Also means the 5th item sits invisible for 5 seconds. |
| `animate__pulse`, `animate__heartBeat`, `animate__flash`, `animate__shakeX/Y`, `animate__tada`, `animate__rubberBand`, `animate__jello`, `animate__swing`, `animate__wobble`, `animate__headShake` used decoratively | **decorative pulse** and friends. These are the "attention seekers" category; the docs say they *"should be used to bring the user's attention to something special in your interface and not only as a way to bring 'flashiness' to it."* |
| `animate__infinite` | infinite decorative motion. Docs: *"Infinite animations should be avoided … It will just distract your users and might annoy a good slice of them."* |
| `animate__bounce`, `animate__bounceIn*`, `animate__backIn*`, `animate__jackInTheBox` | **bounce easing** on elements with no mass. |
| `animate__hinge`, `animate__rollIn/Out`, `animate__lightSpeedIn*`, `animate__flip*` | novelty motion; nothing in a real product needs a hinge. |
| any `animate__*Big` (`fadeInUpBig`, `fadeInLeftBig`, …) | 2000px travel distances. Guaranteed vestibular problem and guaranteed horizontal scrollbar (see Overflow gotcha). |
| `animate__animated` on `<html>`/`<body>` or a full-bleed hero | docs: *"Don't animate large elements"*, *"Don't animate root elements"*. |
| Raw `@keyframes` usage (`animation: bounce;`) | silently opts out of the reduced-motion block. |
| `animate.compat.css` | unprefixed class names — defeats every `animate__` scanner regex and collides with project classes. |

## Accessibility

**animate.css is the only one of the four that ships reduced-motion by default.** The exact block
shipped in `animate.css` v4.1.1:

```css
@media print, (prefers-reduced-motion: reduce) {
  .animate__animated {
    -webkit-animation-duration: 1ms !important;
    animation-duration: 1ms !important;
    -webkit-transition-duration: 1ms !important;
    transition-duration: 1ms !important;
    -webkit-animation-iteration-count: 1 !important;
    animation-iteration-count: 1 !important;
  }

  .animate__animated[class*='Out'] {
    opacity: 0;
  }
}
```

Read that carefully — three things matter for the skill:

1. **It collapses duration to `1ms`, it does not remove the animation.** Because every
   `.animate__animated` sets `animation-fill-mode: both`, the element still snaps to its final
   keyframe state. That's why the second rule exists: any `*Out` animation is forced to
   `opacity: 0` so exit animations still hide their target. This is a *good* reference
   implementation of "reduce, don't break".
2. **It also fires under `@media print`** — animations would otherwise leave elements mid-transform
   in a printout.
3. **It only matches `.animate__animated`.** If the project uses the raw `@keyframes` (a
   documented usage path) or `animate.compat.css` (`.animated`, not `.animate__animated`), the
   protection does not apply and the project must add its own block.

The docs' own statement, verbatim, worth quoting into the skill:

> **Don't disable the `prefers-reduced-motion` media query** — Since version 3.7.0 Animate.css
> supports the `prefers-reduced-motion` media query which disables animations based on the OS
> system's preference on supporting browsers (most current browsers support it. This is a
> **critical accessibility feature** and should never be disabled! This is built into browsers to
> help people with vestibular and seizure disorders. … If your web-thing needs the animations to
> function, warn users, but don't disable the feature.

Timing guidance from the docs: default `--animate-duration: 1s` is **long** for UI feedback —
`animate__faster` (500ms) or a local `--animate-duration: .2s` is the appropriate range for a
state change. The delay classes (1–5s) exist for choreography, not for staggering lists.

## Scanner signatures — animate.css misuse

```
# entrance carpet — count matches per file/template
animate__(fadeIn|fadeInUp|fadeInDown|slideInUp|zoomIn|backInUp|bounceIn)\b
   → >3 occurrences in one template, or present on a repeated/mapped list item = carpet
(?s)\.map\([^)]*animate__(fadeIn|slideIn|zoomIn)      # applied inside a list render
animate__delay-[2-5]s[\s\S]{0,400}animate__delay-[2-5]s  # fake stagger via delay chain

# decorative / infinite / bounce
animate__infinite                                    # HARD FAIL unless justified
animate__(pulse|heartBeat|flash|tada|rubberBand|jello|wobble|swing|shakeX|shakeY|headShake)
animate__(bounce|bounceIn|bounceOut|backIn|backOut|jackInTheBox)
animate__(hinge|rollIn|rollOut|lightSpeedIn|lightSpeedOut|flipIn|flipOut)
animate__\w+Big\b                                    # 2000px travel

# structural misuse
<(html|body)[^>]*animate__animated
class="[^"]*animate__animated[^"]*"[^>]*>\s*$        # on a full-bleed wrapper → inspect

# reduced-motion protection defeated
animation:\s*(bounce|pulse|fadeInUp|flash|shakeX|tada|heartBeat)\b   # raw @keyframes usage
animate\.compat\.css                                  # unprefixed build

# HARD FAIL: the library's own block removed or overridden
prefers-reduced-motion[\s\S]{0,400}animation-duration:\s*(?!1ms)     # weakened
# or: animate__animated present in markup AND no `prefers-reduced-motion` anywhere in shipped CSS
#     (true when the raw keyframes path or a custom/partial build is used)

# licence
"animate\.css"                                        # → check policy: Hippocratic 2.1, not MIT
```

## Gotchas

- **Licence:** Hippocratic License 2.1, **not** MIT despite the npm metadata. Not OSI-approved.
  Contains an indemnity clause and auto-termination. Check before shipping in a commercial
  codebase.
- **Bundle size:** the full unminified `animate.css` is **95,378 bytes** (~57 KB minified) for ~90
  keyframe sets. If you use three, you are shipping 87 you don't. Do a custom build.
- **Cannot animate inline elements.** Docs: *"this goes against the CSS animation specs and will
  break on some browsers or eventually cease to work. Always animate block or inline-block level
  elements… You can set an element to `display: inline-block`."*
- **Overflow / phantom scrollbars.** Docs: *"Most of the Animate.css animations will move elements
  across the screen and might create scrollbars on your web-thing. This is manageable using the
  `overflow: hidden` property … in the parent holding the animated element."* Worst with the
  `*Big` variants.
- **`animation-fill-mode: both` is the default** — the element retains the final keyframe state
  after the animation. Combined with the reduced-motion block this is why `*Out` needs the
  `opacity: 0` compensation.
- **No interval between repeats.** Docs: *"Unfortunately, this isn't possible with pure CSS right
  now. You have to use Javascript to achieve this result."*
- **v3 → v4 is a breaking rename.** All classes gained the `animate__` prefix. `animate.compat.css`
  exists as a migration escape hatch, and the docs say *"in later versions, we might decide to
  discontinue the `animate.compat.css` file."* Never start a new project on compat.
- **No SSR/React-specific hazards** (it's a stylesheet), but adding classes in a `useEffect`
  under StrictMode can double-fire the `animationend` listener if you don't pass `{ once: true }`
  — the official helper does.
- **Custom builds require the git repo**, not the npm package.

---

# animate-ui

## What it is / licence / current version

- **What: not an npm library — a shadcn-style component registry.** Repo README:
  *"A fully animated, open-source component distribution built with React, TypeScript, Tailwind
  CSS, and Motion."* Docs `index.mdx` verbatim:

  > **Animate UI is a distribution of React components** built with Tailwind CSS and Motion,
  > based on the shadcn registry and inspired by shadcn/ui and Magic UI. …
  > **Not a library—an open component distribution** — Like shadcn/ui, **Animate UI is not a
  > typical install‑from‑NPM library**. It's an open collection you can **copy, modify, and
  > customize** directly in your codebase.

  Three things are included, per the docs:
  1. *"**Primitives (animated)**: Building blocks with animation baked in. Authored by Animate UI
     or ported from popular primitive libraries (Radix UI, Base UI, Headless UI)."*
  2. *"**Components**: Essential UI pieces with baseline styles inspired by shadcn/ui … built on
     the animated primitives."*
  3. *"**Icons**: Animated Lucide icons."*
- **Licence: MIT** (`https://github.com/imskyleen/animate-ui/blob/main/LICENSE.md`; README badge
  and License section both say MIT). The cleanest licence of the four.
- **Version:** the monorepo `package.json` is `"name": "animate-ui", "version": "1.0.27",
  "private": true` — there is no published npm package to version-pin. **You copy source at a
  point in time; there is no upgrade path and no CVE channel.** The registry index published at
  `https://animate-ui.com/r/registry.json` currently carries **580 items**:
  1 `index` style, **81 primitives**, **73 components**, 260 icons, 5 hooks, 1 lib, 159 demos.
- **Peer stack** (from `apps/www/package.json`): `motion ^12.23.24`, `react`/`react-dom ^19.1.2`,
  `tailwindcss ^4.1.13`, `radix-ui ^1.4.3`, `@base-ui-components/react 1.0.0-beta.4`,
  `@headlessui/react ^2.2.6`, `lucide-react`, `tw-animate-css`, `class-variance-authority`,
  `tailwind-merge`.

## Install

Docs `installation.mdx`, verbatim — *"**Note:** We use installation process as shadcn/ui."*

```bash
# 1. Initialize shadcn/ui
npx shadcn@latest init
# pnpm dlx shadcn@latest init   |   yarn shadcn@latest init   |   bunx --bun shadcn@latest init

# 2. Add a component (namespaced registry item)
npx shadcn@latest add @animate-ui/primitives-texts-sliding-number
```

```tsx
// 3. Import from where it was written into YOUR codebase
import { SlidingNumber } from '@/components/animate-ui/primitives/texts/sliding-number';

export default function Home() {
  return (
    <div>
      <SlidingNumber />
    </div>
  );
}
```

Registry manifest: `https://animate-ui.com/r/registry.json`
(`"$schema": "https://ui.shadcn.com/schema/registry.json", "name": "Animate UI",
"homepage": "https://animate-ui.com"`). Item naming is
`<kind>-<group>-<name>`, e.g. `primitives-effects-fade`, `components-backgrounds-stars`,
`components-radix-accordion`. Files land under `components/animate-ui/…` in your repo.

## Core API — actual registry contents

These are the real group names and item names from `registry.json`, so the skill can reason about
them precisely.

**Primitives (81):**
- `animate-*` (11): `avatar-group, code-block, cursor, github-stars, motion-grid, pinned-list,
  scroll-progress, slot, spring, tabs, tooltip`
- `radix-*` (18) / `base-*` (17) / `headless-*` (6): animated wrappers over Radix UI, Base UI and
  Headless UI — `accordion, alert-dialog, checkbox, collapsible, dialog, dropdown-menu, files,
  hover-card, popover, preview-card, preview-link-card, progress, radio-group, sheet, switch,
  tabs, toggle, tooltip…`
- `effects-*` (14): `auto-height, blur, click, effect, fade, highlight, image-zoom, magnetic,
  particles, shine, slide, theme-toggler, tilt, zoom`
- `texts-*` (11): `counting-number, gradient, highlight, morphing, rolling, rotating,
  scrolling-number, shimmering, sliding-number, splitting, typing`
- `buttons-*` (4): `button, flip, liquid, ripple`

**Components (73):** `animate-*` (7), `backgrounds-*` (7: `bubble, fireworks, gradient,
gravity-stars, hexagon, hole, stars`), `base-*` (16), `buttons-*` (8: `button, copy, flip,
github-stars, icon, liquid, ripple, theme-toggler`), `community-*` (11), `headless-*` (6),
`radix-*` (18).

**Hooks (5):** `use-auto-height, use-controlled-state, use-data-state, use-is-in-view,
use-motion-value-state`.

**Representative source** — `registry/primitives/effects/fade/index.tsx`, abridged verbatim:

```tsx
'use client';
import { motion, type HTMLMotionProps } from 'motion/react';
import { useIsInView, type UseIsInViewOptions } from '@/registry/hooks/use-is-in-view';

function Fade({
  transition = { type: 'spring', stiffness: 200, damping: 20 },
  delay = 0, inView = false, inViewMargin = '0px', inViewOnce = true,
  initialOpacity = 0, opacity = 1, asChild = false, ...props
}: FadeProps) {
  const { ref: localRef, isInView } = useIsInView(ref, { inView, inViewOnce, inViewMargin });
  const Component = asChild ? Slot : motion.div;
  return (
    <Component ref={localRef} initial="hidden" animate={isInView ? 'visible' : 'hidden'}
      exit="hidden"
      variants={{ hidden: { opacity: initialOpacity }, visible: { opacity } }}
      transition={{ ...transition, delay: (transition?.delay ?? 0) + delay / 1000 }}
      {...props} />
  );
}
```
There is also a `Fades` (and, in `slide`, a `Slides`) wrapper that maps over children applying an
incrementing `delay + index * holdDelay` — a purpose-built list-stagger.

## ADOPT — what animate-ui earns its place for

- **Animated wrappers over real accessible primitives.** The `radix-*`, `base-*` and `headless-*`
  groups (41 primitives + 40 components) are the defensible half of this library: an accordion,
  dialog, popover, dropdown, tabs or collapsible that keeps Radix/Base/Headless's focus
  management, `aria-*` wiring and keyboard behaviour, with the open/close *state transition*
  animated. That is exactly the "animation shows a state change" case the register wants.
- **`primitives-effects-auto-height` / `hooks-use-auto-height`.** Height-auto transitions are
  genuinely awkward to hand-roll; this is a legitimate mechanical win for accordions and
  expanding panels.
- **Numeric/data-driven text.** `texts-counting-number`, `texts-sliding-number`,
  `texts-scrolling-number` — motion that encodes a *value change*, not decoration. This is
  data-driven motion, the good kind.
- **`primitives-animate-slot`** (`asChild` polymorphism) and `hooks-use-controlled-state` /
  `use-data-state` / `use-motion-value-state` — sound composition plumbing you'd otherwise write.
- **Copy-first is the real advantage.** Source lands in your repo, so you can strip the
  decoration, retune the springs, and add the reduced-motion gate the upstream lacks. Treat every
  item as a starting draft, not a dependency.

## AVOID — how animate-ui produces the AI-slop tells

This library ships the register's forbidden list as named, installable, one-line components.
Every mapping below is from the actual registry index and shipped source.

| Registry item | Register tell — with evidence |
|---|---|
| `components-backgrounds-stars`, `-gravity-stars`, `-fireworks`, `-bubble`, `-hole`, `-hexagon`, `-gradient` | **particle / animated background.** All 7 items in the `backgrounds` group are decorative full-bleed backdrops. `registry/components/backgrounds/stars/index.tsx` ships `StarLayer` with `count = 1000`, `transition = { repeat: Infinity, duration: 50, ease: 'linear' }`, `animate={{ y: [0, -2000] }}` — a thousand `box-shadow` stars translating forever. |
| `primitives-effects-particles` | **particle background** as a wrappable primitive. |
| `primitives-buttons-button` (and `components-buttons-button`) | **hover:scale everywhere — baked into the defaults.** Source: `hoverScale = 1.05, tapScale = 0.95` … `whileTap={{ scale: tapScale }}` `whileHover={{ scale: hoverScale }}`. Every button installed from this registry scales on hover unless you pass props to stop it. |
| `primitives-buttons-ripple` | same `hoverScale = 1.05 / tapScale = 0.95` defaults, plus a Material-style expanding ripple on click. |
| `primitives-buttons-liquid`, `primitives-effects-shine` | shimmer/gloss sweep over a button — decorative, no state meaning. |
| `primitives-effects-fade` + `primitives-effects-slide` with `inView` | **fade-up-on-scroll on every element.** `Slide` defaults are `direction = 'up'`, `offset = 100`, `inView`, spring transition — i.e. the tell, verbatim, as a named component. `Fades` / `Slides` exist specifically to apply it down a list with `holdDelay`. |
| `primitives-effects-blur`, `-zoom` with `inView` | the same scroll-reveal carpet in other flavours. |
| `primitives-effects-magnetic`, `-tilt` | cursor-follow / 3D-tilt cards. Pointer-only, meaningless to keyboard and touch users, and a reliable "AI landing page" signal. |
| `primitives-texts-shimmering`, `-gradient` | animated gradient text — decorative pulse in text form. |
| `primitives-texts-typing` | typewriter headline. |
| `primitives-texts-rotating`, `-morphing`, `-rolling`, `-splitting` | "We help you [rotating word]" headlines. |
| `primitives-animate-cursor`, `components-animate-cursor` | custom cursor replacement — breaks the OS cursor contract. |
| `primitives-animate-motion-grid` | animated dot grid — decorative field. |
| `components-community-*` (11) | community-contributed showpieces (`radial-menu`, `radial-intro`, `playful-todolist`, `flip-card`, …) — demo-grade, not product-grade. |
| `primitives-animate-scroll-progress` | fine as a *reading-progress affordance*; slop when it's a decorative bar on a 3-screen marketing page. |

## Accessibility

**This is animate-ui's weakest area and the most important thing to record.**

Verified 2026-09-04: searching the published registry manifest
(`https://animate-ui.com/r/registry.json` / `apps/www/public/r/registry.json`, 580 items, 417 KB)
returns **0 occurrences** of `useReducedMotion`, `MotionConfig`, `reducedMotion`, or
`prefers-reduced-motion`. Reading six shipped sources directly —
`primitives/effects/fade`, `primitives/effects/slide`, `primitives/effects/particles`,
`primitives/texts/typing`, `components/backgrounds/stars`, `primitives/buttons/ripple` —
found **0 occurrences in any of them**. None of the six consults the user's motion preference.
(Six of 580 is a sample, not a proof of absence across the whole registry — but it covers the
highest-risk items and none of them handles it.)

**Consequence for the skill: every animate-ui item must be treated as reduced-motion-unsafe on
install, and gated by the consuming app.** Because everything is Motion-based, the fix is
Motion's own API (`https://motion.dev/docs/react-accessibility`):

```tsx
// App-wide: "user" disables transform and layout animations, keeps opacity
import { MotionConfig } from 'motion/react';

<MotionConfig reducedMotion="user">
  {children}
</MotionConfig>
```
`reducedMotion` accepts `"user"` | `"always"` | `"never"`. Per-component:

```tsx
import { useReducedMotion } from 'motion/react';
const shouldReduceMotion = useReducedMotion();  // true/false from the OS setting
```
Motion's documented guidance, which matches the register: **replace transform with opacity**
under reduced motion rather than removing the transition; disable autoplaying video
(`autoplay={!shouldReduceMotion}`); pass `0` instead of a motion value for parallax.

Note that `reducedMotion="user"` neutralises `x`/`y`/`scale`/`layout` but **does not stop an
infinite `repeat: Infinity` opacity/background loop** and does not stop a `setInterval`-driven
typewriter. The `backgrounds-*` items and `texts-typing` need explicit `useReducedMotion()`
guards, not just the provider.

Additional a11y notes:
- The `radix-*` / `base-*` / `headless-*` groups inherit their underlying library's a11y — that
  is their whole value. The `animate-*`, `effects-*`, `texts-*`, `backgrounds-*` and
  `community-*` groups inherit nothing.
- `texts-splitting` / `texts-typing` render text character-by-character into the DOM with no
  documented `aria-label` fallback — unlike GSAP SplitText (`aria: "auto"`) and anime.js
  `splitText({ accessible: true })`, both of which handle this by default. Assume the accessible
  name is destroyed and add one.
- `components-animate-cursor` / `primitives-animate-cursor` replace the system cursor; that harms
  low-vision users who rely on OS cursor size/contrast settings.

## Scanner signatures — animate-ui misuse

```
# import-path signatures (the components land in YOUR repo at a known path)
@/components/animate-ui/components/backgrounds/(stars|fireworks|bubble|hole|gravity-stars|hexagon|gradient)
@/components/animate-ui/primitives/effects/(particles|magnetic|tilt|shine)
@/components/animate-ui/primitives/texts/(typing|shimmering|gradient|rotating|morphing)
@/components/animate-ui/primitives/buttons/(liquid|ripple)
@/components/animate-ui/primitives/animate/cursor

# install-command signatures (in scripts, READMEs, agent transcripts)
shadcn@latest add @animate-ui/components-backgrounds-
shadcn@latest add @animate-ui/primitives-effects-(particles|magnetic|tilt|shine)
shadcn@latest add @animate-ui/primitives-texts-(typing|shimmering|gradient|rotating)
shadcn@latest add @animate-ui/components-community-

# fade-up-on-scroll carpet
<(Fade|Slide|Blur|Zoom)\b[^>]*\binView\b            # count; >3 = carpet
<(Fades|Slides)\b                                   # the list-stagger wrappers
\.map\([^)]*<\s*(Fade|Slide)\b
direction=["']up["'][^>]*inView|inView[^>]*direction=["']up["']

# hover:scale — the shipped defaults
whileHover=\{\{\s*scale:\s*1\.0[1-9]
hoverScale|tapScale                                 # present at all = the default 1.05/0.95 path
<Button\b(?![^>]*hoverScale=\{?1\b)                 # animate-ui Button without hoverScale={1}

# infinite decorative motion
repeat:\s*Infinity
<StarLayer|count=\{?\d{3,}                          # 3+ digit particle counts

# HARD FAIL: motion in the tree with no reduced-motion gate anywhere in the app
from ['"]motion/react['"]   AND NOT   MotionConfig|useReducedMotion
<MotionConfig(?![^>]*reducedMotion)                 # provider present but preference ignored
reducedMotion=["'](never|always)["']                # overrides the user's OS setting
```

## Gotchas

- **No version pin, no upgrade path, no security channel.** There is no published npm package
  (`animate-ui` on npm is an unrelated `0.0.4` stub; the repo package is `private: true`). You
  copy files at a point in time. Record the commit you pulled from.
- **Heavy transitive peer surface.** Individual items pull `motion`, and depending on the group,
  `radix-ui`, `@base-ui-components/react` (a **beta**: `1.0.0-beta.4`), or `@headlessui/react`.
  Mixing groups means shipping two or three primitive libraries.
- **React 19 + Tailwind v4 + Motion 12.** These are the versions the registry is authored against.
  On React 18 or Tailwind v3 expect breakage (`ref` as a prop, `@theme` tokens, `tw-animate-css`).
- **`'use client'` everywhere.** Every primitive is a client component; dropping one into a Next.js
  server component tree pushes the boundary further up than you may intend, and none of it renders
  meaningfully during SSR.
- **StrictMode double-fire.** `use-is-in-view` and the interval-driven `texts-typing` /
  `texts-counting-number` set state in effects; under React 18/19 StrictMode dev double-invoke,
  verify counters don't double-step and observers get disconnected.
- **`inViewOnce = true` is the default** on the effects primitives — good (it doesn't re-fire on
  every scroll pass), but it also means the content is invisible until intersection, so a failed
  observer = invisible content. Anything containing text must be visible without JS.
- **The `backgrounds-*` items generate randomness in `useEffect`** (`generateStars` uses
  `Math.random()` inside an effect) — no hydration mismatch, but 1000 `box-shadow` entries in one
  string is a real paint cost on low-end devices.
- **MIT licence is clean** — this is the one licence in the set with no caveats.

---

# Which to use when

| | **GSAP 3.15** | **anime.js 4.5** | **animate.css 4.1.1** | **animate-ui** |
|---|---|---|---|---|
| **Kind** | JS engine + plugins | Modular JS engine | Pure-CSS class library | shadcn-style React registry (copy-in source) |
| **Licence** | GSAP Standard "no charge" (proprietary, Webflow) — free incl. commercial, Prohibited-Uses clause. **Not MIT** | **MIT** | **Hippocratic 2.1** (not OSI; npm metadata wrongly says MIT) | **MIT** |
| **Cost on the wire** | 73 KB min core, +45 KB ScrollTrigger | 24.5 KB modular ESM / 118 KB UMD; 3 KB `waapi` path | 95 KB raw for ~90 keyframes (custom-build it) | per-component; pulls `motion` ~ and Radix/Base/Headless |
| **Reach for it when** | FLIP layout transitions, interruptible/reversible state, SVG draw + morph, drag with real inertia, precise multi-step choreography | Same jobs at a fraction of the bytes; data-driven tweening of JS objects; you want WAAPI where possible | One-shot emphasis after a user action, zero JS, zero build | You're on React 19 + Tailwind 4 and want animated **Radix/Base/Headless** primitives with the a11y intact |
| **Killer feature** | `Flip.getState()` → DOM change → `Flip.from()` | modular imports + `waapi.animate()` + `createScope({ mediaQueries })` | one `<link>`, ships its own reduced-motion block | `radix-*` / `base-*` / `headless-*` groups; source lands in your repo so you can fix it |
| **Reduced motion** | Opt-in: `gsap.matchMedia({ reduceMotion: "(prefers-reduced-motion: reduce)" })`, auto-reverts | Opt-in: `createScope({ mediaQueries: { reduceMotion: '(prefers-reduced-motion)' } })` | **Built in** (`.animate__animated` only; raw-keyframes path unprotected) | **None shipped** — you must add `<MotionConfig reducedMotion="user">` + `useReducedMotion()` |
| **Text-split a11y** | `SplitText { aria: "auto" }` — safe default | `splitText({ accessible: true })` — safe default | n/a | none — assume broken |
| **Highest slop risk** | `ScrollTrigger.batch()`, `ScrollSmoother`, `back/elastic/bounce` eases, `repeat: -1` | `autoplay: onScroll()` on everything, `loop: true, alternate: true`, `createSpring({bounce})`, grid staggers | `animate__fadeInUp` carpet, attention-seekers as decor, `animate__infinite`, `*Big` | `backgrounds-*` (all 7), `effects-particles/magnetic/tilt/shine`, `texts-typing/shimmering`, `Button` default `hoverScale: 1.05` |
| **Don't use it for** | a fade-in (117 KB is not a fade-in budget) | anything needing GSAP-only plugins (MorphSVG quality, Flip maturity) | anything scroll-driven, interruptible, or reversible | anything outside React 19 / Tailwind 4; anything from `backgrounds-*` or `community-*` |

**Default recommendation order for the skill:** CSS transitions on real state changes → nothing
at all → `animate.css` (custom build) for a one-shot → `anime.js` modular for anything scripted →
`GSAP` only when Flip / DrawSVG / MorphSVG / Draggable+Inertia / real timeline choreography is the
actual requirement → `animate-ui` only for its `radix-*` / `base-*` / `headless-*` groups, never
for `backgrounds-*`, `effects-*` decoration, or `texts-*` novelty.
