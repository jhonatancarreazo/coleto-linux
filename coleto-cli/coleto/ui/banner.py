from rich.panel import Panel

def get_banner():
    return Panel.fit(
        "[bold cyan]🐧 Coleto Linux[/bold cyan]\n\n"
        "[green]Ligero, bacano y estable.[/green]\n\n"
        "[white] Qué hacemos hoy, Causa?[/white]",
        border_style="cyan",
    )