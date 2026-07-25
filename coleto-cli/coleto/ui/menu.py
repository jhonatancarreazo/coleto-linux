from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()




def show_menu() -> None:

    table = Table(
        show_header=True,
        header_style="bold white",
        border_style="bright_white",
        expand=False,
    )

    table.add_column("#", justify="center", style="bold cyan", width=4)
    table.add_column("Acción", style="bold")

    # ==========================
    # Gestión de paquetes
    # ==========================

    table.add_row(
    "",
    Panel.fit(
        "[bold cyan]📦 Gestión de paquetes[/bold cyan]",
        border_style="cyan",
        padding=(0, 1),
    ),
    )

    table.add_row("1", "🔎 Buscar paquetes")
    table.add_row("2", "📥  Instalar un paquete")
    table.add_row("3", "🗑️  Eliminar un paquete")
    table.add_row("4", "ℹ️  Información de un paquete")

    table.add_section()

    # ==========================
    # Mantenimiento
    # ==========================

    table.add_row(
    "",
    Panel.fit(
        "[bold yellow]🔧 Mantenimiento[/bold yellow]",
        border_style="yellow",
        padding=(0, 1),
    ),
   )

    table.add_row("5", "🔄 Actualizar repositorios")
    table.add_row("6", "⬆️  Actualizar paquetes")
    table.add_row("7", "🧹 Limpiar caché")
    table.add_row("8", "✔ Eliminar dependencias")

    table.add_section()

    # ==========================
    # Consultas
    # ==========================

    table.add_row(
    "",
    Panel.fit(
        "[bold green]📋 Consultas[/bold green]",
        border_style="green",
        padding=(0, 1),
    ),
  )

    table.add_row("9", "📦 Ver instalados")
    table.add_row("10", "⬆️ Ver  actualizables")
    table.add_row("11", "💻 Información del sistema")
    table.add_row("12", "❓ Ayuda")

    table.add_section()

    # ==========================
    # Salir
    # ==========================

    table.add_row("0", "🚪 Salir")

    console.print(table)