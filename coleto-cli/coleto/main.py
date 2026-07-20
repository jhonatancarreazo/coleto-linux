import typer
from rich.console import Console

from coleto.ui.banner import get_banner

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


if __name__ == "__main__":
    app()