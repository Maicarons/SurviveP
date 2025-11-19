# SurviveP - 基于Leaves的Minecraft生存服务器

![Minecraft Version](https://img.shields.io/badge/Minecraft-1.21.8-blue)
![License](https://img.shields.io/github/license/Maicarons/SurviveP)

## 🎮 简介

SurviveP 是一个基于 `Leaves` 核心构建的功能丰富的 Minecraft 生存服务器。它集成了众多实用插件，提供了完整的生存游戏体验，包括家园系统、经济系统、领地保护、传送系统、职业系统等。

SurviveP 是 [SurviveX](https://github.com/KiteMC/SurviveX) 的分支，致力于打造腐竹小白也能一键上手开服的服务器整合包。

## 📋 环境要求

- 🎯 **核心版本**：Leaves 1.21.8
- ☕ **运行环境**：Java 21+

## 🚀 快速开始

### 一键开服平台：

请上传整合包后，选中`leaves.jar`文件作为你的启动核心。

### Linux/MacOS:
```bash
cd shell
./start_auto.sh # 自动获取系统配置并选择合适的参数运行。
# or ./start.sh 如果你想保持每次配置是不变的，请修改start.sh。
```
### Windows:
```powershell
cd shell
.\start.cmd
```

## 🔧 插件生态

插件及注意事项详见 [插件列表](plugin.md)。

## ⭐ 特色功能

- [x] Windows/Linux/MacOS 启动脚本  
- [x] GUI 配置修改
- [ ] 预构建多场景地图  

## 🔧 配置编辑器

项目提供图形化配置工具，方便管理员修改服务器设置：

### 简易配置编辑器
位于根目录的 `simple_leaves_editor.py` 提供了对关键配置项的快速修改功能，适合新手管理员使用。

### 完整配置编辑器
`edit_leaves_config.py` 是一个功能完整的配置编辑器（开发中），支持对 Leaves 服务端所有配置文件的全面修改。

### 使用方法
```bash
# 运行简易配置编辑器
python3 simple_leaves_editor.py

# 运行完整配置编辑器
python3 edit_leaves_config.py
```

### 使用CMI替代EssentialsX（可选）

如果希望使用CMI作为主要管理插件，请按以下步骤操作：

1. 📁 确保 `CMI` 插件在 `plugins` 目录下
2. 🔄 将 `plugins` 目录下的 `EssentialsX.jar` 重命名为 `EssentialsX.jar[disabled]`
3. 🔄 将 `plugins` 目录下的 `CMIEInjector.jar[disabled]` 重命名为 `CMIEInjector.jar`
4. 🔄 将 `plugins/PlayerMenu/menu` 目录下的 `home_select.yml[disabled]` 重命名为 `home_select.yml`（需覆盖原文件）

## 📄 许可证

本项目采用 [GPLv3 License](LICENSE) 开源协议。

Project forked from [SurviveX](https://github.com/KiteMC/SurviveX) with [GPLv3 License](https://github.com/KiteMC/SurviveX/LICENSE).

## 🔗 相关链接

- 📥 [GitHub 仓库](https://github.com/Maicarons/SurviveP)
- ⚡ [下载最新整合包（Github）](https://github.com/Maicarons/SurviveP/releases/latest/download/SurviveP.zip) 

## ⭐ Star History

如果本项目对您有帮助，请给我们一个Star！

[![Star History Chart](https://api.star-history.com/svg?repos=Maicarons/SurviveP&type=Date)](https://www.star-history.com/#Maicarons/SurviveP&Date)