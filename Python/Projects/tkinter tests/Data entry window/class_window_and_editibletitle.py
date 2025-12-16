from imports import tk, ttk

class root_window_class:
    def __init__(self, root_window_title="No Title Provided"):
        self.root_window_variable = tk.Tk()
        self.root_window_variable.geometry("400x300")
        self.root_window_title = root_window_title
        self.root_window_variable.wm_geometry

        self.root_window_MAINFRAME = tk.Frame(self.root_window_variable)
        self.root_window_MAINFRAME.pack()

        self.root_window_SECONDARYFRAME = tk.Frame(self.root_window_variable)
        self.root_window_SECONDARYFRAME.pack()

    def create_root_window(self):
        self.root_window_variable.title(self.root_window_title)
        self.label1 = tk.Label(self.root_window_MAINFRAME, text="This is the root window")
        self.label1.grid(row=0, column=0, pady=10)
        self.label2 = tk.Label(self.root_window_MAINFRAME, text=f"root_window variable: {self.root_window_variable}")
        self.label2.grid(row=1, column=0, pady=10)
        self.label3 = tk.Label(self.root_window_MAINFRAME, text=f"root_window title: {self.root_window_title}")
        self.label3.grid(row=2, column=0, pady=10)
        
        self.change_root_title_button()

    def start_root_window(self):
        self.create_root_window()
        self.root_window_variable.mainloop()

    def change_root_title_button(self):
        def change_root_title():
            new_title = change_title_entry_var.get()
            print("Changing root title to:", new_title)
            #self.new_root_window(new_title)
            self.root_window_variable.wm_title(new_title)

        change_title_entry_var = tk.StringVar()
        change_title_entry = tk.Entry(self.root_window_MAINFRAME, textvariable=change_title_entry_var)
        change_title_button = tk.Button(self.root_window_MAINFRAME, text="Change Root Title", command=change_root_title)
        change_title_entry.grid(row=3, column=0, pady=10)
        change_title_button.grid(row=4, column=0, pady=10)


    def new_root_window(self, new_root_title):
        self.root_window_variable.destroy()
        root(new_root_title)
        #root(f"(New Root) {new_root_title}")

def root(root_window_title=False):
    if not root_window_title:
        root_window_instance = root_window_class()
    else:
        root_window_instance = root_window_class(root_window_title)

    root_window_instance.start_root_window()

root()