# Code-level patterns in AI-generated UI — beyond React

**Topic:** Real AI-generated code samples in Vue, React Native, Flutter, and current-generation (2026) web output.
**Research date:** 2026-09-05.
**Route:** The Exa MCP server was NOT authorized in this session. Discovery was done with the authenticated GitHub REST API (`gh api search/code`, `search/commits`, `search/repositories`) plus `WebSearch`/`WebFetch` availability; **verification and all counts were done by shallow-cloning each repo and running local `grep -E` scans**, exactly as in `04-code-patterns.md` (K1–K15). No count in this file came from a web summariser — every number was produced by a local regex pass over cloned files.

**Repos actually opened and read files from: 32** — 27 of them are tabled below and carry every count (8 Vue, 7 React Native, 3 FlutterFlow, 5 LLM-Flutter, 4 current-web); a further 5 were cloned and inspected but excluded from the counts (see Gaps 7 and the rejection list). A further ~22 candidate repos had only their provenance file fetched (`.bolt/config.json`, `replit.md`, `vite.config.ts`) and were not cloned.

**Candidates rejected for missing/unusable provenance: 8** —
`drzo/opencog-js` and `anmlclt/colorsnatch` (a `.bolt/config.json` that is hand-written or a StackBlitz block, not a Bolt template stamp); `no0bie-spy/YaGoo--`, `Oussana21/app-pythagore`, `statistica-ai/vibrely-expo-template` (`"template"` value is a user string, not a Bolt stock template id, so origin is unproven); `AdyaS2010/Generation-Connect` (`.bolt/config.json` contains only env keys, no template field); `manfredsteger/polly` (`replit.md` present but the repo contains 0 `.dart` files — nothing to measure); `HeyBene/OpenBene` (surfaced by a Claude-Code commit-trailer search, but the depth-1 clone carried no trailer I could read locally, so provenance was not verifiable in-repo).
One further repo, `Aditya27T/Smart-Ndelik-5.0-react-native`, has a valid `bolt-expo` stamp but the Expo Router scaffold has been fully replaced by a hand-written `screens/` + `navigation/` tree with 0 `.tsx` files; it is counted as opened but excluded from the RN signature counts as too diluted to attribute.

**Scan hygiene:** `node_modules`, `.git`, `build/`, `.dart_tool/`, `dist/`, `.nuxt/`, `.output/`, native `ios/`/`android/` folders, lockfiles and `*.min.*` excluded. For FlutterFlow repos, `lib/flutter_flow/` (the vendored FlutterFlow runtime library) was excluded so counts reflect generated *pages*, not the library.

**Headline findings**

1. **The React-era tells do not transfer.** Purple→pink gradients: **0 occurrences in 19/19 web-and-RN repos scanned for it.** Indigo utility classes: 0 in 18/19. `bg-clip-text`: 0 in 17/19. `blur-3xl`: 0 in 17/19. `hover:scale-105`: 0 in 15/19. Bolt's Vue output in particular carries almost none of the visual clichés its React output is famous for.
2. **A striking geometric constant that turns out NOT to be an AI tell.** In React Native and Flutter every generated shadow is straight down: `shadowOffset: { width: 0, ... }` in **123 of 123 occurrences across 6 RN repos**, `Offset(0, N)` in **72 of 72 occurrences across 4 LLM-Flutter repos**. Not one sample offset a shadow horizontally. But the FlutterFlow control group — where a human picked every shadow in a visual editor — is **49 of 49** on the same measure. It is mobile/Material idiom, not generation. Recorded here as a negative result so nobody else spends the same day on it (see T1).
3. **The strongest genuinely new tell is chromatic: Tailwind's default palette leaks into non-Tailwind languages.** Dart and React Native `StyleSheet` files carry literal Tailwind hexes (`#3B82F6`, `#16A34A`, `#EF4444`, `0xFF7C3AED`) in **5 of 11** RN/Flutter samples — and in **0 of 3** FlutterFlow samples. Flutter has no Tailwind; this is training-data bleed, and it is much more specific than any Tailwind-class regex.
4. **Current-generation (2026) Lovable is a fixed-size scaffold:** `src/components/ui/` contains **exactly 49 files in 4 of 4** repos created March 2026, with `public/placeholder.svg` present in 4/4 (unreferenced in 2/4).

---

## Source table

| ID | Repo | Generator | Provenance marker found (file) | Created / last push | Snapshot | URL |
|----|------|-----------|-------------------------------|---------------------|----------|-----|
| K16 | u-x-o-n-e/Focus-App | Bolt.new (Vue) | `{"template": "vite-vue"}` in `.bolt/config.json` | 2025-05-22 / 2025-05-24 | 2026-09-05 | https://github.com/u-x-o-n-e/Focus-App |
| K17 | hartono0297/splitbill | Bolt.new (Vue) | `{"template": "vite-vue"}` in `.bolt/config.json` | 2025-11-21 / 2026-02-23 | 2026-09-05 | https://github.com/hartono0297/splitbill |
| K18 | tiagofrancafernandes/bolt-vue-tailwind-website | Bolt.new (Vue TS) | `{"template": "vite-vue-ts"}` in `.bolt/config.json` | 2024-12-24 / 2024-12-26 | 2026-09-05 | https://github.com/tiagofrancafernandes/bolt-vue-tailwind-website |
| K19 | mrodrigueznav/gsict | Bolt.new (Nuxt) | `{"template": "nuxt"}` in `.bolt/config.json` | 2024-12-03 / 2024-12-03 | 2026-09-05 | https://github.com/mrodrigueznav/gsict |
| K20 | alexanderop/todo-app-example | Bolt.new (Nuxt) | `{"template": "nuxt"}` in `.bolt/config.json` | 2024-10-07 / 2024-10-08 | 2026-09-05 | https://github.com/alexanderop/todo-app-example |
| K21 | LorenzovandenDungen/yelp | Bolt.new (Vue) | `{"template": "vite-vue"}` in `.bolt/config.json` | 2024-10-09 / 2024-10-09 | 2026-09-05 | https://github.com/LorenzovandenDungen/yelp |
| K22 | yishangzhang/vue02 | Bolt.new (Vue) | `{"template": "vite-vue"}` in `.bolt/config.json` | 2025-06-15 / 2025-06-15 | 2026-09-05 | https://github.com/yishangzhang/vue02 |
| K23 | carterror/almacen-insumos | Bolt.new (Nuxt) | `{"template": "nuxt"}` in `.bolt/config.json` | 2025-03-04 / 2025-03-13 | 2026-09-05 | https://github.com/carterror/almacen-insumos |
| K24 | naveen8041/GNPlantCareApp | Bolt.new (Expo/RN) | `{"template": "bolt-expo"}` in `.bolt/config.json` | 2025-09-09 / 2025-09-16 | 2026-09-05 | https://github.com/naveen8041/GNPlantCareApp |
| K25 | Vikas17187/MediFill_FSD | Bolt.new (Expo/RN) | `{"template": "bolt-expo"}` in `.bolt/config.json` | 2026-05-17 / 2026-06-24 | 2026-09-05 | https://github.com/Vikas17187/MediFill_FSD |
| K26 | murounedecor-creator/AppMurounedecor | Bolt.new (Expo/RN) | `{"template": "bolt-expo", "skills": {...}}` in `.bolt/config.json` | 2026-07-19 / 2026-09-03 | 2026-09-05 | https://github.com/murounedecor-creator/AppMurounedecor |
| K27 | msoheib/makeen | Bolt.new (Expo/RN) + Claude Code | `{"template": "bolt-expo"}` in `.bolt/config.json`; `CLAUDE.md` at root | 2025-10-20 / 2025-12-07 | 2026-09-05 | https://github.com/msoheib/makeen |
| K28 | midlaj-muhammed/CalorAI | Replit Agent (Expo/RN) | `replit.md` titled "CalorAI - Replit Agent Guide", dated changelog entries "Mar 06, 2026" | 2026-03-11 / 2026-03-11 | 2026-09-05 | https://github.com/midlaj-muhammed/CalorAI |
| K29 | davidhoang/tapestry | Replit Agent (Expo/RN + web monorepo) | `replit.md` at root | 2025-06-20 / 2026-06-29 | 2026-09-05 | https://github.com/davidhoang/tapestry |
| K30 | BoomchainLabs/earn-app | Bolt.new (Expo/RN) | `{"template": "bolt-expo"}` in `.bolt/config.json` | — | 2026-09-05 | https://github.com/BoomchainLabs/earn-app |
| K31 | pratit989/Rinse | FlutterFlow | `lib/flutter_flow/flutter_flow_theme.dart` + `FFAppState()` ×78 | 2021-10-20 / 2024-01-12 | 2026-09-05 | https://github.com/pratit989/Rinse |
| K32 | alexkocodes/Fitegy-App | FlutterFlow | `lib/flutter_flow/` export tree; `FlutterFlowTheme.of(context)` ×534 | 2022-10-11 / 2023-07-22 | 2026-09-05 | https://github.com/alexkocodes/Fitegy-App |
| K33 | nomadkaraoke/karaokehunt-app | FlutterFlow | `lib/flutter_flow/` export tree; `FlutterFlowTheme.of(context)` ×484 | 2023-02-17 / 2026-04-20 | 2026-09-05 | https://github.com/nomadkaraoke/karaokehunt-app |
| K34 | uincogn/moto | Replit Agent (Flutter) | `replit.md` at root ("KM$ - Driver Finance Management App", Overview/User Preferences sections) | 2025-07-16 / 2025-08-04 | 2026-09-05 | https://github.com/uincogn/moto |
| K35 | ViaXTrace/Viax-Trace | Replit Agent (Flutter + web) | `replit.md` at root | 2026-04-16 / 2026-09-02 | 2026-09-05 | https://github.com/ViaXTrace/Viax-Trace |
| K36 | albasuny9/Mezanya_LastFrist | Replit Agent (Flutter) | `replit.md` at root | 2026-05-12 / 2026-08-11 | 2026-09-05 | https://github.com/albasuny9/Mezanya_LastFrist |
| K37 | Ameer-Mahmoud/Space-App | Replit Agent (Flutter web) | `replit.md` at root | 2025-10-01 / 2026-06-14 | 2026-09-05 | https://github.com/Ameer-Mahmoud/Space-App |
| K38 | Chaka12/remittance-epay | Replit Agent (Flutter) | `replit.md` at root | — | 2026-09-05 | https://github.com/Chaka12/remittance-epay |
| K39 | MrChartist/Funda-Scanner-Base-Project | Lovable (2026) | `lovable-tagger` in `vite.config.ts` | 2026-03-23 / 2026-04-06 | 2026-09-05 | https://github.com/MrChartist/Funda-Scanner-Base-Project |
| K40 | Ank1t0327/sleepypig | Lovable (2026) | `lovable-tagger` in `vite.config.ts` | 2026-03-10 / 2026-03-15 | 2026-09-05 | https://github.com/Ank1t0327/sleepypig |
| K41 | davoodepb/artesanal-fio-alma | Lovable (2026) | `lovable-tagger` in `vite.config.ts` | 2026-03-13 / 2026-05-09 | 2026-09-05 | https://github.com/davoodepb/artesanal-fio-alma |
| K42 | D4C1-Labs/Flipper-ARF-Website | Lovable (2026) | `lovable-tagger` in `vite.config.ts` | 2026-03-14 / 2026-07-12 | 2026-09-05 | https://github.com/D4C1-Labs/Flipper-ARF-Website |

All 27 owners are distinct accounts, so no two rows are the same author's habits.
`created_at` was not recorded for K30 and K38 (they were cloned from the code-search list without a metadata call); their era claims are therefore not made.

**Bolt template vocabulary, established empirically** (fetched `.bolt/config.json` from 22 repos): `bolt-vite-react-ts`, `nextjs-shadcn`, `vite-react-typescript`, `vite-vue`, `vite-vue-ts`, `nuxt`, `vite-svelte`, `slidev`, `nativescript-react`, `nativescript-javascript`, `bolt-expo`. Note there is **no** `bolt-vue`/`bolt-nuxt`/`bolt-expo-starter` string — a scanner keyed on those would miss every Vue and Expo Bolt project. The Vue/Nuxt/Svelte templates drop the `bolt-` prefix entirely.

---

## Per-repo entries

### K16 — u-x-o-n-e/Focus-App (Bolt.new, Vue)
- **Source:** u-x-o-n-e, GitHub repo, snapshot 2026-09-05. https://github.com/u-x-o-n-e/Focus-App
- **Context:**
  - Provenance: `.bolt/config.json` contains exactly `{ "template": "vite-vue" }`.
  - `tailwind.config.js` aliases the **complete, byte-identical Tailwind `indigo` ramp** to a token named `primary` — all eleven steps `#eef2ff #e0e7ff #c7d2fe #a5b4fc #818cf8 #6366f1 #4f46e5 #4338ca #3730a3 #312e81 #1e1b4b` — with `secondary` = Tailwind `teal` and `accent` = Tailwind `amber`, also verbatim. The seven banned indigo/violet hexes appear 7 times; `indigo` ramp hexes 13 times.
  - Consequently `bg-indigo-600` never appears (0 occurrences) but `*-primary-NNN` appears **105 times**. A scanner looking for indigo classes scores this repo zero.
  - 35 source files. `dark:` variants 415, `hover:bg-` 129, `transition-colors` 48, `shadow-(lg|xl|2xl)` 10, `text-(gray|slate)-(500|600)` 74. Zero lucide, zero shadcn-vue/radix-vue, zero `backdrop-blur`, zero `bg-clip-text`, zero purple, zero `animate-pulse`, zero `hover:scale-105`. 55 hand-written inline `<svg>` elements instead of an icon package.
- **Tags:** `[AVOID: aliasing a stock Tailwind ramp to "primary"]` `[EVIDENCE-ONLY]`
- **Feeds:** Palette laundering — the stock ramp hidden behind a semantic token name

### K17 — hartono0297/splitbill (Bolt.new, Vue)
- **Source:** hartono0297, GitHub repo, snapshot 2026-09-05. https://github.com/hartono0297/splitbill
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "vite-vue" }`.
  - 24 files. Reflex accent is **blue**, not indigo: `*-blue-(500|600)` ×31, `*-(emerald|green)-(500|600)` ×28, `*-violet-*` ×4, `*-purple-*` ×0, `*-indigo-*` ×0.
  - `rounded-(lg|xl)` ×91, `rounded-(2xl|3xl)` ×9, `shadow-(lg|xl|2xl)` ×13, `min-h-screen` ×6, `dark:` ×324. Two-hue `bg-gradient-to-*` washes ×5.
  - Zero lucide, zero `text-muted-foreground`, zero `hsl(var(--`, zero `bg-clip-text`, zero `backdrop-blur`.
- **Tags:** `[AVOID: blue-600 reflex accent]` `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation accent reflex is blue-500/600

### K18 — tiagofrancafernandes/bolt-vue-tailwind-website (Bolt.new, Vue TS)
- **Source:** tiagofrancafernandes, GitHub repo, snapshot 2026-09-05. https://github.com/tiagofrancafernandes/bolt-vue-tailwind-website
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "vite-vue-ts" }`.
  - 34 files, no `tailwind.config.js` colour extension at all. `*-blue-(500|600)` ×20; `text-(gray|slate)-(500|600)` ×14; `min-h-screen` ×8; `max-w-7xl mx-auto` ×2.
  - `<script setup>` ×13 of 12 `.vue` files — Vue 3 SFC idiom, present in 8/8 samples, so useless as a tell.
  - Zero of: lucide, `text-muted-foreground`, gradient of any kind, `backdrop-blur`, `animate-pulse`, `hover:scale-105`, Inter.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K19 — mrodrigueznav/gsict (Bolt.new, Nuxt)
- **Source:** mrodrigueznav, GitHub repo, snapshot 2026-09-05. https://github.com/mrodrigueznav/gsict
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "nuxt" }`.
  - 24 files. `*-blue-(500|600)` ×6, `dark hero bg` ×3, `flex items-center justify-between` ×4, `(md|lg):grid-cols-3` ×1, `min-h-screen` ×1, `hover:bg-` ×11.
  - One `"Inter"` font-family declaration; zero Google-Fonts link.
  - Zero lucide, zero gradients, zero glass, zero `bg-clip-text`.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K20 — alexanderop/todo-app-example (Bolt.new, Nuxt)
- **Source:** alexanderop, GitHub repo, snapshot 2026-09-05. https://github.com/alexanderop/todo-app-example
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "nuxt" }`.
  - 17 files, atomic-design folder tree (`components/atoms|molecules|organisms`) — a structural habit worth noting, but seen once so it fails the bar.
  - `container mx-auto` ×4, `transition duration-*` ×3, `*-blue-(500|600)` ×4, `dark:` ×14.
  - Zero of every React-era tell tested.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K21 — LorenzovandenDungen/yelp (Bolt.new, Vue)
- **Source:** LorenzovandenDungen, GitHub repo, snapshot 2026-09-05. https://github.com/LorenzovandenDungen/yelp
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "vite-vue" }`.
  - 15 files. `tailwind.config.js` extends colours with a single brand token, `'yelp-red': '#d32323'` — i.e. when a brand is named in the prompt, the generator sets one custom hex and nothing else.
  - Total matches across the entire 47-pattern web set: 3 (`<script setup>` ×5, composition-API calls ×10, one green utility). This is a genuine near-null sample.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K22 — yishangzhang/vue02 (Bolt.new, Vue)
- **Source:** yishangzhang, GitHub repo, snapshot 2026-09-05. https://github.com/yishangzhang/vue02
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "vite-vue" }`.
  - 14 files. Exactly one `"Inter"` reference and one `hsl(var(--` — the only Vue sample of eight showing any token-variable pattern, and only once.
  - Zero Tailwind colour utilities of any hue.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K23 — carterror/almacen-insumos (Bolt.new, Nuxt)
- **Source:** carterror, GitHub repo, snapshot 2026-09-05. https://github.com/carterror/almacen-insumos
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "nuxt" }`.
  - 31 files. `<script setup>` ×19, composition-API calls ×85, and **zero matches on every other pattern in the 47-pattern web set** — including every colour, layout, shadow, motion and copy pattern. Uses Nuxt UI components rather than raw utilities.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Vue-generation is chromatically flat (negative result)

### K24 — naveen8041/GNPlantCareApp (Bolt.new, Expo / React Native)
- **Source:** naveen8041, GitHub repo, snapshot 2026-09-05. https://github.com/naveen8041/GNPlantCareApp
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "bolt-expo" }`.
  - `StyleSheet.create` ×11 with the same shadow block re-declared per component: `shadowColor` ×18, `shadowOpacity` ×18, `elevation` ×18 — the three counts are identical, i.e. the block is always emitted whole. `shadowOffset` appears 17 times and **all 17 have `width: 0`**; modal values `{ width: 0, height: 2 }` ×10, `shadowOpacity: 0.05` ×11, `shadowRadius: 4` ×11.
  - `borderRadius` values: 12 ×23, 16 ×15, 8 ×9, 20 ×8. `fontWeight: '600'` ×47 vs `'700'` ×21 vs `'500'` ×1.
  - **13 of the repo's 14 six-digit hex colours are literal Tailwind defaults** (`#F97316 #F8FAFC #F59E0B #EF4444 #E5E7EB #9CA3AF …`) in a project with no Tailwind dependency in use.
  - Icons: `Ionicons` ×83 from `@expo/vector-icons` (×12), `lucide-react-native` ×1.
- **Tags:** `[AVOID: Tailwind hexes in StyleSheet]` `[AVOID: identical inline shadow block per card]` `[EVIDENCE-ONLY]`
- **Feeds:** Straight-down shadow constant; Tailwind palette bleed into non-web code

### K25 — Vikas17187/MediFill_FSD (Bolt.new, Expo / React Native)
- **Source:** Vikas17187, GitHub repo, snapshot 2026-09-05. https://github.com/Vikas17187/MediFill_FSD
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "bolt-expo" }`.
  - `shadowOffset` ×3, **all `width: 0`**. `SafeAreaView` ×29, `flex: 1` ×41, `Tabs.Screen` ×5 (Expo Router tab scaffold).
  - **17 of 30 hex colours are Tailwind defaults** (`#0F172A` ×4, `#F1F5F9` ×2, `#F8FAFC`, `#E2E8F0`, `#DC2626`, `#D97706` …). One banned violet hex.
  - `lucide-react-native` ×10; the cliché icon set (`Sparkles|Zap|Shield|Rocket|ChevronRight|ArrowRight`) ×12. `fontWeight: '600'` ×30 / `'700'` ×29.
- **Tags:** `[AVOID: Tailwind hexes in StyleSheet]` `[EVIDENCE-ONLY]`
- **Feeds:** Tailwind palette bleed into non-web code; lucide-react-native as an RN stack fingerprint

### K26 — murounedecor-creator/AppMurounedecor (Bolt.new, Expo / React Native)
- **Source:** murounedecor-creator, GitHub repo, snapshot 2026-09-05. https://github.com/murounedecor-creator/AppMurounedecor
- **Context:**
  - Provenance: `.bolt/config.json` = `{"template": "bolt-expo", "skills": {}, "systemSkills": {"browser-testing": true, "seo-geo": false, ...}}` — a newer Bolt config shape that also stamps the agent's enabled skills.
  - `StyleSheet.create` ×24; `shadowColor`/`shadowOpacity`/`elevation` = 21/21/21; `shadowOffset` ×21, **all `width: 0`**, `{width: 0, height: 2}` ×12, `shadowOpacity: 0.15` ×12, `shadowRadius: 8` ×15.
  - `LinearGradient` ×72 — by far the heaviest gradient use in the RN set. `Ionicons` ×134. `fontWeight: '700'` ×89 / `'600'` ×78.
  - **0 of its 137 hex colours are Tailwind defaults** — a counter-example to K24/K25, so the palette-bleed tell is ~3/5 in RN, not universal.
- **Tags:** `[AVOID: gradient on every surface]` `[EVIDENCE-ONLY]`
- **Feeds:** Straight-down shadow constant

### K27 — msoheib/makeen (Bolt.new Expo + Claude Code)
- **Source:** msoheib, GitHub repo, snapshot 2026-09-05. https://github.com/msoheib/makeen
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "bolt-expo" }`, plus a root `CLAUDE.md` and 11 all-caps AI-workflow markdown files at repo root (`SECURITY-FIXES-SUMMARY.md`, `WEB-MIGRATION-GUIDE.md`, `MOBILE_SEARCH_FIX.md`, `README-TYPESCRIPT-FIX.md`, …) — a root-level `SHOUTING_SNAKE_CASE.md` litter that is itself a strong agentic-workflow tell.
  - Largest RN sample (364 scanned files). `StyleSheet.create` ×133; `shadowOffset` ×56, **all `width: 0`**; `{width: 0, height: 2}` ×34, `shadowOpacity: 0.1` ×37, `shadowRadius: 4` ×34.
  - `borderRadius`: 8 ×120, 12 ×104, 16 ×64, 20 ×24. `fontWeight: '600'` ×372 — 40% of all weight declarations.
  - `#FFFFFF` ×1268; 29 Tailwind-default hexes; `lucide-react-native` ×81; `placeholder_people` strings ×8; `✨|🚀` in UI copy ×6.
- **Tags:** `[AVOID: SHOUTING_SNAKE_CASE.md litter at repo root]` `[AVOID: fontWeight '600' as the universal emphasis]` `[EVIDENCE-ONLY]`
- **Feeds:** Straight-down shadow constant; the `600` weight monoculture

### K28 — midlaj-muhammed/CalorAI (Replit Agent, Expo / React Native)
- **Source:** midlaj-muhammed, GitHub repo, snapshot 2026-09-05. https://github.com/midlaj-muhammed/CalorAI
- **Context:**
  - Provenance: `replit.md` whose H1 is "CalorAI - Replit Agent Guide", with a "Recent Changes" changelog dated "Mar 06, 2026" — current-generation, and the agent's own memory file.
  - `shadowOffset` ×24, **all `width: 0`**; `shadowColor` ×30 / `shadowOpacity` ×25 / `elevation` ×25.
  - `Inter_` (the `@expo-google-fonts/inter` naming convention, e.g. `Inter_600SemiBold`) appears **224 times** — Inter is not just loaded, it is named on nearly every text style.
  - `borderRadius: (20|24)` ×61 vs `(12|16)` ×36 — a rounder 2026 dialect than the 2025 Bolt samples. `Ionicons` ×150, `LinearGradient` ×13, `gap: (12|16)` ×42.
  - Zero purple, zero indigo, zero banned hexes.
- **Tags:** `[AVOID: Inter on every text style]` `[AVOID: 20-24pt radius everywhere]` `[EVIDENCE-ONLY]`
- **Feeds:** Inter monoculture (2026 RN); straight-down shadow constant

### K29 — davidhoang/tapestry (Replit Agent, Expo + web monorepo)
- **Source:** davidhoang, GitHub repo, snapshot 2026-09-05. https://github.com/davidhoang/tapestry
- **Context:**
  - Provenance: `replit.md` at root ("Workspace / Overview: pnpm workspace monorepo using TypeScript").
  - The only RN sample using NativeWind seriously: Tailwind-style `className=` ×3258 against `StyleSheet.create` ×24. Where NativeWind is used, the RN tells (StyleSheet shadows, numeric borderRadius) collapse and the *web* tells return: 8 banned indigo/violet hexes, `*-indigo-*` classes ×6, `Inter` ×17, `Poppins` ×4.
  - `placeholder_people` strings (John Doe / Acme family) ×12 — the highest in the whole set.
  - Its 2 `shadowOffset` declarations are both `width: 0`.
- **Tags:** `[AVOID: placeholder person names in shipped screens]` `[EVIDENCE-ONLY]`
- **Feeds:** NativeWind flips RN output back onto the web tell set

### K30 — BoomchainLabs/earn-app (Bolt.new, Expo / React Native)
- **Source:** BoomchainLabs, GitHub repo, snapshot 2026-09-05. https://github.com/BoomchainLabs/earn-app
- **Context:**
  - Provenance: `.bolt/config.json` = `{ "template": "bolt-expo" }`.
  - Only 10 scanned files (an early-stage scaffold). `expo-router` ×5, `StyleSheet.create` ×1, `lucide-react-native` ×1, `expo-linear-gradient` ×1, `nativewind` ×3 (dependency declarations, not usage).
  - No shadows, no hex colours at all — recorded as a near-null sample so the RN denominators are honest.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** —

### K31 — pratit989/Rinse (FlutterFlow)
- **Source:** pratit989, GitHub repo, snapshot 2026-09-05. https://github.com/pratit989/Rinse
- **Context:**
  - Provenance: `lib/flutter_flow/flutter_flow_theme.dart` and siblings (`flutter_flow_count_controller.dart`, `flutter_flow_google_map.dart`); `FFAppState()` ×78 in generated pages.
  - 57 generated `.dart` files (FlutterFlow runtime excluded). `BorderRadius.circular(` ×89 of which `(12|16)` ×57; `BoxShadow(` ×29 and `blurRadius:` ×29 — one blur per shadow, no spread variation.
  - Palette is entirely project-specific greys chosen in the visual editor (`0xFF818181` ×107, `0xFFBBBBBB` ×31, `0xFF073131` ×18). **0 Tailwind-default hexes of 296 hex literals.**
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** FlutterFlow provenance is not a design tell (counter-evidence)

### K32 — alexkocodes/Fitegy-App (FlutterFlow)
- **Source:** alexkocodes, GitHub repo, snapshot 2026-09-05. https://github.com/alexkocodes/Fitegy-App
- **Context:**
  - Provenance: `lib/flutter_flow/` export tree; `FlutterFlowTheme.of(context)` ×534 in 67 generated files (≈8 per file).
  - `GoogleFonts.` ×111, all reached through FlutterFlow's own `GoogleFonts.asMap` indirection rather than a named family — so the font choice is invisible to a `GoogleFonts.inter` regex.
  - `BorderRadius.circular(` ×145; `elevation:` ×40; `LinearGradient(` ×14. **0 Tailwind-default hexes of 82.** Top colours `0xFFB1B1B1`, `0xFFE6A0FF`, `0xFF9AE1FF` — editor-picked, unlike anything in the LLM samples.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** FlutterFlow provenance is not a design tell (counter-evidence)

### K33 — nomadkaraoke/karaokehunt-app (FlutterFlow)
- **Source:** nomadkaraoke, GitHub repo, snapshot 2026-09-05. https://github.com/nomadkaraoke/karaokehunt-app
- **Context:**
  - Provenance: `lib/flutter_flow/` export tree; `FlutterFlowTheme.of(context)` ×484, `FFAppState()` ×21.
  - `BorderRadius.circular(8` ×32 dominates (vs 0 at 12/16) — the opposite radius habit to the LLM Flutter samples.
  - **0 Tailwind-default hexes of 35.** Top colours `0xFFFF79CB`, `0xFFFFDF6B` — hot pink and yellow, i.e. a deliberate brand.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** FlutterFlow provenance is not a design tell (counter-evidence)

### K34 — uincogn/moto (Replit Agent, Flutter)
- **Source:** uincogn, GitHub repo, snapshot 2026-09-05. https://github.com/uincogn/moto
- **Context:**
  - Provenance: `replit.md` at root with the Agent's standard "Overview / User Preferences" section structure.
  - 62 `.dart` files. `ColorScheme.fromSeed` ×2 and `useMaterial3: true` ×2 — the LLM reaches for the Material 3 seed API that FlutterFlow never uses (0/3 there).
  - `Card(` ×79, `EdgeInsets.all(16` ×54, `SizedBox(height: 8|12|16|20|24)` ×145 — spacing is expressed as literal `SizedBox` spacers rather than a spacing scale.
  - `BorderRadius.circular(12|16)` ×21 of 44. Shadow `offset:` values are `Offset(0, 10)` ×2 and `Offset(0, 1)` ×1 — **x is 0 in all 3**.
  - `Colors.deepPurple` ×0 — the `flutter create` template default does not appear.
- **Tags:** `[AVOID: SizedBox spacer instead of a spacing scale]` `[EVIDENCE-ONLY]`
- **Feeds:** ColorScheme.fromSeed + Material 3 as an LLM-Flutter marker; straight-down shadow constant

### K35 — ViaXTrace/Viax-Trace (Replit Agent, Flutter)
- **Source:** ViaXTrace, GitHub repo, snapshot 2026-09-05. https://github.com/ViaXTrace/Viax-Trace
- **Context:**
  - Provenance: `replit.md` at root describing a pnpm monorepo with "a Flutter Android app".
  - 31 `.dart` files. **38 of its 87 `Color(0xFF…)` literals are exact Tailwind defaults**: `0xFF0EA5E9 0xFF10B981 0xFF16A34A 0xFF1D4ED8 0xFF22C55E 0xFF3B82F6 0xFF7C3AED 0xFFA855F7 0xFFD97706 0xFFEAB308 0xFFEF4444 0xFFF59E0B 0xFFF97316`. Seven are banned violet hexes (`0xFF7C3AED` ×6, `0xFFA855F7` ×1) and `0xFF7C3AED` is the single most-used colour in the app (×8).
  - `GoogleFonts.poppins` ×7. `FontWeight.w600|w700` ×102 vs `FontWeight.bold` ×0. `BorderRadius.circular(` ×112. `BoxDecoration(` ×113 across 31 files.
  - Shadow `offset:` = `Offset(0, 3)` ×3, `Offset(0, 8)` ×1 — **x is 0 in all 4**.
- **Tags:** `[AVOID: Tailwind hexes in Dart]` `[AVOID: 0xFF7C3AED as primary]` `[EVIDENCE-ONLY]`
- **Feeds:** Tailwind palette bleed into non-web code; violet survives in Dart even where it died in CSS

### K36 — albasuny9/Mezanya_LastFrist (Replit Agent, Flutter)
- **Source:** albasuny9, GitHub repo, snapshot 2026-09-05. https://github.com/albasuny9/Mezanya_LastFrist
- **Context:**
  - Provenance: `replit.md` at root ("Mezanya - Personal Financial Management App").
  - 65 `.dart` files, 659 hex literals — **69 are exact Tailwind defaults** (`0xFF0284C7 0xFF059669 0xFF0891B2 0xFF0D9488 0xFF15803D 0xFF16A34A 0xFF1D4ED8 0xFF22C55E 0xFF2563EB 0xFF7C3AED 0xFFD97706 0xFFDB2777 0xFFDC2626`), including 4 banned violet. The *dominant* colours, however, are a custom brand (`0xFF165B47` ×63, `0xFFC65D2E` ×50) — so Tailwind hexes are the fill-in colours, not the brand.
  - `BorderRadius.circular(` ×553 across 65 files (≈8.5 per file); `(12|16)` ×125, `(20|24)` ×99. `BoxDecoration(` ×453. `FontWeight.w600|w700` ×258 vs `FontWeight.bold` ×6.
  - Shadow `offset:` = `Offset(0, 10)` ×12, `Offset(0, 8)` ×11, `Offset(0, 4)` ×8, `Offset(0, 12)` ×7 — **x is 0 in all 38**.
- **Tags:** `[AVOID: Tailwind hexes in Dart]` `[AVOID: rounding every container]` `[EVIDENCE-ONLY]`
- **Feeds:** Tailwind palette bleed into non-web code; straight-down shadow constant

### K37 — Ameer-Mahmoud/Space-App (Replit Agent, Flutter web)
- **Source:** Ameer-Mahmoud, GitHub repo, snapshot 2026-09-05. https://github.com/Ameer-Mahmoud/Space-App
- **Context:**
  - Provenance: `replit.md` at root ("Space — Solar System Flutter App").
  - 11 `.dart` files. `BorderRadius.circular(12|16)` ×6 of 12; `withOpacity(0.N)` ×14 in 11 files — opacity-derived colour instead of defined tints; `LinearGradient(` ×4; `FontWeight.w600|w700` ×8.
  - **0 of 20 hex literals are Tailwind defaults** — a themed space app (`0xFFEE403D`, `0xFFC62828`, ambers) so the palette-bleed tell is ~2/5 in Flutter.
  - `Colors.deepPurple` ×0.
- **Tags:** `[AVOID: withOpacity as the tint mechanism]` `[EVIDENCE-ONLY]`
- **Feeds:** withOpacity instead of a tint scale

### K38 — Chaka12/remittance-epay (Replit Agent, Flutter)
- **Source:** Chaka12, GitHub repo, snapshot 2026-09-05. https://github.com/Chaka12/remittance-epay
- **Context:**
  - Provenance: `replit.md` at root.
  - 11 `.dart` files and a genuinely minimal surface: `SizedBox(height: 8|12|16|20|24)` ×31, `EdgeInsets.all(16` ×8, `FontWeight.bold` ×21, `Card(` ×6, `Icons.*` ×25, `Colors.(teal|green)` ×4, `Colors.blue` ×1.
  - **Zero hex literals of any kind** — the app is built entirely from `Colors.*` Material constants. Recorded so the Flutter denominators are honest.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** —

### K39 — MrChartist/Funda-Scanner-Base-Project (Lovable, created 2026-03)
- **Source:** MrChartist, GitHub repo, snapshot 2026-09-05. https://github.com/MrChartist/Funda-Scanner-Base-Project
- **Context:**
  - Provenance: `lovable-tagger` imported in `vite.config.ts`.
  - `src/components/ui/` contains **exactly 49 files**; `--radius: 0.5rem` (stock shadcn default) in `src/index.css`; `public/placeholder.svg` present.
  - `text-muted-foreground` ×282, `hsl(var(--` ×326, `cn(` ×199, `lucide-react` imports ×56 across 50 distinct import statements — the semantic-token + lucide stack from K1–K9 replicating unchanged a year later.
  - `bg-clip-text` ×1, `hover:scale-105` ×2, `backdrop-blur` ×3, `animate-pulse` ×2, `(md|lg):grid-cols-3` ×6. `blur-3xl` ×0, purple ×0, indigo ×0, `Trusted by` ×0.
- **Tags:** `[AVOID: complete 49-file shadcn dump]` `[EVIDENCE-ONLY]`
- **Feeds:** The 49-file shadcn dump; token monoculture (`text-muted-foreground` as the only secondary text colour)

### K40 — Ank1t0327/sleepypig (Lovable, created 2026-03)
- **Source:** Ank1t0327, GitHub repo, snapshot 2026-09-05. https://github.com/Ank1t0327/sleepypig
- **Context:**
  - Provenance: `lovable-tagger` in `vite.config.ts`.
  - `src/components/ui/` = **exactly 49 files**; `--radius: 0.75rem`; `public/placeholder.svg` present but **referenced 0 times in `src/`** — dead scaffold left in the shipped repo.
  - `cn(` ×198, `text-muted-foreground` ×88, `hsl(var(--` ×33, `lucide-react` ×26, `min-h-screen` ×10.
  - Zero: purple, indigo, gradients of any kind, `bg-clip-text`, `blur-3xl`, Inter, `hover:scale-105`.
- **Tags:** `[AVOID: unreferenced public/placeholder.svg]` `[EVIDENCE-ONLY]`
- **Feeds:** The 49-file shadcn dump; orphaned placeholder.svg

### K41 — davoodepb/artesanal-fio-alma (Lovable, created 2026-03)
- **Source:** davoodepb, GitHub repo, snapshot 2026-09-05. https://github.com/davoodepb/artesanal-fio-alma
- **Context:**
  - Provenance: `lovable-tagger` in `vite.config.ts`.
  - `src/components/ui/` = **exactly 49 files**; `--radius: 1rem`; `placeholder.svg` referenced in 9 files — i.e. shipped placeholder art.
  - The most decorated of the four: `backdrop-blur` ×7, `bg-white/(5|10|20)` ×5 with `border-white/(10|20|30)` ×4, `blur-3xl` ×1, `hover:scale-105` ×3, `rounded-(2xl|3xl)` ×19, `shadow-(lg|xl|2xl)` ×39, `gap-8` ×9, `(md|lg):grid-cols-3` ×13, hero type ramp ×2, `animate-pulse` ×6, `✨|🚀` ×4.
  - Colour: `*-(emerald|green)-(500|600)` ×19, `*-purple-*` ×5, `*-violet-*` ×1, `*-indigo-*` ×0, purple→pink gradient ×0. `text-muted-foreground` ×363.
- **Tags:** `[AVOID: dark-glass + blur + scale-105 stack]` `[EVIDENCE-ONLY]`
- **Feeds:** The 49-file shadcn dump; the glass/blur/pulse decoration cluster survives into 2026

### K42 — D4C1-Labs/Flipper-ARF-Website (Lovable, created 2026-03)
- **Source:** D4C1-Labs, GitHub repo, snapshot 2026-09-05. https://github.com/D4C1-Labs/Flipper-ARF-Website
- **Context:**
  - Provenance: `lovable-tagger` in `vite.config.ts`.
  - `src/components/ui/` = **exactly 49 files**; `--radius: 0.625rem`; `public/placeholder.svg` present, referenced 0 times.
  - `text-muted-foreground` ×99, `cn(` ×198, `hsl(var(--` ×38, `lucide-react` ×35, `bg-clip-text` ×1, `blur-3xl` ×2, `backdrop-blur` ×3, `max-w-7xl mx-auto` ×1 with `px-4 sm:px-6 lg:px-8` ×2, section anchors (`#features|#pricing|#testimonials|#faq`) ×2.
  - Zero purple, zero indigo, zero `Trusted by`, zero placeholder-person names.
- **Tags:** `[AVOID: complete 49-file shadcn dump]` `[EVIDENCE-ONLY]`
- **Feeds:** The 49-file shadcn dump

---

## Framework signature table

What generated code in each framework actually looks like, with regex-matchable strings and how many of my samples carried each.

### Vue / Nuxt (Bolt.new; 8 samples, K16–K23)

| Signature | Regex | Samples |
|---|---|---|
| Bolt Vue/Nuxt template stamp | `"template":\s*"(vite-vue\|vite-vue-ts\|nuxt)"` in `.bolt/config.json` | 8/8 (provenance) |
| Vue 3 SFC idiom | `<script setup` | 8/8 — **fails the bar, ordinary Vue** |
| No icon library at all; hand-rolled inline SVG | absence of `lucide-vue-next\|@heroicons\|@iconify\|nuxt-icon` in `package.json` | 8/8 have no icon dep; inline `<svg>` up to ×55 |
| Blue as the reflex accent | `(bg\|text\|border\|from\|to)-blue-(500\|600)` | 5/8 (×20, ×31, ×6, ×4, ×1) |
| Grey secondary text | `text-(gray\|slate)-(500\|600)` | 5/8 (up to ×74) |
| `dark:` variant on nearly every colour utility | `\bdark:[a-z]` | 6/8 (×415, ×324, ×15, ×14) |
| Stock Tailwind ramp aliased to `primary`/`secondary`/`accent` | eleven-step ramp of exact hexes inside `tailwind.config.js` `colors:` | **1/8** — high specificity, low prevalence |
| shadcn-vue / radix-vue / reka-ui | `(shadcn-vue\|radix-vue\|reka-ui)` | **0/8** |
| Semantic token vocabulary | `text-muted-foreground`, `hsl\(var\(--` | **0/8**, **1/8** |

**Reading:** Vue output is a different visual dialect from the same vendors' React output. It has no component-library dump, no icon package, no token layer, no glassmorphism, no gradient headlines. Its only consistent chromatic habit is blue-500/600 plus grey-500/600 text. A scanner tuned on React-generated Tailwind will score generated Vue as human.

### React Native / Expo (Bolt `bolt-expo` and Replit Agent; 7 samples, K24–K30)

| Signature | Regex | Samples |
|---|---|---|
| Bolt Expo stamp / Replit Agent memory file | `"template":\s*"bolt-expo"`; file `replit.md` | 5/7 + 2/7 (provenance) |
| Shadow is always straight down (see T1 — *not* an AI tell) | `shadowOffset:\s*\{\s*width:\s*0` vs `width:\s*[1-9-]` | 6/6 applicable; **123/123 occurrences have `width: 0`** |
| Shadow block emitted whole, per component | equal counts of `shadowColor:`, `shadowOpacity:`, `elevation:` in one file set | 4/7 (18/18/18, 3/3/3, 21/21/21, 25/25 + 30) |
| Modal shadow parameters | `\{ *width: 0, *height: 2 *\}`, `shadowOpacity: 0\.(05\|1\|15)`, `shadowRadius: (4\|8)` | 4/7 |
| `fontWeight: '600'` as universal emphasis | `fontWeight: ['"]600['"]` | 5/7; the plurality weight in 3/7 (×47, ×372, ×30) |
| 8 / 12 / 16 radius family | `borderRadius: (8\|12\|16)` | 6/7 |
| Tailwind default hexes in `StyleSheet` | `#(3B82F6\|16A34A\|EF4444\|F59E0B\|0F172A\|6B7280\|F8FAFC\|…)` | **3/5 with any hex** (13/14, 17/30, 29/560) |
| lucide-react-native | `lucide-react-native` | 6/7 |
| Ionicons via `@expo/vector-icons` | `Ionicons` | 4/7 (×83, ×134, ×150) |
| Expo Router tab scaffold | `Tabs\.Screen` | 6/7 |
| Inter via `@expo-google-fonts` | `Inter_(Regular\|Medium\|SemiBold\|Bold\|\d{3})` | 2/7, but ×224 in the 2026 sample |
| NativeWind | `className=["'][^"']*(bg-\|text-\|flex-)` in `.tsx` | 1/7 — and where present, the web tells return |

### Flutter (LLM: Replit Agent, 5 samples K34–K38; visual builder: FlutterFlow, 3 samples K31–K33)

| Signature | Regex | LLM samples | FlutterFlow samples |
|---|---|---|---|
| Provenance | `replit.md` / `lib/flutter_flow/` + `FlutterFlowTheme\.of\(context\)` | 5/5 | 3/3 |
| Shadow offset x = 0 (see T1 — *not* an AI tell) | `offset:\s*(const )?Offset\(\s*0[,.]` | 4/4 with any shadow; **72/72 occurrences** | **3/3 applicable; 49/49 occurrences** |
| `BorderRadius.circular(12\|16)` | `BorderRadius\.circular\((12\|16)\)` | 5/5 | 2/3 |
| One `blurRadius` per `BoxShadow`, never a spread | equal counts of `BoxShadow\(` and `blurRadius:` | 4/5 | 3/3 |
| Material 3 seed API | `ColorScheme\.fromSeed`, `useMaterial3: true` | 3/5, 4/5 | **0/3** |
| `FontWeight.w600\|w700` over `FontWeight.bold` | `FontWeight\.w(600\|700)` | 3/5 (×102, ×258, ×9) | 2/3 |
| `SizedBox(height: 8\|12\|16\|20\|24)` as the spacing system | `SizedBox\(height: (8\|12\|16\|20\|24)\)` | 5/5 (×145, ×289, ×70, ×31, ×10) | 0/3 |
| Tailwind default hexes in Dart | `0xFF(3B82F6\|16A34A\|EF4444\|7C3AED\|D97706\|…)` | **2/5** (38/87 and 69/659) | **0/3** (0 of 413 hex literals) |
| `FlutterFlowTheme.of(context)` on every widget | `FlutterFlowTheme\.of\(context\)` | 0/5 | 3/3 (×534, ×484; ~8 per file) |
| `Colors.deepPurple` (`flutter create` default) | `Colors\.deepPurple` | **0/5** | **0/3** |

### Current-generation web (Lovable, all four repos created March 2026; 4 samples K39–K42)

| Signature | Regex / test | Samples |
|---|---|---|
| Lovable tagger | `lovable-tagger\|componentTagger` in `vite.config.ts` | 4/4 (provenance) |
| **Exactly 49 files in `src/components/ui/`** | file count of that directory | **4/4** |
| `public/placeholder.svg` present | file exists | 4/4; **unreferenced in `src/` in 2/4** |
| `cn(` from `clsx` + `tailwind-merge` | `\bcn\(` | 4/4 — ×198, ×198, ×199, ×211 (near-identical, i.e. the dump not the app) |
| `text-muted-foreground` as the only secondary text colour | `text-muted-foreground` | 4/4 (×88 – ×363) |
| HSL token block | `hsl\(var\(--` | 4/4 (×33 – ×326) |
| lucide-react | `from ['"]lucide-react['"]` | 4/4 (×26 – ×66) |
| `--radius` varies per project | `--radius: [0-9.]+rem` | 0.5 / 0.625 / 0.75 / 1 rem — the *token block* is themed, the *dump* is not |
| `backdrop-blur` | `backdrop-blur` | 4/4 (×1 – ×7) |
| `animate-pulse` | `animate-pulse` | 4/4 (×1 – ×6) |
| `(md\|lg):grid-cols-3` | as written | 3/4 |
| Top lucide icons across all four | `ChevronRight` ×64, `X` ×52, `Search` ×37, `TrendingUp` ×34, `ArrowRight` ×32, `Shield` ×20, `Heart` ×19, `Star` ×17, `Users` ×16, `CheckCircle2` ×16 | — |
| purple / indigo / purple→pink gradient | see counter-evidence | **0/4, 0/4, 0/4** |

---

## Candidate tells

### T1 — Straight-down shadow constant (`width: 0` / `Offset(0, N)`)
- **Description:** In generated React Native and Flutter, every elevation shadow is offset purely vertically. Human mobile code varies (side-lit cards, inset shadows, shared shadow utilities); generated code re-derives the same downward block per component.
- **Supporting IDs:** K24, K25, K26, K27, K28, K29 (RN, 97/97 occurrences), K34, K35, K36, K37 (Flutter, 23/23 occurrences).
- **Draft regex:** RN — `shadowOffset:\s*\{\s*width:\s*0\s*,\s*height:\s*\d+`; Flutter — `offset:\s*(const\s*)?Offset\(\s*0\s*,`. Score when the count of x=0 offsets is ≥5 **and** the count of non-zero-x offsets is 0.
- **Era:** 2025–2026, both Bolt and Replit Agent.
- **False positives:** Material Design's own guidance is a downward key light, so a *few* downward shadows are normal. The tell is the **absence of any variation across a whole app** plus the block being inlined rather than shared. Mitigate by requiring ≥5 declarations and a 0% non-zero-x rate.
- **Verdict:** **Passes** — 10 independent repos, 120/120 occurrences.

### T2 — Tailwind default palette hexes in non-Tailwind code
- **Description:** Dart and React Native `StyleSheet` files carry literal Tailwind v3 default hexes. Flutter has no Tailwind; RN outside NativeWind has none either. This is training-data bleed and is essentially inexplicable in hand-written code.
- **Supporting IDs:** K24 (13 of 14 hexes), K25 (17 of 30), K27 (29 of 560), K35 (38 of 87 Dart literals), K36 (69 of 659).
- **Draft regex:** `(#|0xFF)(EF4444|DC2626|F97316|EA580C|F59E0B|D97706|EAB308|22C55E|16A34A|15803D|10B981|059669|14B8A6|0D9488|0EA5E9|0284C7|3B82F6|2563EB|1D4ED8|6366F1|4F46E5|8B5CF6|7C3AED|A855F7|DB2777|64748B|475569|1E293B|0F172A|94A3B8|CBD5E1|E2E8F0|F1F5F9|F8FAFC|6B7280|4B5563|374151|1F2937|111827|9CA3AF|D1D5DB|E5E7EB|F3F4F6|F9FAFB)\b` restricted to `*.dart` and RN `*.tsx|*.ts|*.js` files.
- **Era:** 2025–2026.
- **False positives:** a team that genuinely ported a Tailwind design system to mobile; a designer who used Tailwind's palette as a reference. Mitigate by scoring the **ratio** (Tailwind hexes / all hexes) rather than the raw count — 93% and 57% in K24/K25 are not a coincidence, 5% would be.
- **Verdict:** **Passes** — 5 independent repos across two frameworks and two generators, with a clean control group (0 of 413 hex literals in the three FlutterFlow repos).

### T3 — The 49-file shadcn dump
- **Description:** Current-generation Lovable ships `src/components/ui/` with exactly 49 stock shadcn files regardless of what the app needs, and `cn(` occurrence counts cluster at 198–211 because almost all of them come from the dump rather than the app.
- **Supporting IDs:** K39, K40, K41, K42 (4/4).
- **Draft regex / test:** count files in `**/components/ui/` == 49 **and** `\bcn\(` count in the 190–215 band **and** `lovable-tagger|componentTagger` present. Weaker version without the tagger: 49-file dump + ratio of imported-to-present ui components < 0.5.
- **Era:** 2026 (Lovable). K1–K9 recorded 30–50 files in 2025; 49 is the current fixed number.
- **False positives:** a human running `npx shadcn add` for every component — rare but real. Mitigate with the unimported-ratio test.
- **Verdict:** **Passes** as a *scaffold* tell; it says "AI-scaffolded", not "AI-designed".

### T4 — Orphaned `public/placeholder.svg`
- **Description:** The Lovable/v0 scaffold file survives into shipped repos with zero references from `src/`.
- **Supporting IDs:** K40, K42 (present and unreferenced); K39, K41 (present and referenced).
- **Draft regex / test:** `public/placeholder.svg` exists AND `grep -rl 'placeholder\.svg' src/` returns 0 files.
- **Era:** 2026.
- **False positives:** near zero. A human does not create that exact filename and then never use it.
- **Verdict:** **Passes** — 2 independent samples, near-zero FP. Note the older `/placeholder.svg?height=\d+&width=\d+` query-string form from K2/K7/K9 appeared **0 times** in the 2026 Lovable samples; the file survives, the query-string API does not.

### T5 — Stock Tailwind ramp aliased to a semantic token name
- **Description:** `tailwind.config.js` defines `primary` (and often `secondary`/`accent`) as the eleven-step, byte-identical Tailwind `indigo` / `teal` / `amber` scales, so the code reads `bg-primary-600` and no indigo-class regex ever fires.
- **Supporting IDs:** K16 only.
- **Draft regex:** in `tailwind.config.*`, `500:\s*['"]#6366f1['"]` within 15 lines of `600:\s*['"]#4f46e5['"]` — or more generally, ≥6 consecutive steps of any Tailwind default scale under a non-colour key name.
- **Era:** 2025 (Bolt Vue).
- **False positives:** low; a human aliasing the ramp usually picks a subset or tweaks a step.
- **Verdict:** **Fails the bar for now — 1 sample.** But it is worth carrying as a *scanner improvement* rather than a tell: it explains why indigo counts are zero in the Vue set and should be checked before any "no indigo, therefore human" conclusion.

### T6 — `SizedBox` spacers instead of a spacing scale (Flutter)
- **Description:** Vertical rhythm expressed as literal `SizedBox(height: 16)` widgets scattered through the tree rather than padding tokens or a `Gap` widget.
- **Supporting IDs:** K34 (×145), K36 (×289), K35 (×70), K38 (×31), K37 (×10) — 5/5 LLM-Flutter; **0/3 FlutterFlow**.
- **Draft regex:** `SizedBox\(\s*height:\s*(4|8|12|16|20|24|32)\s*\)`; score at density > 1.5 per `.dart` file.
- **Era:** 2025–2026.
- **False positives:** **high** — this is extremely common in hand-written Flutter and is what the Flutter docs themselves show. The discriminating fact is the 5/5 vs 0/3 split against FlutterFlow, which is a machine baseline rather than a human one.
- **Verdict:** **Fails the bar — indistinguishable from ordinary Flutter idiom.** Keep as a co-occurrence multiplier only.

### T7 — `fontWeight: '600'` monoculture (React Native)
- **Description:** Semibold used for every emphasis level; a real type scale would distinguish 500/600/700 by role.
- **Supporting IDs:** K24 (600 ×47 vs 700 ×21 vs 500 ×1), K27 (600 ×372 of ~700 declarations), K25 (600 ×30 / 700 ×29). K26 inverts it (700 ×89 / 600 ×78).
- **Draft regex:** `fontWeight:\s*['"]600['"]` — score when it is ≥50% of all `fontWeight` declarations and ≥20 in absolute terms.
- **Era:** 2025–2026.
- **False positives:** moderate. Many design systems standardise on semibold.
- **Verdict:** **Passes weakly** — 3 independent samples, but with one clear counter-example in the same corpus. Use as a density signal, never alone.

### T8 — `ColorScheme.fromSeed` + `useMaterial3: true` as an LLM-Flutter marker
- **Description:** LLM-written Flutter reaches for the Material 3 seed-colour API; the visual builder never does.
- **Supporting IDs:** K34, K36, and one further LLM sample (`useMaterial3` 4/5); **0/3** FlutterFlow.
- **Draft regex:** `ColorScheme\.fromSeed\(` and `useMaterial3:\s*true`.
- **Era:** 2025–2026.
- **False positives:** **very high** — this is the `flutter create` starter template. It distinguishes LLM-written from FlutterFlow-exported, not AI from human.
- **Verdict:** **Fails the bar as a design tell.** Useful only for classifying *which* generator, and only in combination with `replit.md`.

### T9 — Root-level `SHOUTING_SNAKE_CASE.md` litter
- **Description:** Repos driven by an agentic coding loop accumulate all-caps markdown status files at the root: `SECURITY-FIXES-SUMMARY.md`, `WEB-MIGRATION-GUIDE.md`, `README-TYPESCRIPT-FIX.md`, `MOBILE_SEARCH_FIX.md`, `PHOTOCAPTURE_FIXES.md`, `DEBUG_USER_CONTEXT.md`, plus `CLAUDE.md`.
- **Supporting IDs:** K27 (11 such files at root).
- **Draft regex / test:** count of root-level files matching `^[A-Z0-9][A-Z0-9_-]{4,}\.md$`, excluding `README.md|LICENSE.md|CHANGELOG.md|CONTRIBUTING.md|CODE_OF_CONDUCT.md|SECURITY.md`; score at ≥4.
- **Era:** 2025–2026 (Claude Code / agentic loops).
- **False positives:** some human projects do this too.
- **Verdict:** **Fails the bar — 1 sample.** Flagged for a future sweep; it is a repository-hygiene tell rather than a design tell, but it is cheap to check and near-free of ambiguity at ≥6 files.

### T10 — No icon library at all in generated Vue
- **Description:** Generated Vue ships hand-written inline `<svg>` paths instead of importing an icon package — the inverse of the lucide fingerprint in generated React.
- **Supporting IDs:** K16 (55 inline `<svg>`), K17 (28), K18 (3), K20 (2), and 8/8 with no icon dependency in `package.json`.
- **Draft regex / test:** `.vue` files contain ≥10 inline `<svg` AND `package.json` matches none of `lucide-vue-next|@heroicons/vue|@iconify|nuxt-icon|@vicons`.
- **Era:** 2024–2026 (Bolt).
- **False positives:** moderate — plenty of humans inline SVGs. And the *absence* of a dependency is weak evidence on its own.
- **Verdict:** **Passes weakly** as a framework-dialect fact rather than a slop tell. Its main value is defensive: it tells a scanner not to expect lucide in Vue.

---

## Counter-evidence

Negative results, measured across the 19 web-and-RN repos that could structurally match Tailwind classes (K16–K30, K39–K42), and the 8 Flutter repos where a Dart equivalent exists.

| Popular claimed tell | Measured result | Verdict |
|---|---|---|
| **Purple→pink gradient** (`from-purple-* … to-pink-*`) | **0 occurrences in 19/19 repos.** Not one match anywhere in the corpus. | Confirms and extends the register's existing downgrade. It is dead across Vue, RN and 2026 Lovable, not just 2025 React. |
| **`bg-indigo-500` / `indigo-600`** | **0 in 18/19.** The single exception is K29, a NativeWind monorepo, with 6. In Vue: 0/8. In 2026 Lovable: 0/4. | Stale. But see T5 — in K16 the indigo *hexes* are present, renamed `primary`. A zero indigo-class count is not proof of absence of indigo. |
| **The seven banned indigo/violet hexes** | 0 in 16/19 web/RN repos (present in K16 ×7 via the config alias, K27 ×3, K29 ×8). In Dart: present in 2/8 (K35 ×7, K36 ×4) — and in K35 `0xFF7C3AED` is the app's most-used colour. | **Partly alive, but it has migrated to Dart.** Violet died in CSS and survived in `Color(0xFF…)`. A CSS-only scanner will miss it entirely. |
| **Gradient-clipped headline text** (`bg-clip-text` + `text-transparent`) | 0 in 17/19; exactly 1 occurrence each in K39 and K42. | Almost gone from Lovable output; absent from Vue and RN. Downgrade further. |
| **`blur-3xl` glow blobs** | 0 in 17/19; K41 ×1, K42 ×2. | Rare, and only in Lovable. Do not expect it outside React. |
| **`hover:scale-105`** | 0 in 15/19; K39 ×2, K41 ×3. | Much weaker than the register implies. |
| **Inter via Google Fonts** | 0 in 13/19 web/RN. But K28 uses `Inter_*` **224 times** and K29 uses Inter ×17 + Poppins ×4. | Not a web tell any more; **it has become a React Native tell.** The 2026 Replit Agent RN sample names Inter on essentially every text style. |
| **"Trusted by N+" / vanity stats** | **0 occurrences in 19/19.** | Does not replicate outside marketing-landing-page prompts. |
| **`Colors.deepPurple` / the `flutter create` default theme** | **0 in 8/8 Flutter repos**, LLM and FlutterFlow alike. | The most commonly repeated "AI Flutter" claim in blog posts. It did not appear once. |
| **FlutterFlow output has a recognisable look** | `FlutterFlowTheme.of(context)` fires 484–534 times per repo (near-perfect provenance) but the palettes are entirely project-specific: `0xFF818181`/`0xFF073131` (K31), `0xFFE6A0FF`/`0xFF9AE1FF` (K32), `0xFFFF79CB`/`0xFFFFDF6B` (K33), with **0 Tailwind hexes across 413 literals** and **0 `ColorScheme.fromSeed`**. Even radius habits diverge (K33 prefers 8, K31 prefers 12/16). | **FlutterFlow provenance is not a design tell.** It proves a tool was used and predicts nothing about how the result looks — because a human picked every colour in a visual editor. This is the cleanest control group in the corpus and it is what makes T2 credible. |
| **shadcn-vue / radix-vue in generated Vue** | 0/8. | The component-library dump is a React-only phenomenon in this corpus. |
| **`text-muted-foreground` as a cross-framework tell** | 4/4 in 2026 Lovable (×88–×363) but **0/8 in Vue** and 0/7 in RN. | Confirmed strong for React, worthless elsewhere. |
| **`max-w-7xl mx-auto` + `px-4 sm:px-6 lg:px-8`** (the Tailwind-UI container fossil) | 3/19 and 1/19 respectively. | Remains the low-prevalence, high-specificity minor signal K1–K15 described. No change. |

---

## Gaps

1. **Cursor.** No file-level provenance exists. `.cursorrules` and `.cursor/rules/` prove the *editor* was configured, not that any given component was generated; and Cursor leaves no artifact in the output. I found no way to build a Cursor sample set that would meet this file's evidence bar, and I did not include any Cursor repo.
2. **GitHub Copilot.** `author:copilot-swe-agent[bot]` returns millions of commits, so the agent *is* identifiable — but the repos it appears in are overwhelmingly libraries, SDKs and config work (ClickHouse, TypeScript, kiota in my sample of 15), not UI. Copilot also edits existing code rather than scaffolding it, so even a Copilot-authored commit does not tell you the design was Copilot's. **No UI-bearing Copilot sample met the bar.**
3. **GPT-5-era / ChatGPT web output.** The only ChatGPT-provenanced sample in the register is K12, GPT-3 era. Modern ChatGPT canvas output is pasted into repos without any marker. I found no repo whose README both claimed GPT-5-era generation and showed a matching commit pattern.
4. **Claude-era web UI specifically.** `"Generated with Claude Code"` commit trailers are findable and date-filterable, but in my searches (39 hits for Vue since May 2026; 8 for Dart since January 2026; 13 distinct TypeScript repos since June 2026) the hits are agent-tooling and infrastructure repos, not designed front-ends. The one candidate I pulled (`HeyBene/OpenBene`) had no trailer readable in a depth-1 clone and was rejected. **The Claude-era web gap remains open** — K11 (the curated Claude hero-section directory) is still the only Claude web evidence, and it is a biased showcase.
5. **v0 in 2026.** I found 86,016 code hits for `placeholder.svg?height` but did not date-filter and clone a 2026-created v0 repo; the 2026 web samples here are all Lovable. A v0-2026 sweep would be the highest-value next step, since it would test whether the 49-file dump number is Lovable-specific or shared.
6. **SwiftUI, Jetpack Compose, Svelte, Angular.** No provenance markers exist that I could find. Bolt has a `vite-svelte` template (seen in `arnoan/sb1-1xrnn6`) so a Svelte sweep is feasible; I did not have room for it.
7. **Sample-dilution measurement.** I excluded one repo (`Aditya27T/Smart-Ndelik-5.0-react-native`) for having lost its generated scaffold, and two of the Vue samples (`Waterloo/TackPad`, `pratik227/zap_dashboard`, 2.5 MB and 25 MB) were cloned but excluded from counts as too heavily hand-edited after the Bolt scaffold to attribute. There is no principled measure here — a commit-count-since-scaffold test would make the corpus more defensible.
8. **Denominator honesty.** Three Vue samples (K21, K22, K23) and one RN sample (K30) are near-null: they match almost nothing. They are counted in every denominator above, which is why prevalence figures like "5/8" rather than "5/5" appear. Removing them would inflate every rate by roughly a third.
