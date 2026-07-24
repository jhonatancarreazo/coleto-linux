from rich.console import Console

from coleto.services.packages import install_package

console = Console()


def run(package: str) -> None:
    console.print(f"📦 Instalando [cyan]{package}[/cyan]...\n")

    success = install_package(package)

    if success:
        console.print(
            f"[bold green]✓ {package} instalado correctamente.[/bold green]"
        )
    else:
        console.print(
            f"[bold red]✗ Joa... No fue posible instalar  {package}.[/bold red]"
        )