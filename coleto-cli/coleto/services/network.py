from __future__ import annotations

import socket


def has_internet(timeout: int = 3) -> bool:
    """Retorna True si hay conexión a Internet."""
    try:
        socket.setdefaulttimeout(timeout)
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False


def get_local_ip() -> str:
    """Retorna la IP local."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "Desconocida"