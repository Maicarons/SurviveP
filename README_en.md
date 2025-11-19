# SurviveP - Minecraft Survival Server Pack Based on Leaves

![Minecraft Version](https://img.shields.io/badge/Minecraft-1.21.8-blue)
![License](https://img.shields.io/github/license/Maicarons/SurviveP)

## 🌐 Language Navigation

[:us: English](README_en.md) | [:cn: Chinese](README.md) | [:jp: Japanese](README_ja.md) | [:ru: Russian](README_ru.md) | [:fr: French](README_fr.md) | [:de: German](README_de.md) | [:es: Spanish](README_es.md) | [:kr: Korean](README_ko.md)

## 🎮 Introduction

SurviveP is a feature-rich Minecraft survival server built on the `Leaves` core. It integrates many practical plugins, providing a complete survival gaming experience, including home systems, economic systems, territory protection, teleportation systems, job systems, and more.

SurviveP is a branch of [SurviveX](https://github.com/KiteMC/SurviveX), dedicated to creating a server package that even novice server operators can easily deploy with one click.

## 📋 Environment Requirements

- 🎯 **Core Version**: Leaves 1.21.8
- ☕ **Runtime Environment**: Java 21+

## 🚀 Quick Start

### One-Click Server Platform:

After uploading the package, select the `leaves.jar` file as your startup core.

### Linux/MacOS:
```bash
cd shell
./start_auto.sh # Automatically gets system configuration and selects appropriate parameters to run.
# or ./start.sh if you want to keep the configuration unchanged each time, please modify start.sh.
```
### Windows:
```powershell
cd shell
.\start.cmd
```

## 🔧 Plugin Ecosystem

See [Plugin List](plugin.md) for plugins and precautions.

## ⭐ Features

- [x] Windows/Linux/MacOS startup scripts  
- [x] GUI configuration modification
- [ ] Pre-built multi-scenario maps  

## Client

Players should use the Minecraft Java Edition 1.21.8 client to join the server. Optimization and information display mods can be appropriately installed, while assistance and cheating mods will be detected and banned by the server.

## 🔧 Configuration Editor

The project provides a graphical configuration tool to facilitate administrators in modifying server settings:

### Simple Configuration Editor
The `simple_leaves_editor.py` located in the root directory provides quick modification functions for key configuration items, suitable for novice administrators.

### Full Configuration Editor
`edit_leaves_config.py` is a fully functional configuration editor (under development) that supports comprehensive modification of all configuration files of the Leaves server.

### Usage
```bash
# Run simple configuration editor
python3 simple_leaves_editor.py

# Run full configuration editor
python3 edit_leaves_config.py
```

### Using CMI instead of EssentialsX (Optional)

If you want to use CMI as the main management plugin, please follow these steps:

1. 📁 Ensure the `CMI` plugin is in the `plugins` directory
2. 🔄 Rename `EssentialsX.jar` under the `plugins` directory to `EssentialsX.jar[disabled]`
3. 🔄 Rename `CMIEInjector.jar[disabled]` under the `plugins` directory to `CMIEInjector.jar`
4. 🔄 Rename `home_select.yml[disabled]` under the `plugins/PlayerMenu/menu` directory to `home_select.yml` (need to overwrite the original file)

## 📄 License

This project adopts the [GPLv3 License](LICENSE) open source protocol.

Project forked from [SurviveX](https://github.com/KiteMC/SurviveX) with [GPLv3 License](https://github.com/KiteMC/SurviveX/LICENSE).

> [!WARNING]
> Important Statement About Plugin Copyrights
>
> This project is an open-source Minecraft server integration package, and the various plugins contained therein are intellectual property of their respective copyright holders.  
> This project makes no express or implied warranties regarding the legality, functionality or suitability of the included plugins.  
> Users should bear the relevant risks when using this integration package and comply with the license agreements of each plugin.  
> This project does not provide any commitments or guarantees regarding the availability, stability or compatibility of plugins.  

## 🔗 Related Links

- 📥 [GitHub Repository](https://github.com/Maicarons/SurviveP)
- ⚡ [Download Latest Package (GitHub)](https://github.com/Maicarons/SurviveP/releases/latest/download/SurviveP.zip) 

## ⭐ Star History

If this project is helpful to you, please give us a Star!

[![Star History Chart](https://api.star-history.com/svg?repos=Maicarons/SurviveP&type=Date)](https://www.star-history.com/#Maicarons/SurviveP&Date)