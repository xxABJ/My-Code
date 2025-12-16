import tkinter as tk
from tkinter import ttk

# create a window
# add a title label
# add a textbox with a text label
# add a entry
# add a button that prints 'a button was pressed'
# add another textbox with a button thts prints hello
# add text label 'my label' should be between textbox and button

#functions
def button1():
    print('A button has been pressed!')
def button2():
    print('Hello')

#fonts
title_font = ("Calibri", 24, 'bold')
button1_font = ("Arial", 'italic')
button2_font = ("Impact", 'bold', 'italic')

#window
window = tk.Tk()
window.title("Windows and widgets !")
window.geometry("800x500")

#ttk title label
title = ttk.Label(master = window, text = 'Windows and Widgets !', font = title_font, foreground = 'red')
title.pack(pady = 5)

#ttk frame 1
frame1 = ttk.Frame(master = window)
frame1.pack(pady = 5)

#sidebar scroll
#scrollbar = tk.Scrollbar(master = window,frame1)
#scrollbar.pack()

#ttk text label
text1 = ttk.Label(master = frame1, text = 'This is a text label, which is over a textbox label "ttk.Text()"')
text1.pack()

#tk textbox
textbox1 = tk.Text(master = frame1)
textbox1.pack()

#ttk entry
entry1 = ttk.Entry(master = frame1)
entry1.pack(pady = 5)

#ttk text label 2 excercise
text2 = ttk.Label(master = frame1, text = 'my label')
text2.pack()

#ttk button 1
button1 = ttk.Button(master = frame1, text = 'Button 1', command = button1)
button1.pack(pady = 5)

#ttk button 2 excercise
button2 = ttk.Button(master = frame1, text = 'Excercise Button 2', command = button2)
button2.pack(pady = 5)

#run
window.mainloop()