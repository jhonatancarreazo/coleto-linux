from rich.console import Console
from rich.table import Table

from coleto.services.packages import search_package

console = Console()


def run(query: str) -> None:
    console.print(f"🔎 Buscando [cyan]{query}[/cyan]...\n")

    packages = search_package(query)

    if not packages:
        console.print("[yellow]Hey!... No se encontraron paquetes.[/yellow]")
        return

    table = Table(title="Resultados")

    table.add_column("Nombre", style="cyan")
    table.add_column("Descripción", style="green")

    for pkg in packages:
        table.add_row(
            pkg.name,
            pkg.description
        )

    console.print(table)