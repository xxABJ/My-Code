
import sys

decor_left = "[["
decor_right = "]]"
buffer = "asdf"

# Print the frame and move cursor inside
sys.stdout.write(f"{decor_left}{' ' * 10}{decor_right}\r")  # Reserve space
sys.stdout.write(f"\033[{len(decor_left)+1}C")  # Move cursor inside brackets
sys.stdout.flush()

while True:

    ch = sys.stdin.read(1)  # Read one character
    if ch == "\n":  # Enter key
        break
    elif ch in ("\x7f", "\b"):  # Backspace
        buffer = buffer[:-1]
    else:
        buffer += ch

    if len(buffer) > 10:
        buffer = buffer[:10]
        continue

    # Redraw inside the brackets without moving cursor outside
    sys.stdout.write("\r" + f"{decor_left} {buffer}{decor_right}")
    sys.stdout.write(f"\033[{len(decor_left)+len(buffer)+1}C")  # Put cursor after typed text
    sys.stdout.flush()

print(f"\nYou typed: {buffer}")

#print(help(sys))