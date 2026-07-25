from rich.console import Console

from coleto.commands.buscar import run as buscar_run
from coleto.commands.instalar import run as instalar_run
from coleto.commands.eliminar import run as eliminar_run
from coleto.commands.actualizar import run as actualizar_run
from coleto.commands.upgrade import run as upgrade_run
from coleto.commands.listar import run as listar_run
from coleto.commands.info import run as info_run
from coleto.commands.doctor import run as doctor_run
from coleto.commands.ayuda import run as ayuda_run
from coleto.commands.autoremove import run as autoremove_run
from coleto.commands.limpiar import run as limpiar_run

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

def info():
    package = console.input(
        "[cyan]¿De qué paquete deseas ver la información?[/cyan] "
    )

    info_run(package)


def doctor():
    doctor_run()

def autoremove():
    autoremove_run()

def limpiar():
    limpiar_run()

def ayuda():
    ayuda_run()

ACTIONS = {
    # Gestión de paquetes
    "1": buscar,
    "2": instalar,
    "3": eliminar,
    "4": info,

    # Mantenimineto
    "5": actualizar,
    "6": upgrade,
    "7": limpiar,
    "8": autoremove,

    # Consultas
    "9": listar_instalados,
    "10": listar_actualizables,
    "11": doctor,
    "12": ayuda,

    # "0": salir,
}

def execute_action(option: str) -> None:
    action = ACTIONS.get(option)

    if action is None:
        console.print("[bold red]Opción no válida.[/bold red]")
        return

    action()