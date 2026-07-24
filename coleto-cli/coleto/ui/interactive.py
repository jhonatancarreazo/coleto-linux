from rich.console import Console

console = Console()


def ask_option() -> int:
    """
    Solicita una opción válida del menú principal.
    """

    while True:

        option = console.input(
            "\n[bold cyan]Selecciona una opción, Causa:[/bold cyan] "
        ).strip()

        if option.isdigit():

            option = int(option)

            if 0 <= option <= 8:
                return option

        # Mensaje coleto cuando hunden lo que no es
        console.print(
            "[bold red]✗ ¡Erda! Esa opción no va papi. Pon un número que sea válido.[/bold red]"
        )
