import tkinter as tk
from tkinter import ttk

def pad(y, x):
    return {"pady":y, "padx":x}
def alignment(side):
    return {"side":side}
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = tk.Tk()
window.title("Miles to Kilometers!")
window.geometry("300x150")

#title
title_label = ttk.Label(master = window, text = 'Type in a value: (Miles)' , font = 'Courier 12 bold')
title_label_pad = pad(20,0)
#title_label_alignment = {"side":"left"}
title_label_packing = title_label_pad
#title_label.pack(pady = 10)

#input
input_frame = ttk.Frame(master = window)
input_pad = pad(5,0)
input_packing = input_pad

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
entry_pad = pad(5,5)
entry_alignment = alignment("left")
entry_packing = entry_pad,entry_alignment

button = ttk.Button(master = input_frame, text = "Convert!", command = convert)
button_pad = pad(5,0)
button_alignment = alignment("left")
button_packing = button_pad,button_alignment
#entry.pack()
#button.pack()
#input_frame.pack()

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'insert_output_here', font = 'Courier 8', textvariable = output_string)
output_pad = pad(10,0)
output_packing = output_pad
#output_label.pack()

packing = {
    "title": title_label.pack(title_label_packing),
    "input": input_frame.pack(input_packing),
    "entry": entry.pack(entry_packing),
    "button": button.pack(button_packing),
    #"input": input_frame.pack(input_packing),
    "output": output_label.pack(output_packing)
    }

#run

def main():     
    for i, v in enumerate(packing):
        v = compile
    window.mainloop()

main()