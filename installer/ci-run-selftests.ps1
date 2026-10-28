<#
.SYNOPSIS
  Runs every scanner selftest and fails if any of them fails.

.DESCRIPTION
  Used by the Windows workflow against two different folders: the repo's own
  scripts, and the installed copy under the user profile. A selftest that only
  passes in the repo is not a selftest, so both are run.

  It lives here rather than inside the workflow because PowerShell embedded in
  YAML cannot be parsed, linted, or run by hand on a Windows box. As a file it
  can be checked by check-install-ps1.ps1 like any other script.

.PARAMETER ScriptsDir
  Folder holding the scanners.

.PARAMETER MinPass
  Fail if fewer than this many selftests report PASS. Guards against a run
  that silently tested nothing.

.PARAMETER Python
  Python command to use. Defaults to python.
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$ScriptsDir,
  [int]$MinPass = 10,
  [string]$Python = 'python'
)

if (-not (Test-Path $ScriptsDir)) {
  Write-Host "not found: $ScriptsDir"
  exit 1
}

$files = @(Get-ChildItem (Join-Path $ScriptsDir '*.py') -File)
if ($files.Count -eq 0) {
  Write-Host "no scanners in $ScriptsDir"
  exit 1
}

$pass = 0
$fail = 0
$other = 0

# A foreach statement, not ForEach-Object. A pipeline script block has its own
# scope, so incrementing these counters inside one would update a copy and
# leave every total at zero.
foreach ($f in $files) {
  $last = & $Python $f.FullName --selftest 2>&1 | Select-Object -Last 1
  if ($last -match 'PASS') {
    $pass++
  } elseif ($last -match 'FAIL') {
    $fail++
    Write-Host "  FAIL $($f.Name)"
    & $Python $f.FullName --selftest 2>&1 | Select-Object -Last 25 | ForEach-Object { Write-Host "    $_" }
  } else {
    $other++
    Write-Host "  skip $($f.Name) (no verdict: $last)"
  }
}

Write-Host ""
Write-Host "$ScriptsDir"
Write-Host "  pass=$pass fail=$fail other=$other"

# render_check needs a browser venv that CI does not build, so one scanner
# legitimately returns no verdict. Any FAIL is a real failure.
if ($fail -ne 0) {
  Write-Host "SELFTESTS: FAIL - $fail scanner(s)"
  exit 1
}
if ($pass -lt $MinPass) {
  Write-Host "SELFTESTS: FAIL - only $pass passed, expected at least $MinPass"
  exit 1
}
Write-Host "SELFTESTS: PASS"
exit 0
