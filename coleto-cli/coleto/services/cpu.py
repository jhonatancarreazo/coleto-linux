from __future__ import annotations
import psutil

def get_cpu_percent() -> float:
    """Retorna el porcentaje de uso del CPU."""
    return psutil.cpu_percent(interval=1)


def get_cpu_count() -> int:
    """Retorna la cantidad de núcleos lógicos."""
    return psutil.cpu_count()

def get_cpu_fisical_count() ->

def get_cpu_frecuency() ->

def get_cpu_model() ->

def get_cpu_load_average() ->