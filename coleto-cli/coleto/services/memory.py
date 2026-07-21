from __future__ import annotations
import psutil


def get_memory_total() -> float:
    """Retorna la memoria RAM total en GB."""
    memory = psutil.virtual_memory()
    return round(memory.total / (1024 ** 3), 2)


def get_memory_used() -> float:
    """Retorna la memoria RAM usada en GB."""
    memory = psutil.virtual_memory()
    return round(memory.used / (1024 ** 3), 2)


def get_memory_available() -> float:
    """Retorna la memoria RAM disponible en GB."""
    memory = psutil.virtual_memory()
    return round(memory.available / (1024 ** 3), 2)


def get_memory_percent() -> float:
    """Retorna el porcentaje de RAM utilizada."""
    return psutil.virtual_memory().percent
