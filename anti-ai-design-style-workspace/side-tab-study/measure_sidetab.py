#!/usr/bin/env python3
"""Count Tailwind side-tab accents. Two tiers, both reported.

Why two tiers. The documented definition needs a non-neutral border colour.
In shadcn-style generated code the colour is often a semantic token
(`border-l-primary`) or arrives through a variable
(`className={`border-l-4 ${stat.borderColor}`}`), so it cannot be resolved
from text at all. A strict measure therefore has poor recall on exactly the
corpus that matters, and a loose measure cannot tell a coloured accent from a
grey one.

  strict - a resolvable non-neutral colour on the element
  loose  - border-[lr]-(2|4|8) present, with the radius interaction

Neither is "the" answer. The control group decides which, if either,
discriminates. Reporting one alone would hide the trade-off.
"""
import os, re, sys, json

# Any quoted or backticked run of text is a class-string candidate. This beats
# parsing class attributes, which misses cn(...) helpers and template literals.
STRINGS = re.compile(r'"([^"\n]{0,400})"|\'([^\'\n]{0,400})\'|`([^`\n]{0,400})`')
SIDE = re.compile(r'\bborder-([lr])-(2|4|8)\b')
ROUNDED = re.compile(r'\brounded(-[a-z0-9]+)?\b')
FULL_BORDER = re.compile(r'\bborder(-(\d))?\b(?![-\w])')
OTHER_SIDE = re.compile(r'\bborder-([tbxy])-(\d)\b')
# Palette hue form, e.g. border-purple-500 / border-l-blue-600
HUE = re.compile(r'\bborder-(?:[lrtbxy]-)?([a-z]+)-(\d{2,3})\b')
# Semantic token form, e.g. border-l-primary / border-destructive
TOKEN = re.compile(r'\bborder-(?:[lrtbxy]-)?([a-z]+)(?:/\d+)?\b(?!-)')
NEUTRAL_HUES = {"gray", "grey", "slate", "zinc", "neutral", "stone"}
NEUTRAL_TOKENS = {"border", "input", "muted", "background", "white", "black",
                  "transparent", "current", "inherit", "foreground", "card",
                  "popover", "secondary"}
CHROMATIC_TOKENS = {"primary", "destructive", "accent", "success", "warning",
                    "danger", "info", "ring"}
INTERP = re.compile(r'\$\{[^}]*\}')
EXTS = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".js", ".ts"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", "vendor", "__pycache__"}
SAFE_TAGS = {"blockquote", "nav", "input", "textarea", "select", "pre", "code",
             "th", "td", "tr", "li", "hr"}
TAG_BEFORE = re.compile(r"<\s*([A-Za-z][A-Za-z0-9]*)[^<>]{0,600}$")


def geometry_ok(cls):
    m = SIDE.search(cls)
    if not m:
        return False, 0
    side_w = int(m.group(2))
    base = 0
    fb = FULL_BORDER.search(cls)
    if fb:
        base = int(fb.group(2)) if fb.group(2) else 1
    others = [base] * 3 + [int(o.group(2)) for o in OTHER_SIDE.finditer(cls)]
    max_other = max(others)
    if not (side_w >= 2 and (max_other <= 1 or side_w >= max_other * 2)):
        return False, side_w
    if not ROUNDED.search(cls) and side_w < 4:
        return False, side_w
    return True, side_w


def colour_state(cls):
    """'chromatic' | 'neutral' | 'unresolved'"""
    hues = [h for h in HUE.findall(cls)]
    if any(h[0] not in NEUTRAL_HUES for h in hues):
        return "chromatic"
    toks = set(TOKEN.findall(cls))
    if toks & CHROMATIC_TOKENS:
        return "chromatic"
    if INTERP.search(cls):
        return "unresolved"
    if hues or (toks & NEUTRAL_TOKENS):
        return "neutral"
    return "unresolved"


def scan_file(path):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return {"strict": 0, "loose": 0, "unresolved": 0, "any_border": 0, "ex": []}
    strict = loose = unresolved = any_border = 0
    ex = []
    for m in STRINGS.finditer(text):
        cls = m.group(1) or m.group(2) or m.group(3) or ""
        if "border" not in cls:
            continue
        any_border += 1
        tag = TAG_BEFORE.search(text, max(0, m.start() - 600), m.start())
        if tag and tag.group(1).lower() in SAFE_TAGS:
            continue
        ok, w = geometry_ok(cls)
        if not ok:
            continue
        loose += 1
        state = colour_state(cls)
        if state == "chromatic":
            strict += 1
            if len(ex) < 2:
                ex.append(cls.strip()[:70])
        elif state == "unresolved":
            unresolved += 1
            if len(ex) < 2:
                ex.append("(colour unresolved) " + cls.strip()[:60])
    return {"strict": strict, "loose": loose, "unresolved": unresolved,
            "any_border": any_border, "ex": ex}


def scan_repo(root):
    tot = {"strict": 0, "loose": 0, "unresolved": 0, "files_loose": 0,
           "files_any_border": 0, "examples": []}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if os.path.splitext(f)[1].lower() not in EXTS:
                continue
            r = scan_file(os.path.join(dp, f))
            for k in ("strict", "loose", "unresolved"):
                tot[k] += r[k]
            if r["any_border"]:
                tot["files_any_border"] += 1
            if r["loose"]:
                tot["files_loose"] += 1
            for e in r["ex"]:
                if len(tot["examples"]) < 3:
                    tot["examples"].append(e)
    return tot


if __name__ == "__main__":
    out = {}
    for p in sys.argv[1:]:
        name = os.path.basename(p.rstrip("/"))
        if os.path.isdir(p):
            out[name] = scan_repo(p)
        else:
            r = scan_file(p)
            out[name] = {"strict": r["strict"], "loose": r["loose"],
                         "unresolved": r["unresolved"],
                         "files_loose": 1 if r["loose"] else 0,
                         "files_any_border": 1 if r["any_border"] else 0,
                         "examples": r["ex"]}
    print(json.dumps(out, indent=2))
