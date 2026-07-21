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
    get_cpu_count,
    get_cpu_percent,
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
    get_architecture,

)



console = Console()

def run() -> None:
    table = Table(title="🩺 Coleto Doctor")

    table.add_column("Propiedad", style="cyan")

    table.add_column("Valor", style="green")

    table.add_row("Sistema operativo", get_os())

    table.add_row("Versión", get_os_version())

    table.add_row("Arquitectura", get_architecture())

    table.add_row("Python", get_python_version())

    table.add_row("Plataforma", get_platform())

    table.add_row("Kernel", get_kernel())

    table.add_row("Usuario", get_username())

    table.add_row("Hostname", get_hostname())

    table.add_row("Directorio", get_current_directory())

    table.add_row(
        "Internet",
        "🟢 Estas conectado" if has_internet() else "🔴 No tienes internet"
    )

    table.add_row("IP local", get_local_ip())

    total, used, free = get_disk_usage()

    table.add_row("Disco total", f"{bytes_to_gb(total)} GB")
    table.add_row("Disco usado", f"{bytes_to_gb(used)} GB")
    table.add_row("Disco libre", f"{bytes_to_gb(free)} GB")
    table.add_row("Uso del disco", f"{get_disk_percent()} %")


    table.add_row("CPU", f"{get_cpu_percent()} %")
    table.add_row("Nucleos", str(get_cpu_count()))

    table.add_row("RAM total", f"{get_memory_total()} GB")
    table.add_row("RAM usado", f"{get_memory_used()} GB")
    table.add_row("RAM libre", f"{get_memory_available()} GB")
    table.add_row("Uso de RAM", f"{get_memory_percent()} %")

    console.print(table)

    console.print("\n[bold green]✓ Todo parece estar en orden.[/bold green]")