# anti-ai-design-style installer — shared behaviour spec

Both layers (`install.sh`, `install.ps1`) implement THIS SAME algorithm and
read `installer/manifest.json`. Same inputs → same result. `ahmedbenaw` is
substituted at publish time. The shape is borrowed from refactor-chain's
installer, by the same author; the differences are called out at the end.

## The rule that overrides everything else

**Install this skill and nothing else.** No Node, no npm packages, no system
package-manager calls, no third-party installer. Every path written belongs
to this skill, and every one is listed before it is written.

This rule was added on 2026-09-12 after a live test. The installer had an
editor step that ran `npx -y skills@latest`. That step downloaded a
third-party CLI. It created an npm cache and a lock file naming other tools.
It installed the skill into the shared `~/.agents/skills` folder. Then it
printed "cursor — installed (agent: cursor)", and nothing Cursor-specific had
been written.

Two faults in one step. It installed software nobody asked for. And it
reported a per-editor success it had not achieved. Editors are now a printed
command the user runs knowingly.

## Algorithm (every layer)

1. **Locate the source.** If run from inside a clone (the file
   `anti-ai-design-style/.claude-plugin/plugin.json` exists next to
   `installer/`), use local files. Otherwise download the tarball from
   `manifest.tarball` (curl → wget; PowerShell: `Invoke-WebRequest`) into a
   temp dir and extract. **git is optional.**

2. **Detect the platform and the runtime.** OS, and `python3` (Windows:
   `python`, or the `py` launcher) at 3.8 or newer. Python is the only
   runtime the hooks need. It ships with macOS and most Linux. **Never
   install it.** If it is missing, say so and print the one command that
   fixes it. Install the files anyway. Skip the hooks, with a line saying to
   re-run once Python is there.

3. **Detect installed surfaces.** Two, and only two. `claude-code` is
   always tried. `codex` is PRESENT when `~/.codex` exists. `claude-cowork`
   shares `~/.claude` with `claude-code` (`same_as`); never double-install.

4. **Show the plan.** One screen: the detected OS and Python, then a
   checklist of surfaces that WILL be installed and those skipped (not
   present). Ask to proceed, or proceed automatically with `--yes`. Plain
   words, no jargon, "here is exactly what I will do."

5. **Install per surface by `method`:**
   - **claude-home** (Claude Code / Cowork): copy the skill folder →
     `~/.claude/skills/anti-ai-design-style/`. A clean replace, never a
     merge, so a file the new version deleted cannot linger. Copy
     `commands/*.md` → `~/.claude/commands/` **with `${CLAUDE_PLUGIN_ROOT}`
     replaced by the absolute installed skill path**. Register the 2
     `manifest.hooks` in `~/.claude/settings.json` as
     `python3 <hook_scripts_at>/<script>`. Back up `settings.json` first.
     Idempotently remove any prior entries whose command contains
     `anti-ai-design-style/scripts/` before adding. Refuse to write a hook
     whose path contains a space, and say so.
   - **codex-home** (Codex): copy the skill folder →
     `~/.agents/skills/anti-ai-design-style/`. That is the same convention
     this skill's own `scripts/install.py --codex` writes for one project.
     Append the "Design checks" section to `~/.codex/AGENTS.md` when that
     file exists and does not already mention the skill. **No hooks**: Codex
     hook wiring cannot be verified from here, so it is neither written nor
     claimed. Tell the user the per-project command.
   - **Editors** (Cursor, VS Code, the rest): not installed. Print the one
     `npx skills` command at the end as advice, never execute it. See the
     rule at the top of this file for why.

6. **Verify each surface** via its `verify` paths. Then, for claude-home, run
   the installed skill's own proof: `python3 <skill>/scripts/verify_all.py
   <skill>/examples/fixed-example.html` must print a line starting `PASS:`.
   A copied file is not a working install; a printed PASS is.

7. **Self-troubleshoot:**
   - python3 missing → print the one install command; never run it.
   - `settings.json` malformed → restore the backup, report.
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

| Flag | What it does |
|---|---|
| `--yes` | Non-interactive; skip the proceed prompt |
| `--dry-run` | Detect and plan only. Writes nothing |
| `--only <id,id>` | Act on these surfaces only |
| `--skip <id,id>` | Leave these surfaces alone |
| `--owner <name>` | Override the GitHub owner |
| `--details` | Print the source path and the surfaces not found |
| `--uninstall` | Remove the skill folder, the three commands and the hook entries |

Surface ids: `claude-code`, `codex`.

When piping the script into `sh`, flags come after `sh -s --`. For example:
`… | sh -s -- --dry-run`.

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
| Installs editors via `npx skills`, bootstraps Node | Installs neither; prints the editor command as advice | Measured: that step downloads a third-party CLI and npm packages, then reports a per-editor success it did not achieve |
| Bootstraps a missing runtime with the package manager | Prints the command instead | Installing software nobody asked for is not installing this skill |
