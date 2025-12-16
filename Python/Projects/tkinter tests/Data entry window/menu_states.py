import tkinter as tk

def show_frame(frame_to_show):
    # Hide all frames first
    for frame in frames:
        frame.pack_forget()
    # Show the selected frame
    frame_to_show.pack(fill="both", expand=True)

root = tk.Tk()
root.geometry("400x300")
root.title("Tkinter Menu States")

# Create frames
main_menu = tk.Frame(root, bg="lightblue")
settings_menu = tk.Frame(root, bg="lightgreen")

frames = [main_menu, settings_menu]

# Main Menu widgets
tk.Label(main_menu, text="Main Menu", font=("Arial", 18)).pack(pady=20)
tk.Button(main_menu, text="Go to Settings", command=lambda: show_frame(settings_menu)).pack()

# Settings Menu widgets
tk.Label(settings_menu, text="Settings", font=("Arial", 18)).pack(pady=20)
tk.Button(settings_menu, text="Back to Main", command=lambda: show_frame(main_menu)).pack()

# Show initial frame
show_frame(main_menu)

root.mainloop()
