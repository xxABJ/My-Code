import tkinter as tk
from tkinter import ttk

def small_to_capital():
    entry_input = entry.get()
    #print(entry_input.upper())
    output_str.set(entry_input.upper())

#window
main = tk.Tk()
main.title("testing the window")
main.geometry("400x200")

title_font = 'Arial 25 bold'

#title
title = ttk.Label(master = main, text = 'This is a test', font = title_font, foreground = 'Red')
title.pack(pady = 5)

#frame1
frame1 = ttk.Frame(master = main)
frame1.pack(pady = 5)

#entry
entry_str = tk.StringVar()
entry = ttk.Entry(master = frame1, textvariable = entry_str)
entry.pack(side = 'left')

#button
button = ttk.Button(master = frame1, text = 'Convert', command = small_to_capital)
button.pack(side = 'left', padx = 10)

#frame2
frame2 = ttk.Frame(master = main)
frame2.pack(pady = 5)

#output
output_str = tk.StringVar()
output = ttk.Label(master = frame2, textvariable = output_str)
output.pack(pady = 5)

#run
main.mainloop()