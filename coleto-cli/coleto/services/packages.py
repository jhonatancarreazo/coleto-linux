import shutil
import subprocess
import platform

from coleto.models.packages import Package
from coleto.services import apt



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