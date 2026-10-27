#!/usr/bin/env python3
"""Findings a project's owner has ruled on, reported as accepted.

Some findings are correct and still not to be fixed. A founder's approved
palette can sit close to another brand's colours; a founder's own copy can
use more dashes than this skill likes. Editing those to clear the gate would
overrule the person who owns them. Leaving them failing means the gate fails
forever and people learn to ignore it. Both are worse than writing the
ruling down.

So a project can list accepted findings in

    <project>/.claude/anti-ai-design-style.exceptions.json

and verify_all.py reports them as accepted. The rules:

  * Narrow. An entry names one check, the exact files, and what it accepts:
    a colour code for brand_distance, a phrase from the finding text for
    copy. It never covers a whole check or a whole folder by default.
  * Ruled. An entry with no "ruling" is ignored and reported as invalid.
    An exception nobody decided is just a silenced finding.
  * Visible. Every accepted item comes back to the caller, and the proof
    line prints the count and the rulings. Nothing becomes a silent pass.
  * Fail closed. A file that cannot be read accepts nothing, and the error
    is reported. Entries that matched nothing are reported as unused, so a
    stale exception is seen rather than left lying around.

The file is found by walking up from each checked file, not from the current
folder, because hooks do not always run where the project is.

Format:

    {"version": 1,
     "accept": [
       {"check": "brand_distance", "hex": "#2E86C8" | ["#..", ...],
        "paths": ["design-system/page.html", "docs/*.html"],
        "ruling": "DECISIONS #37 (A)", "why": "..."},
       {"check": "copy", "finding": "Heavy em-dash use",
        "paths": ["design-system/book.html"], "ruling": "...", "why": "..."}]}

Paths are relative to the project folder (the one holding .claude/) and may
use shell-style wildcards.
"""

import copy as _copy
import fnmatch
import json
import os
import sys

FILENAME = os.path.join(".claude", "anti-ai-design-style.exceptions.json")
CHECKS = ("brand_distance", "copy")


def find_root(path):
    """The nearest folder above `path` that holds an exceptions file."""
    d = os.path.dirname(os.path.abspath(path))
    while True:
        if os.path.isfile(os.path.join(d, FILENAME)):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def _as_list(v):
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple)) else [v]


def load(root):
    """Read one project's file. Returns (valid entries, invalid, errors)."""
    path = os.path.join(root, FILENAME)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        entries = data.get("accept", [])
        if not isinstance(entries, list):
            raise ValueError('"accept" must be a list')
    except (OSError, ValueError) as e:
        return [], [], ["{}: {}".format(path, e)]
    valid, invalid = [], []
    for i, e in enumerate(entries):
        problem = None
        if not isinstance(e, dict):
            problem = "not an object"
        elif e.get("check") not in CHECKS:
            problem = "check must be one of {}".format(", ".join(CHECKS))
        elif not str(e.get("ruling") or "").strip():
            problem = "no ruling"
        elif not _as_list(e.get("paths")):
            problem = "no paths"
        elif e["check"] == "brand_distance" and not _as_list(e.get("hex")):
            problem = "no hex"
        elif e["check"] == "copy" and not str(e.get("finding") or "").strip():
            problem = "no finding"
        if problem:
            invalid.append({"file": path, "index": i, "problem": problem})
        else:
            valid.append(dict(e, _index=i, _used=0))
    return valid, invalid, []


def _rel(path, root):
    return os.path.relpath(os.path.abspath(path), root).replace(os.sep, "/")


def _path_matches(entry, rel):
    return any(fnmatch.fnmatchcase(rel, p.replace(os.sep, "/"))
               for p in _as_list(entry.get("paths")))


def apply(results, paths):
    """Mark accepted findings in `results`, in place. Returns what was done.

    `results` is the dict verify_all.gather() builds. Only results["brand"]
    and results["copy"] are touched. The brand cross-check, if any, was
    already compared on the raw verdicts and is left alone.
    """
    roots = {}
    for p in paths:
        r = find_root(p)
        if r and r not in roots:
            roots[r] = load(r)
    out = {"brand": [], "copy": [], "unused": [], "invalid": [],
           "errors": [], "sources": []}
    for r, (valid, invalid, errors) in roots.items():
        out["invalid"] += invalid
        out["errors"] += errors
        out["sources"].append(os.path.join(r, FILENAME))

    def entries_for(path, check):
        r = find_root(path)
        if not r or r not in roots:
            return [], None
        return [e for e in roots[r][0] if e["check"] == check
                and _path_matches(e, _rel(path, r))], r

    brand = results.get("brand")
    if brand and isinstance(brand.get("files"), list):
        total = 0
        for f in brand["files"]:
            entries, _ = entries_for(f.get("file", ""), "brand_distance")
            accepted_here = 0
            for c in f.get("colors", []):
                if c.get("verdict") in ("PASS", "ACCEPTED"):
                    continue
                hexv = str(c.get("hex", "")).upper()
                for e in entries:
                    if hexv in (h.upper() for h in _as_list(e.get("hex"))):
                        c["verdict"] = "ACCEPTED"
                        c["ruling"] = e["ruling"]
                        e["_used"] += 1
                        accepted_here += 1
                        out["brand"].append({"file": f.get("file"), "hex": hexv,
                                             "ruling": e["ruling"]})
                        break
            if accepted_here and isinstance(f.get("violations"), int):
                f["violations"] = max(0, f["violations"] - accepted_here)
            total += f.get("violations", 0) if isinstance(f.get("violations"), int) else 0
        if out["brand"] and isinstance(brand.get("violations"), int):
            brand["violations_before_exceptions"] = brand["violations"]
            brand["violations"] = total
            if total == 0 and brand.get("verdict") == "NON-COMPLIANT":
                brand["verdict_before_exceptions"] = brand["verdict"]
                brand["verdict"] = "COMPLIANT"

    copyr = results.get("copy")
    if isinstance(copyr, dict):
        for path, v in copyr.items():
            if not isinstance(v, dict) or not v.get("findings"):
                continue
            entries, _ = entries_for(path, "copy")
            keep = []
            for finding in v["findings"]:
                text = finding if isinstance(finding, str) else json.dumps(finding)
                hit = next((e for e in entries if e["finding"] in text), None)
                if hit:
                    hit["_used"] += 1
                    out["copy"].append({"file": path, "finding": text,
                                        "ruling": hit["ruling"]})
                else:
                    keep.append(finding)
            if len(keep) != len(v["findings"]):
                v["accepted_findings"] = len(v["findings"]) - len(keep)
                v["findings"] = keep

    for r, (valid, _, _) in roots.items():
        for e in valid:
            if not e["_used"]:
                out["unused"].append({"file": os.path.join(r, FILENAME),
                                      "index": e["_index"], "check": e["check"]})
    return out


def describe(accepted):
    """The proof-line fragment. Empty when nothing was accepted or wrong."""
    if not accepted:
        return ""
    parts = []
    for key, label in (("brand", "brand distance"), ("copy", "copy")):
        if accepted.get(key):
            parts.append("{} {}".format(label, len(accepted[key])))
    rulings = sorted({a["ruling"] for k in ("brand", "copy")
                      for a in accepted.get(k, [])})
    bits = []
    if parts:
        bits.append("accepted by ruling: {} ({})".format(
            ", ".join(parts), "; ".join(rulings)))
    if accepted.get("invalid"):
        bits.append("{} invalid exception(s) ignored".format(len(accepted["invalid"])))
    if accepted.get("errors"):
        bits.append("exceptions file unreadable, nothing accepted")
    return (" | " + " | ".join(bits)) if bits else ""


def selftest(quiet=False):
    import tempfile
    checks = []
    d = tempfile.mkdtemp(prefix="exceptions-selftest-")
    os.makedirs(os.path.join(d, ".claude"))
    page = os.path.join(d, "site", "page.html")
    other = os.path.join(d, "site", "other.html")
    os.makedirs(os.path.dirname(page))
    for p in (page, other):
        open(p, "w").write("<p>x</p>")

    def write(entries):
        with open(os.path.join(d, FILENAME), "w") as f:
            json.dump({"version": 1, "accept": entries}, f)

    def results():
        return {
            "brand": {"verdict": "NON-COMPLIANT", "violations": 2, "files": [
                {"file": page, "violations": 1,
                 "colors": [{"hex": "#2E86C8", "verdict": "FAIL"}]},
                {"file": other, "violations": 1,
                 "colors": [{"hex": "#2E86C8", "verdict": "FAIL"}]}]},
            "copy": {page: {"grade": 4.0, "findings": [
                "Heavy em-dash use (44 dashes, ~13 per 1000 words)",
                "1 sentence(s) over 25 words (e.g. ...)"]}}}

    brand_entry = {"check": "brand_distance", "hex": "#2e86c8",
                   "paths": ["site/page.html"], "ruling": "R1"}
    copy_entry = {"check": "copy", "finding": "Heavy em-dash use",
                  "paths": ["site/*.html"], "ruling": "R2"}

    write([brand_entry, copy_entry])
    r = results()
    a = apply(r, [page, other])
    checks.append(("a listed colour in a listed file is accepted",
                   len(a["brand"]) == 1 and a["brand"][0]["file"] == page))
    checks.append(("the same colour in an unlisted file still fails",
                   r["brand"]["verdict"] == "NON-COMPLIANT" and r["brand"]["violations"] == 1))
    checks.append(("a listed copy finding is accepted, an unlisted one stays",
                   r["copy"][page]["findings"] == ["1 sentence(s) over 25 words (e.g. ...)"]))
    checks.append(("the proof fragment names what was accepted and why",
                   "accepted by ruling: brand distance 1, copy 1 (R1; R2)" in describe(a)))

    write([dict(brand_entry, paths=["site/*.html"]), copy_entry])
    r = results()
    a = apply(r, [page, other])
    checks.append(("when every violation is ruled on, the verdict reads COMPLIANT",
                   r["brand"]["verdict"] == "COMPLIANT"
                   and r["brand"]["verdict_before_exceptions"] == "NON-COMPLIANT"))

    write([dict(brand_entry, ruling="")])
    r = results()
    a = apply(r, [page])
    checks.append(("an entry with no ruling accepts nothing and is reported",
                   not a["brand"] and a["invalid"] and a["invalid"][0]["problem"] == "no ruling"))

    write([dict(brand_entry, hex="#000000")])
    a = apply(results(), [page])
    checks.append(("an entry that matched nothing is reported as unused",
                   len(a["unused"]) == 1))

    with open(os.path.join(d, FILENAME), "w") as f:
        f.write("{ not json")
    r = results()
    a = apply(r, [page])
    checks.append(("an unreadable file accepts nothing and says so",
                   not a["brand"] and a["errors"]
                   and "unreadable" in describe(a)
                   and r["brand"]["verdict"] == "NON-COMPLIANT"))

    loose = os.path.join(tempfile.mkdtemp(prefix="no-exceptions-"), "p.html")
    open(loose, "w").write("x")
    r = results()
    r["brand"]["files"][0]["file"] = loose
    a = apply(r, [loose])
    checks.append(("a project without the file is untouched",
                   not a["brand"] and not a["sources"] and describe(a) == ""))

    if not quiet:
        for label, ok in checks:
            print("  {} {}".format("ok  " if ok else "FAIL", label))
    passed = all(ok for _, ok in checks)
    if not quiet:
        print("SELFTEST: {}".format("PASS" if passed else "FAIL"))
    return 0 if passed else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    files = [a for a in sys.argv[1:] if not a.startswith("-")]
    for f in files:
        root = find_root(f)
        print(f, "->", os.path.join(root, FILENAME) if root else "no exceptions file")
