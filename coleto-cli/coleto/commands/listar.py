from rich.console import Console
from rich.table import Table

from coleto.services.packages import list_installed_packages
from coleto.services.utils import filter_packages

console = Console()


def run(
    mode: str,
    buscar: str | None = None,
    limitar: int = 20,
) -> None:

    if mode == "instalados":
        packages = list_installed_packages()
    else:
        # Error de modo
        console.print("[red]¡Papi, tas miando fuera del tiesto! Ese modo no existe.[/red]")
        return

    packages = filter_packages(
    packages,
    search=buscar,
    limit=limitar,
)

    if not packages:
        # No se encontró nada
        console.print("[yellow]¡Firme! Pero no encontré ni un solo paquete por ahí.[/yellow]")
        return

    # Título de la tabla con flow
    table = Table(title="📦 El tierrero de paquetes instalados")

    table.add_column("Nombre", style="cyan")
    table.add_column("Estado", style="green")

    for package in packages:
        table.add_row(
            package.name,
            package.description,
        )

    console.print(table)

    # Conteo de resultados
    console.print(
        f"\nTe tiré en la cara {len(packages)} resultado(s), cuadro."
    )
