import tkinter as tk

window = tk.Tk()
window.title("testing")

frame1 = tk.Frame(window)
frame1.pack(padx=10, pady=10)

text = tk.Text(frame1, height=10, width=40)
text.pack()

window.bind("<Shift-KeyPress>", lambda event: print(f"Mousewheel"))
text.bind("<FocusIn>"+"<MouseWheel>", lambda event: print("Text widget focused and mouse wheel used"))

frame2 = tk.Frame(window)
frame2.pack(padx=10, pady=10)

entry = tk.Entry(frame2)
entry.pack()



window.mainloop()