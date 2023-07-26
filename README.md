# travel-x-perience
## Updates / Änderungen vornehmen
### Voraussetzungen / Setup
1. Folgendes installieren
	- [Python](https://www.python.org/downloads/)
	- Für Linux / Mac: [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux)
	- [npm (incl. node.js)](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) oder nur [node.js](https://nodejs.org/en/)
	- [VS Code](https://code.visualstudio.com) (empfohlen) oder stattdessen nur [git](https://git-scm.com/downloads) bzw. [git für Windows](https://gitforwindows.org)
1. Private Dateien erhalten, die nicht Teil des öffentlichen Repositories sind, verfügbar unter [diesem OneDrive-Ordner](https://xeniumagmuenchen.sharepoint.com/:f:/s/X-Reiseclub/EhQIhy2b-KVJn2BYUei-cEgBawiYyfM5FT76KCZxKuceJg?e=mXq8FA)
1. Einen eigenen Xenium-[Github-Account erstellen](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjJj_a6hq2AAxWqcfEDHWTKBr4QFnoECA8QAQ&url=https%3A%2F%2Fgithub.com%2Fjoin&usg=AOvVaw0H9TK-nu7JfXaoNeNMgJEk&opi=89978449) dann den [OneDrive-Ordner](https://xeniumagmuenchen.sharepoint.com/:f:/s/X-Reiseclub/EhQIhy2b-KVJn2BYUei-cEgBawiYyfM5FT76KCZxKuceJg?e=mXq8FA) mit [diesem Repository](https://github.com/Xenium-AG/travel-x-perience/) synchronisieren
1. Konsole öffnen (in VS Code per *Strg+J*)
1. Kommando `npm i` ausführen

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