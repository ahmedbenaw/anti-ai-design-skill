#!/usr/bin/env python3
"""Load a page in a real browser and measure the craft you cannot see in source.

What this does NOT do, and will never do: guess whether a design was made by
an AI. As of 2026-09-05 no published classifier detects AI-designed interfaces
from rendered output. The nearest things are a different task - detectors for
diffusion-synthesised images score below 80% and a browser render has no
synthesis artefacts at all, and the one 100%-accurate 2025 result classifies
the page's prose, not its pixels. So this measures craft against WCAG 2.2,
where the numbers are normative and the verdict is not a matter of taste.

Why bother, if it does not detect AI? Because source-reading misses what the
browser computes. A colour written as a variable, inherited, then overridden
is 4.5:1 in the stylesheet and 2.1:1 on screen. This measures the screen.

Needs Playwright. It is optional on purpose: verify_all.py reports
"render: SKIPPED" when it is missing rather than failing, because most of this
skill works without a browser.

  python3 -m venv .venv && .venv/bin/pip install playwright
  .venv/bin/playwright install chromium
  .venv/bin/python scripts/render_check.py page.html
"""

import argparse
import json
import os
import sys

# Every check below cites the criterion it enforces, at its real level. Two
# of these are AAA and are reported as advice, not as failures, because
# calling an AAA item a violation is the kind of error that gets a whole
# report dismissed.
CRITERIA = {
    "contrast_text": ("1.4.3", "AA", "Text contrast at least 4.5:1 (3:1 for large text)"),
    "contrast_ui": ("1.4.11", "AA", "UI component and graphics contrast at least 3:1"),
    "target_size": ("2.5.8", "AA", "Pointer targets at least 24x24 CSS px"),
    "target_size_enhanced": ("2.5.5", "AAA", "Pointer targets at least 44x44 CSS px"),
    "focus_visible": ("2.4.7", "AA", "Keyboard focus is always visible"),
    "reflow": ("1.4.10", "AA", "Usable at 320x256 CSS px without two-way scrolling"),
    "reduced_motion": ("2.3.3", "AAA", "Animation from interactions can be disabled"),
}

# Measured in the page. Kept as one script so there is a single place where
# "what the browser computed" is defined.
PAGE_SCRIPT = r"""
() => {
  const px = v => parseFloat(v) || 0;

  // sRGB relative luminance, per WCAG 2.x definition.
  const lum = ([r, g, b]) => {
    const f = c => { c /= 255; return c <= 0.03928 ? c / 12.92
                                                   : Math.pow((c + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const parse = s => {
    const m = (s || '').match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(x => parseFloat(x));
    return { rgb: [p[0], p[1], p[2]], a: p.length > 3 ? p[3] : 1 };
  };
  // Walk up for the first opaque background. Transparent backgrounds are the
  // usual reason a naive contrast check reports a false pass.
  const bgOf = el => {
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const c = parse(getComputedStyle(n).backgroundColor);
      if (c && c.a >= 0.95) return c.rgb;
    }
    return [255, 255, 255];
  };
  const ratio = (a, b) => {
    const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m);
    return (x + 0.05) / (y + 0.05);
  };

  const visible = el => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden' || px(s.opacity) === 0)
      return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };

  const out = { text: [], targets: [], focus: [], animated: [] };

  // How much author CSS actually made it into the page. This is what tells
  // us whether a blocked stylesheet mattered: a page with its own inline
  // styles survives losing a webfont link, whereas a page whose entire
  // design is a CDN <script> renders as bare HTML and cannot be measured.
  let rules = 0;
  for (const sheet of Array.from(document.styleSheets)) {
    try { rules += sheet.cssRules.length; } catch (e) { /* opaque sheet */ }
  }
  out.author_style_rules = rules;

  // --- text contrast (1.4.3)
  for (const el of document.querySelectorAll('body *')) {
    if (!visible(el)) continue;
    const own = Array.from(el.childNodes)
      .filter(n => n.nodeType === 3 && n.textContent.trim().length > 1)
      .map(n => n.textContent.trim()).join(' ');
    if (!own) continue;
    const s = getComputedStyle(el);
    const fg = parse(s.color);
    if (!fg) continue;
    const size = px(s.fontSize);
    const weight = parseInt(s.fontWeight, 10) || 400;
    // "Large text" is >=24px, or >=18.66px when bold.
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const r = ratio(fg.rgb, bgOf(el));
    out.text.push({ tag: el.tagName.toLowerCase(), size, weight, large,
                    ratio: Math.round(r * 100) / 100,
                    need: large ? 3 : 4.5,
                    sample: own.slice(0, 60) });
  }

  // --- target size (2.5.8 AA / 2.5.5 AAA)
  const clickable = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [onclick]';
  for (const el of document.querySelectorAll(clickable)) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    out.targets.push({ tag: el.tagName.toLowerCase(),
                       w: Math.round(r.width), h: Math.round(r.height),
                       label: (el.innerText || el.value || el.getAttribute('aria-label') || '').trim().slice(0, 40) });
  }

  // --- focus removed without replacement (2.4.7)
  for (const el of document.querySelectorAll(clickable)) {
    if (!visible(el)) continue;
    el.focus({ preventScroll: true });
    const s = getComputedStyle(el);
    const noOutline = s.outlineStyle === 'none' || px(s.outlineWidth) === 0;
    const noRing = (s.boxShadow === 'none' || !s.boxShadow);
    if (noOutline && noRing) {
      out.focus.push({ tag: el.tagName.toLowerCase(),
                       label: (el.innerText || '').trim().slice(0, 40) });
    }
  }
  if (document.activeElement && document.activeElement.blur)
    document.activeElement.blur();

  // --- anything still moving (2.3.3 / 2.2.2)
  for (const el of document.querySelectorAll('body *')) {
    if (!visible(el)) continue;
    const s = getComputedStyle(el);
    const dur = px(s.animationDuration) + px(s.transitionDuration);
    if (s.animationName !== 'none' && dur > 0) {
      out.animated.push({ tag: el.tagName.toLowerCase(),
                          name: s.animationName,
                          iteration: s.animationIterationCount });
    }
  }
  return out;
}
"""


def measure(path, width=1280, height=800, reduced_motion=None, screenshot=None,
            allow_network=False):
    """Render the page and read what the browser computed.

    Third-party requests are blocked by default. Two reasons, and the second
    matters more than the first. It makes the measurement deterministic - the
    same page gives the same numbers whether or not a CDN is up, and the check
    still runs offline. And it stops the tool hanging: a stylesheet link in
    <head> blocks parsing until the request resolves, and a request that is
    dropped rather than refused never resolves at all. Pages generated by AI
    tools are full of CDN font and script tags, so this is the normal case,
    not the edge case.

    The cost is honest and worth stating: webfonts do not load, so text falls
    back and glyph widths differ slightly. Contrast and focus are unaffected.
    Target sizes can shift by a pixel or two. Pass allow_network=True to
    measure with the real assets when you have a network and want exact
    metrics.
    """
    from playwright.sync_api import sync_playwright
    url = path if "://" in path else "file://" + os.path.abspath(path)
    blocked = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": width, "height": height},
            reduced_motion=reduced_motion)
        page = ctx.new_page()
        if not allow_network:
            def gate(route, request):
                if request.url.startswith(("file://", "data:", "blob:")):
                    route.continue_()
                else:
                    blocked.append({"url": request.url,
                                    "type": request.resource_type})
                    route.abort()
            page.route("**/*", gate)
        # domcontentloaded, not load. AI-generated pages are full of CDN font
        # and script tags, and "load" waits for every one of them. On a slow
        # or offline network that hangs for the full timeout and the check
        # never runs - which would make this tool useless on exactly the
        # pages it exists to measure.
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=4000)
        except Exception:
            pass          # slow third-party asset; measure what rendered
        page.wait_for_timeout(300)
        data = page.evaluate(PAGE_SCRIPT)
        if screenshot:
            page.screenshot(path=screenshot, full_page=True)
        browser.close()
    data["blocked_requests"] = blocked
    # A blocked image or avatar changes nothing we measure. A blocked
    # stylesheet or script can be the entire design: a page whose styling
    # comes from a CDN renders as unstyled HTML, and every number below is
    # then measured on something the user will never see. That has to
    # invalidate the run, not quietly produce confident findings.
    data["styles_incomplete"] = any(
        b["type"] in ("stylesheet", "script", "font") for b in blocked)
    return data


def findings_for(desktop, touch, motion_off):
    """Turn measurements into findings, each tied to a criterion at its level."""
    out = []

    bad = [t for t in desktop["text"] if t["ratio"] < t["need"]]
    if bad:
        worst = sorted(bad, key=lambda t: t["ratio"])[:5]
        out.append({
            "id": "RC1", "criterion": CRITERIA["contrast_text"], "level": "AA",
            "count": len(bad),
            "detail": ["{} {:.2f}:1 (needs {}) - \"{}\"".format(
                t["tag"], t["ratio"], t["need"], t["sample"]) for t in worst],
            "fix": "Darken the text or lighten what sits behind it. The "
                   "browser computed these, so a value in your stylesheet is "
                   "being inherited or overridden."})

    small = [t for t in touch["targets"] if t["w"] < 24 or t["h"] < 24]
    if small:
        out.append({
            "id": "RC2", "criterion": CRITERIA["target_size"], "level": "AA",
            "count": len(small),
            "detail": ["{} {}x{}px - \"{}\"".format(
                t["tag"], t["w"], t["h"], t["label"]) for t in small[:5]],
            "fix": "Give it at least 24x24 CSS px, or leave a 24px gap around "
                   "it. Padding counts; the visible box does not have to grow."})

    under44 = [t for t in touch["targets"] if t["w"] < 44 or t["h"] < 44]
    if under44:
        out.append({
            "id": "RC3", "criterion": CRITERIA["target_size_enhanced"],
            "level": "AAA (advice, not a failure)",
            "count": len(under44),
            "detail": ["{} {}x{}px - \"{}\"".format(
                t["tag"], t["w"], t["h"], t["label"]) for t in under44[:5]],
            "fix": "Apple asks for 44pt and Material for 48dp on touch. This "
                   "is above what WCAG requires at AA, so treat it as a "
                   "quality bar rather than a violation."})

    if desktop["focus"]:
        out.append({
            "id": "RC4", "criterion": CRITERIA["focus_visible"], "level": "AA",
            "count": len(desktop["focus"]),
            "detail": ["{} - \"{}\"".format(f["tag"], f["label"])
                       for f in desktop["focus"][:5]],
            "fix": "Something removed the focus ring without replacing it. Add "
                   "a visible :focus-visible style. Keyboard users cannot see "
                   "where they are without it."})

    still_moving = motion_off["animated"] if motion_off else []
    if still_moving:
        out.append({
            "id": "RC5", "criterion": CRITERIA["reduced_motion"],
            "level": "AAA (advice, not a failure)",
            "count": len(still_moving),
            "detail": ["{} runs \"{}\"".format(a["tag"], a["name"])
                       for a in still_moving[:5]],
            "fix": "These keep animating with prefers-reduced-motion: reduce "
                   "set. Wrap them in @media (prefers-reduced-motion: "
                   "no-preference), or stop them in a reduce block."})
    return out


def report(path, args):
    net = getattr(args, "allow_network", False)
    desktop = measure(path, 1280, 800, screenshot=args.screenshot,
                      allow_network=net)
    touch = measure(path, 390, 844, allow_network=net)
    motion_off = measure(path, 1280, 800, reduced_motion="reduce",
                         allow_network=net)
    found = findings_for(desktop, touch, motion_off)

    # Fonts alone shift glyph widths a little. A blocked stylesheet or script
    # can mean nothing was styled at all, so those two invalidate the run.
    hard_blocked = [b for b in desktop.get("blocked_requests", [])
                    if b["type"] in ("stylesheet", "script")]
    # Judge by effect, not by URL. Losing a webfont stylesheet from a page
    # that carries its own CSS shifts glyph widths and nothing else. Losing
    # the CDN script that IS the design leaves bare HTML. The difference
    # shows up in how many author style rules ended up applied, which is a
    # property of the render rather than a guess about the hostname.
    STYLED_ENOUGH = 5
    applied = desktop.get("author_style_rules", 0)
    inconclusive = bool(hard_blocked) and applied < STYLED_ENOUGH

    fails = [f for f in found if f["level"] == "AA"]
    result = {
        "file": path,
        "measured": {"text_nodes": len(desktop["text"]),
                     "targets": len(touch["targets"]),
                     "animated_after_reduce": len(motion_off["animated"]),
                     "blocked_requests": desktop.get("blocked_requests", []),
                     "author_style_rules": desktop.get("author_style_rules", 0)},
        "findings": found,
        "aa_failures": len(fails),
        "inconclusive": inconclusive,
        "blocked_styling": [b["url"] for b in hard_blocked],
        "verdict": ("INCONCLUSIVE" if inconclusive
                    else "PASS" if not fails else "FAIL"),
        "note": "Craft only. This does not detect whether a design was "
                "AI-generated, and no published tool does.",
    }
    if args.screenshot:
        result["screenshot"] = args.screenshot
    return result


def print_text(res):
    print("=== Rendered craft check: {} ===".format(res["file"]))
    m = res["measured"]
    print("measured {} text nodes, {} tap targets, in a real browser".format(
        m["text_nodes"], m["targets"]))
    if m.get("blocked_requests"):
        print("blocked {} third-party request(s) so the result is repeatable; "
              "{} author style rules still applied.".format(
                  len(m["blocked_requests"]), m.get("author_style_rules", 0)))
    if res.get("blocked_styling") and not res.get("inconclusive"):
        print("Webfonts or extras did not load, so glyph widths differ a "
              "little. Contrast and\nfocus are unaffected. Use --allow-network "
              "for exact text metrics.")
    if res.get("inconclusive"):
        print("\nCANNOT MEASURE THIS PAGE OFFLINE.")
        print("Its styling comes from a server this run did not contact:")
        for u in res["blocked_styling"][:4]:
            print("   -", u)
        print("Without it the page renders as unstyled HTML, so anything "
              "measured\nbelow describes a page nobody will ever see. Re-run "
              "with --allow-network\non a working connection, or inline the "
              "styles first.")
    if not res["findings"]:
        print("No findings. Contrast, target size, focus and reduced motion "
              "all measured clean.")
    for f in res["findings"]:
        num, level, name = f["criterion"]
        print("\n[{}] {}  (WCAG {} {}) x{}".format(
            f["id"], name, num, f["level"], f["count"]))
        for d in f["detail"]:
            print("   -", d)
        print("   do this:", f["fix"])
    print("\n" + res["note"])
    if res["verdict"] == "INCONCLUSIVE":
        print("Verdict: INCONCLUSIVE - the page did not render as designed.")
    else:
        print("Verdict: {} ({} AA failures)".format(res["verdict"],
                                                    res["aa_failures"]))


def selftest():
    """Known-answer test: a deliberately broken page must produce findings,
    and a careful one must produce none. Written as files so the check runs
    against a real browser render rather than a mocked one."""
    import tempfile
    bad = """<!doctype html><html><head><style>
      body{background:#fff;font-family:system-ui}
      p{color:#cfcfcf}
      button{outline:none;border:none;width:16px;height:16px;padding:0}
      @keyframes spin{to{transform:rotate(360deg)}}
      .spin{animation:spin 2s linear infinite;width:20px;height:20px}
    </style></head><body>
      <p>This grey text does not have enough contrast to be read.</p>
      <button>x</button><div class="spin"></div></body></html>"""
    good = """<!doctype html><html><head><style>
      body{background:#fff;color:#1a1a1a;font-family:system-ui;font-size:16px}
      button{min-width:48px;min-height:48px;background:#1a1a1a;color:#fff;border:0}
      button:focus-visible{outline:3px solid #1a1a1a;outline-offset:2px}
      @media (prefers-reduced-motion: no-preference){
        @keyframes fade{from{opacity:0}to{opacity:1}}
        .fade{animation:fade .3s ease both}
      }
    </style></head><body>
      <p class="fade">Body text at a readable contrast.</p>
      <button>Save invoice</button></body></html>"""
    # A page whose entire design lives on a CDN. Offline it renders as bare
    # HTML, and the honest answer is "I cannot measure this", not a verdict.
    cdn_only = """<!doctype html><html><head>
      <link rel="stylesheet" href="https://cdn.example.invalid/all.css">
      </head><body><p>Text</p><button>Go</button></body></html>"""
    checks = []
    d = tempfile.mkdtemp(prefix="render-selftest-")
    try:
        p = os.path.join(d, "cdn.html")
        open(p, "w").write(cdn_only)
        res = report(p, argparse.Namespace(screenshot=None))
        checks.append(("a CDN-styled page offline is INCONCLUSIVE, not a verdict",
                       res["verdict"] == "INCONCLUSIVE"))
        for name, html in (("bad", bad), ("good", good)):
            p = os.path.join(d, name + ".html")
            open(p, "w").write(html)
            res = report(p, argparse.Namespace(screenshot=None))
            ids = {f["id"] for f in res["findings"]}
            if name == "bad":
                checks.append(("low contrast is caught", "RC1" in ids))
                checks.append(("tiny tap target is caught", "RC2" in ids))
                checks.append(("removed focus ring is caught", "RC4" in ids))
                checks.append(("motion ignoring reduce is caught", "RC5" in ids))
                checks.append(("broken page fails", res["verdict"] == "FAIL"))
            else:
                checks.append(("careful page has no AA failure",
                               res["aa_failures"] == 0))
                checks.append(("careful page passes", res["verdict"] == "PASS"))
                checks.append(("reduced-motion done right is not flagged",
                               "RC5" not in ids))
    finally:
        pass
    for label, ok in checks:
        print("  {} {}".format("ok  " if ok else "FAIL", label))
    passed = all(ok for _, ok in checks)
    print("SELFTEST: {}".format("PASS" if passed else "FAIL"))
    return 0 if passed else 1


def main():
    ap = argparse.ArgumentParser(
        description="Measure rendered craft (contrast, target size, focus, "
                    "reduced motion) in a real browser. Does not detect AI.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--screenshot", help="save a full-page PNG here")
    ap.add_argument("--allow-network", action="store_true",
                    help="let the page load CDN fonts and scripts. Slower, "
                         "and the result then depends on those servers")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    try:
        import playwright  # noqa: F401
    except ImportError:
        sys.stderr.write(
            "Playwright is not installed, so the rendered check cannot run.\n"
            "It is optional. Everything else in this skill works without it.\n"
            "To add it:\n"
            "  python3 -m venv .venv\n"
            "  .venv/bin/pip install playwright\n"
            "  .venv/bin/playwright install chromium\n"
            "Then run this script with .venv/bin/python.\n")
        return 2

    if args.selftest:
        return selftest()
    if not args.paths:
        ap.error("give me at least one file to check")

    worst = 0
    for path in args.paths:
        res = report(path, args)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print_text(res)
        worst = max(worst, 0 if res["verdict"] == "PASS" else 1)
    return worst


if __name__ == "__main__":
    sys.exit(main())
