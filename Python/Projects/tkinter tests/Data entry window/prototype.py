import tkinter as tk
from tkinter import ttk

class PrototypeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Prototype Application")
        self.root.geometry("500x400")

        self.create_widgets_menu()

    def create_widgets_menu(self):
        menubar = tk.Menu(self.root)
        widgets_menu = tk.Menu(menubar, tearoff=0)
        widgets_menu.add_command(label="Add Editable Button", command=self.add_editable_button)
        widgets_menu.add_command(label="Add Movable Label", command=self.add_movable_label)
        menubar.add_cascade(label="Widgets", menu=widgets_menu)
        self.root.config(menu=menubar)
    def add_editable_button(self):
        button = tk.Button(self.root, text="Editable Button", bg="lightcoral", font=("Arial", 16))
        button.pack(pady=10)
        button.bind("<Button-3>", lambda event: self.edit_button(event, button))
        button.edit_icon_button = None
    def edit_button(self, event, button):
        if button.edit_icon_button is None:
            edit_icon = tk.PhotoImage(file="edit.png").subsample(20, 20)
            button.edit_icon_button = tk.Button(button.master, image=edit_icon, height=20, width=20, relief="flat", bg="white", borderwidth=0)
            button.edit_icon_button.image = edit_icon  # Keep a reference
            x = button.winfo_x() + button.winfo_width() - 20
            y = button.winfo_y() + button.winfo_height()
            button.edit_icon_button.place(x=x, y=y)
            print("Edit icon added.")
        else:
            button.edit_icon_button.destroy()
            button.edit_icon_button = None
            print("Edit icon removed.")
    def add_movable_label(self):
        label = tk.Label(self.root, text="Drag me around!", bg="lightblue", font=("Arial", 24))
        label.place(x=150, y=130)

        label.bind("<Button-1>", lambda event: self.on_start_move(label, event))
        label.bind("<ButtonRelease-1>", lambda event: self.on_stop_move(label, event))
        label.bind("<B1-Motion>", lambda event: self.on_move(label, event))
    def on_start_move(self, label, event):
        label.startX = event.x
        label.startY = event.y
    def on_move(self, label, event):
        label.configure(relief="groove", bd=1, cursor="fleur")
        x = label.winfo_x() - label.startX + event.x
        y = label.winfo_y() - label.startY + event.y
        label.place(x=x, y=y)
    def on_stop_move(self, label, event):
        label.configure(relief="flat", bd=0, cursor="arrow")


if __name__ == "__main__":
    root = tk.Tk()
    app = PrototypeEditor(root)
    root.mainloop()
