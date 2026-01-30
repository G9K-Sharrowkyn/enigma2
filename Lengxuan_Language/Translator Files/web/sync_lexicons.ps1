Param(
  [string]$TranslatorFilesDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$outDir = Join-Path $TranslatorFilesDir "out"
$publicDir = Join-Path $PSScriptRoot "public"

Copy-Item -Force (Join-Path $outDir "lexicon_pl2lx.tsv") (Join-Path $publicDir "lexicon_pl2lx.tsv")
Copy-Item -Force (Join-Path $outDir "lexicon_lx2pl.tsv") (Join-Path $publicDir "lexicon_lx2pl.tsv")

Write-Host "OK: synced lexicons to web/public" -ForegroundColor Green

