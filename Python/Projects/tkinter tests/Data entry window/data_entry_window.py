from imports import tk, ttk, messagebox

def confirm_submission():
    if terms_info_checkbutton_var.get() == 1:
        tk.messagebox.showinfo(title= "Submission Confirmed", message= "Thank you for your submission!")
    else:
        tk.messagebox.showwarning(title= "Terms Not Accepted", message= "You must agree to the terms and conditions before submitting.")

# Window
WINDOW = tk.Tk()
WINDOW.title("Sponsorship Data-Entry Template")

# Widgets

# Main frame
MAIN_FRAME = tk.Frame(master= WINDOW)
MAIN_FRAME.pack()

# Sub-label frames
USER_INFO_FRAME = tk.LabelFrame(master= MAIN_FRAME, text= "User Information")
CAREER_INFO_FRAME = tk.LabelFrame(master= MAIN_FRAME, text= "Career Information")
TERMS_INFO_FRAME = tk.LabelFrame(master= MAIN_FRAME, text= "Terms & Conditions")

USER_INFO_FRAME.grid(row= 0, column= 0, sticky= "news", padx= 10, pady= 10)
CAREER_INFO_FRAME.grid(row= 1, column= 0, sticky= "news", padx= 10, pady= 10)
TERMS_INFO_FRAME.grid(row= 2, column= 0, sticky= "news", padx= 10, pady= 10)

# User Information Labels and Entries
userinfo_title_label = tk.Label(master= USER_INFO_FRAME, text= "Title")
userinfo_title_combobox = ttk.Combobox(master= USER_INFO_FRAME, values= ["", "Mr.", "Ms.", "Mrs.", "Dr.", "Prof."])
userinfo_firstname_label = tk.Label(master= USER_INFO_FRAME, text= "First Name")
userinfo_firstname_entry = tk.Entry(master= USER_INFO_FRAME)
userinfo_lastname_label = tk.Label(master= USER_INFO_FRAME, text= "Last Name")
userinfo_lastname_entry = tk.Entry(master= USER_INFO_FRAME)
userinfo_age_label = tk.Label(master= USER_INFO_FRAME, text= "Age")
userinfo_age_spinbox = tk.Spinbox(master= USER_INFO_FRAME, from_= 18, to= 110)
userinfo_nationality_label = tk.Label(master= USER_INFO_FRAME, text= "Nationality")
userinfo_nationality_combobox = ttk.Combobox(master= USER_INFO_FRAME, values= ["", "Qatari", "Saudi", "Emirati", "Bahraini", "Omani", "Kuwaiti", "Other"])
userinfo_status_label = tk.Label(master= USER_INFO_FRAME, text= "Status")
userinfo_status_combobox = ttk.Combobox(master= USER_INFO_FRAME, values= ["", "Single", "Relationship", "Married", "Divorced"])

userinfo_title_label.grid(row= 0, column= 0)
userinfo_title_combobox.grid(row= 1, column= 0)
userinfo_firstname_label.grid(row= 0, column= 1)
userinfo_firstname_entry.grid(row= 1, column= 1)
userinfo_lastname_label.grid(row= 0, column= 2)
userinfo_lastname_entry.grid(row= 1, column= 2)
userinfo_age_label.grid(row= 2, column= 0)
userinfo_age_spinbox.grid(row= 3, column= 0)
userinfo_nationality_label.grid(row= 2, column= 1)
userinfo_nationality_combobox.grid(row= 3, column= 1)
userinfo_status_label.grid(row= 2, column= 2)
userinfo_status_combobox.grid(row= 3, column= 2)

for userinfo_wigdet in USER_INFO_FRAME.winfo_children():
    userinfo_wigdet.grid_configure(padx= 15, pady= 5)

# Career Information Labels and Entries
careerinfo_occupation_label = tk.Label(master= CAREER_INFO_FRAME, text= "Occupation")
careerinfo_occupation_entry = tk.Entry(master= CAREER_INFO_FRAME) 
careerinfo_employer_label = tk.Label(master= CAREER_INFO_FRAME, text= "Employer")
careerinfo_employer_entry = tk.Entry(master= CAREER_INFO_FRAME)
careerinfo_experience_label = tk.Label(master= CAREER_INFO_FRAME, text= "Years of Experience")
careerinfo_experience_spinbox = tk.Spinbox(master= CAREER_INFO_FRAME, from_= 0, to= 80)

careerinfo_occupation_label.grid(row= 0, column= 0)
careerinfo_occupation_entry.grid(row= 1, column= 0)
careerinfo_employer_label.grid(row= 0, column= 1)
careerinfo_employer_entry.grid(row= 1, column= 1)
careerinfo_experience_label.grid(row= 0, column= 2)
careerinfo_experience_spinbox.grid(row= 1, column= 2)

for careerinfo_widget in CAREER_INFO_FRAME.winfo_children():
    careerinfo_widget.grid_configure(padx= 15, pady= 5)

# Terms & Conditions Labels and Entries
terms_info_checkbutton_var = tk.IntVar()
terms_info_checkbutton = tk.Checkbutton(master= TERMS_INFO_FRAME, variable= terms_info_checkbutton_var, text= "I agree to the terms and conditions.")
terms_info_checkbutton.grid(row= 0, column= 0)

terms_info_confirm_button = tk.Button(master= MAIN_FRAME, text= "Confirm", command= confirm_submission)
terms_info_confirm_button.grid(row= 4, column= 0, sticky= "news", padx= 10, pady= 10)

for terms_info_widget in TERMS_INFO_FRAME.winfo_children():
    terms_info_widget.grid_configure(padx= 15, pady= 5)

# Main loop
WINDOW.mainloop()