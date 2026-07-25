from rich.console import Console

from coleto.commands.buscar import run as buscar_run
from coleto.commands.instalar import run as instalar_run
from coleto.commands.eliminar import run as eliminar_run
from coleto.commands.actualizar import run as actualizar_run
from coleto.commands.upgrade import run as upgrade_run
from coleto.commands.listar import run as listar_run
from coleto.commands.doctor import run as doctor_run
from coleto.commands.ayuda import run as ayuda_run

console = Console()


def buscar():
    package = console.input("[cyan]¿Qué paquete deseas buscar?[/cyan] ")
    buscar_run(package)


def instalar():
    package = console.input("[cyan]¿Qué paquete deseas instalar?[/cyan] ")
    instalar_run(package)


def eliminar():
    package = console.input("[cyan]¿Qué paquete deseas eliminar?[/cyan] ")
    eliminar_run(package)


def actualizar():
    actualizar_run()

def upgrade():
    upgrade_run()


def listar_instalados():
    listar_run("instalados")


def listar_actualizables():
    listar_run("actualizables")


def doctor():
    doctor_run()


def ayuda():
    ayuda_run()

ACTIONS = {
    "1": buscar,
    "2": instalar,
    "3": eliminar,
    "4": actualizar,
    "5": upgrade,
    "6": listar_instalados,
    "7": listar_actualizables,
    "8": doctor,
    "9": ayuda,
    #"0": salir,
}

def execute_action(option: str) -> None:
    action = ACTIONS.get(option)

    if action is None:
        console.print("[bold red]Opción no válida.[/bold red]")
        return

    action()