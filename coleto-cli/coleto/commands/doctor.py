from rich.console import Console
from rich.table import Table
from coleto.services.network import has_internet, get_local_ip
from coleto.services.disk import (
    get_disk_usage,
    get_disk_percent,
    bytes_to_gb
)
from coleto.services.memory import (
    get_memory_available,
    get_memory_percent,
    get_memory_total,
    get_memory_used,
)

from coleto.services.cpu import (
    get_cpu_name,
    get_cpu_count,
    get_cpu_threads,
    get_cpu_percent,
    get_cpu_frecuency, 
    get_cpu_max_frecuency,
    get_load_average,
)

from coleto.services.system import (
    get_architecture,
    get_current_directory,
    get_hostname,
    get_os_version,
    get_os,
    get_python_version,
    get_username,
    get_platform,
    get_kernel,

)

from coleto.services.packages import(
    get_package_manager,
    get_package_manager_version,
    has_snap,
    has_flatpak,
    
)

from coleto.services.packages import (
    get_package_manager,
    has_snap,
    has_flatpak,
    
)

console = Console()

### Sistema #######

def add_system_rows(table):
    table.add_row("Sistema", get_os())
    table.add_row("Version", get_os_version())
    table.add_row("Kernel", get_kernel())
    table.add_row("Arquitectura", get_architecture())
    table.add_row("Python", get_python_version())
    table.add_row("Usuario", get_username())
    table.add_row("Hostname", get_hostname())
    table.add_row("Directorio", get_current_directory())

### CPU #######
def add_cpu_rows(table):
    table.add_row("Procesador", get_cpu_name())
    table.add_row("Núcleos", str(get_cpu_count()))
    table.add_row("Hilos", str(get_cpu_threads()))
    table.add_row("Uso CPU", f"{get_cpu_percent():.1f}%")
    table.add_row(
        "Frecuencia",
        f"{get_cpu_frecuency() / 1000:.2f} GHz"
    )
    load1, load5, load15 = get_load_average()

    table.add_row(
        "Carga",
        f"{load1:.2f} | {load5:.2f} | {load15:.2f}"
    )

### Memoria #######
def add_memory_rows(table):
    table.add_row("RAM Total", f"{get_memory_total()} GB")
    table.add_row("RAM Usada", f"{get_memory_used()} GB")
    table.add_row("RAM Libre", f"{get_memory_available()} GB")
    table.add_row("Uso RAM", f"{get_memory_percent()} %")

### Disco #######
def add_disk_rows(table):
    total, used, free = get_disk_usage()
    table.add_row("Disco total", f"{bytes_to_gb(total)} GB")
    table.add_row("Disco usado", f"{bytes_to_gb(used)} GB")
    table.add_row("Disco libre", f"{bytes_to_gb(free)} GB")
    table.add_row("Uso del disco", f"{get_disk_percent()} %")

### Red #######
def add_network_rows(table):
    table.add_row( "Internet",
        "🟢 Estas conectado" if has_internet() else "🔴 No tienes internet")
    table.add_row("IP local", get_local_ip())
    #table.add_row(...)

##### Paquetes #######
def add_package_rows(table):
    table.add_row(
        "Gestor de paquetes",
        get_package_manager()
    )

    table.add_row(
        "Version",
        get_package_manager_version()
    )

    table.add_row(
        "Snap",
        "🟢 Disponible" if has_snap() else "🔴 No disponible"
    )

    table.add_row(
        "Flatpak",
        "🟢 Disponible" if has_flatpak() else "🔴 No disponible"
    )

    


def run() -> None:
    table = Table(title="🩺 Coleto Doctor")

    table.add_column("Propiedad", style="cyan")
    table.add_column("Valor", style="green")

    add_system_rows(table)
    add_cpu_rows(table)
    add_memory_rows(table)
    add_disk_rows(table)
    add_network_rows(table)
    add_package_rows(table)
    

    console.print(table)

    console.print(
        "\n[bold green]✓ Todo parece estar en orden.[/bold green]"
    )




  