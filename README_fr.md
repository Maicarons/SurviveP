# SurviveP - Pack de serveur Minecraft Survival basé sur Leaves

![Version Minecraft](https://img.shields.io/badge/Minecraft-1.21.8-blue)
![Licence](https://img.shields.io/github/license/Maicarons/SurviveP)

## 🌐 Navigation linguistique

[:us: English](README_en.md) | [:cn: Chinese](README.md) | [:jp: Japanese](README_ja.md) | [:ru: Russian](README_ru.md) | [:fr: French](README_fr.md) | [:de: German](README_de.md) | [:es: Spanish](README_es.md) | [:kr: Korean](README_ko.md)

## 🎮 Introduction

SurviveP est un serveur Minecraft Survival riche en fonctionnalités construit sur le noyau [Leaves](https://github.com/LeavesMC/Leaves). Il intègre de nombreux plugins utiles et offre une expérience de jeu complète, incluant des systèmes de maisons, d'économie, de protection de territoires, de téléportation et de métiers.

SurviveP est une branche de [SurviveX](https://github.com/KiteMC/SurviveX), dédiée à la création d'un pack de serveur que même les débutants peuvent déployer en un clic.

## 📋 Conditions requises

- 🎯 **Version du noyau** : Leaves 1.21.8
- ☕ **Environnement d'exécution** : Java 21+

## 🚀 Démarrage rapide

### Plateforme de déploiement en un clic :

Après avoir téléchargé le pack, sélectionnez le fichier `leaves.jar` comme noyau de démarrage.

### Linux/MacOS :
```bash
cd shell
./start_auto.sh # Récupère automatiquement la configuration système et choisit les paramètres appropriés pour l'exécution.
# ou ./start.sh si vous souhaitez conserver la même configuration à chaque fois, veuillez modifier start.sh.
```
### Windows :
```powershell
cd shell
.\start.cmd
```

## 🔧 Écosystème de plugins

Voir [Liste des plugins](plugin.md) pour les plugins et précautions.

## ⭐ Fonctionnalités

- [x] Scripts de démarrage pour Windows/Linux/MacOS  
- [x] Modification de configuration via interface graphique
- [ ] Cartes multi-scénarios préconstruites  

## Client

Les joueurs doivent utiliser le client Minecraft Java Edition 1.21.8 pour rejoindre le serveur. Il est possible d'installer modérément des mods d'optimisation et d'affichage d'informations, mais les mods d'assistance et de triche seront détectés et bannis par le serveur.

## 🔧 Éditeur de configuration

Le projet fournit un outil de configuration graphique pour faciliter la modification des paramètres du serveur par les administrateurs :

### Éditeur de configuration simplifié
Le fichier `simple_leaves_editor.py` situé dans le répertoire racine permet de modifier rapidement les éléments clés de configuration, adapté aux administrateurs débutants.

### Éditeur de configuration complet
`edit_leaves_config.py` est un éditeur de configuration complet (en développement) qui prend en charge la modification complète de tous les fichiers de configuration du serveur Leaves.

### Utilisation
```bash
# Exécuter l'éditeur de configuration simplifié
python3 simple_leaves_editor.py

# Exécuter l'éditeur de configuration complet
python3 edit_leaves_config.py
```

### Utiliser CMI au lieu d'EssentialsX (Optionnel)

Si vous souhaitez utiliser CMI comme plugin de gestion principal, suivez ces étapes :

1. 📁 Assurez-vous que le plugin `CMI` se trouve dans le répertoire `plugins`
2. 🔄 Renommez `EssentialsX.jar` dans le répertoire `plugins` en `EssentialsX.jar[disabled]`
3. 🔄 Renommez `CMIEInjector.jar[disabled]` dans le répertoire `plugins` en `CMIEInjector.jar`
4. 🔄 Renommez `home_select.yml[disabled]` dans le répertoire `plugins/PlayerMenu/menu` en `home_select.yml` (nécessite d'écraser le fichier original)

## 📄 Licence

Ce projet adopte le protocole open source [Licence GPLv3](LICENSE).

Projet dérivé de [SurviveX](https://github.com/KiteMC/SurviveX) sous [Licence GPLv3](https://github.com/KiteMC/SurviveX/LICENSE).

> [!WARNING]
> Déclaration importante concernant les droits d'auteur des plugins
>
> Ce projet est un pack de serveur Minecraft open-source intégrant divers plugins qui sont la propriété intellectuelle de leurs auteurs respectifs.
> Ce projet ne donne aucune garantie expresse ou implicite quant à la légalité, la fonctionnalité ou l'adéquation des plugins inclus.
> Les utilisateurs doivent assumer les risques liés à l'utilisation de ce pack d'intégration et respecter les accords de licence de chaque plugin.
> Ce projet ne fournit aucun engagement ou garantie concernant la disponibilité, la stabilité ou la compatibilité des plugins.

## 🔗 Liens associés

- 📥 [Dépôt GitHub](https://github.com/Maicarons/SurviveP)
- ⚡ [Télécharger le dernier pack (GitHub)](https://github.com/Maicarons/SurviveP/releases/latest/download/SurviveP.zip) 

## ⭐ Historique des étoiles

Si ce projet vous a été utile, merci de nous donner une étoile !

[![Graphique de l'historique des étoiles](https://api.star-history.com/svg?repos=Maicarons/SurviveP&type=Date)](https://www.star-history.com/#Maicarons/SurviveP&Date)