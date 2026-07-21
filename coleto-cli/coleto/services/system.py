"""
Servicios para obtener información del sistema.
"""

from __future__ import annotations

import os
import platform
import socket
from pathlib import Path


def get_os() -> str:
    """Retorna el nombre del sistema operativo."""
    return platform.system()


def get_os_version() -> str:
    """Retorna la versión del sistema operativo."""
    return platform.version()


def get_platform() -> str:
    """Retorna una descripción amigable de la plataforma."""
    return platform.platform()


def get_kernel() -> str:
    """Retorna la versión del kernel."""
    return platform.release()


def get_architecture() -> str:
    """Retorna la arquitectura del sistema."""
    return platform.machine()


def get_python_version() -> str:
    """Retorna la versión de Python."""
    return platform.python_version()


def get_hostname() -> str:
    """Retorna el nombre del equipo."""
    return socket.gethostname()


def get_username() -> str:
    """Retorna el usuario actual."""
    return os.getenv("USER") or os.getenv("USERNAME") or "Desconocido"


def get_home_directory() -> Path:
    """Retorna el directorio HOME."""
    return Path.home()

def get_current_directory() -> str:
    return os.getcwd()