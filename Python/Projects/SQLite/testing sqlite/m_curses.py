
import curses
import textwrap

def ascii_box_input(prompt="Enter text: ", width=40):
    """
    Interactive input inside a dynamic ASCII box using curses.
    :param prompt: Prompt displayed at the top.
    :param width: Max width before wrapping text.
    :return: Final input string.
    """
    def _input_loop(stdscr):
        curses.curs_set(1)
        stdscr.clear()
        buffer = ""

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, prompt)

            # Wrap text and build box
            wrapped = textwrap.wrap(buffer, width)
            box_width = width + 2
            box_lines = ["+" + "-" * box_width + "+"]
            for line in wrapped or [""]:
                box_lines.append("| " + line.ljust(width) + " |")
            box_lines.append("+" + "-" * box_width + "+")

            # Display box
            for i, line in enumerate(box_lines, start=2):
                stdscr.addstr(i, 0, line)

            stdscr.refresh()

            key = stdscr.get_wch()
            if isinstance(key, str) and key == "\n":  # Enter key
                break
            elif key in (curses.KEY_BACKSPACE, '\b', '\x7f'):
                buffer = buffer[:-1]
            elif isinstance(key, str):
                buffer += key

        return buffer

    return curses.wrapper(_input_loop)

# Example usage:
if __name__ == "__main__":
    text = ascii_box_input("Type your message (Enter to finish): ", width=30)
    print("\nFinal input:\n", text)
