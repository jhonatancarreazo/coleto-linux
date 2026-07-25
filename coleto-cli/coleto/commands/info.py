from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from coleto.services.packages import package_info

console = Console()

def run(package: str) -> None:

    info = package_info(package)

    if info is None:

        console.print(
            f"[bold red]✗ No se encontró el paquete '{package}'.[/bold red]"
        )

        return
    console.print()

    console.print(
        Panel.fit(
            f"📦 [bold cyan]{info.name}[/bold cyan]",
            border_style="cyan",
        )
    )

    table = Table(show_header=False)

    table.add_row("Versión", info.version)
    table.add_row("Arquitectura", info.architecture)
    table.add_row("Tamaño", info.installed_size)
    table.add_row("Mantenedor", info.maintainer)
    table.add_row("Repositorio", info.repository)

    console.print(table)

    console.print()

    console.print(
        Panel(
            info.description,
            title="Descripción",
            border_style="green",
        )
    )
    
    