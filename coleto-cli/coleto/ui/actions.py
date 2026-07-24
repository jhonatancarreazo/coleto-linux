from rich.console import Console

from coleto.commands.buscar import run as buscar_run
from coleto.commands.instalar import run as instalar_run
from coleto.commands.eliminar import run as eliminar_run
from coleto.commands.actualizar import run as actualizar_run
from coleto.commands.listar import run as listar_run
from coleto.commands.doctor import run as doctor_run
from coleto.commands.ayuda import run as ayuda_run

console = Console()


def execute(option: int) -> None:

    actions = {
        1: search,
        2: install,
        3: remove,
        4: update,
        5: list_installed,
        6: list_upgradable,
        7: doctor,
        8: help_menu,
    }

    action = actions.get(option)

    if action:
        action()


def search():
    query = console.input("\nPaquete a buscar: ")
    buscar_run(query)


def install():
    package = console.input("\nPaquete a instalar: ")
    instalar_run(package)


def remove():
    package = console.input("\nPaquete a eliminar: ")
    eliminar_run(package)


def update():
    actualizar_run()


def list_installed():
    listar_run("instalados")


def list_upgradable():
    listar_run("actualizables")


def doctor():
    doctor_run()


def help_menu():
    ayuda_run()