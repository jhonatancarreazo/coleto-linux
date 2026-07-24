from rich.panel import Panel
from rich.text import Text

from coleto import __version__


def get_banner():
    text = Text()

    # Título principal
    text.append(f"🐧 Coleto Linux v{__version__}\n", style="bold cyan")
    text.append("\n")
    # Tu nuevo lema oficial con las viñetas
    text.append("Ligero • Bacano • Estable\n", style="green")
    text.append("\n")
    # Identidad técnica del sistema
    text.append("Una distribución bien montada, basada en Debian.\n", style="magenta")
    text.append("\n")
    text.append("\n")
    # Instrucción de inicio
    text.append("Escribe el comando ", style="yellow")
    text.append("coleto ayuda", style="bold cyan")
    text.append(" para que te dejes guiar.", style="yellow")

    return Panel(
        text,
        border_style="cyan",
        expand=False,
    )
