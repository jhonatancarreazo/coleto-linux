from rich.table import Table
from rich.console import Console

console = Console()

def show_menu():
    table = Table(show_header=True)

    table.add_column("#", justify="center", style="cyan", width=4)
    table.add_column("Acción", style="white")

    table.add_row("1", "🔎 Buscar paquetes")
    table.add_row("2", "📦 Instalar un paquete")
    table.add_row("3", "🗑 Eliminar un paquete")
    table.add_row("4", "🔄 Actualizar paquetes")
    table.add_row("5", "📋 Ver paquetes instalados")
    table.add_row("6", "⬆ Ver paquetes actualizables")
    table.add_row("7", "💻 Información del sistema")
    table.add_row("8", "❓ Ayuda")

    table.add_section()
    
    table.add_row("0", "🚪 Salir")

    console.print(table)