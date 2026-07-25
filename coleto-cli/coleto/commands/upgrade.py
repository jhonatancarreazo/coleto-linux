from rich.console import Console

from coleto.services.packages import upgrade_packages

console = Console()


def run() -> None:
    console.print("[cyan]⬆️ Actualizando paquetes instalados...[/cyan]\n")

    if upgrade_packages():
        console.print(
            "[bold green]✓ Sistema actualizado correctamente.[/bold green]"
        )
    else:
        console.print(
            "[bold red]✗ Joda..! No fue posible actualizar los paquetes.[/bold red]"
        )