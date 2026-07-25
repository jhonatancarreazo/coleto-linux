from rich.console import Console

from coleto.services.packages import clean_packages

console = Console()


def run() -> None:
    console.print("🧹 Limpiando la caché de paquetes...\n")

    if clean_packages():
        console.print(
            "[bold green]✓ Caché limpiada correctamente.[/bold green]"
        )
    else:
        console.print(
            "[bold red]✗ Hey... No fue posible limpiar la caché.[/bold red]"
        )