#!/usr/bin/env python3
"""ai_tell_scan.py - measures how "AI-generated" a design's code looks.

Part of the anti-ai-design-style skill. Python 3.8+, standard library only.

What it does, in plain words:
  It reads your web files and looks for the patterns that make sites read as
  AI-generated (the "tells register" in reference/tells-register.md). It gives
  two separate scores:

    AI-look score  (0-100, lower is better) - how strongly the code matches
                   known AI-output patterns. Co-occurrence matters: no single
                   ordinary tell can fail you on its own.
    Craft flags    - accessibility/quality problems (low contrast, no
                   reduced-motion path, ...). These are NOT proof of AI;
                   they are just problems worth fixing.
    Library misuse - a ported library (GSAP, animate.css, Lenis, PixiJS,
                   Leaflet, ...) used in the way that produces a known tell.
                   The library is fine; this use of it is not.

  "Near-proof" findings (generator plumbing like lovable-tagger) are reported
  separately - one of those means the project was AI-generated, full stop.

Usage:
  python3 ai_tell_scan.py path/to/file-or-folder [more paths...]
  python3 ai_tell_scan.py page.html --json          # machine-readable output
  python3 ai_tell_scan.py --selftest                # verify the scanner works
  python3 ai_tell_scan.py page.html --max-ai 20     # custom pass threshold

Exit codes: 0 = pass (AI score below threshold, no provenance hits)
            1 = fail (fix the named findings and rescan)
            3 = usage / internal error
"""

import argparse
import json
import os
import re
import sys
import hashlib
from collections import defaultdict

SCAN_EXTENSIONS = {".html", ".htm", ".css", ".scss", ".less", ".js", ".jsx",
                   ".ts", ".tsx", ".vue", ".svelte", ".astro", ".mdx",
                   # Mobile source. Several 2026 tells only exist here: a Flutter
                   # theme file or a Compose theme is where the untouched scaffold
                   # palette survives, and neither is reachable from a .html scan.
                   ".dart", ".kt"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "vendor",
             "__pycache__", ".venv"}
DEFAULT_MAX_AI = 20
AI_SCORE_CAP = 100

HERE = os.path.dirname(os.path.abspath(__file__))


def rules_path():
    return os.path.join(HERE, "rules.json")


def fingerprint(path=None):
    """Short hash of the rule data itself.

    Two scans quoting the same fingerprint provably ran against the same
    rules. It hashes rules.json, not this file, because the rules are what
    a verdict actually depends on - editing a threshold changes the answer,
    and the fingerprint changes with it. Same idea as the brand guard's
    fingerprint over its derived colour set.
    """
    with open(path or rules_path(), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def load_rules():
    with open(rules_path(), encoding="utf-8") as f:
        return json.load(f)


def gather_files(paths):
    """Expand files/folders into the list of scannable files."""
    out = []
    for p in paths:
        if os.path.isfile(p):
            out.append(p)
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for name in files:
                    if os.path.splitext(name)[1].lower() in SCAN_EXTENSIONS \
                            or name in ("replit.md", "config.json", "README.md",
                                        "package.json", "vite.config.ts"):
                        out.append(os.path.join(root, name))
        else:
            print(f"warning: {p} not found, skipping", file=sys.stderr)
    return out


def compile_patterns(patterns):
    compiled = []
    for pat in patterns:
        try:
            compiled.append(re.compile(pat))
        except re.error as e:
            print(f"internal: bad pattern {pat!r}: {e}", file=sys.stderr)
    return compiled


class Finding:
    def __init__(self, rule_id, name, points, files, evidence, explain, fix, kind):
        self.rule_id = rule_id
        self.name = name
        self.points = points
        self.files = sorted(set(files))
        self.evidence = evidence[:3]  # keep reports short
        self.explain = explain
        self.fix = fix
        self.kind = kind  # provenance | tell | craft | library

    def to_dict(self):
        return {"id": self.rule_id, "name": self.name, "points": self.points,
                "files": self.files, "evidence": self.evidence,
                "why_it_matters": self.explain, "fix": self.fix, "kind": self.kind}


def scan_texts(texts, rules):
    """texts: {path: content}. Returns (provenance, tells, craft, library)."""
    findings_prov, findings_tell, findings_craft = [], [], []
    all_text = "\n".join(texts.values())
    basenames = {os.path.basename(p).lower() for p in texts}

    # --- Provenance -------------------------------------------------------
    for rule in rules["provenance"]:
        hits, files = [], []
        for pat in compile_patterns(rule.get("patterns", [])):
            for path, text in texts.items():
                m = pat.search(text)
                if m:
                    hits.append(m.group(0)[:80])
                    files.append(path)
        for fname in rule.get("filenames", []):
            if fname.lower() in basenames:
                hits.append(fname)
                files.append(fname)
        if hits:
            findings_prov.append(Finding(rule["id"], rule["name"], rule["points"],
                                         files, hits, rule["explain"], rule["fix"],
                                         "provenance"))

    # --- Code tells -------------------------------------------------------
    for rule in rules["code_tells"]:
        matched_files, evidence = [], []
        # A rule may be scoped to file types. Tailwind's default hexes mean
        # nothing in a Tailwind project and quite a lot in a .dart file, so the
        # scope is part of the evidence, not an optimisation.
        if rule.get("only_ext"):
            scope = {path: text for path, text in texts.items()
                     if os.path.splitext(path)[1].lower() in rule["only_ext"]}
            if not scope:
                continue
        else:
            scope = texts
        if "combo" in rule:
            # every combo member is checked project-wide; scores when
            # combo_min of them are present (co-occurrence logic)
            present = []
            for pat_src in rule["combo"]:
                pat = re.compile(pat_src)
                m = pat.search("\n".join(scope.values()))
                if m:
                    present.append(m.group(0)[:60])
            extra_ok = True
            if "extra" in rule:
                extra_ok = re.search(rule["extra"], "\n".join(scope.values())) is not None
            if len(present) >= rule.get("combo_min", len(rule["combo"])) and extra_ok:
                evidence = present
                matched_files = [p for p, t in scope.items()
                                 if any(re.search(c, t) for c in rule["combo"])]
        else:
            distinct = set()
            count = 0
            for pat in compile_patterns(rule.get("patterns", [])):
                for path, text in scope.items():
                    for m in pat.finditer(text):
                        if rule.get("exclude_context"):
                            start = max(0, m.start() - 120)
                            ctx = text[start:m.end() + 120]
                            if re.search(rule["exclude_context"], ctx):
                                continue
                        count += 1
                        distinct.add(m.group(0))
                        if len(evidence) < 5:
                            evidence.append(m.group(0)[:60])
                        matched_files.append(path)
            if rule.get("min_distinct") and len(distinct) < rule["min_distinct"]:
                continue
            if rule.get("min_count") and count < rule["min_count"]:
                continue
            if count == 0:
                continue
        if evidence:
            findings_tell.append(Finding(rule["id"], rule["name"], rule["points"],
                                         matched_files or list(scope), evidence,
                                         rule["explain"], rule["fix"], "tell"))

    # --- Copy tells on markup text ---------------------------------------
    ct = rules["copy_tells"]
    lower_all = all_text.lower()
    verb_hits = sorted({w for w in ct["transformation_verbs"] if w in lower_all})
    if verb_hits:
        pts = min(len(verb_hits), 4)
        findings_tell.append(Finding(
            "CP1", "Buzzword copy", pts, list(texts), verb_hits,
            "Words like these fit 500 other products, which is exactly the problem"
            " - and they are the words AI reaches for first.",
            "Replace each with the specific thing your product does"
            " ('saves you re-typing invoices' beats 'streamlines workflows').",
            "tell"))
    cadence_hits = sorted({w for w in ct["ai_cadence"] if w in lower_all})
    if len(cadence_hits) >= 2:
        findings_tell.append(Finding(
            "CP2", "AI writing cadence", 2, list(texts), cadence_hits,
            "Two or more classic AI phrasings together ('it's not just X...',"
            " 'in today's fast-paced world').",
            "Read it aloud. Rewrite in the words you'd say to a customer.",
            "tell"))
    fake_hits = []
    for pat in compile_patterns(ct["fake_proof_regex"]):
        m = pat.search(all_text)
        if m:
            fake_hits.append(m.group(0))
    if fake_hits:
        findings_tell.append(Finding(
            "CP3", "Fake-looking proof", min(1 + len(fake_hits), 4), list(texts),
            fake_hits,
            "Round unverifiable numbers read as invented and destroy trust.",
            "Use a real number you can back up, or drop the claim.", "tell"))

    # --- Craft checks -----------------------------------------------------
    for chk in rules["craft_checks"]["checks"]:
        if "requires" in chk:
            has_req = any(re.search(r, all_text) for r in chk["requires"])
            missing = all(not re.search(mreg, all_text) for mreg in chk["missing"])
            if has_req and missing:
                findings_craft.append(Finding(chk["id"], chk["name"], 0,
                                              list(texts), [],
                                              chk["explain"], chk["fix"], "craft"))
            continue
        count, evidence, files = 0, [], []
        for pat in compile_patterns(chk.get("patterns", [])):
            for path, text in texts.items():
                for m in pat.finditer(text):
                    count += 1
                    if len(evidence) < 3:
                        evidence.append(m.group(0)[:60])
                    files.append(path)
        if count and count >= chk.get("min_count", 1):
            if "missing" in chk and any(re.search(mreg, all_text) for mreg in chk["missing"]):
                continue
            findings_craft.append(Finding(chk["id"], chk["name"], 0, files,
                                          evidence, chk["explain"], chk["fix"],
                                          "craft"))


    # --- Library misuse -------------------------------------------------
    findings_lib = []
    for rule in rules.get("library_misuse", {}).get("rules", []):
        evidence, files = [], []
        if "requires" in rule:
            if any(re.search(r, all_text) for r in rule["requires"]) and \
               all(not re.search(m, all_text) for m in rule["missing"]):
                evidence = ["library present, required option missing"]
                files = list(texts)
        else:
            count = 0
            for pat in compile_patterns(rule.get("patterns", [])):
                for path, text in texts.items():
                    for m in pat.finditer(text):
                        count += 1
                        if len(evidence) < 4:
                            evidence.append(m.group(0)[:60])
                        files.append(path)
            if count < rule.get("min_count", 1):
                evidence = []
        if evidence:
            findings_lib.append(Finding(rule["id"], rule["name"], rule["points"],
                                        files or list(texts), evidence,
                                        rule["explain"], rule["fix"], "library"))

    return findings_prov, findings_tell, findings_craft, findings_lib


def band_for(score, rules):
    for lo, hi, label in rules["scoring"]["ai_bands"]:
        if lo <= score <= hi:
            return label
    return "off the scale"


def report(prov, tells, craft, lib, rules, max_ai, as_json=False, scanned=0):
    ai_score = min(sum(f.points for f in prov) + sum(f.points for f in tells)
                   + sum(f.points for f in lib), AI_SCORE_CAP)
    verdict_fail = bool(prov) or ai_score >= max_ai
    result = {
        "register_version": rules["register_version"],
        "rules_fingerprint": fingerprint(),
        "files_scanned": scanned,
        "ai_score": ai_score,
        "ai_band": band_for(ai_score, rules),
        "pass_threshold": max_ai,
        "verdict": "FAIL" if verdict_fail else "PASS",
        "near_proof": [f.to_dict() for f in prov],
        "tells": [f.to_dict() for f in sorted(tells, key=lambda f: -f.points)],
        "craft_flags": [f.to_dict() for f in craft],
        "library_misuse": [f.to_dict() for f in sorted(lib, key=lambda f: -f.points)],
    }
    if as_json:
        print(json.dumps(result, indent=2))
        return verdict_fail

    print(f"\n=== AI-look scan (register {rules['register_version']},"
          f" fingerprint {result['rules_fingerprint']}) ===")
    print(f"Files scanned: {scanned}")
    print(f"\nAI-look score: {ai_score}/100  ->  {result['ai_band']}")
    if prov:
        print("\nNEAR-PROOF findings (generator plumbing - one of these means"
              " the project was AI-generated):")
        for f in prov:
            print(f"  [{f.rule_id}] {f.name}")
            print(f"      found: {', '.join(f.evidence)}")
            print(f"      do this: {f.fix}")
    if tells:
        print(f"\nAI-look tells found ({len(tells)}):")
        for f in sorted(tells, key=lambda f: -f.points):
            print(f"  [{f.rule_id}] {f.name}  (+{f.points})")
            if f.evidence:
                print(f"      found: {', '.join(str(e) for e in f.evidence)}")
            print(f"      why it matters: {f.explain}")
            print(f"      do this: {f.fix}")
    else:
        print("\nNo AI-look tells found.")
    if lib:
        print(f"\nLibrary misuse ({len(lib)}) - these libraries are fine; this use of them is not:")
        for f in sorted(lib, key=lambda f: -f.points):
            print(f"  [{f.rule_id}] {f.name}  (+{f.points})")
            if f.evidence:
                print(f"      found: {', '.join(str(e) for e in f.evidence)}")
            print(f"      why it matters: {f.explain}")
            print(f"      do this: {f.fix}")
    if craft:
        print(f"\nCraft flags ({len(craft)}) - not AI proof, just problems worth fixing:")
        for f in craft:
            print(f"  [{f.rule_id}] {f.name}")
            print(f"      why it matters: {f.explain}")
            print(f"      do this: {f.fix}")
    print(f"\nVerdict: {result['verdict']}"
          f" (threshold: AI score under {max_ai} and no near-proof findings)")
    if verdict_fail:
        print("Next step: apply the 'do this' lines above, then run the scan again.")
    else:
        print("Next step: present it, with the proof line:"
              f' "AI-look score {ai_score}/100 ({result["ai_band"]}),'
              f' register {rules["register_version"]},'
              f' fingerprint {result["rules_fingerprint"]}."'
              "\n  (Full proof line, all guards: python3 scripts/verify_all.py <files>)")
    return verdict_fail


# --------------------------------------------------------------------------
# Selftest: one deliberately AI-looking page must FAIL, one clean page must PASS.
# --------------------------------------------------------------------------
SLOP_FIXTURE = """
<html><head>
<link href="https://fonts.googleapis.com/css2?family=Inter&family=Space+Grotesk" rel="stylesheet">
</head><body class="bg-gray-900 min-h-screen">
<div class="absolute rounded-full bg-purple-500 blur-3xl opacity-30"></div>
<section class="min-h-screen text-center">
  <span class="uppercase tracking-widest text-xs">✨ AI-POWERED</span>
  <h1 class="text-5xl md:text-6xl font-bold tracking-tight
     bg-clip-text text-transparent bg-gradient-to-r from-purple-500 to-pink-500">
     Elevate your workflow, seamlessly</h1>
  <p class="text-gray-400">In today's fast-paced world, it's not just a tool.</p>
  <button>Get Started</button><button>Learn More</button>
  <p>Trusted by 10,000+ teams · 99.9% uptime</p>
  <div class="bg-white/10 border border-white/20 backdrop-blur rounded-2xl">
    <div class="w-10 h-10 rounded-lg bg-blue-100"><svg>Sparkles</svg></div>
    <svg>Zap</svg><svg>Shield</svg>
  </div>
  <img src="https://i.pravatar.cc/100" alt="John Doe">
  <div id="features"></div><div id="pricing"></div><div id="faq"></div>
  <div class="min-h-screen"></div><div class="min-h-screen"></div><div class="min-h-screen"></div>
  <div class="animate-pulse w-2 h-2 rounded-full bg-green-500"></div>
  <style>.x{animation: marquee 10s linear infinite}</style>
</section></body></html>
"""

CLEAN_FIXTURE = """
<html><head><style>
:root { --ink: #1a2b23; --paper: #f2efe9; --moss: #4a6b52; }
body { font-family: "Newsreader", Georgia, serif; color: var(--ink);
       background: var(--paper); font-size: 17px; line-height: 1.55;
       max-width: 68ch; margin: 0 auto; }
h1 { font-family: "Archivo", sans-serif; font-size: 2.4rem; }
a:focus-visible { outline: 3px solid var(--moss); }
@media (prefers-reduced-motion: no-preference) {
  .note { transition: border-color 180ms ease-out; }
}
</style></head><body>
<h1>Fadl's Ledger</h1>
<p>Track the seventeen invoices your bakery sends each week without
   re-typing a single customer name. Made for Cairo bakeries.</p>
<a href="/pricing-egp">See prices in EGP</a>
</body></html>
"""



# A page that uses the ported libraries in exactly the wrong way.
LIB_MISUSE_FIXTURE = """
<html><head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/animate.css@4/animate.min.css">
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
</head><body>
<section class="animate__animated animate__fadeInUp">one</section>
<section class="animate__animated animate__fadeInUp animate__delay-2s">two</section>
<section class="animate__animated animate__fadeInDown">three</section>
<section class="animate__animated animate__zoomIn">four</section>
<div class="animate__animated animate__pulse animate__infinite">live</div>
<div id="map"></div>
<canvas id="bg"></canvas>
<script>
  const lenis = new Lenis({ duration: 1.2 });
  gsap.to(".blob", { x: 100, repeat: -1, yoyo: true, ease: "elastic.out(1, 0.3)" });
  ScrollTrigger.batch(".card", { onEnter: b => gsap.from(b, { y: 60, opacity: 0 }) });
  const app = new PIXI.Application();
  L.tileLayer("https://tile.example/{z}/{x}/{y}.png").addTo(L.map("map"));
  animate(".a", { opacity: [0, 1], autoplay: onScroll({ container: "#s" }) });
  animate(".b", { y: [40, 0], autoplay: onScroll({ container: "#s" }) });
  animate(".c", { scale: [0.9, 1], autoplay: onScroll({ container: "#s" }) });
  animate(".float", { y: -12, loop: true, alternate: true });
  const { chars } = splitText("h1", { chars: true, accessible: false });
</script>
</body></html>
"""


MOBILE_FIXTURE = """
// lib/ui/theme.dart - shipped as generated
const Color danger = Color(0xFFEF4444);
const Color slate = Color(0xFF64748B);
const Color surface = Color(0xFFF9FAFB);
"""

MOBILE_COMPOSE_FIXTURE = """
// ui/theme/Color.kt - straight out of the Empty Activity template
val Purple80 = Color(0xFFD0BCFF)
val PurpleGrey80 = Color(0xFFCCC2DC)
val Pink80 = Color(0xFFEFB8C8)
val Purple40 = Color(0xFF6650a4)
"""

MOBILE_EXPO_FIXTURE = """
// app/(tabs)/_layout.tsx
export default function TabLayout() {
  return (
    <Tabs screenOptions={{ tabBarActiveTintColor: '#2f95dc' }}>
      <Tabs.Screen name="index" options={{ title: 'Tab One',
        tabBarIcon: () => <IconSymbol name="chevron.left.forwardslash.chevron.right" /> }} />
      <Tabs.Screen name="two" options={{ title: 'Tab Two' }} />
    </Tabs>
  );
}
"""

MOBILE_CLEAN_FIXTURE = """
// lib/ui/theme.dart - a real palette, generated with generate_palette.py
const Color ink = Color(0xFF1B2A20);
const Color canvas = Color(0xFFF4F1E8);
const Color signal = Color(0xFFB4531F);

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});
}
"""

# Transcribed from expo-template-default (published 57.0.23, and unchanged at
# expo/expo@5ad6930). This is the scaffold a bare `npx create-expo-app` produces,
# which is NOT the tabs template MB2 covers - the two share no literals at all.
MOBILE_EXPO_DEFAULT_FIXTURE = """
// src/app/index.tsx
import { HintRow } from '@/components/hint-row';
import { WebBadge } from '@/components/web-badge';
import { BottomTabInset, MaxContentWidth, Spacing } from '@/constants/theme';

export default function Index() {
  return <ThemedText>Edit src/app/index.tsx to edit this screen.</ThemedText>;
}
"""

# The false-positive guard for MB4, kept permanently so the filter cannot be
# quietly loosened later. Every literal in here was considered for MB4 and
# rejected: `unstable-native-tabs` is a real API import a human must write,
# Home/Explore are ordinary tab names, the greys are Radix Colors steps that
# any human using Radix legitimately has, and MaxContentWidth is just a number.
# A human app built on the same API must score 0.
MOBILE_EXPO_HUMAN_FIXTURE = """
// src/components/app-tabs.tsx - hand-built on the same public API
import { NativeTabs } from 'expo-router/unstable-native-tabs';
const palette = { backgroundElement: '#F0F0F3', backgroundSelected: '#E0E1E6',
                  textSecondary: '#60646C' };
export const MaxContentWidth = 800;
export default function AppTabs() {
  return (
    <NativeTabs backgroundColor={palette.backgroundElement}>
      <NativeTabs.Trigger name="index">
        <NativeTabs.Trigger.Label>Home</NativeTabs.Trigger.Label>
      </NativeTabs.Trigger>
      <NativeTabs.Trigger name="explore">
        <NativeTabs.Trigger.Label>Explore</NativeTabs.Trigger.Label>
      </NativeTabs.Trigger>
    </NativeTabs>
  );
}
"""

def selftest():
    rules = load_rules()
    prov1, tells1, craft1, lib1 = scan_texts({"slop.html": SLOP_FIXTURE}, rules)
    score1 = min(sum(f.points for f in tells1), AI_SCORE_CAP)
    prov2, tells2, craft2, lib2 = scan_texts({"clean.html": CLEAN_FIXTURE}, rules)
    score2 = min(sum(f.points for f in tells2), AI_SCORE_CAP)
    ids1 = {f.rule_id for f in tells1}
    expect_in_slop = {"CO2", "CO4", "CO5", "TY5", "LA5", "LA6", "IC1", "IC2",
                      "IC5", "LA11", "CP1", "CP2", "CP3", "LA1", "MO4"}
    missing = expect_in_slop - ids1
    prov3, tells3, craft3, lib3 = scan_texts({"libs.html": LIB_MISUSE_FIXTURE}, rules)
    _, tells4, _, _ = scan_texts({"theme.dart": MOBILE_FIXTURE,
                                  "Color.kt": MOBILE_COMPOSE_FIXTURE,
                                  "_layout.tsx": MOBILE_EXPO_FIXTURE,
                                  "index.tsx": MOBILE_EXPO_DEFAULT_FIXTURE}, rules)
    _, tells5, _, _ = scan_texts({"theme.dart": MOBILE_CLEAN_FIXTURE}, rules)
    _, tells6, _, _ = scan_texts({"app-tabs.tsx": MOBILE_EXPO_HUMAN_FIXTURE}, rules)
    mobile_ids = {f.rule_id for f in tells4}
    missing_mobile = {"MB1", "MB2", "MB3", "MB4"} - mobile_ids
    lib_ids = {f.rule_id for f in lib3}
    expect_lib = {"LB1", "LB2", "LB3", "LB4", "LB5", "LB6", "LB7", "LB8",
                  "LB9", "LB10", "LB11", "LB12"}
    missing_lib = expect_lib - lib_ids

    problems = []
    for ext in (".dart", ".kt"):
        if ext not in SCAN_EXTENSIONS:
            problems.append(f"{ext} files are not scanned, so no mobile rule can ever fire")
    if missing_mobile:
        problems.append(f"mobile fixture missed expected rules: {sorted(missing_mobile)}")
    if tells5:
        problems.append("clean mobile fixture wrongly flagged: "
                        f"{[f.rule_id for f in tells5]}")
    if any(f.rule_id == "MB4" for f in tells6):
        problems.append("MB4 fired on a hand-built app using the same public API; "
                        "the false-positive filter has been loosened")
    if missing_lib:
        problems.append(f"library fixture missed expected rules: {sorted(missing_lib)}")
    if lib2:
        problems.append(f"clean fixture wrongly flagged for library misuse: "
                        f"{[f.rule_id for f in lib2]}")
    if score1 < DEFAULT_MAX_AI:
        problems.append(f"slop fixture scored only {score1}, expected >= {DEFAULT_MAX_AI}")
    if missing:
        problems.append(f"slop fixture missed expected rules: {sorted(missing)}")
    if score2 >= DEFAULT_MAX_AI or prov2:
        problems.append(f"clean fixture scored {score2} (tells: {[f.rule_id for f in tells2]})"
                        " - should pass")
    craft_ids1 = {f.rule_id for f in craft1}
    if "CR1" not in craft_ids1:
        problems.append("slop fixture: low-contrast craft flag (CR1) not raised")
    if any(f.rule_id == "CR2" for f in craft2):
        problems.append("clean fixture wrongly flagged for reduced-motion (it has the query)")
    if problems:
        print("SELFTEST: FAIL")
        for p in problems:
            print("  -", p)
        return 1
    print(f"SELFTEST: PASS (slop page scored {score1}, {len(tells1)} tells,"
          f" {len(craft1)} craft flags; clean page scored {score2};"
          f" library fixture caught {len(lib3)} misuse rules)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Measure how AI-generated a design's code looks.")
    ap.add_argument("paths", nargs="*", help="files or folders to scan")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--max-ai", type=int, default=DEFAULT_MAX_AI,
                    help=f"AI score that fails the scan (default {DEFAULT_MAX_AI})")
    ap.add_argument("--selftest", action="store_true", help="verify the scanner works")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if not args.paths:
        ap.print_help()
        return 3

    rules = load_rules()
    files = gather_files(args.paths)
    if not files:
        print("No scannable files found. I can read: " + ", ".join(sorted(SCAN_EXTENSIONS)))
        return 3
    texts = {}
    for path in files:
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                texts[path] = f.read()
        except OSError as e:
            print(f"warning: cannot read {path}: {e}", file=sys.stderr)
    prov, tells, craft, lib = scan_texts(texts, rules)
    failed = report(prov, tells, craft, lib, rules, args.max_ai,
                    as_json=args.json, scanned=len(texts))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
