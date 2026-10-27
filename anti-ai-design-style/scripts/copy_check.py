#!/usr/bin/env python3
"""copy_check.py - checks writing for AI-sounding copy and hard-to-read text.

Part of the anti-ai-design-style skill. Python 3.8+, standard library only.

What it does, in plain words:
  1. Reading grade - estimates how hard the text is to read
     (Flesch-Kincaid). Target: grade 9 or lower for anything users read.
     That target is our convention, not a standard. GOV.UK's "reading age 9"
     is a different scale - roughly US grade 4 - and the digits matching is a
     coincidence, not a citation. See reference/accessibility.md.
  2. Sentence length - flags sentences over 25 words (GOV.UK's limit).
  3. AI-copy tells - buzzwords, AI cadence phrases, em-dash density,
     fake-proof numbers. These use the same rules.json as the code scanner.

  It works on .md, .txt, and .html files (HTML tags are stripped first).
  Given a stylesheet or a component (.css, .scss, .jsx, .tsx, .js, .ts,
  .vue, .svelte, .astro), it grades only the copy inside it: text a user
  sees or hears. Imports, class names, comments and logic are never prose.
  A page's own ban list is read for readability but never counted as the
  words in use (rules.json copy_tells.banned_markers; register Part 5).

Usage:
  python3 copy_check.py README.md page.html
  python3 copy_check.py docs/ --max-grade 9
  python3 copy_check.py --selftest

Exit codes: 0 = pass, 1 = findings to fix, 3 = usage error.
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# One loader, used by both run() and selftest(). They read the same rule file
# as ai_tell_scan.py, so a copy tell and a code tell can never drift apart.
sys.path.insert(0, HERE)
from ai_tell_scan import load_rules, fingerprint, drop_banned  # noqa: E402
VOWELS = "aeiouy"


def strip_html(text):
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text,
                  flags=re.DOTALL | re.IGNORECASE)
    # A closing block tag ends a thought. Insert a full stop so nav links,
    # table cells and headings are not glued into one giant "sentence".
    text = re.sub(r"</(p|li|h[1-6]|td|th|tr|div|section|article|nav|header|"
                  r"footer|button|a|dt|dd|label|figcaption|summary)>|<br\s*/?>",
                  ". ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"(\.\s*){2,}", ". ", text)   # collapse runs of full stops
    text = re.sub(r"&[a-z]+;", " ", text)
    return text


def strip_markdown(text):
    """Keep only running prose. Code, tables, front-matter and quoted
    examples (in backticks or "double quotes") are not the author's voice,
    so they are dropped before scoring."""
    text = re.sub(r"\A---.*?---", " ", text, flags=re.DOTALL)         # front-matter
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)            # code blocks
    text = re.sub(r"`[^`]+`", " ", text)                               # inline code
    text = re.sub(r"^\s*\|.*$", " ", text, flags=re.MULTILINE)         # table rows
    text = re.sub(r"\"[^\"\n]{3,120}\"", " ", text)                    # quoted examples
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)               # links -> text
    # headings and list items end where the line ends - give them a full
    # stop so they are not glued onto the next paragraph as one sentence
    text = re.sub(r"^(#+\s*.+?)\s*$", r"\1.", text, flags=re.MULTILINE)
    text = re.sub(r"^(\s*(?:[-*]|\d+\.)\s+.*[^.!?:\s])\s*$", r"\1.", text, flags=re.MULTILINE)
    text = re.sub(r"\[ \]", " ", text)                                 # checkboxes
    text = re.sub(r"^[#>\-\*\|\s]+", "", text, flags=re.MULTILINE)     # list/heading marks
    return text


# --- Copy inside code --------------------------------------------------------
# A stylesheet or a component is code with a little copy in it. Graded whole,
# One client's app.css scored reading grade 627 and two components scored 19 and
# 20 on their import lines, and every session that touched one failed the
# stop hook with nothing an edit could fix. So only the copy is pulled out.

STYLE_EXTS = (".css", ".scss", ".sass", ".less")
SCRIPT_EXTS = (".jsx", ".tsx", ".js", ".mjs", ".cjs", ".ts", ".mts", ".cts")
TEMPLATE_EXTS = (".vue", ".svelte", ".astro")
NO_JSX_EXTS = (".ts", ".mts", ".cts")      # `<Foo>x` there is a type cast

# Attributes a user sees or hears. Their values are copy even when short, so
# aria-label="Unlock Pro" is read. Any other attribute counts only when its
# value reads as a sentence, which a class list or an SVG path never does.
VISIBLE_ATTRS = {"alt", "title", "placeholder", "label", "aria-label",
                 "aria-description", "aria-placeholder", "aria-roledescription",
                 "aria-valuetext"}
# Strings passed to these are for developers: logs, test names, module paths.
DEV_CALLS = {"console", "describe", "it", "test", "expect", "require", "import"}
DEV_ERRORS = {"Error", "TypeError", "RangeError"}
# A string in code is copy when most of it is words and one of them is a
# word only sentences have. "flex items-center", "warning" and "M4 12a8 8"
# never contain one; "Your draft was saved" does. "a" and "i" are left out:
# as single letters they are also tag names and SVG commands.
FUNCTION_WORDS = {"an", "the", "and", "or", "but", "to", "of", "in", "on",
                  "at", "for", "with", "from", "by", "as", "is", "are", "was",
                  "be", "it", "its", "this", "that", "we", "you", "your", "our",
                  "us", "my", "not", "no", "can", "will", "if", "all"}
# A string that holds a stylesheet or a piece of markup (a shadow-DOM style
# block, an innerHTML template) is read the way that file type would be.
_CSS_LIKE = re.compile(r"/\*|[\w-]+\s*:\s*[^;{}()\n]+;\s*[\w-]+\s*:"
                       r"|\(\s*[\w-]+\s*:\s*[\w.-]+\s*\)")
_MARKUP_LIKE = re.compile(r"<([A-Za-z][\w-]*)\b[^<>]*>.*?</\1\s*>", re.DOTALL)
# Closing one of these ends a sentence: the list strip_html uses. A capitalised
# component (a <Badge>, a <Card>) is a block of its own and ends one too.
SENTENCE_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th",
                 "tr", "div", "section", "article", "nav", "header", "footer",
                 "button", "a", "dt", "dd", "label", "figcaption", "summary"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
             "link", "meta", "source", "track", "wbr"}
_WORD = re.compile(r"[^\w]*[A-Za-z][A-Za-z'\u2019-]*[^\w]*")
_TAG_NAME = re.compile(r"<([A-Za-z][\w.:-]*)?")
_ATTR_NAME = re.compile(r"[@:#]?[A-Za-z_][\w:.@-]*")
_CLOSE_TAG = re.compile(r"</\s*([A-Za-z][\w.:-]*)?\s*>")
_ESCAPE = re.compile(r"\\(?:u\{([0-9a-fA-F]+)\}|u([0-9a-fA-F]{4})|x([0-9a-fA-F]{2}))")


def _has_letters(s):
    return bool(re.search(r"[A-Za-z]", s))


def _reads_as_sentence(s):
    toks = s.split()
    if len(toks) < 2:
        return False
    words = [t for t in toks if _WORD.fullmatch(t)]
    return (len(words) >= 0.6 * len(toks)
            and any(w.strip(".,;:!?\"'()").lower() in FUNCTION_WORDS for w in words))


def _reads_as_label(s):
    """Short visible text, like a button label. One lower-case token is a
    value ("warning", "elevated"), not copy."""
    return _has_letters(s) and not re.fullmatch(r"[a-z][\w.:-]*", s)


def _dev_call(callee):
    return callee.split(".")[0] in DEV_CALLS or callee in DEV_ERRORS


class _CopyScanner:
    """Walks a component and keeps only what a user would read.

    Three modes, entered by the brackets that start them: code (a string is
    kept only when it reads as a sentence), a tag (attributes a user sees are
    kept), and a tag's children (text is kept). It is not a parser. Anything
    that does not look like a tag stays code, so a comparison or a TypeScript
    generic is never read as markup, and an apostrophe in "It's" or the // in
    a URL never starts a string or a comment, because text is not code.
    """

    def __init__(self, src, expr="{", lenient=False, jsx=True):
        self.s, self.n = src, len(src)
        self.expr = expr          # what opens an expression in text: { or {{
        self.lenient = lenient    # templates may leave a <p> or <li> open
        self.jsx = jsx
        self.out, self.run, self.stack = [], [], []

    def keep(self, text, test):
        text = " ".join(re.sub(r"&#?\w+;", " ", text).split())
        if text and test(text):
            self.out.append(text)

    def flush(self):
        self.keep("".join(self.run), _has_letters)
        self.run = []

    def string(self, i):
        """The string literal at i: (index after it, its text)."""
        s, q = self.s, self.s[i]
        j, text = i + 1, []
        while j < self.n:
            c = s[j]
            if c == "\\":
                esc = _ESCAPE.match(s, j)
                if esc:                                 # \u2014 is a dash, not "u2014"
                    text.append(chr(int(next(g for g in esc.groups() if g), 16)))
                    j = esc.end()
                    continue
                nxt = s[j + 1:j + 2]
                text.append(" " if nxt in "nrt" else nxt)
                j += 2
            elif c == q:
                return j + 1, "".join(text)
            elif q == "`" and s.startswith("${", j):
                text.append(" ")
                j = self.code(j + 2, "}", quiet=True)
            elif c == "\n" and q != "`":
                break                 # not a string after all; resync at the line end
            else:
                text.append(c)
                j += 1
        return j, "".join(text)

    def code(self, i, close=None, quiet=False, visible=False):
        """Scan JavaScript from i up to the bracket `close`; index after it."""
        s = self.s
        while i < self.n:
            c = s[i]
            if c == close:
                return i + 1
            if s.startswith("//", i) and s[i - 1:i] != ":":    # not the // in https://
                j = s.find("\n", i)
                i = self.n if j < 0 else j
            elif s.startswith("/*", i):
                j = s.find("*/", i + 2)
                i = self.n if j < 0 else j + 2
            elif c in "\"'`":
                i, text = self.string(i)
                if quiet:
                    pass
                elif _MARKUP_LIKE.search(text):
                    self.keep(strip_html(text), _has_letters)
                elif _CSS_LIKE.search(text):
                    self.keep(code_copy("embedded.css", text), _has_letters)
                else:
                    self.keep(text, _reads_as_label if visible else _reads_as_sentence)
            elif c in "([{":
                callee = re.search(r"([\w$.]+)\s*$", s[max(0, i - 60):i]) if c == "(" else None
                dev = bool(callee) and _dev_call(callee.group(1))
                i = self.code(i + 1, ")]}"["([{".index(c)], quiet or dev, visible)
            elif c == "<" and self.markup_starts(i):
                i = self.element(i) or i + 1
            else:
                i += 1
        return i

    def markup_starts(self, i):
        """Is the < at i a tag? Not after a name or a bracket, where it is a
        comparison or a generic (`a<b`, `useState<number>`), unless the name
        is a keyword such as `return`."""
        nxt = self.s[i + 1:i + 2]
        if not self.jsx or not (nxt.isalpha() or nxt == ">"):
            return False
        before = self.s[max(0, i - 40):i].rstrip()
        if before and (before[-1].isalnum() or before[-1] in "_$)]"):
            return bool(re.search(r"\b(?:return|yield|default|case|else|do|in|of|await)$", before))
        return True

    def attributes(self, j):
        """Read a tag's attributes: (index after the tag, self-closed), or
        None when this was not a tag after all."""
        s = self.s
        while j < self.n:
            while j < self.n and s[j].isspace():
                j += 1
            if s.startswith("/>", j):
                return j + 2, True
            if s.startswith(">", j):
                return j + 1, False
            if s.startswith("{", j):                    # {...props}
                j = self.code(j + 1, "}", quiet=True)
                continue
            m = _ATTR_NAME.match(s, j)
            if not m or m.group(0) == "extends":       # <T extends X>: a generic
                return None
            attr, j = m.group(0), m.end()
            while j < self.n and s[j].isspace():
                j += 1
            if not s.startswith("=", j):
                continue                                # a bare flag: disabled
            j += 1
            while j < self.n and s[j].isspace():
                j += 1
            visible = re.sub(r"^(?:v-bind)?:", "", attr).lower() in VISIBLE_ATTRS
            test = _reads_as_label if visible else _reads_as_sentence
            q = s[j:j + 1]
            if q and q in "\"'":
                end = s.find(q, j + 1)
                if end < 0:
                    return None
                if attr[0] in ":@#" or attr.startswith("v-"):   # Vue: the value is code
                    self.code(j + 1, q, visible=visible)
                else:
                    self.keep(re.sub(r"\{[^{}]*\}", " ", s[j + 1:end]), test)
                j = end + 1
            elif q == "{":
                j = self.code(j + 1, "}", visible=visible)
            else:
                m = re.compile(r"[^\s>]*").match(s, j)  # unquoted HTML value
                j = m.end()
        return None

    def element(self, i):
        """The element at i and everything inside it: index after it, or
        None when this < turned out not to be a tag. A tag that never closes
        in a script file was a comparison, so what it collected is dropped."""
        m = _TAG_NAME.match(self.s, i)
        name = m.group(1) or ""                         # "" is a fragment, <>
        kept = (len(self.out), len(self.run))
        after = self.attributes(m.end())
        if after is None:
            return None
        j, closed = after
        low = name.lower()
        if closed or low in VOID_TAGS:
            return j
        if low in ("script", "style"):
            end = self.s.lower().find("</" + low, j)
            end = self.n if end < 0 else end
            if low == "script":
                inner = _CopyScanner(self.s[j:end])
                inner.code(0)
                self.out += inner.out
            k = self.s.find(">", end)
            return self.n if k < 0 else k + 1
        self.stack.append(low)
        k = self.children(j, low)
        self.stack.pop()
        if k is None:
            del self.out[kept[0]:]
            del self.run[kept[1]:]
            return None
        if low in SENTENCE_TAGS or name[:1].isupper():
            self.flush()
        else:
            self.run.append(" ")                        # an inline tag still separates words
        return k

    def children(self, j, name):
        """Text inside an element, up to its closing tag."""
        s = self.s
        while j < self.n:
            if s.startswith("</", j):
                m = _CLOSE_TAG.match(s, j)
                if m:
                    closing = (m.group(1) or "").lower()
                    if closing == name:
                        return m.end()
                    if closing in self.stack[:-1]:
                        return j                        # a parent closes: this was left open
                    j = m.end()                         # a stray closing tag
                    continue
            if s.startswith("<!--", j):
                k = s.find("-->", j)
                j = self.n if k < 0 else k + 3
                continue
            if s.startswith("<", j) and (s[j + 1:j + 2].isalpha() or s[j + 1:j + 2] == ">"):
                self.run.append(" ")
                k = self.element(j)
                if k:
                    j = k
                    continue
            if s.startswith(self.expr, j):
                self.run.append(" ")                    # a value filled in at runtime
                j = self.code(j + len(self.expr), "}")
                if self.expr == "{{" and s.startswith("}", j):
                    j += 1
                continue
            self.run.append(s[j])
            j += 1
        return j if self.lenient else None


def code_copy(name, raw):
    """The copy in a stylesheet or component, one fragment per sentence."""
    low = name.lower()
    if low.endswith(STYLE_EXTS):
        # Only `content:` is ever shown to a user. Comments are for developers.
        body = re.sub(r"/\*.*?\*/", " ", raw, flags=re.DOTALL)
        if not low.endswith(".css"):
            body = re.sub(r"(?m)(?:^|\s)//.*$", " ", body)
        frags = [re.sub(r"\\[0-9a-fA-F]{1,6}\s?", " ", m.group(2)).strip()
                 for m in re.finditer(
                     r"(?<![\w-])content\s*:\s*([\"'])((?:\\.|(?!\1).)*)\1", body)]
        return ". ".join(f for f in frags if _has_letters(f))
    if low.endswith(SCRIPT_EXTS):
        sc = _CopyScanner(raw, jsx=not low.endswith(NO_JSX_EXTS))
        sc.code(0)
    else:
        sc = _CopyScanner(raw, expr="{{" if low.endswith(".vue") else "{", lenient=True)
        start = 0
        front = re.match(r"\s*---\r?\n(.*?)\r?\n---", raw, re.DOTALL)
        if low.endswith(".astro") and front:            # Astro's frontmatter is code
            inner = _CopyScanner(front.group(1))
            inner.code(0)
            sc.out += inner.out
            start = front.end()
        sc.children(start, "")
    sc.flush()
    return ". ".join(sc.out)


def copy_of(name, raw):
    """What a reader actually reads in this file, as plain text."""
    low = name.lower()
    if low.endswith((".html", ".htm")):
        return strip_html(raw)
    if low.endswith((".md", ".mdx")):
        return strip_markdown(raw)
    if low.endswith(STYLE_EXTS + SCRIPT_EXTS + TEMPLATE_EXTS):
        return code_copy(low, raw)
    return raw


def count_syllables(word):
    """Rough but consistent syllable estimate - fine for grade scoring."""
    word = word.lower().strip(".,;:!?\"'()")
    if not word:
        return 0
    count, prev_vowel = 0, False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def sentences_of(text):
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in parts if len(s.strip().split()) >= 3]


def fk_grade(text):
    sents = sentences_of(text)
    words = [w for s in sents for w in s.split()]
    if not sents or len(words) < 20:
        return None  # too little prose to score honestly
    syllables = sum(count_syllables(w) for w in words)
    grade = (0.39 * (len(words) / len(sents))
             + 11.8 * (syllables / len(words)) - 15.59)
    return round(grade, 1)


def check_text(name, raw, rules, max_grade):
    # Two views of one file. `text` is everything a reader reads, and the
    # reading checks run on it. `used` drops what the page marks as banned:
    # a brand book's list of words it never uses is still read, so it is
    # still graded, but it is not those words in use, so every check after
    # the reading checks - placeholders, buzzwords, cadence, dashes, fake
    # proof - runs on `used`. Register Part 5.
    text = copy_of(name, raw)
    used_raw = drop_banned(raw, rules["copy_tells"].get("banned_markers"))
    used = copy_of(name, used_raw)

    findings = []

    grade = fk_grade(text)
    if grade is not None and grade > max_grade:
        findings.append((
            f"Reading grade {grade} (target: {max_grade} or lower)",
            "Shorter sentences and everyday words. 'Use' beats 'utilize'."))

    long_sents = [s for s in sentences_of(text) if len(s.split()) > 25]
    if long_sents:
        example = " ".join(long_sents[0].split()[:12]) + "..."
        findings.append((
            f"{len(long_sents)} sentence(s) over 25 words (e.g. \"{example}\")",
            "Split them. One idea per sentence."))

    # Shipped placeholders. A bracketed run that reads like a blank: two or
    # more words in capitals, a field word, something ending in "name", or a
    # field word first. Citations like [1], keys like [Enter], flags like
    # [optional] and one-word badges like [PDF] or [NOTE] do not match.
    ph = re.findall(
        r"\[\s*(?:[A-Z]{2,}(?: [A-Z]{2,})+|(?:NAME|ADDRESS|PHONE|EMAIL|CITY|PRICE|DATE|COMPANY|LOGO|TBD|XXX+)\b[A-Z ]{0,40}|[A-Za-z ]{2,30}\bname|"
        r"(?:Street|Address|Phone|Email|Logo|Your|Landmark|Company|Insert|Placeholder)\b[^\]]{0,40})\s*\]",
        used)
    if ph:
        findings.append((
            f"Shipped placeholder(s): {', '.join(dict.fromkeys(p.strip() for p in ph[:3]))}",
            "Ask for the real name, price or address. If nobody can answer, write a "
            "clearly marked stand-in and say so at the top of your reply."))
    ct = rules["copy_tells"]
    # Headings are labels and cited titles, not the author's own marketing
    # copy. A paper called "Unlocking ..." is a proper noun, not a buzzword.
    # Drop headings from the RAW text, before the markdown marks are stripped.
    markdown = name.lower().endswith((".md", ".mdx"))
    if markdown:
        body_raw = "\n".join(ln for ln in used_raw.splitlines()
                             if not re.match(r"^\s*#", ln))
        body_only = strip_markdown(body_raw).lower()
    else:
        body_only = used.lower()
    buzz = sorted({w for w in ct["transformation_verbs"] if w in body_only})
    if buzz:
        findings.append((
            "Buzzwords: " + ", ".join(buzz[:6]),
            "Swap each for the concrete thing the product does."))
    # Cadence is scored per era, and never on a single hit. One fashionable
    # word is a coincidence; several together is a habit. The 2025 bucket
    # needs three because those words - "enhance", "highlighting" - are
    # ordinary marketing English. Two of them in honest copy is normal, and
    # a rule that flags honest copy gets switched off, taking the rest with it.
    for key, need, era in (("ai_cadence", 2, "structural"),
                           ("ai_cadence_legacy_2023", 2, "2023-24 era"),
                           ("ai_cadence_current_2025", 3, "2025-26 era"),
                           ("ai_cadence_generator_specific", 3, "Grok-flavoured")):
        hits = sorted({w for w in ct.get(key, []) if w in body_only})
        if len(hits) >= need:
            findings.append((
                "AI cadence phrases (%s): %s" % (era, ", ".join(hits[:4])),
                "Rewrite in the words you would say out loud to a customer."))

    words_n = max(len(used.split()), 1)
    # Count dashes in running prose only. A dash used as a separator in a
    # heading ("Part 1 - Setup") or a list label ("- `cmd` - what it does")
    # is typography, not the AI writing cadence the register describes.
    # For HTML and code, count in the visible text: script payloads (Next.js
    # data, translations) and `calc(100% - 2rem)` are not the author's voice.
    source = used_raw if markdown else used
    no_code = re.sub(r"```.*?```", " ", source, flags=re.DOTALL)
    no_code = re.sub(r"\A---.*?---", " ", no_code, flags=re.DOTALL)
    prose_lines = []
    for ln in no_code.splitlines():
        if re.match(r"^\s*(#|\|)", ln):
            continue                      # headings and table rows: typography
        # drop the list marker itself so "  - item" is not counted as a dash
        ln = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", ln)
        prose_lines.append(ln)
    prose = "\n".join(prose_lines)
    dashes = prose.count("—") + len(re.findall(r"\S[ \t]--?[ \t]\S", prose))
    per_1000 = dashes * 1000 / words_n
    if dashes >= 3 and per_1000 > 8:
        findings.append((
            f"Heavy em-dash use ({dashes} dashes, ~{per_1000:.0f} per 1000 words)",
            "Most can become commas, colons, or full stops."))

    for pat in ct["fake_proof_regex"]:
        m = re.search(pat, used)
        if m:
            findings.append((
                f"Unverifiable-looking stat: \"{m.group(0)}\"",
                "Real number you can back up, or cut the claim."))
            break

    return grade, findings


def run(paths, max_grade, as_json=False):
    rules = load_rules()
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, fs in os.walk(p):
                dirs[:] = [d for d in dirs if d not in
                           {"node_modules", ".git", "dist", "build"}]
                files += [os.path.join(root, x) for x in fs
                          if x.endswith((".md", ".mdx", ".txt", ".html", ".htm"))]
        elif os.path.isfile(p):
            files.append(p)
    if not files:
        print("No .md/.txt/.html files found to check.")
        return 3

    any_findings = False
    results = {}
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        grade, findings = check_text(path, raw, rules, max_grade)
        results[path] = {"grade": grade, "findings": [f[0] for f in findings]}
        if not as_json:
            gtxt = f"grade {grade}" if grade is not None else "too short to grade"
            print(f"\n{path}  ({gtxt})")
            if findings:
                any_findings = True
                for what, fix in findings:
                    print(f"  - {what}")
                    print(f"    do this: {fix}")
            else:
                print("  reads clean")
        elif findings:
            any_findings = True
    if as_json:
        print(json.dumps(results, indent=2))
    else:
        print("\nVerdict:", "FIX AND RE-CHECK" if any_findings else "PASS")
    return 1 if any_findings else 0


SLOP_COPY = """Elevate your workflow with our cutting-edge, all-in-one platform.
In today's fast-paced world, it's not just a tool - it's a revolution - a
comprehensive solution that seamlessly integrates every aspect of your
operational infrastructure while simultaneously empowering your organization
to unlock unprecedented productivity gains across all departments and teams.
Trusted by 10,000+ teams. 99.9% uptime."""

CLEAN_COPY = """Fadl's Ledger tracks the invoices your bakery sends each week.
You type a customer's name once. After that, the app fills it in for you.
Most bakeries finish their weekly billing in ten minutes.
It costs 120 EGP a month. The first month is free."""


# Copy in the vocabulary era current as of 2026. These words are ordinary
# marketing English, unlike "delve" or "tapestry", so the scanner must need
# several of them together before it says anything.
CURRENT_ERA_COPY = """
Our platform emphasizing collaboration is designed to enhance how your team
works. By highlighting the metrics that matter and showcasing progress in real
time, we align with the way modern teams operate. Take a deep dive into your
data and see the difference.
"""

# The false-positive guard. Real human product copy that happens to reach for
# two of the same ordinary words. If the scanner flags this, the rule is worse
# than useless: people will turn it off and lose the rest of the checks too.
HONEST_MARKETING_COPY = """
We built this to enhance the weekly shop. It shows what you spent, and it
sorts the list by aisle so you walk the shop once. Two taps to add a receipt.
No account needed for the first month.
"""


# A page that shipped with its blanks still in it. Honest about not inventing
# a clinic, and still not something anyone would upload.
PLACEHOLDER_COPY = """<h1>[ CLINIC NAME ] physiotherapy</h1>
<p>Three therapists in Alexandria. Call [ Phone number ] or visit [ Street and building ].</p>
<p>[ Therapist name ] runs the first visits. Find us at [YOUR ADDRESS] or [INSERT MAP LINK].</p>"""

# Square brackets that are not placeholders: citations, keyboard hints,
# optional flags, and a markdown link. None of these may be flagged.
# A Next.js page carries its data as script payloads. Dashes inside those
# ("Sunday - Thursday", "9 AM - 5 PM", repeated per locale) are not the
# author's prose; only the visible text counts.
REACT_COMMENTS_COPY = """<html><body><h1>Invest<!-- --> <em>fractionally</em> <!-- -->in real estate.</h1>
<p>Start your journey with us in real estate easily and securely.</p>
<small>All rights reserved - Fadl Stationery 2026</small>
<script>self.__next_f.push([1,"{\\"hours\\":\\"Sunday - Thursday\\",\\"time\\":\\"9 AM - 5 PM\\",\\"a\\":\\"x - y\\",\\"b\\":\\"x - y\\",\\"c\\":\\"x - y\\",\\"d\\":\\"x - y\\"}"])</script>
</body></html>"""

BRACKETS_OK_COPY = """<p>See the register [1] and press [Enter] to continue. The --render flag is [optional].</p>
<p><a href="/x">[read more]</a> about our bakery in Bab al-Louq.</p>
<p>[NOTE] Grab the menu as a [PDF]. Shipping by [DHL]. Press [ESC] to close. [BETA] features are marked.</p>"""


# Code is not copy. These are the shapes that failed the stop hook on the
# a client repo on 2026-10-11: a stylesheet graded 627 and two components graded
# 19 and 20 on their import lines. The comments carry an apostrophe and a URL
# on purpose, because each one breaks a naive reader.
STYLESHEET = """/* Reset. Don't touch: see https://example.com/docs/tokens for why the
   scale is fixed and what happens to the whole layout when someone changes it. */
* { box-sizing: border-box; } html { scroll-behavior: smooth; }
body { margin: 0; font: 400 1rem/1.5 var(--lin-font-body); }
.lin-bar { display: flex; justify-content: space-between; width: calc(100% - 2rem); }
.lin-bar > span { padding: 0 var(--lin-space-2) - 1px; }
.lin-step::before { content: "\\2192"; }"""
STYLESHEET_COPY = '.badge-new::after { content: "Unlock seamless savings"; }'

COMPONENT = """import React from "react";
import { Badge } from "../atoms/Badge.jsx";

// Owner is a placeholder when omitted: a real name belongs to a real account,
// never to a component default. See https://example.com/docs/owners - it's long.
const STAGE_CSS = `
  /* The stage keeps its own black so the page never flashes white on load. */
  :host { position: fixed; inset: 0; display: block; }
  @media (hover: hover) { .rail { opacity: 0; } }`;
const INLINE_TAGS = "a abbr b bdi bdo br cite code del dfn em i ins kbd mark q s samp small span";

export function DecisionRecord({ recommendation, ruling, owner, when, items }) {
  const [open, setOpen] = useState<boolean>(false);
  const tone = owner && items.length < 3 ? "info" : "warning";
  return (
    <section className="lin-decision-record grid gap-4" aria-label="Delivery decision record">
      <div><span>Recommendation</span><strong>{recommendation}</strong></div>
      <div><span>Current ruling</span><strong>{ruling}</strong></div>
      <p><strong>Option A</strong><span>Baseline first</span></p>
      <Badge tone={tone} data-action="decide">Final owner · {owner || "\\u2014 the name on your account"}</Badge>
      {when ? <span className={cn("lin-micro", "text-sm")}>{when}</span> : null}
      <svg viewBox="0 0 24 24"><path d="M 4 12 a 8 8 0 1 0 16 0 a 8 8 0 1 0 -16 0" /></svg>
    </section>
  );
}"""
# Words that must never reach the grader from COMPONENT: an import, a path,
# a comment, a class name, an enum value, an SVG path, a style block, a list
# of tag names, and an escape read as letters.
CODE_LEAKS = ("import", "react", "badge.jsx", "placeholder", "example.com",
              "lin-", "gap-4", "warning", "decide", "viewbox", "16 0",
              "position", "flashes", "hover", "abbr", "u2014")

SLOP_COMPONENT = """import { Sparkles } from "lucide-react";

const features = [
  { title: "Built for teams", body: "Unlock seamless collaboration with an all-in-one workspace for your team." },
];
const card = `<div class="card"><p>Supercharge every release with ${name}.</p></div>`;

export default function Hero() {
  return (
    <section className="hero">
      <h1>Elevate your workflow with our cutting-edge platform.</h1>
      <p>It's not just a tool. In today's fast-paced world, it's a revolution.</p>
      <a href="/start" aria-label="Trusted by 10,000+ teams">Get started</a>
      {features.map((f) => <p key={f.title}>{f.body}</p>)}
    </section>
  );
}"""

# A .ts file cannot hold JSX: `<HTMLElement>x` is a type cast, and what
# follows it is code, never text. The sentence string is still copy.
TYPESCRIPT = """const el = <HTMLElement>document.querySelector("main");
const note = "Your draft was saved to this device.";
if (el.childElementCount < 3) { el.dataset.state = "empty"; }"""

# The same rule for the three template formats: script and frontmatter strings
# are read only when they read as sentences, and an import never is.
TEMPLATE_PAGES = {
    "Hero.vue": """<script setup>
import Badge from "./Badge.vue";
const note = "Welcome to the future of seamless invoicing for your bakery.";
</script>
<template>
  <section class="hero">
    <h1>Elevate your workflow with our cutting-edge platform.</h1>
    <p :title="note">{{ note }}</p>
  </section>
</template>
<style scoped>.hero { justify-content: space-between; }</style>""",
    "Hero.svelte": """<script>
  import Badge from "./Badge.svelte";
  const note = "Welcome to the future of seamless invoicing for your bakery.";
</script>
<section class="hero">
  <h1>Elevate your workflow with our cutting-edge platform.</h1>
  {#if note}<p>{note}</p>{/if}
</section>
<style>.hero { justify-content: space-between; }</style>""",
    "Hero.astro": """---
import Layout from "../layouts/Layout.astro";
const note = "Welcome to the future of seamless invoicing for your bakery.";
---
<Layout title="Home">
  <section class="hero">
    <h1>Elevate your workflow with our cutting-edge platform.</h1>
    <p>{note}</p>
  </section>
</Layout>""",
}

# A brand book's own ban list, nested the way a client brand book nests it: a box,
# a label, then the list. Mentioned, not used, so no vocabulary finding. The
# long item stays in on purpose: a ban list is still read, so it is still
# graded for readability, and that finding must survive the exclusion.
BANLIST_PAGE = """<section><h3>Words that never appear</h3>
<p>Every word on this page is one we chose. The list below is closed.</p>
<div class="specbox no"><div class="speclbl">English</div><ul>
<li>Seamless · robust · cutting-edge · revolutionary</li>
<li>Unlock · empower · supercharge · elevate</li>
<li>Delve · tapestry · testament · landscape</li>
<li>Any sentence that runs on and on past twenty-five words because the writer would not stop to think about where one idea ends and the next idea begins.</li>
</ul></div>
<ul data-copy-check="banned"><li>Trusted by 10,000+ teams</li><li>[ COMPANY NAME ]</li></ul>
<p>Write <del>leverage</del> use.</p></section>"""
# The same page, using two of the banned words in its own voice. Those count.
BANLIST_USED_PAGE = BANLIST_PAGE + "<p>Unlock seamless reporting for your team.</p>"


def selftest():
    rules = load_rules()
    problems = []

    def says(findings, word):
        return any(word in f[0].lower() for f in findings)

    css_grade, f_css = check_text("app.css", STYLESHEET, rules, 9)
    if f_css or css_grade is not None:
        problems.append(f"a stylesheet was graded as prose: grade {css_grade}, {[x[0] for x in f_css]}")
    _, f_css2 = check_text("badges.css", STYLESHEET_COPY, rules, 9)
    if not says(f_css2, "unlock"):
        problems.append(f"a buzzword in a CSS content: string was not read: {[x[0] for x in f_css2]}")
    comp_copy = copy_of("DecisionRecord.jsx", COMPONENT).lower()
    leaks = [w for w in CODE_LEAKS if w in comp_copy]
    if leaks:
        problems.append(f"code reached the grader from a component: {leaks} in {comp_copy!r}")
    for want in ("delivery decision record", "recommendation", "the name on your account",
                 "option a baseline first"):
        if want not in comp_copy:
            problems.append(f"component copy {want!r} was not read: {comp_copy!r}")
    _, f_comp = check_text("DecisionRecord.jsx", COMPONENT, rules, 9)
    if f_comp:
        problems.append(f"a clean component was flagged: {[x[0] for x in f_comp]}")
    _, f_slopc = check_text("Hero.jsx", SLOP_COMPONENT, rules, 9)
    for word, where in (("elevate", "JSX text"), ("unlock", "a string in code"),
                        ("supercharge", "markup in a template literal"),
                        ("cadence", "JSX text with an apostrophe"),
                        ("10,000+", "an aria-label")):
        if not says(f_slopc, word):
            problems.append(f"slop in {where} was not caught in a component: {[x[0] for x in f_slopc]}")
    if "sparkles" in copy_of("Hero.jsx", SLOP_COMPONENT).lower():
        problems.append("an import reached the grader")
    ts_copy = copy_of("store.ts", TYPESCRIPT)
    if ts_copy != "Your draft was saved to this device.":
        problems.append(f"a TypeScript cast was read as markup, or its copy was lost: {ts_copy!r}")
    for fname, page in TEMPLATE_PAGES.items():
        _, f_t = check_text(fname, page, rules, 9)
        page_copy = copy_of(fname, page).lower()
        if not (says(f_t, "elevate") and says(f_t, "seamless")):
            problems.append(f"{fname}: template or script copy was not caught: {[x[0] for x in f_t]}")
        if "import" in page_copy or "space-between" in page_copy:
            problems.append(f"{fname}: code reached the grader: {page_copy!r}")

    _, f_ban = check_text("brand.html", BANLIST_PAGE, rules, 9)
    for word in ("buzzword", "cadence", "unverifiable", "placeholder"):
        if says(f_ban, word):
            problems.append(f"a ban list was scored as {word}s in use: {[x[0] for x in f_ban]}")
    if not says(f_ban, "over 25 words"):
        problems.append(f"the exclusion also dropped readability: {[x[0] for x in f_ban]}")
    _, f_used = check_text("brand.html", BANLIST_USED_PAGE, rules, 9)
    if "Buzzwords: seamless, unlock" not in [x[0] for x in f_used]:
        problems.append("words used outside the ban list were not caught, or the list "
                        f"leaked into them: {[x[0] for x in f_used]}")

    _, f5 = check_text("placeholders.html", PLACEHOLDER_COPY, rules, 9)
    _, f6 = check_text("brackets.html", BRACKETS_OK_COPY, rules, 9)
    _, f7 = check_text("react.html", REACT_COMMENTS_COPY, rules, 9)
    g1, f1 = check_text("slop.txt", SLOP_COPY, rules, 9)
    g2, f2 = check_text("clean.txt", CLEAN_COPY, rules, 9)
    _, f3 = check_text("current-era.txt", CURRENT_ERA_COPY, rules, 9)
    _, f4 = check_text("honest.txt", HONEST_MARKETING_COPY, rules, 9)
    if any("dash" in x[0].lower() for x in f7):
        problems.append(f"React text-node comments counted as dashes: {[x[0] for x in f7]}")
    if not any("cadence" in x[0].lower() for x in f3):
        problems.append(
            "current-era AI copy was not caught as cadence: "
            f"{[x[0] for x in f3]}")
    if any("cadence" in x[0].lower() for x in f4):
        problems.append(
            "honest marketing copy wrongly flagged as AI cadence: "
            f"{[x[0] for x in f4]}")
    if not any("placeholder" in x[0].lower() for x in f5):
        problems.append(f"shipped [ CLINIC NAME ] placeholders were not caught: {[x[0] for x in f5]}")
    if any("placeholder" in x[0].lower() for x in f6):
        problems.append(f"ordinary square brackets wrongly flagged as placeholders: {[x[0] for x in f6]}")
    if len(f1) < 3:
        problems.append(f"slop copy raised only {len(f1)} findings: {[x[0] for x in f1]}")
    if f2:
        problems.append(f"clean copy wrongly flagged: {[x[0] for x in f2]}")
    if g2 is not None and g2 > 9:
        problems.append(f"clean copy graded {g2}, expected <= 9")
    if problems:
        print("SELFTEST: FAIL")
        for p in problems:
            print("  -", p)
        return 1
    print(f"SELFTEST: PASS (slop copy: {len(f1)} findings, grade {g1};"
          f" clean copy: 0 findings, grade {g2};"
          f" current-era copy caught; honest copy not flagged;"
          f" stylesheet and component code not graded, their copy still caught"
          f" in {len(TEMPLATE_PAGES) + 2} formats; a ban list read but not counted)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check writing for AI-sounding copy and readability.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--max-grade", type=float, default=9.0)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.paths:
        ap.print_help()
        return 3
    return run(args.paths, args.max_grade, args.json)


if __name__ == "__main__":
    sys.exit(main())
