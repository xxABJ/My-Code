import tkinter as tk


def edit(event, edit_icon):
    # indicator for an icon is already present
    button = event.widget
    if not button_bool:
        # create new button with the edit icon
        edit_icon_button = tk.Button(button.master, image=edit_icon, height=20, width=20, relief="flat", bg="white", borderwidth=0)
        edit_icon_button.pack(pady=10)
        # place new button at bottom right of the original button - adjust as much as the size of the icon
        x = button.winfo_x() + button.winfo_width() - 20
        y = button.winfo_y() + button.winfo_height()
        edit_icon_button.place(x=x, y=y)
        button_bool = True
        print("Edit icon added.")
        # store reference to the edit icon button in the original button
    else:
        print("Edit icon already present or no button found.")
        # delete the edit icon button if clicked anywhereoutside the button area
        if hasattr(button, 'edit_icon_button'):
            button.edit_icon_button.destroy()
            del button.edit_icon_button

    






    
    


window = tk.Tk()
window.title("Edible Buttons")
window.geometry("400x300")

edit_icon = tk.PhotoImage(file="edit.png")  # Load your edit icon image here
edit_icon = edit_icon.subsample(20, 20)  # Resize if necessary

button1 = tk.Button(window, text="editable button", bg="lightcoral", font=("Arial", 16))
button1.pack(pady=20)

button1.bind("<Button-3>", lambda event: edit(event, edit_icon)) # right-click event

window.mainloop()
