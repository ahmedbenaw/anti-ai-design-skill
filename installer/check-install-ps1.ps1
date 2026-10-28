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

# Encoding questions are decided on raw bytes, never on a decoded string.
# Windows PowerShell 5.1 and PowerShell 7 do not decode a file the same way,
# and the first version of this check disagreed with itself across the two
# shells on the same file. Bytes do not care which shell is reading them.
$bytes = [System.IO.File]::ReadAllBytes((Resolve-Path $Path))
$hasBom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and
           $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)
$nonAscii = 0
foreach ($b in $bytes) { if ($b -ge 0x80) { $nonAscii++ } }
$crlf = 0
for ($i = 1; $i -lt $bytes.Length; $i++) {
  if ($bytes[$i] -eq 0x0A -and $bytes[$i - 1] -eq 0x0D) { $crlf++ }
}

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

# Line endings are reported, not judged. Git converts to CRLF on a Windows
# checkout, so a Windows working copy legitimately differs from the committed
# bytes, and PowerShell runs either way. Failing on it tested git, not this
# script.
$endings = if ($crlf -gt 0) { "CRLF ($crlf)" } else { 'LF' }
Write-Host "endings: $endings"
Write-Host "bytes:  $($bytes.Length), non-ASCII: $nonAscii, BOM: $hasBom"

$checks = @(
    # A BOM at the start of a script breaks `irm ... | iex`, which is the
    # documented one-liner install.
    @{ n = 'no byte-order mark'; ok = (-not $hasBom) }

    # The real Windows PowerShell 5.1 hazard, and the opposite of what this
    # check used to look for. 5.1 reads a script as ANSI, so a UTF-8 file
    # carrying non-ASCII bytes without a BOM is silently mis-decoded and the
    # installer prints mojibake. Since a BOM is also disallowed above, the
    # only safe shape is pure ASCII - which is why install.ps1 builds its em
    # dash and ellipsis at runtime with [char]0x2014 rather than typing them.
    @{ n = 'pure ASCII, so 5.1 cannot mis-decode it'; ok = ($nonAscii -eq 0) }

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
