# SurviveP - Paquete de servidor Minecraft Survival basado en Leaves

![Versión de Minecraft](https://img.shields.io/badge/Minecraft-1.21.8-blue)
![Licencia](https://img.shields.io/github/license/Maicarons/SurviveP)

## 🌐 Navegación por idiomas

[:us: English](README_en.md) | [:cn: Chinese](README.md) | [:jp: Japanese](README_ja.md) | [:ru: Russian](README_ru.md) | [:fr: French](README_fr.md) | [:de: German](README_de.md) | [:es: Spanish](README_es.md) | [:kr: Korean](README_ko.md)

## 🎮 Introducción

SurviveP es un servidor Minecraft Survival rico en funciones construido sobre el núcleo [Leaves](https://github.com/LeavesMC/Leaves). Integra numerosos plugins útiles y proporciona una experiencia completa de juego de supervivencia, incluyendo sistemas de hogar, sistemas económicos, protección de territorios, sistemas de teletransporte y sistemas de profesiones.

SurviveP es una rama de [SurviveX](https://github.com/KiteMC/SurviveX), dedicada a crear un paquete de servidor que incluso los operadores novatos puedan implementar con un solo clic.

## 📋 Requisitos del entorno

- 🎯 **Versión del núcleo**: Leaves 1.21.8
- ☕ **Entorno de ejecución**: Java 21+

## 🚀 Inicio rápido

### Plataforma de servidor con un clic:

Después de cargar el paquete, seleccione el archivo `leaves.jar` como su núcleo de inicio.

### Linux/MacOS:
```bash
cd shell
./start_auto.sh # Obtiene automáticamente la configuración del sistema y selecciona los parámetros apropiados para ejecutar.
# o ./start.sh si desea mantener la configuración sin cambios cada vez, por favor modifique start.sh.
```
### Windows:
```powershell
cd shell
.\start.cmd
```

## 🔧 Ecosistema de plugins

Consulte [Lista de plugins](plugin.md) para ver plugins y precauciones.

## ⭐ Características

- [x] Scripts de inicio para Windows/Linux/MacOS  
- [x] Modificación de configuración mediante GUI
- [ ] Mapas multiescenario preconstruidos  

## Cliente

Los jugadores deben usar el cliente Minecraft Java Edition 1.21.8 para unirse al servidor. Se pueden instalar moderadamente mods de optimización y visualización de información, mientras que los mods de ayuda y trampas serán detectados y prohibidos por el servidor.

## 🔧 Editor de configuración

El proyecto proporciona una herramienta de configuración gráfica para facilitar a los administradores la modificación de la configuración del servidor:

### Editor de configuración simple
El `simple_leaves_editor.py` ubicado en el directorio raíz proporciona funciones de modificación rápida para elementos clave de configuración, adecuado para administradores principiantes.

### Editor de configuración completo
`edit_leaves_config.py` es un editor de configuración completamente funcional (en desarrollo) que admite la modificación integral de todos los archivos de configuración del servidor Leaves.

### Uso
```bash
# Ejecutar editor de configuración simple
python3 simple_leaves_editor.py

# Ejecutar editor de configuración completo
python3 edit_leaves_config.py
```

### Usar CMI en lugar de EssentialsX (Opcional)

Si desea usar CMI como plugin de gestión principal, siga estos pasos:

1. 📁 Asegúrese de que el plugin `CMI` esté en el directorio `plugins`
2. 🔄 Cambie el nombre de `EssentialsX.jar` en el directorio `plugins` a `EssentialsX.jar[disabled]`
3. 🔄 Cambie el nombre de `CMIEInjector.jar[disabled]` en el directorio `plugins` a `CMIEInjector.jar`
4. 🔄 Cambie el nombre de `home_select.yml[disabled]` en el directorio `plugins/PlayerMenu/menu` a `home_select.yml` (necesita sobrescribir el archivo original)

## 📄 Licencia

Este proyecto adopta el protocolo de código abierto [Licencia GPLv3](LICENSE).

Proyecto derivado de [SurviveX](https://github.com/KiteMC/SurviveX) con [Licencia GPLv3](https://github.com/KiteMC/SurviveX/LICENSE).

> [!WARNING]
> Declaración importante sobre derechos de autor de plugins
>
> Este proyecto es un paquete de integración de servidor Minecraft de código abierto, y los diversos plugins contenidos son propiedad intelectual de sus respectivos titulares de derechos de autor.
> Este proyecto no ofrece garantías expresas o implícitas sobre la legalidad, funcionalidad o idoneidad de los plugins incluidos.
> Los usuarios deben asumir los riesgos relacionados al usar este paquete de integración y cumplir con los acuerdos de licencia de cada plugin.
> Este proyecto no proporciona ningún compromiso o garantía sobre la disponibilidad, estabilidad o compatibilidad de los plugins.

## 🔗 Enlaces relacionados

- 📥 [Repositorio de GitHub](https://github.com/Maicarons/SurviveP)
- ⚡ [Descargar paquete más reciente (GitHub)](https://github.com/Maicarons/SurviveP/releases/latest/download/SurviveP.zip) 

## ⭐ Historial de estrellas

¡Si este proyecto le ha sido útil, por favor danos una estrella!

[![Gráfico del historial de estrellas](https://api.star-history.com/svg?repos=Maicarons/SurviveP&type=Date)](https://www.star-history.com/#Maicarons/SurviveP&Date)