
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.styles import Style
import textwrap

def ascii_box_input(prompt="Enter text: ", width=40):
    buffer = ""

    # Key bindings
    kb = KeyBindings()

    @kb.add("enter")
    def _(event):
        event.app.exit(result=buffer)

    @kb.add("backspace")
    def _(event):
        nonlocal buffer
        if buffer:
            buffer = buffer[:-1]
        event.app.invalidate()

    @kb.add("<any>")
    def _(event):
        nonlocal buffer
        char = event.data
        if char and char != "\n":  # Ignore Enter
            buffer += char
        event.app.invalidate()

    # Dynamic box rendering
    def get_text():
        wrapped = textwrap.wrap(buffer, width)
        box_width = width + 2
        box_lines = ["+" + "-" * box_width + "+"]
        for line in wrapped or [""]:
            box_lines.append("| " + line.ljust(width) + " |")
        box_lines.append("+" + "-" * box_width + "+")
        return [("", prompt + "\n" + "\n".join(box_lines))]  # ✅ Use empty string instead of None

    root_container = HSplit([Window(content=FormattedTextControl(get_text))])
    layout = Layout(root_container)
    style = Style.from_dict({"": "#064206"})  # Green text

    app = Application(layout=layout, key_bindings=kb, style=style, full_screen=False)
    return app.run()

# Example usage:
if __name__ == "__main__":
    text = ascii_box_input("Type your message (Enter to finish): ", width=30)
    print("\nFinal input:\n", text)
