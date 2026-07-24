from rich.console import Console

from coleto.services.packages import remove_package

console = Console()


def run(package: str) -> None:
    console.print(f"🗑️ Eliminando [cyan]{package}[/cyan]...\n")

    if remove_package(package):
        console.print(
            f"[bold green]✓ {package} eliminado correctamente.[/bold green]"
        )
    else:
        console.print(
            f"[bold red]✗ No fue posible eliminar {package}.[/bold red]"
        )