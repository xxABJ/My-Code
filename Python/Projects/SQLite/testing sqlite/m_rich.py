
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()
decor_left = "[[ "
decor_right = " ]]"
buffer = ""

with Live(refresh_per_second=1) as live:
    chars = 5
    old_ch = ""
    while len(buffer) < chars:
        ch = input()  # Capture full input at once (simpler)
        buffer = ch
        text = Text()
        text.append(decor_left, style="bold cyan")
        if old_ch != ch:
            buffer = old_ch + ch
            text.append(buffer, style="bold green")
        else:
            text.append(buffer, style="bold green")
        text.append(decor_right, style="bold cyan")
        live.update(text)
        ch += old_ch

        break  # Exit after one input for simplicity

console.print(f"\nYou typed: [bold green]{buffer}[/bold green]")