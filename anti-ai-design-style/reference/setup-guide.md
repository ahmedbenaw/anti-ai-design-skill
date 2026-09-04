# Setup guide

**TL;DR:** save the skill, and it works. No other setup. The extras below
(scanner on your own computer, warning rules, slash commands) are optional.
Each section says what you need, how long it takes, and what you'll see.

## Before you start

You need:
- [ ] A Claude account (claude.ai, the desktop app, or Claude Code)
- [ ] About 2 minutes (10 if you add the optional extras)

No coding knowledge is needed for the basic setup.

---

## Part 1 — Use the skill in Claude (2 minutes, everyone)

1. **Save the skill.**
   When Claude sends you the `anti-ai-design-style.skill` file, click it,
   then click **Save skill**.
   *You'll see:* the skill appears in your skills list.

2. **Try it.**
   Ask Claude: "Make me a landing page for [your real product]."
   *You'll see:* Claude asks a few plain questions first (that's the design
   brief). Then it builds the page and runs the scanner on it. It ends with
   a proof line like "AI-look score 6/100 (distinct)".

3. **Check something you already have.**
   Attach an HTML file (or paste your page's code) and say:
   "Check this for AI design tells."
   *You'll see:* a short plain-language list of findings, worst first, each
   with a fix.

That's the whole basic setup. Parts 2-4 are optional power-ups.

---

## Part 2 — Run the scanner yourself (optional, 5 minutes)

Works on any computer with Python 3 (Macs have it built in; on Windows,
install it from python.org and choose "Add to PATH" when asked).

1. **Unzip the skill file** somewhere you can find it (a `.skill` file is a
   zip. Rename it to `.zip` if your computer complains).
   *You'll see:* a folder with `scripts`, `reference`, `templates` inside.

2. **Open a terminal** in that folder.
   Mac: right-click the folder → Services → New Terminal at Folder.
   Windows: open the folder, type `cmd` in the address bar, press Enter.

3. **Check the scanner works.** Type:
   `python3 scripts/ai_tell_scan.py --selftest`
   *You'll see:* `SELFTEST: PASS ...`. If you see "python3 is not
   recognized", try `python` instead of `python3`.

4. **Scan your project.** Type:
   `python3 scripts/ai_tell_scan.py path/to/your/project`
   *You'll see:* your AI-look score, each finding with a "do this" line,
   and a PASS or FAIL verdict.

## Part 3 — Warning rules for Claude Code (optional, 3 minutes)

Needs: Claude Code with the **hookify** plugin installed.
These make Claude warn itself the moment it writes an AI-looking pattern.

1. Copy the four files from the skill's `hookify/` folder into your
   project's `.claude/` folder.
2. In each file, replace `<skill-path>` with the real path to the skill
   folder on your computer.
3. That's it. Rules load on the next tool use, no restart needed.
   *You'll see:* when Claude writes something like gradient headline text,
   a warning appears in its context and it corrects itself.

To turn a rule off: open its file and change `enabled: true` to
`enabled: false`.

## Part 4 — Slash commands for Claude Code (optional, 2 minutes)

1. Copy the three files from the skill's `commands/` folder into
   `.claude/commands/` in your project (create the folder if needed).
2. Replace `<skill-path>` in each file with the skill folder's real path.
   *You'll see:* three new commands when you type `/` in Claude Code:
   - `/design-check`: scan and explain in plain words
   - `/design-fix`: fix everything found, prove it with a rescan
   - `/design-brief`: a guided interview that writes your DESIGN.md

## Using other tools? (Lovable, Bolt, v0, Cursor)

You don't need any of the above. Open `templates/prompt-packs.md`, fill in
`templates/design-brief.md`, and copy the block for your tool.

## If something goes wrong

- **"SELFTEST: FAIL"**. The skill files were changed or half-copied.
  Re-unzip a fresh copy. Nothing on your computer is affected.
- **"No scannable files found"**. The scanner reads web files (.html, .css,
  .jsx and similar). Point it at the folder that contains them.
- **A command does nothing in Claude Code**. Check the file is inside
  `.claude/commands/` and ends in `.md`, then restart Claude Code.
- **Stuck?** Ask Claude: "The anti-ai-design-style skill isn't working,
  here's what I see: [paste the message]". Your files are never changed by
  a scan. Scanning only reads.
