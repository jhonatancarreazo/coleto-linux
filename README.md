# 🐧 Coleto Linux

![Version](https://img.shields.io/badge/version-v0.2.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![License: GPL v3](https://img.shields.io/badge/License-GNU_GPL_v3-blue)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Ligero, bacano y estable.**

Coleto Linux es una distribución GNU/Linux basada en Debian que busca ofrecer una experiencia moderna, ligera y amigable, manteniendo la estabilidad del ecosistema Debian mientras desarrolla una identidad propia.

Actualmente el proyecto se encuentra en desarrollo activo y está compuesto por varios componentes independientes que, en conjunto, dan vida a la distribución.

---

## ⚡ Inicio Rápido (`coleto-cli`)

Si quieres probar el CLI en tu entorno local o máquina virtual con Debian/Ubuntu:

```bash
# 1. Clonar el repositorio
git clone https://github.com/jhonatancarreazo/coleto-linux.git
cd coleto-linux/coleto-cli

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Probar la herramienta
python3 -m coleto_cli.main --help
# o ejecutar el menú interactivo
python3 -m coleto_cli.main
```

---

## 🚧 Estado del proyecto

**Versión actual:** `v0.2.0` (ISO de prueba con CLI integrado disponible)

### Completado

- ✅ Arquitectura inicial del proyecto.
- ✅ Desarrollo de Coleto CLI v0.2.0 (`Typer` + `Rich`).
- ✅ Empaquetado del CLI en formato `.deb`.
- ✅ Generación de la primera ISO funcional con `live-build` e integración de `coleto-cli`.
- ✅ Organización del repositorio y documentación comunitaria (`CONTRIBUTING.md` y `CODE_OF_CONDUCT.md`).

### En desarrollo

- 🚧 Tema visual propio (Coleto Theme).
- 🚧 Paquete de íconos (Coleto Icons).
- 🚧 Fondos de pantalla oficiales (Coleto Wallpapers).
- 🚧 Integración del entorno de escritorio personalizado en la ISO.
- 🚧 Instalador gráfico (Coleto Installer).

---

## 🎯 Objetivos

- Mantener la estabilidad de Debian.
- Mejorar la experiencia del usuario desde la terminal.
- Tener una identidad visual y de software propia.
- Ser ligero y de bajo consumo de recursos.
- Ser intuitivo y fácil de usar.

---

# 📦 Componentes

## ✅ Coleto CLI

Herramienta de línea de comandos desarrollada en Python para facilitar la administración del sistema.

Actualmente incluye:

- 🔎 Buscar paquetes.
- 📥 Instalar paquetes.
- 🗑️ Eliminar paquetes.
- ℹ️ Consultar información de paquetes.
- 🔄 Actualizar repositorios.
- ⬆️ Actualizar paquetes.
- 🧹 Eliminar dependencias innecesarias.
- 🧼 Limpiar la caché de paquetes.
- 📋 Listar paquetes instalados.
- 📦 Listar paquetes actualizables.
- 💻 Información del sistema (`doctor`).
- 🎨 Menú interactivo visual.

---

## ✅ Live Build

Configuración de `live-build` para generar la imagen ISO oficial de Coleto Linux basada en Debian, con el paquete `.deb` de `coleto-cli` preinstalado.

---

## 🚧 Coleto Theme
Tema visual oficial de Coleto Linux.

## 🚧 Coleto Icons
Paquete de íconos oficial de Coleto Linux.

## 🚧 Coleto Wallpapers
Fondos de pantalla oficiales.

## 🚧 Coleto Installer
Instalador gráfico para la distribución.

---

# 🛣️ Roadmap

## ✅ v0.2.0 (Release Actual)

### Live Build & Sistema Base
- ✅ Configuración de `live-build` para Debian.
- ✅ Integración del paquete `.deb` de `coleto-cli` preinstalado en la ISO.
- ✅ Publicación de la primera ISO de prueba (v0.2.0).

### Coleto CLI
- ✅ Gestión de paquetes mediante APT.
- ✅ Menú interactivo visual en terminal.
- ✅ Navegación mediante opciones numéricas.
- ✅ Diagnóstico del sistema (`coleto doctor`).
- ✅ Arquitectura modular (`commands`, `services`, `models` y `ui`).

### Comandos disponibles
- `buscar`
- `instalar`
- `eliminar`
- `info`
- `actualizar`
- `upgrade`
- `autoremove`
- `limpiar`
- `listar instalados`
- `listar actualizables`
- `doctor`
- `ayuda`

---

## 🚧 Próximo objetivo (v0.3.0)

- Integración de **Coleto Theme** e **Icons** dentro de la ISO.
- Personalización del entorno de escritorio por defecto (look & feel propio).
- Optimización del tiempo de arranque y consumo de RAM de la ISO.
- Primeras pruebas del instalador gráfico.

---

## 📁 Estructura del proyecto

```text
coleto-linux/
├── coleto-cli/      # Herramienta CLI en Python (Typer, Rich)
├── coleto-theme/    # Tema visual (En desarrollo)
├── coleto-icons/    # Paquete de íconos (En desarrollo)
├── live-build/      # Configuración de compilación ISO Debian
├── docs/            # Documentación del proyecto
├── scripts/         # Scripts auxiliares de compilación
└── assets/          # Capturas de pantalla y recursos gráficos
```

---

## 📷 Capturas de pantalla

| Menú Interactivo | Ayuda del CLI |
| :---: | :---: |
| ![Menú Interactivo](assets/coleto.png) | ![Ayuda](assets/coleto-ayuda.png) |

| Información de Paquetes | Listado de Paquetes |
| :---: | :---: |
| ![Información](assets/coleto-info.png) | ![Listar Instalados](assets/coleto-listar-instalados.png) |

---

## 🤝 Contribuciones

¡Las contribuciones son la esencia del código abierto! Si quieres colaborar con código en Python, probar la ISO, reportar fallos o proponer ideas de diseño:

1. Lee nuestra **[Guía de Contribución](CONTRIBUTING.md)** para conocer el entorno de desarrollo y flujo de trabajo.
2. Revisa nuestro **[Código de Conducta](CODE_OF_CONDUCT.md)** para asegurar una comunidad respetuosa e inclusiva.
3. Revisa la pestaña de **[Issues](https://github.com/jhonatancarreazo/coleto-linux/issues)** para ver las tareas disponibles.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **GNU General Public License v3.0 (GPL-3.0)**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
