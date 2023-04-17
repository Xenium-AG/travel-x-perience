# travel-x-perience
## Updates / Änderungen vornehmen
### Voraussetzungen
1. Private Dateien erhalten, die nicht Teil des öffentlichen Repositories sind
2. [Python](https://www.python.org/downloads/) installieren
3. Für Linux / Mac: [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux) installieren

### Einfache Anpassungen an der Karte machen
1. Datei *besuchte-laender.tsv* mit neuen Änderungen anpassen (*Nicht* die Datei ...template.tsv!)
2. Konsole öffnen (in VS Code per *Strg+J*)
3. Kommando `.\encrypt.ps1` ausführen

### Komplexere Änderungen
Die Datei *index-unencrypted.html* (*Nicht* ...template!) beinhaltet den Code und weiteren Text der Website. Hier kann alles weitere beliebig angepasst werden.

Folgende Bereiche werden bei Karten-Updates von *update.py* (aufgerufen durch *encrypt.ps1*) automatisch überschrieben:
- Automatisierte Länderliste (zwischen `// START OF AUTOMATED PARSING LIST` und `// END OF AUTOMATED PARSING LIST`)
- Die Zahl unter `<!--TOTAL COUNT-->`
- Die Zahl unter `<!--NEXT GOAL-->`