from __future__ import annotations
import platform
import psutil

def get_cpu_name() -> str:
    """
    Retorna el nombre del procesador
    """
    return platform.processor()

def get_cpu_count() -> int:
    """Retorna la cantidad de núcleos lógicos."""
    return psutil.cpu_count()

def get_cpu_threads() -> int:
    """Retorna la cantidad de procesadores
    """
    return psutil.cpu_count(logical=True)

def get_cpu_percent() -> float:
    """Retorna el porcentaje de uso del CPU."""
    return psutil.cpu_percent(interval=1)

def get_cpu_frecuency() -> float:
    """Retorna la frecuencia actual del CPU
    """
    freq = psutil.cpu_freq()

    if freq is None:
        return 0.0

    return  freq.current

def get_cpu_max_frecuency() -> float:
    """
    Retorna al frecuencia máxima del CPU.
    """
    freq = psutil.cpu_freq()

    if freq is None:
        return 0.0
    
    return freq.max

def get_load_average() -> tuple[float, float, float]:
     """Retorna la carga promedio de 1, 5 y 15 minutos.
    """
     return psutil.getloadavg()