from rich.console import Console

from coleto.services.packages import autoremove_packages

console = Console()


def run() -> None:
    console.print(
        "🧹 Eliminando dependencias innecesarias...\n"
    )

    if autoremove_packages():
        console.print(
            "[bold green]✓ Dependencias eliminadas correctamente.[/bold green]"
        )
    else:
        console.print(
            "[bold red]✗ Hey... No fue posible eliminar las dependencias.[/bold red]"
        )