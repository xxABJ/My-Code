import tkinter as tk
from tkinter import ttk

def button():
    output['text'] = string_var.get()

#window
window = tk.Tk()
window.title("dynamic string variables")
window.geometry("300x300")

# tk string variable
string_var = tk.StringVar(value = "Test")

#widgets
label = ttk.Label(master = window, textvariable = string_var)
label.pack(pady = 10)

entry = ttk.Entry(master = window, textvariable = string_var,)
entry.pack(pady = 5)

button = ttk.Button(master = window, text = 'Button!', command = button)
button.pack(pady = 5)

output = ttk.Label(master = window, text = "", font = "Impact 30 bold", foreground = "red")
output.pack(pady = 10)

#run
window.mainloop()