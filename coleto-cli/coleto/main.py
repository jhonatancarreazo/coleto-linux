import typer

from coleto.interactive import run as interactive_run

from coleto.commands.buscar import run as buscar_run
from coleto.commands.doctor import run as doctor_run
from coleto.commands.instalar import run as install_run
from coleto.commands.eliminar import run as remove_run
from coleto.commands.actualizar import run as update_run
from coleto.commands.upgrade import run as upgrade_run
from coleto.commands.listar import run as list_run
from coleto.commands.info import run as info_run
from coleto.commands.ayuda import run as ayuda_run
from coleto.commands.autoremove import run as autoremove_run
from coleto.commands.limpiar import run as limpiar_run

app = typer.Typer(
    help="Coleto Linux CLI"
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
    
        interactive_run()    
    

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

@app.command("actualizar")
def actualizar():
    """
    Actualizar la lista de paquetes.
    """
    update_run()

@app.command("upgrade")
def upgrade():
    """
    Actualiza todos los paquetes instalados.
    """
    upgrade_run()

@app.command("listar")
def listar(
    tipo: str,
    buscar: str | None = None,
    limitar: int = 20,
    ):
    """
    Lista paquetes del sistema.
    """
    list_run(tipo, buscar, limitar)


@app.command("autoremove")
def autoremove():
    """
    Elimina dependencias que ya no son necesarias.
    """
    autoremove_run()

@app.command("limpiar")
def clean():
    """
    Limpia la caché de paquetes.
    """
    limpiar_run()


@app.command("ayuda")
def ayuda():
    """
    Muestra la ayuda de Coleto.
    """
    ayuda_run()

@app.command("info")
def info(package: str):
    """
    Muestra información detallada de un paquete.
    """
    info_run(package)
   

   
if __name__ == "__main__":
    app()