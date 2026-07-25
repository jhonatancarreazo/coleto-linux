from rich.console import Console

from coleto.ui.banner import get_banner

console = Console()


def run() -> None:
    console.print(get_banner())
    console.print()

    console.print("[bold cyan]📦 Gestión de paquetes[/bold cyan]")
    console.print("  buscar <paquete>              Buscar paquetes")
    console.print("  instalar <paquete>            Instalar un paquete")
    console.print("  eliminar <paquete>            Eliminar un paquete")
    console.print("  info <paquete>                Mostrar información de un paquete")
    console.print("  listar instalados             Listar paquetes instalados")
    console.print("  listar actualizables          Listar paquetes actualizables")

    console.print()

    console.print("[bold cyan]🛠 Mantenimiento[/bold cyan]")
    console.print("  actualizar                    Actualizar la lista de paquetes")
    console.print("  upgrade                       Actualizar los paquetes instalados")
    console.print("  autoremove                    Eliminar dependencias innecesarias")
    console.print("  clean                         Limpiar la caché de paquetes")

    console.print()

    console.print("[bold cyan]🖥 Sistema[/bold cyan]")
    console.print("  doctor                        Información del sistema")

    console.print()

    console.print("[bold cyan]💡 Ejemplos[/bold cyan]")
    console.print("  coleto buscar firefox")
    console.print("  coleto info firefox")
    console.print("  coleto instalar fastfetch")
    console.print("  coleto eliminar nano")
    console.print("  coleto actualizar")
    console.print("  coleto upgrade")
    console.print("  coleto autoremove")
    console.print("  coleto clean")
    console.print("  coleto listar instalados")
    console.print("  coleto doctor")

    console.print()
    console.print("[yellow]También puedes ejecutar:[/yellow] [bold]coleto[/bold]")
    console.print("para abrir el menú interactivo.")