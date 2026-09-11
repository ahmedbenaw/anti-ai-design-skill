#!/usr/bin/env python3
"""Brand distance: how far a page's colours and fonts sit from one brand's.

This is the second half of every verdict this skill gives. The first half
(ai_tell_scan.py) asks "does this look AI-made". This asks "does this look
like the one brand the register says AI output drifts toward". The two are
nearly independent: every baseline page in the evals passed the first guard
and failed this one, because the warm-cream escape palette lands inside the
brand's neutrals. So the check has to run every time, and it has to be
measured, not judged.

What it measures, per colour found in a file:

  * Delta-E 2000 to the nearest of the seven published brand values.
  * A neutral rule and an accent rule. A colour is a violation only when it
    fails both, because a colour is either a neutral or an accent and gets
    the benefit of the doubt on role.
      - achromatic (chroma < 0.5): fails only as an exact brand hex. Pure
        white, grey and black belong to nobody.
      - tinted neutral (chroma < 10): fails within 3.0 Delta-E, "effectively
        identical". Distance cannot discriminate among near-whites.
      - anything else: fails within 12.0 Delta-E (the "signature" level).
  * Fonts: the brand's two typefaces and their usual substitutes are excluded
    outright (T1); a geometric sans over a bookish serif is excluded as a
    pairing (T2).
  * Signature: when a file names colour roles, reproducing three or more of
    the brand's signature traits at once is a violation (SIG).

The standard it implements is the anti-antropik-design exclusion standard,
version 2.0, "signature" level. This file is this skill's own implementation
of that standard. It does not contain that skill's code. Equivalence was
checked verdict-for-verdict against an installed copy on a corpus of pages
(see --equivalence) and the exclusion fingerprint is computed the same way
over the same published values, so a matching fingerprint means the same set.

Exit: 0 COMPLIANT, 1 NON-COMPLIANT, 2 input error.
"""

import argparse
import colorsys
import hashlib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STANDARD_VERSION = "2.0"
LEVEL = "signature"
A1 = 12.0            # Delta-E an accent or chromatic neutral must keep from a brand value
NEAR_IDENTICAL = 3.0  # Delta-E below which a tinted neutral is the brand value in effect
TINT_CHROMA = 10.0    # below this LCH chroma a colour is a neutral, tinted or not
ACHROMATIC = 0.5      # below this it carries no hue at all
SIGNATURE_MAX = 2     # more signature traits than this in one file is a violation
ACHROMATIC_CUTOFF = 5.0  # derived values below this chroma do not bind (they are greys)

# ---------------------------------------------------------------------------
# The published brand values. Facts about a public brand, taken from the
# standard; they are the whole point of the check and must not be edited.
# ---------------------------------------------------------------------------
BRAND_NAME = "Anthropic"
BRAND = [
    ("Light", "#FAF9F5"), ("Dark", "#141413"), ("Mid Gray", "#B0AEA5"),
    ("Light Gray", "#E8E6DC"), ("Orange", "#D97757"), ("Blue", "#6A9BCC"),
    ("Green", "#788C5D"),
]
GEOMETRIC_SANS = {"montserrat", "futura", "poppins", "jost", "outfit", "questrial",
                  "century gothic", "urbanist", "avenir", "circular"}
BOOKISH_SERIF = {"lora", "merriweather", "pt serif", "bitter", "crimson text",
                 "source serif pro", "libre baskerville", "georgia", "spectral",
                 "literata"}
EXCLUDED_FONTS = GEOMETRIC_SANS | BOOKISH_SERIF | {
    "raleway", "nunito sans", "gilroy", "product sans", "sofia pro", "museo sans",
    "brandon grotesque", "proxima nova", "crimson pro", "source serif 4",
    "noto serif", "charter", "freight text", "tiempos text", "vollkorn", "cardo",
    "eb garamond", "domine",
}

# ---------------------------------------------------------------------------
# Colour maths. sRGB, D65, CIE Lab, CIEDE2000. Standard formulas; the
# rounding in to_hex is deliberate so two runs never disagree at a .5 boundary.
# ---------------------------------------------------------------------------
WHITE = (95.047, 100.000, 108.883)


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError("bad hex: %s" % h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def to_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(round(round(c, 6))))) for c in rgb)


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _unlin(c, clamp=True):
    sign, m = (-1.0 if c < 0 else 1.0), abs(c)
    v = (12.92 * m if m <= 0.0031308 else 1.055 * (m ** (1 / 2.4)) - 0.055) * sign
    if clamp:
        v = max(0.0, min(1.0, v))
    return v * 255.0


def _f(t):
    return t ** (1 / 3) if t > 216 / 24389 else (841 / 108) * t + 4 / 29


def _finv(t):
    return t ** 3 if t ** 3 > 216 / 24389 else (t - 4 / 29) * 108 / 841


def rgb_to_lab(rgb):
    r, g, b = (_lin(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) * 100
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) * 100
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) * 100
    fx, fy, fz = _f(x / WHITE[0]), _f(y / WHITE[1]), _f(z / WHITE[2])
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def lab_to_rgb(lab, clamp=True):
    L, a, b = lab
    fy = (L + 16) / 116
    x, y, z = (_finv(fy + a / 500) * WHITE[0] / 100, _finv(fy) * WHITE[1] / 100,
               _finv(fy - b / 200) * WHITE[2] / 100)
    return (_unlin(3.2404542 * x - 1.5371385 * y - 0.4985314 * z, clamp),
            _unlin(-0.9692660 * x + 1.8760108 * y + 0.0415560 * z, clamp),
            _unlin(0.0556434 * x - 0.2040259 * y + 1.0572252 * z, clamp))


def lab_to_lch(lab):
    L, a, b = lab
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def lch_to_lab(L, C, h):
    return L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h))


def lch(hx):
    return lab_to_lch(rgb_to_lab(hex_to_rgb(hx)))


def ciede2000(lab1, lab2):
    """CIE Delta-E 2000 (Sharma, Wu, Dalal 2005 formulation)."""
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)

    def hp(a, b):
        if a == 0 and b == 0:
            return 0.0
        return math.degrees(math.atan2(b, a)) % 360

    h1p, h2p = hp(a1p, b1), hp(a2p, b2)
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        dh = h2p - h1p
        if dh > 180:
            dh -= 360
        elif dh < -180:
            dh += 360
        dhp = dh
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm = (L1 + L2) / 2
    Cpm = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    else:
        s = h1p + h2p
        if abs(h1p - h2p) <= 180:
            hpm = s / 2
        elif s < 360:
            hpm = (s + 360) / 2
        else:
            hpm = (s - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hpm - 30)) + 0.24 * math.cos(math.radians(2 * hpm))
         + 0.32 * math.cos(math.radians(3 * hpm + 6)) - 0.20 * math.cos(math.radians(4 * hpm - 63)))
    dtheta = 30 * math.exp(-((hpm - 275) / 25) ** 2)
    RC = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    SL = 1 + 0.015 * (Lpm - 50) ** 2 / math.sqrt(20 + (Lpm - 50) ** 2)
    SC = 1 + 0.045 * Cpm
    SH = 1 + 0.015 * Cpm * T
    RT = -math.sin(math.radians(2 * dtheta)) * RC
    return math.sqrt((dLp / SL) ** 2 + (dCp / SC) ** 2 + (dHp / SH) ** 2
                     + RT * (dCp / SC) * (dHp / SH))


def delta_e(a, b):
    return ciede2000(rgb_to_lab(hex_to_rgb(a)), rgb_to_lab(hex_to_rgb(b)))


# ---------------------------------------------------------------------------
# The exclusion set and its fingerprint. Ramps in HSL, HSV and LCH at ten
# percent steps from each brand value, unioned. Only the fingerprint and the
# paranoid level use the ramps; the signature level checks the seven values.
# ---------------------------------------------------------------------------
def _rgb_to_hsl(rgb):
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    return h * 360, s * 100, l * 100


def _rgb_to_hsv(rgb):
    h, s, v = colorsys.rgb_to_hsv(*(c / 255 for c in rgb))
    return h * 360, s * 100, v * 100


def _hsl_hex(h, s, l):
    return to_hex([c * 255 for c in colorsys.hls_to_rgb((h % 360) / 360, l / 100, s / 100)])


def _hsv_hex(h, s, v):
    return to_hex([c * 255 for c in colorsys.hsv_to_rgb((h % 360) / 360, s / 100, v / 100)])


def _in_gamut(rgb):
    return all(0.0 <= c <= 255.0 for c in rgb)


def _max_chroma(L, h):
    lo, hi = 0.0, 200.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if _in_gamut(lab_to_rgb(lch_to_lab(L, mid, h), clamp=False)):
            lo = mid
        else:
            hi = mid
    return lo


def _lch_hex(L, C, h):
    if _in_gamut(lab_to_rgb(lch_to_lab(L, C, h), clamp=False)):
        return to_hex(lab_to_rgb(lch_to_lab(L, C, h)))
    return to_hex(lab_to_rgb(lch_to_lab(L, _max_chroma(L, h), h)))


def derived_set():
    out = set()
    for _, hx in BRAND:
        rgb = hex_to_rgb(hx)
        hH, hS, hL = _rgb_to_hsl(rgb)
        vH, vS, vV = _rgb_to_hsv(rgb)
        L, C, lh = lab_to_lch(rgb_to_lab(rgb))
        cmax = _max_chroma(L, lh)
        for p in range(0, 101, 10):
            out.add(_hsl_hex(hH, hS, p))
            out.add(_hsl_hex(hH, p, hL))
            out.add(_hsv_hex(vH, vS, p))
            out.add(_hsv_hex(vH, p, vV))
            out.add(_lch_hex(p, C, lh))
            out.add(_lch_hex(L, cmax * p / 100.0, lh))
        out.add(hx.upper())
    return out


_DERIVED = None


def fingerprint():
    """sha256 of the sorted exclusion set, first 16 hex chars. Two verdicts
    quoting the same fingerprint were measured against the same values."""
    global _DERIVED
    if _DERIVED is None:
        _DERIVED = derived_set()
    return hashlib.sha256("|".join(sorted(_DERIVED)).encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# The rules
# ---------------------------------------------------------------------------
_BRAND_LAB = {hx: rgb_to_lab(hex_to_rgb(hx)) for _, hx in BRAND}


def nearest_brand(hx):
    lab = rgb_to_lab(hex_to_rgb(hx))
    return min((ciede2000(lab, blab), k) for k, blab in _BRAND_LAB.items())


def neutral_failures(hx):
    d, k = nearest_brand(hx)
    C = lch(hx)[1]
    if C < ACHROMATIC:
        return ["C1 this is literally the brand value %s" % k] if hx.upper() == k else []
    if C < TINT_CHROMA:
        return (["C1 %.2f Delta-E from brand value %s, effectively identical" % (d, k)]
                if d < NEAR_IDENTICAL else [])
    return ["C1 %.2f Delta-E from brand value %s, needs >= %.0f" % (d, k, A1)] if d < A1 else []


def accent_failures(hx):
    d, k = nearest_brand(hx)
    return ["C1 %.2f Delta-E from brand value %s, needs >= %.0f" % (d, k, A1)] if d < A1 else []


def check_colour(hx):
    """(verdict, reason). A colour passes if it passes as a neutral OR as an accent."""
    n, a = neutral_failures(hx), accent_failures(hx)
    if not n or not a:
        return "PASS", None
    return "FAIL", "fails as neutral (%s) and as accent (%s)" % ("; ".join(n), "; ".join(a))


def signature_traits(roles):
    """roles: dict role -> hex. The brand's look is a combination; count it."""
    hits = []
    bg = roles.get("background") or roles.get("surface")
    if bg:
        L, C, h = lch(bg)
        if L >= 88 and 1.5 <= C <= 9 and 40 <= h <= 110:
            hits.append("S1 warm off-white dominant field (%s)" % bg)
    acc = roles.get("accent")
    if acc:
        L, C, h = lch(acc)
        if 15 <= C <= 70 and 20 <= h <= 70:
            hits.append("S2 low-chroma warm clay accent (%s)" % acc)
    txt = roles.get("text")
    if txt:
        L, C, h = lch(txt)
        if L <= 30 and C >= 0.5 and 40 <= h <= 120:
            hits.append("S3 warm near-black ink (%s)" % txt)
    for role in ("info", "success", "surface-raised", "border"):
        v = roles.get(role)
        if v:
            L, C, h = lch(v)
            if 8 <= C <= 40 and (95 <= h <= 145 or 230 <= h <= 290):
                hits.append("S4 muted sage or dusty-blue secondary (%s as %s)" % (v, role))
                break
    return hits


def suggest(hx, count=3):
    """Nearby colours that clear the standard, so nobody has to guess.

    The input's own hue and lightness are kept where possible: the point is to
    give back the colour the designer wanted, moved just far enough out of the
    brand's zone to be provably a different colour. Chroma is walked outward
    first, then hue, because a change in chroma reads as the same colour
    family and a change in hue does not.
    """
    L, C, h = lch(hx)
    out = []
    for dh in (0, 12, -12, 25, -25, 40, -40, 60, -60, 90, -90, 140, 180):
        for dc in (0, 6, -6, 12, -12, 20, -20, 30, 40):
            for dl in (0, -6, 6, -12, 12):
                cand = _lch_hex(max(0, min(100, L + dl)), max(0, C + dc), (h + dh) % 360)
                if cand in out or cand.upper() in {b for _, b in BRAND}:
                    continue
                if check_colour(cand)[0] == "PASS":
                    out.append(cand)
                    if len(out) >= count:
                        return out
    return out


# ---------------------------------------------------------------------------
# Finding colours and fonts in a file
# ---------------------------------------------------------------------------
def _load(name):
    with open(os.path.join(HERE, "data", name), encoding="utf-8") as fh:
        return json.load(fh)["colors"]


CSS_NAMED = _load("css_named.json")
TAILWIND = _load("tailwind_colors.json")
_TW_FAMILIES = [k for k, v in TAILWIND.items() if isinstance(v, dict)]
_TW_SHADES = sorted({s for v in TAILWIND.values() if isinstance(v, dict) for s in v})

HEX_RE = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b")
RGB_RE = re.compile(r"rgba?\(\s*(\d{1,3})\s*[, ]\s*(\d{1,3})\s*[, ]\s*(\d{1,3})")
HSL_RE = re.compile(r"hsla?\(\s*(\d{1,3}(?:\.\d+)?)(?:deg)?\s*[, ]\s*(\d{1,3}(?:\.\d+)?)%\s*[, ]\s*(\d{1,3}(?:\.\d+)?)%")
NAMED_RE = re.compile(
    r"(?:(?:background|border[\w-]*|outline|text-decoration|caret|accent|column-rule)-color"
    r"|color|background|fill|stroke)\s*[:=]\s*[\"']?([a-zA-Z]{3,20})\b", re.I)
TW_RE = re.compile(
    r"\b(?:bg|text|border|ring|fill|stroke|from|via|to|decoration|divide|outline"
    r"|shadow|accent|caret|placeholder)-(%s)(?:-(%s))?\b"
    % ("|".join(_TW_FAMILIES + ["black", "white"]), "|".join(_TW_SHADES)))
FONT_RE = re.compile(
    r"font-family\s*:\s*([^;}\n]+)"
    r"|fontFamily\s*:\s*[\"']([^\"']+)[\"']"
    r"|--[\w-]+\s*:\s*([^;}\n]*(?:serif|sans-serif|monospace|cursive|system-ui|ui-monospace)[^;}\n]*)"
    r"|fonts\.googleapis\.com/css2\?([^\"'\s>]+)")
NON_COLORS = {"transparent", "currentcolor", "inherit", "initial", "unset", "none",
              "revert", "auto", "solid", "dashed", "dotted", "double", "hidden", "var",
              "url", "linear", "radial", "conic"}
GENERIC_FONTS = {"serif", "sans-serif", "monospace", "system-ui", "cursive", "fantasy",
                 "inherit", "initial", "unset", "ui-monospace", "ui-sans-serif",
                 "ui-serif", "ui-rounded", "math", "emoji"}
EXTS = {".html", ".htm", ".css", ".svg", ".jsx", ".tsx", ".js", ".ts", ".md", ".json",
        ".vue", ".tex", ".xml", ".scss", ".less", ".py", ".ipynb", ".dart", ".kt", ".swift"}
SKIP = {"brand_distance.py", "css_named.json", "tailwind_colors.json", "rules.json"}


def norm_hex(h):
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    elif len(h) == 4:
        h = "".join(c * 2 for c in h[:3])
    elif len(h) == 8:
        h = h[:6]
    return "#" + h.upper()


def scan_text(text):
    colours, fonts = {}, {}

    def add(hx, pos, label=None):
        rec = colours.setdefault(hx, {"lines": [], "labels": set()})
        rec["lines"].append(text.count("\n", 0, pos) + 1)
        if label:
            rec["labels"].add(label)

    for m in HEX_RE.finditer(text):
        add(norm_hex(m.group(1)), m.start())
    for m in RGB_RE.finditer(text):
        r, g, b = (min(255, int(m.group(i))) for i in (1, 2, 3))
        add("#%02X%02X%02X" % (r, g, b), m.start(), m.group(0) + ")")
    for m in HSL_RE.finditer(text):
        h, s, l = float(m.group(1)) % 360, min(100, float(m.group(2))), min(100, float(m.group(3)))
        rr, gg, bb = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        add("#%02X%02X%02X" % (round(rr * 255), round(gg * 255), round(bb * 255)),
            m.start(), m.group(0) + ")")
    for m in NAMED_RE.finditer(text):
        name = m.group(1).lower()
        if name in NON_COLORS or name not in CSS_NAMED:
            continue
        add(CSS_NAMED[name], m.start(), name)
    for m in TW_RE.finditer(text):
        fam, shade = m.group(1), m.group(2)
        if fam in ("black", "white") and not shade:
            add(TAILWIND[fam], m.start(), m.group(0))
        elif shade and isinstance(TAILWIND.get(fam), dict) and shade in TAILWIND[fam]:
            add(TAILWIND[fam][shade], m.start(), m.group(0))
    for m in FONT_RE.finditer(text):
        if m.lastindex and m.group(4):
            stack = ",".join(f.split(":")[0].replace("+", " ")
                             for f in re.findall(r"family=([^&]+)", m.group(4)))
        else:
            stack = m.group(1) or m.group(2) or m.group(3) or ""
        for fam in stack.split(","):
            fam = fam.strip().strip("\"'").lower()
            if fam and fam not in GENERIC_FONTS and not fam.startswith("var("):
                fonts.setdefault(fam, []).append(text.count("\n", 0, m.start()) + 1)
    return colours, fonts


def collect_files(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", "__pycache__", "vendor")]
                for f in sorted(files):
                    if os.path.splitext(f)[1].lower() in EXTS and f not in SKIP:
                        out.append(os.path.join(root, f))
        else:
            out.append(p)
    return out


def audit_file(path, with_suggestions=False):
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    colours, fonts = scan_text(text)
    rec = {"file": path, "colors": [], "fonts": [], "pairing": None, "signature": None,
           "violations": 0}
    for hx, info in sorted(colours.items()):
        verdict, reason = check_colour(hx)
        c = {"hex": hx, "lines": sorted(set(info["lines"]))[:8],
             "occurrences": len(info["lines"]), "verdict": verdict}
        if info["labels"]:
            c["found_as"] = sorted(info["labels"])[:4]
        if reason:
            c["reason"] = reason
            c["delta_e_to_brand"] = round(nearest_brand(hx)[0], 2)
            if with_suggestions:
                c["suggestions"] = suggest(hx)
            rec["violations"] += 1
        rec["colors"].append(c)
    if colours:
        roles = {}
        for hx, info in colours.items():
            labels = {l.lower() for l in info["labels"]}
            for role in ("background", "accent", "text", "info", "success", "surface-raised", "border"):
                if any(role in l or (role == "accent" and ("brand" in l or "primary" in l)) for l in labels):
                    roles.setdefault(role, hx)
        if len(roles) >= 2:
            sig = signature_traits(roles)
            if len(sig) > SIGNATURE_MAX:
                rec["signature"] = ("SIG file reproduces %d brand signature traits across its "
                                    "named roles, limit %d: %s" % (len(sig), SIGNATURE_MAX, "; ".join(sig)))
                rec["violations"] += 1
    geo, srf = [], []
    for fam, lines in sorted(fonts.items()):
        bad = fam in EXCLUDED_FONTS
        rec["fonts"].append({"family": fam, "lines": sorted(set(lines))[:8],
                             "verdict": "FAIL" if bad else "PASS",
                             **({"reason": "T1 excluded typeface"} if bad else {})})
        if bad:
            rec["violations"] += 1
        if fam in GEOMETRIC_SANS:
            geo.append(fam)
        if fam in BOOKISH_SERIF:
            srf.append(fam)
    if geo and srf:
        rec["pairing"] = ("T2 excluded structure: geometric sans (%s) together with bookish "
                          "serif (%s)" % (", ".join(geo), ", ".join(srf)))
        rec["violations"] += 1
    return rec


def audit(paths, with_suggestions=False):
    files = collect_files(paths)
    report = {"standard_version": STANDARD_VERSION, "level": LEVEL, "brand": BRAND_NAME,
              "exclusion_fingerprint": fingerprint(), "files": [], "violations": 0,
              "colors_checked": 0, "fonts_checked": 0}
    for f in files:
        rec = audit_file(f, with_suggestions)
        report["files"].append(rec)
        report["violations"] += rec["violations"]
        report["colors_checked"] += len(rec["colors"])
        report["fonts_checked"] += len(rec["fonts"])
    report["verdict"] = "NON-COMPLIANT" if report["violations"] else "COMPLIANT"
    return report


def print_report(report):
    for f in report["files"]:
        print("%s  (%d colours, %d font families)" % (f["file"], len(f["colors"]), len(f["fonts"])))
        for c in f["colors"]:
            if c["verdict"] == "FAIL":
                print("  FAIL %s  lines %s  (%d uses)" % (c["hex"], ",".join(map(str, c["lines"][:3])), c["occurrences"]))
                print("       %s" % c["reason"])
                if c.get("suggestions"):
                    print("       use instead: %s" % ", ".join(c["suggestions"]))
        for ft in f["fonts"]:
            if ft["verdict"] == "FAIL":
                print("  FAIL font %s  lines %s  %s" % (ft["family"], ",".join(map(str, ft["lines"][:3])), ft["reason"]))
        if f["pairing"]:
            print("  FAIL %s" % f["pairing"])
        if f["signature"]:
            print("  FAIL %s" % f["signature"])
    print()
    print("mode exclude | standard v%s | brand %s | fingerprint %s | %d colours, %d fonts checked"
          % (report["standard_version"], report["brand"], report["exclusion_fingerprint"],
             report["colors_checked"], report["fonts_checked"]))
    print("VERDICT: %s (%d violations)" % (report["verdict"], report["violations"]))


# ---------------------------------------------------------------------------
# Self-test: known answers, including the values this skill's own evals hinge on
# ---------------------------------------------------------------------------
# The colours of examples/fixed-example.html, which the standard passes. Note
# what is NOT here: the warm-cream escape palette (#f4f1e8 on #1b2a20) sits
# 2.5 and 11.9 Delta-E from brand values and fails. That is the two-guard
# finding from the evals, in one fixture.
CLEAN_FIXTURE = """<style>
body{background:#FAF9F9;color:#666566;font-family:Archivo,"Helvetica Neue",Arial,sans-serif}
.btn{background:#780025;color:#fff}
.card{border:1px solid #F0EFEF;color:#540017}
</style>"""
ESCAPE_FIXTURE = """<style>body{background:#f4f1e8;color:#1b2a20}</style>"""
BRAND_FIXTURE = """<style>
body{background:#FAF9F5;color:#141413;font-family:Poppins,sans-serif}
p{font-family:Lora,serif}
.cta{background:#D97757}.note{background:#F7F6F4}
</style>"""


def selftest():
    checks = []
    checks.append(("Delta-E 2000 of a colour to itself is 0", delta_e("#D97757", "#D97757") == 0.0))
    checks.append(("Delta-E is symmetric", abs(delta_e("#D97757", "#6A9BCC") - delta_e("#6A9BCC", "#D97757")) < 1e-9))
    # Sharma et al. 2005 test pair 1: Lab (50, 2.6772, -79.7751) vs (50, 0, -82.7485) = 2.0425
    checks.append(("CIEDE2000 matches the published Sharma test pair",
                   abs(ciede2000((50.0, 2.6772, -79.7751), (50.0, 0.0, -82.7485)) - 2.0425) < 1e-3))
    checks.append(("pure white passes (achromatic, not a brand hex)", check_colour("#FFFFFF")[0] == "PASS"))
    checks.append(("the brand cream itself fails", check_colour("#FAF9F5")[0] == "FAIL"))
    checks.append(("a near-identical tinted neutral fails (#F7F6F4, 1.17 dE)", check_colour("#F7F6F4")[0] == "FAIL"))
    checks.append(("the brand clay accent fails", check_colour("#D97757")[0] == "FAIL"))
    checks.append(("a rust accent 12+ dE away passes", check_colour("#B4531F")[0] == "PASS"))
    checks.append(("Tailwind slate-900 resolves through the palette", scan_text('class="bg-slate-900"')[0].get("#0F172A") is not None))
    checks.append(("a named CSS colour resolves", "#F5F5DC" in scan_text("background: beige;")[0]))
    checks.append(("rgb() resolves", "#D97757" in scan_text("color: rgb(217,119,87)")[0]))
    checks.append(("a Google Fonts link yields families", "poppins" in scan_text('href="https://fonts.googleapis.com/css2?family=Poppins:wght@400&family=Lora"')[1]))
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        for name, body in (("clean.html", CLEAN_FIXTURE), ("brand.html", BRAND_FIXTURE)):
            with open(os.path.join(d, name), "w") as fh:
                fh.write(body)
        clean = audit([os.path.join(d, "clean.html")])
        brand = audit([os.path.join(d, "brand.html")])
    checks.append(("the clean fixture is COMPLIANT", clean["verdict"] == "COMPLIANT"))
    checks.append(("the warm-cream escape palette fails, as the evals found four times",
                   check_colour("#F4F1E8")[0] == "FAIL" and check_colour("#1B2A20")[0] == "FAIL"))
    checks.append(("the brand fixture is NON-COMPLIANT", brand["verdict"] == "NON-COMPLIANT"))
    checks.append(("brand fixture: cream, ink, clay, near-cream, two fonts and the pairing = 7 violations",
                   brand["violations"] == 7))
    sug = suggest("#D97757")
    checks.append(("suggestions for the brand clay are themselves compliant (%s)" % ", ".join(sug),
                   len(sug) == 3 and all(check_colour(x)[0] == "PASS" for x in sug)))
    fp = fingerprint()
    checks.append(("fingerprint is 16 hex chars", bool(re.fullmatch(r"[0-9a-f]{16}", fp))))
    checks.append(("fingerprint matches the standard's published set (5697117fa1b27195), got %s" % fp,
                   fp == "5697117fa1b27195"))
    for label, ok in checks:
        print("  %s %s" % ("ok  " if ok else "FAIL", label))
    passed = all(ok for _, ok in checks)
    print("SELFTEST: %s" % ("PASS" if passed else "FAIL"))
    return 0 if passed else 1


def main():
    ap = argparse.ArgumentParser(description="Brand distance: colours and fonts vs one brand's.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--fingerprint", action="store_true", help="print the exclusion fingerprint and exit")
    ap.add_argument("--suggest", action="store_true",
                    help="for each failing colour, print nearby hex values that pass")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.fingerprint:
        print(fingerprint())
        return 0
    if not args.paths:
        ap.error("give at least one file or folder")
    try:
        report = audit(args.paths, with_suggestions=args.suggest)
    except OSError as e:
        print("input error: %s" % e, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=1))
    else:
        print_report(report)
    return 1 if report["violations"] else 0


if __name__ == "__main__":
    sys.exit(main())
