Write-Host "Executing update script to process new data..." -fore yellow
py .\update.py

remove-item .\index.html
Write-Host "Encrypting website with default password..." -fore yellow
# STATICRYPT COMMAND REMOVED FROM PUBLIC TEMPLATE
Write-Host "Encryption finished." -fore green

Write-Host "Committing changes to github..." -fore yellow
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
# Committing:
git checkout main
git add .\index.html
git commit -m "Automated update with new data on $timestamp"
git push