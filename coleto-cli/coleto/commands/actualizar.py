from rich.console import Console

from coleto.services.packages import update_packages

console = Console()

def run() -> None:
    console.print("🔄 Actualizando lista de paquetes...\n")

    if update_packages():
        console.print(
            "[bold green]✓ Lista de paquetes actualizada correctamente.[/bold green]"
        )
    else:
        console.print(
            "[bold red]✗ No fue posible actualizar la lista de paquetes.[/bold red]"
        )