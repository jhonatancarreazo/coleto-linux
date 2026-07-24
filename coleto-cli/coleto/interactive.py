from rich.console import Console

from coleto.ui.banner import get_banner
from coleto.ui.menu import show_menu

from coleto.commands.buscar import run as buscar_run
from coleto.commands.instalar import run as instalar_run
from coleto.commands.eliminar import run as eliminar_run
from coleto.commands.actualizar import run as actualizar_run
from coleto.commands.listar import run as listar_run
from coleto.commands.doctor import run as doctor_run

console = Console()


def run() -> None:

    while True:

        console.clear()

        console.print(get_banner())
        console.print()

        show_menu()

        console.print()

        opcion = console.input(
            "[bold cyan]Selecciona una opción, Causa:[/bold cyan] "
        ).strip()

        console.print()

        if opcion == "1":
            paquete = console.input(
                "[cyan]¿Qué paquete deseas buscar?[/cyan] "
            )

            buscar_run(paquete)

        elif opcion == "2":
            paquete = console.input(
                "[cyan]¿Qué paquete deseas instalar?[/cyan] "
            )

            instalar_run(paquete)

        elif opcion == "3":
            paquete = console.input(
                "[cyan]¿Qué paquete deseas eliminar?[/cyan] "
            )

            eliminar_run(paquete)

        elif opcion == "4":
            actualizar_run()

        elif opcion == "5":
            listar_run("instalados")

        elif opcion == "6":
            listar_run("actualizables")

        elif opcion == "7":
            doctor_run()

        elif opcion == "8":
            console.print(
                "[green]Usa:[/green] coleto ayuda"
            )

        elif opcion == "0":
            console.print(
                "[yellow]¡Hasta luego, causa! 👋[/yellow]"
            )
            break

        else:
            console.print(
                "[red]Opción no válida.[/red]"
            )

        console.print()

        console.input(
            "[dim]Presiona ENTER para volver al menú...[/dim]"
        )