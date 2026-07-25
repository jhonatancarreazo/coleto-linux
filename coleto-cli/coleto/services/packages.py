import shutil
import subprocess
import platform

from coleto.models.packages import Package
from coleto.services import apt
from coleto.services.apt import upgrade




def has_apt() -> bool:
    if platform.system() != "Linux":
        return False
    
    return shutil.which("apt") is not None


def has_dnf() -> bool:
    if platform.system() != "Linux":
        return False
    
    return shutil.which("dnf") is not None


def has_pacman() -> bool:
    if platform.system() != "Linux":
        return False
    
    return shutil.which("pacman") is not None


def has_snap() -> bool:
    if platform.system() != "Linux":
        return False
    
    return shutil.which("snap") is not None


def has_flatpak() -> bool:
    if platform.system() != "Linux":
        return False
    
    return shutil.which("flatpak") is not None

def get_package_manager() -> str:
    managers = {
        "apt": has_apt,
        "dnf": has_dnf,
        "pacman": has_pacman,
        "snap": has_snap,
        "flatpak": has_flatpak,
    }

    for name, checker in managers.items():
        if checker():
            return name

    return "desconocido"


def get_package_manager_version() -> str:
    manager = get_package_manager()

    if manager == "desconocido":
        return "No disponible"

    try:
        result = subprocess.run(
            [manager, "--version"],
            capture_output=True,
            text=True,
            timeout=3,
        )

        output = result.stdout or result.stderr

        if output:
            return output.splitlines()[0]

    except Exception:
        pass

    return "No disponible"

def search_package(query: str) -> list[Package]:
    manager = get_package_manager()

    if manager == "apt":
        return apt.search(query)

    return []

def list_installed_packages() -> list[Package]:
    """
    Obtiene los paquetes instalados utilizando el gestor detectado.
    """

    manager = get_package_manager()

    if manager == "apt":
        return apt.list_installed()

    return []


def install_package(package: str) -> bool:
    """
    Instala un paquete utilizando el gestor de paquetes detectado
    """

    manager = get_package_manager()
    
    if manager == "apt":
        return apt.install(package)
    
    return False


def remove_package(package: str) -> bool:
    """
    Elimina un paquete utilizando el gestor detectado.
    """

    manager = get_package_manager()

    if manager == "apt":
        from coleto.services import apt
        return apt.remove(package)

    return False

def update_packages() -> bool:
    """
    Actualiza la lista de paquetes utilizando el gestor de paqutes detectado.
    """
    manager = get_package_manager()

    if manager == "apt":
        return apt.update()
    
    return False

def upgrade_packages() -> bool:
    return upgrade()


def autoremove_packages() -> bool:
    """
    Elimina dependencias innecesarias utilizando el gestor detectado.
    """

    manager = get_package_manager()

    if manager == "apt":
        return apt.autoremove()

    return False


def clean_packages() -> bool:
    """
    Limpia la caché utilizando el gestor detectado.
    """

    manager = get_package_manager()

    if manager == "apt":
        return apt.clean()

    return False

def package_info(package: str) -> Package | None:
    """
    Obtiene la información detallada de un paquete delegando en apt.
    """
    manager = get_package_manager()
    
    if manager == "apt":
        return apt.info(package)
        
    return None