import random, tkinter as tk
from tkinter import ttk 

letters = 'abcdefghijklmnopqrstuvwxyz'
Cletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Sletters = '!@#$%^&*()-_+?~'
numbers = '1234567890'

def generate_password() -> None:
    required_length = length_entry_str.get()
    if required_length.isdigit():
        error_label_str.set(value= '')
        
        pw = ""
        for letter in range(int(required_length)):
            random_letter1 = random.choice(letters)
            random_letter2 = random.choice(Cletters)
            random_letter3 = random.choice(Sletters)
            random_letter4 = random.choice(numbers)
            random_letter_variables = random_letter1, random_letter2, random_letter3, random_letter4
            random_letter_choice = random.choice(random_letter_variables)
            pw += random_letter_choice
        
        password_entry_str.set(value= pw)
    
    else:
        password_entry_str.set(value= "")
        error_label_str.set(value= 'MUST NOT BE EMPTY / A VALID NUMBER !')

PW_W = 475 ; PW_H = 200
PW_WINDOW = tk.Tk()
PW_WINDOW.title("Password Generator by ABJ")
PW_WINDOW.geometry(f"{PW_W}x{PW_H}")
PW_WINDOW.grid()

title = ttk.Label(
        master= PW_WINDOW,
        text= 'Password Generator !',
        font= "Arial 14 ",
        foreground = 'blue'
        ).grid(
          column= 1,
          row= 0,
           ipadx= 0,
           ipady= 0,
           padx= 10,
           pady= 20,
          )

length_label = ttk.Label(
         master= PW_WINDOW,
         text= "Length of PW",
         font= "Arial 14",
         foreground= "black"
         ).grid(
           column= 0,
           row= 1,
           ipadx= 0,
           ipady= 0,
           padx= 10,
           pady= 0,
           )

length_entry_str = tk.StringVar()
length_entry = ttk.Entry(
         master= PW_WINDOW,
         textvariable= length_entry_str,
         width= 10
         ).grid(
           column= 1,
           row= 1,
           ipadx= 0,
           ipady= 0,
           padx= 0,
           pady= 0,
           )

button_text = 'Generate'
generate_button = ttk.Button(
         master= PW_WINDOW,
         text= 'Generate',
         command= generate_password,
         width= 15
         ).grid(
           column= 2,
           row= 1,
           ipadx= 0,
           ipady= 0,
           padx= 0,
           pady= 0,
           )

password_entry_str = tk.StringVar()
password_entry = ttk.Entry(
         master= PW_WINDOW,
         textvariable= password_entry_str,
         width= 30
         ).grid(
           column= 1,
           row= 2,
           ipadx= 0,
           ipady= 0,
           padx= 0,
           pady= 20,
           )

error_label_str = tk.StringVar()
error_label = ttk.Label(
         master= PW_WINDOW,
         text= "",
         font= "Arial 8",
         foreground= "red",
         textvariable= error_label_str
         ).grid(
           column= 1,
           row= 3,
           ipadx= 0,
           ipady= 0,
           padx= 0,
           pady= 0,
           )

PW_WINDOW.mainloop()