from rich.console import Console

from coleto.ui.banner import get_banner
from coleto.ui.menu import show_menu
from coleto.ui.actions import execute_action

console = Console()


def run() -> None:

    while True:

        console.clear()

        console.print(get_banner())
        console.print()

        show_menu()

        console.print()

        option = console.input(
            "[bold cyan]Selecciona una opción:[/bold cyan] "
        ).strip()

        if option == "0":
            console.print("\n👋 ¡Hasta luego, causa!")
            break

        console.print()

        execute_action(option)

        console.print()

        console.input(
            "[dim]Presiona ENTER para volver al menú...[/dim]"
        )