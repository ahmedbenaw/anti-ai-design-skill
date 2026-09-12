# anti-ai-design-style installer — shared behaviour spec

Both layers (`install.sh`, `install.ps1`) implement THIS SAME algorithm and
read `installer/manifest.json`. Same inputs → same result. `ahmedbenaw` is
substituted at publish time. The shape is borrowed from refactor-chain's
installer, by the same author; the differences are called out at the end.

## Algorithm (every layer)

1. **Locate the source.** If run from inside a clone (the file
   `anti-ai-design-style/.claude-plugin/plugin.json` exists next to
   `installer/`), use local files. Otherwise download the tarball from
   `manifest.tarball` (curl → wget; PowerShell: `Invoke-WebRequest`) into a
   temp dir and extract. **git is optional.**

2. **Detect the platform.** OS, and the first package manager from
   `manifest.package_managers[os]` found on PATH. Record it for the report.
   Check for `python3` (Windows: `python`). It is the only runtime the hooks
   need and it ships with macOS and most Linux; on Windows, `winget install
   Python.Python.3` is the bootstrap.

3. **Detect installed surfaces.** For each surface in `manifest.surfaces`,
   mark PRESENT if any of its `detect` hits: a `dirs` path exists, an `apps`
   app is installed, a `bins` command is on PATH, a `vscode_ext` extension
   folder exists, or `always_try` is true. `claude-cowork` PRESENT ⇒ covered by
   `claude-code` (`same_as`); never double-install.

4. **Show the plan.** One screen: the detected OS and package manager, then a
   checklist of surfaces that WILL be installed and those skipped (not
   present). Ask to proceed, or proceed automatically with `--yes`. Plain
   words, no jargon, "here is exactly what I will do."

5. **Install per surface by `method`:**
   - **claude-home** (Claude Code / Cowork): copy the skill folder →
     `~/.claude/skills/anti-ai-design-style/` (a clean replace, never a merge,
     so a removed file does not linger); copy `commands/*.md` →
     `~/.claude/commands/` **with `${CLAUDE_PLUGIN_ROOT}` replaced by the
     absolute installed skill path**; register the 2 `manifest.hooks` in
     `~/.claude/settings.json` as `python3 <hook_scripts_at>/<script>`. Back
     up `settings.json` first; idempotently remove any prior entries whose
     command contains `anti-ai-design-style/scripts/` before adding. Refuse to
     write a hook whose path contains a space, and say so.
   - **codex-home** (Codex): copy the skill folder →
     `~/.codex/plugins/anti-ai-design-style/`; merge the 2 hooks into
     `~/.codex/hooks.json` (create if absent; same idempotent rule). Tell the
     user that per-project Codex (`.agents/skills/`) is `install.py --codex`.
   - **npx-skills** (editors): run `manifest.npx_skills_broad` with the
     surface's `agent`. Needs Node/npx; if absent, try to bootstrap via the
     package manager; if that fails, record SKIPPED with the manual one-liner.

6. **Verify each surface** via its `verify` paths. Then, for claude-home, run
   the installed skill's own proof: `python3 <skill>/scripts/verify_all.py
   <skill>/examples/fixed-example.html` must print a line starting `PASS:`.
   A copied file is not a working install; a printed PASS is.

7. **Self-troubleshoot:**
   - python3 missing → bootstrap via package manager; else point at python.org.
   - `settings.json` / `hooks.json` malformed → restore the backup, report.
   - Hook path would contain a space → refuse that hook, warn loudly.
   - Permission denied → print the exact `chmod` hint; never silently sudo.
   - No surfaces detected → say so and list the manual per-surface commands.

8. **Final summary.** What is installed ✓, what was skipped and why, the
   per-project step this installer cannot do (the five hookify rules: run
   `python3 ~/.claude/skills/anti-ai-design-style/scripts/install.py .` inside
   a project), and the ONE next action: "open Claude Code and type
   `/design-check <file>`". Non-zero exit only on a hard failure of a
   requested surface.

## Flags (both layers)

`--yes` (non-interactive), `--only <id,id>`, `--skip <id,id>`, `--dry-run`
(detect + plan, install nothing), `--owner <name>`, `--details`, `--uninstall`
(remove from each surface: delete the skill folder, the three commands, the
hook entries; restore the settings backup on request).

## Tone

Calm, plain-language, ADHD-friendly. One screen per decision. Say what will
happen before doing it. Nothing has to be pre-installed for the shell core:
POSIX sh + curl/wget, or PowerShell + Invoke-WebRequest, are OS defaults.

## Where this differs from refactor-chain's installer, and why

| refactor-chain | this skill | Why |
|---|---|---|
| Runtime is Node; hooks are `.mjs` | Runtime is Python; hooks are `.py` | Every scanner here is dependency-free Python, so the hooks run on the OS's own interpreter with nothing to bootstrap on macOS or Linux |
| 48 skills copied one by one | One skill folder, replaced whole | A merge would keep files a newer version deleted; a clean replace cannot |
| Commands copied verbatim | `${CLAUDE_PLUGIN_ROOT}` substituted | Outside a plugin the variable is unset and the command would call nothing |
| Verify = files exist | Verify = files exist **and** the skill's own proof line prints PASS | This skill's rule: "verified" means a tool printed PASS, never "the files are there" |
| No per-project step | Points at `install.py` for the five hookify rules | Hookify loads rules only from the working folder; a global installer cannot place them |
