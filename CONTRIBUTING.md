# 🤝 Guía de Contribución a Coleto Linux

¡Gracias por tu interés en contribuir a **Coleto Linux**! 🎉

Coleto Linux es un proyecto 100% de Software Libre (GPLv3) diseñado para construir una distribución ligera basada en Debian con herramientas y CLI propio desarrollados en Python. La participación de la comunidad es la fuerza impulsora de este proyecto.

---

## 📋 Formas de Contribuir

No necesitas ser un desarrollador senior para colaborar. Aceptamos contribuciones en múltiples áreas:

- 🐍 **Desarrollo Python:** Módulos para `coleto-cli` (`Typer`, `Rich`, `psutil`).
- 🧪 **Testing:** Probar las ISOs en máquinas virtuales (VirtualBox/QEMU) y reportar errores o consumo de recursos.
- 🐧 **Sysadmin / Live Build:** Optimización de configuración de Debian Live Build y empaquetado `.deb`.
- 🎨 **Diseño:** Vectorización de la mascota del sistema (`.svg`), wallpapers y temas visuales.
- 📝 **Documentación:** Mejora de tutoriales, guías y traducción de documentos.

---

## 🛠️ Configuración del Entorno de Desarrollo (`coleto-cli`)

Para trabajar en el CLI desarrollado en Python:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/jhonatancarreazo/coleto-linux.git](https://github.com/jhonatancarreazo/coleto-linux.git)
cd coleto-linux/coleto-cli
```
### 2. Crear un entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instalar dependencias en modo desarrollo
```bash
pip install -r requirements.txt
pip install -e .
```
### 4. Probar los cambios
```bash
coleto --help
coleto doctor
```

---

## 🌿 Flujo de Trabajo con Git (Git Workflow)

### 1. Haz un Fork del repositorio en GitHub.

### 2. Crea una rama para tu funcionalidad o corrección de error:
```bash
git checkout -b feat/nueva-funcionalidad
# o para un bugfix:
git checkout -b fix/corregir-error-apt
```

### 3. Realiza tus cambios y haz commits descriptivos siguiendo la convención de Conventional Commits:

```feat:``` Nueva característica (ej.```feat(cli): agregar comando coleto red```)

```fix:``` Corrección de un fallo (ej. ```fix(deps): corregir importación de psutil```)

```docs:``` Cambios en la documentación (ej. ```docs: actualizar README.md```)

```style:``` Formato o limpieza de código sin cambiar lógica

```refactor:``` Reestructuración de código

### 4. Sube tus cambios a tu fork:
```bash
git push origin feat/nueva-funcionalidad
 ```


### 5. Abre un Pull Request (PR) hacia la rama main del repositorio principal explicando tus cambios.

---

### ❓ ¿Tienes dudas o sugerencias?
Si quieres proponer una idea antes de escribir código o encontraste un fallo, abre un Issue en la pestaña correspondiente de GitHub. ¡Estaremos encantados de discutirlo!
