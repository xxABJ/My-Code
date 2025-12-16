import tkinter as tk

window = tk.Tk()
window.title("Moving Widgets with Events")
window.geometry("400x300")

label = tk.Label(window, text="Drag me around!", bg="lightblue", font=("Arial", 24))
label.place(x=150, y=130)

label2 = tk.Label(window, text="Right-click me!", bg="lightgreen", font=("Arial", 16))
label2.place(x=150, y=200)

def on_start_move(label, event):
    label.startX = event.x
    label.startY = event.y

def on_move(label, event):
    label.configure(relief="groove", bd=1, cursor="fleur")
    print(f"x: {label.winfo_x()}, y: {label.winfo_y()}")
    x = label.winfo_x() - label.startX + event.x
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)

def on_stop_move(label, event):
    label.configure(relief="flat", bd=0, cursor="arrow")

change_layer_order = [label, label2]
def bring_to_front(label_list):
    change_layer_order.remove(label_list)
    change_layer_order.append(label_list)
    for widget in change_layer_order:
        widget.lift()
    bring_to_front(label)(label)

label.bind("<Button-1>", lambda event: on_start_move(label, event))
label.bind("<ButtonRelease-1>", lambda event: on_stop_move(label, event))
label2.bind("<Button-1>", lambda event: on_start_move(label2, event))
label2.bind("<ButtonRelease-1>", lambda event: on_stop_move(label2, event))

label.bind("<B1-Motion>", lambda event: on_move(label, event))
label2.bind("<B1-Motion>", lambda event: on_move(label2, event))

label.bind("<Button-3>", lambda event: bring_to_front(label))
label2.bind("<Button-3>", lambda event: bring_to_front(label2))

def on_label_click(label, event):
    print(f"Label: {label.cget('text')} clicked!")
#label.bind("<Button-3>", lambda event: on_label_click(label, event))
#label2.bind("<Button-3>", lambda event: on_label_click(label2, event))

def on_key_press(event):
    print(f"Key pressed: {event.char}")
window.bind("<Key>", on_key_press)


window.mainloop()