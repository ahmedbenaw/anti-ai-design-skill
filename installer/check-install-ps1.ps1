<#
.SYNOPSIS
  Checks install.ps1 with PowerShell's own parser.

.DESCRIPTION
  The Windows installer is the one part of this repo that cannot be exercised
  by the Python selftests. This script closes most of that gap. It runs
  anywhere PowerShell runs, including macOS and Linux, so "we have no Windows
  machine" is not a reason to ship it unparsed.

  It reports, in order:
    1. Every parse error PowerShell itself finds. This is the real grammar,
       not an approximation of it, and it is the check that cannot be done
       without PowerShell.
    2. A short set of faults that actually break an installer: CRLF line
       endings, a byte-order mark, and a param() block that is not the first
       executable statement.

  Exit 0 when the file parses and every check passes, 1 otherwise, so it can
  gate a release.

.PARAMETER Path
  The script to check. Defaults to install.ps1 beside this file's parent.

.EXAMPLE
  pwsh -NoProfile -File installer/check-install-ps1.ps1
#>
param(
  [string]$Path = (Join-Path (Split-Path -Parent (Split-Path -Parent $PSCommandPath)) 'install.ps1')
)

if (-not (Test-Path $Path)) {
    Write-Host "not found: $Path" -ForegroundColor Red
    exit 1
}

$tokens = $null
$errors = $null
[void][System.Management.Automation.Language.Parser]::ParseFile(
    $Path, [ref]$tokens, [ref]$errors)

Write-Host ""
Write-Host "file:   $Path"
Write-Host "tokens: $($tokens.Count)"

if ($errors -and $errors.Count -gt 0) {
    Write-Host "PARSE: FAIL - $($errors.Count) error(s)" -ForegroundColor Red
    foreach ($e in $errors) {
        Write-Host ("  line {0}: {1}" -f $e.Extent.StartLineNumber, $e.Message)
    }
    exit 1
}
Write-Host "PARSE: OK - 0 errors" -ForegroundColor Green

$text = Get-Content -Raw $Path

# param() must be the first executable statement, but three things may legally
# precede it: a <# .. #> help block, # line comments, and script attributes
# such as [CmdletBinding()], which belong immediately above param(). An
# earlier version of this check knew about none of them and failed a correct
# file three times running. Strip them, then see what is genuinely first.
$bare = $text -replace '(?s)<#.*?#>', ''
$bare = $bare -replace '(?m)^\s*#.*$', ''
$bare = $bare.TrimStart()
while ($bare -match '^\[[A-Za-z]+\s*\(') {
    $bare = ($bare -replace '^\[[A-Za-z]+\s*\([^)]*\)\s*\]\s*', '').TrimStart()
}

$checks = @(
    @{ n = 'no CRLF line endings'; ok = (-not ($text -match "`r`n")) }
    @{ n = 'no byte-order mark';   ok = (-not $text.StartsWith([char]0xFEFF)) }
    @{ n = 'param block is first'; ok = ($bare -match '^param\s*\(') }
)

Write-Host ""
$failed = 0
foreach ($c in $checks) {
    if ($c.ok) { Write-Host ("  ok   " + $c.n) }
    else { Write-Host ("  FAIL " + $c.n) -ForegroundColor Red; $failed++ }
}

Write-Host ""
if ($failed -gt 0) {
    Write-Host "CHECKS: FAIL - $failed" -ForegroundColor Red
    exit 1
}
Write-Host "CHECKS: PASS" -ForegroundColor Green
exit 0
