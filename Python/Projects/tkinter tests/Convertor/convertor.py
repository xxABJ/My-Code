import tkinter as tk
from tkinter import ttk,font

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

window = tk.Tk()
window.title("Convertor")
window.geometry("400x800")

italic_font = ("Calibri", 10, 'italic')
normal_font = ("Calibri", 10)
answer_font = ("Impact", 16)

#main title
main_title_label = ttk.Label(master = window, text = "The convertor!", font = 'Calibri 24 bold')
main_title_label.pack(pady = 10)

#input frame 1 (miles to km)
input_frame1 = ttk.Frame(master = window)
input_frame1.pack(pady = 5)

#title (miles to km)
title1_label = ttk.Label(master = input_frame1, text = "(miles  ->  km)", font = 'Calibri 14')
title1_label.pack(side = "left", padx = 10)

#entry (miles to km)
entry_int = tk.IntVar()
entry = tk.Entry(master = input_frame1, font = italic_font, textvariable = entry_int, foreground = "grey")
entry.pack(side = "left")

#button (miles to km)
button_text_frame1 = "Convert!"
button = ttk.Button(master = input_frame1, text = button_text_frame1, command = convert)
button.pack(side = "left", padx = 5)

#output (miles to km)
output_string = tk.StringVar()
output = ttk.Label(master = window, font = answer_font, textvariable = output_string, foreground = "green")
output.pack(pady = 5)


#input frame 2 (cm to in)
input_frame2 = ttk.Frame(master = window)
input_frame2.pack(pady = 5)

#title (cm to in)
title2_label = ttk.Label(master = input_frame2, text = "(cm  ->  in)", font = 'Calibri 14')
title2_label.pack(side = "left", padx = 10)
#entry (cm to in)
#button (cm to in)
#output (cm to in)

#title (hours to seconds)
#input frame 3 (hours to seconds)
#entry (hours to seconds)
#button (hours to seconds)
#output (hours to seconds)

#run

#def main():
#    for i in packing:
#        compile
#    window.mainloop()
#
#main()

window.mainloop()