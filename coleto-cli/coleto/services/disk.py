from __future__ import annotations
import shutil

def get_disk_usage() -> tuple[int, int, int]:
    """
    Retorna (total, usado, libre) en bytes.
    """
    usage = shutil.disk_usage("/")

    return(
        usage.total,
        usage.used,
        usage.free,
    )

def bytes_to_gb(size: int) -> float:
    """
    Covierte bytes a GB
    """
    return round(size / (1024 ** 3), 2)

def get_disk_percent() -> float:
    """
    Retorna el poercentaje de uso de disco.
    """
    total, used, _ = get_disk_usage()

    return round((used / total) * 100, 1)