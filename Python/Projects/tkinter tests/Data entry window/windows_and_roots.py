from imports import tk, ttk

def newroot_window():
    window_destroy()
    new_root = tk.Tk()
    new_root.title("New Root Window")
    label = ttk.Label(new_root, text="This is a new root window")
    label.pack(pady=20, padx=20)
    new_root.mainloop()

def window_destroy():
    root.destroy()

def toplevel_window():
    top = tk.Toplevel()
    top.title("New Window")
    change_window_button = tk.Button(top, text="open new root window (root.destroy and new root example)", command=newroot_window)
    change_window_button.pack(pady=20, padx=20)
    
    #label = ttk.Label(top, text="This is a new window")
    #label.pack(pady=20, padx=20)

def open_toplevel_window_withdraw():
    root.withdraw()
    toplevel_window()
    #root.wm_deiconify()

root = tk.Tk()
root.title("Login Window")

withdrawn_button = tk.Button(root, text="open toplevel window (withdraw)", command=open_toplevel_window_withdraw)
withdrawn_button.pack()

root.mainloop()
#root.withdraw()  # Hide the root window