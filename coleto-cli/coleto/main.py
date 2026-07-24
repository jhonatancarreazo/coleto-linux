import typer


from rich.console import Console
from coleto.ui.banner import get_banner
from coleto.commands.buscar import run as buscar_run
from coleto.commands.doctor import run as doctor_run
from coleto.commands.instalar import run as install_run
from coleto.commands.eliminar import run as remove_run

app = typer.Typer(
    help="Coleto Linux CLI"
)

console = Console()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        console.print(get_banner())
        console.print()
        console.print("[yellow]Escribe:[/yellow] coleto --help")

@app.command(name="doctor")
def doctor_cmd():
    """Muestra información del sistema."""
    doctor_run()

@app.command()
def buscar(query: str):
    """Busca paquetes disponibles"""
    buscar_run(query)

@app.command("instalar")
def instalar(package: str):
    """
    Instala un paquete.
    """
    install_run(package)

@app.command("eliminar")
def eliminar(package: str):
    """
    Elimina un paquete instalado
    """
    remove_run(package)

if __name__ == "__main__":
    app()