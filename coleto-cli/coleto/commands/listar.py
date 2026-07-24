from rich.console import Console
from rich.table import Table

from coleto.services.packages import list_installed_packages

console = Console()


def run(mode: str) -> None:

    if mode == "instalados":
        packages = list_installed_packages()

    else:
        console.print("[red]Modo no soportado.[/red]")
        return

    if not packages:
        console.print("[yellow]No se encontraron paquetes.[/yellow]")
        return

    table = Table(title="📦 Paquetes instalados")

    table.add_column("Nombre", style="cyan")
    table.add_column("Estado", style="green")

    for package in packages:
        table.add_row(
            package.name,
            package.description,
        )

    console.print(table)