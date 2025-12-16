import tkinter as tk
from tkinter import ttk

def checkbutton2_func():
    input_bool = checkbutton2_var.get()
    return "ticked" if input_bool else "not ticked"

def radiobutton_func():
    input_int = radiobutton_var.get()
    return f'Radio button {input_int} has been selected!'

#window
window = tk.Tk()
window.title("Check buttons and buttons !")
window.geometry("400x400")

#button
button1 = ttk.Button(
    window,
    text = "This is a button!",
    command = lambda: print("A button has been pressed!")
)
button1.pack()

#checkbutton
checkbutton1_var = tk.StringVar()
checkbutton1 = ttk.Checkbutton(
    window,
    text = "Check button 1",
    variable = checkbutton1_var,
    onvalue = "Checkbutton 1 is ticked!",
    offvalue = "Checkbutton 1 is NOT ticked!",
    command = lambda: print(checkbutton1_var.get()),
)
checkbutton1.pack()

checkbutton2_var = tk.BooleanVar()
checkbutton2 = ttk.Checkbutton(
    window,
    text = "Check button 2",
    variable = checkbutton2_var,
    command = lambda: print(f"Checkbutton 2 is {checkbutton2_var.get()} which means it is {checkbutton2_func()}!")
)
checkbutton2.pack()

#radiobutton
radiobutton_var = tk.IntVar()
radiobutton1 = ttk.Radiobutton(
    window,
    text = "Radio button 1",
    value = 1,
    variable = radiobutton_var,
    command = lambda: print(radiobutton_func())
)
radiobutton1.pack()

radiobutton2 = ttk.Radiobutton(
    window,
    text = "Radio button 2",
    value = 2,
    variable = radiobutton_var,
    command = lambda: print(radiobutton_func())
)
radiobutton2.pack()

radiobutton3 = ttk.Radiobutton(
    window,
    text = "Radio button 3",
    value = 3,
    variable = radiobutton_var,
    command = lambda: print(radiobutton_func())
)
radiobutton3.pack()

#run
window.mainloop()