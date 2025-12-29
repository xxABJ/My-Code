
import sys
import textwrap

def ascii_box_input(prompt="Enter text: ", width=40):
    buffer = ""
    print(prompt)
    while True:
        ch = sys.stdin.read(1)
        if ch == "\n":
            break
        elif ch == "\x7f":  # Backspace
            buffer = buffer[:-1]
        else:
            buffer += ch

        # Clear screen and redraw
        print("\033[H\033[J", end="")  # ANSI clear
        print(prompt)
        wrapped = textwrap.wrap(buffer, width)
        box_width = width + 2
        print("+" + "-" * box_width + "+")
        for line in wrapped or [""]:
            print("| " + line.ljust(width) + " |")
        print("+" + "-" * box_width + "+")

    return buffer

if __name__ == "__main__":
    text = ascii_box_input("Type your message (Enter to finish): ", width=30)
    print("\nFinal input:\n", text)
