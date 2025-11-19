# SurviveP - Minecraft Survival Server Pack basierend auf Leaves

![Minecraft Version](https://img.shields.io/badge/Minecraft-1.21.8-blue)
![Lizenz](https://img.shields.io/github/license/Maicarons/SurviveP)

## 🌐 Sprachnavigation

[:us: English](README_en.md) | [:cn: Chinese](README.md) | [:jp: Japanese](README_ja.md) | [:ru: Russian](README_ru.md) | [:fr: French](README_fr.md) | [:de: German](README_de.md) | [:es: Spanish](README_es.md) | [:kr: Korean](README_ko.md)

## 🎮 Einführung

SurviveP ist ein funktionsreiches Minecraft-Survival-Serverpaket, das auf dem [Leaves](https://github.com/LeavesMC/Leaves)-Kern basiert. Es integriert viele nützliche Plugins und bietet ein vollständiges Survival-Gaming-Erlebnis, einschließlich Home-Systeme, Wirtschaftssysteme, Territoriumsschutz, Teleportationssysteme und Berufssysteme.

SurviveP ist ein Ableger von [SurviveX](https://github.com/KiteMC/SurviveX) und zielt darauf ab, ein Serverpaket zu erstellen, das selbst Anfänger mit einem Klick einfach bereitstellen können.

## 📋 Umgebungsanforderungen

- 🎯 **Kernversion**: Leaves 1.21.8
- ☕ **Laufzeitumgebung**: Java 21+

## 🚀 Schnellstart

### One-Click-Serverplattform:

Nach dem Hochladen des Pakets wählen Sie die Datei [leaves.jar](file:///workspaces/SurviveP/leaves.jar) als Startkern aus.

### Linux/MacOS:
```bash
cd shell
./start_auto.sh # Ruft automatisch die Systemkonfiguration ab und wählt geeignete Parameter zur Ausführung.
# oder ./start.sh wenn Sie die Konfiguration bei jedem Mal unverändert lassen möchten, ändern Sie bitte start.sh.
```
### Windows:
```powershell
cd shell
.\start.cmd
```

## 🔧 Plugin-Ökosystem

Siehe [Plugin-Liste](plugin.md) für Plugins und Vorsichtsmaßnahmen.

## ⭐ Funktionen

- [x] Startskripte für Windows/Linux/MacOS  
- [x] GUI-Konfigurationsänderung
- [ ] Vorgebaute Multi-Szenario-Karten  

## Client

Spieler sollten den Minecraft Java Edition 1.21.8-Client verwenden, um dem Server beizutreten. Optimierungs- und Informationsanzeige-Mods können angemessen installiert werden, während Hilfs- und Cheat-Mods vom Server erkannt und gesperrt werden.

## 🔧 Konfigurationseditor

Das Projekt bietet ein grafisches Konfigurationstool, um Administratoren die Änderung der Servereinstellungen zu erleichtern:

### Einfacher Konfigurationseditor
Die im Stammverzeichnis befindliche Datei `simple_leaves_editor.py` bietet schnelle Änderungsfunktionen für wichtige Konfigurationselemente und eignet sich für Anfänger-Administratoren.

### Vollständiger Konfigurationseditor
`edit_leaves_config.py` ist ein voll funktionsfähiger Konfigurationseditor (in Entwicklung), der eine umfassende Änderung aller Konfigurationsdateien des Leaves-Servers unterstützt.

### Verwendung
```bash
# Einfachen Konfigurationseditor ausführen
python3 simple_leaves_editor.py

# Vollständigen Konfigurationseditor ausführen
python3 edit_leaves_config.py
```

### Verwendung von CMI anstelle von EssentialsX (optional)

Wenn Sie CMI als Hauptverwaltungs-Plugin verwenden möchten, führen Sie bitte folgende Schritte aus:

1. 📁 Stellen Sie sicher, dass sich das `CMI`-Plugin im `plugins`-Verzeichnis befindet
2. 🔄 Benennen Sie `EssentialsX.jar` im `plugins`-Verzeichnis in `EssentialsX.jar[disabled]` um
3. 🔄 Benennen Sie `CMIEInjector.jar[disabled]` im `plugins`-Verzeichnis in `CMIEInjector.jar` um
4. 🔄 Benennen Sie `home_select.yml[disabled]` im Verzeichnis `plugins/PlayerMenu/menu` in `home_select.yml` um (muss die Originaldatei überschreiben)

## 📄 Lizenz

Dieses Projekt verwendet das Open-Source-Protokoll [GPLv3-Lizenz](LICENSE).

Projekt abgeleitet von [SurviveX](https://github.com/KiteMC/SurviveX) mit [GPLv3-Lizenz](https://github.com/KiteMC/SurviveX/LICENSE).

> [!WARNING]
> Wichtige Erklärung zu Plugin-Urheberrechten
>
> Dieses Projekt ist ein Open-Source-Minecraft-Server-Integrationspaket, und die darin enthaltenen verschiedenen Plugins sind geistiges Eigentum ihrer jeweiligen Urheberrechtsinhaber.
> Dieses Projekt übernimmt keine ausdrücklichen oder stillschweigenden Garantien hinsichtlich der Legalität, Funktionalität oder Eignung der enthaltenen Plugins.
> Die Benutzer tragen die damit verbundenen Risiken bei der Verwendung dieses Integrationspakets selbst und müssen sich an die Lizenzvereinbarungen der einzelnen Plugins halten.
> Dieses Projekt gibt keine Zusagen oder Garantien hinsichtlich Verfügbarkeit, Stabilität oder Kompatibilität der Plugins ab.

## 🔗 Verwandte Links

- 📥 [GitHub-Repository](https://github.com/Maicarons/SurviveP)
- ⚡ [Neuestes Paket herunterladen (GitHub)](https://github.com/Maicarons/SurviveP/releases/latest/download/SurviveP.zip) 

## ⭐ Sternverlauf

Wenn Ihnen dieses Projekt geholfen hat, geben Sie uns bitte einen Stern!

[![Sternverlaufsdiagramm](https://api.star-history.com/svg?repos=Maicarons/SurviveP&type=Date)](https://www.star-history.com/#Maicarons/SurviveP&Date)