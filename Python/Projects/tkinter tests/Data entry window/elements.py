# TODO: Resturcture this file to be more convienent and consistent for reading and writing element properties

elements = { #TODO: Create a template for json file structure
    "frame_1_frame": [ # Frame properties (one dictionary inside a list)
        {"Frame":"frame",
        "master": "self.window_variable", #TODO: automate master assignment variable
        "bg": "green"
        }],
    #"frame_2_frame": [ # Frame properties (one dictionary inside a list)
    #    {"Frame":"frame",
    #    "master": "self.window_variable", #TODO: automate master assignment variable
    #    "bg": "lightgreen"
    #    }],

    "frame_1_widgets": [ # Widgets inside frame (list of dictionaries)
        {"Widgets": [ #TODO: seperate each widget into its own list of dictionarys
            {"Label":"label_title",
            "text": "LOGIN FORM",
                "font": "Arial",
                    "size": "24",
                        "row": 0, "column": 0,
                            "padx": 10, "pady": 10},
            {"Label":"label_username",
            "text": "Username:",
                "font": "Arial",
                    "size": "12",
                        "row": 1, "column": 0,
                            "padx": 5, "pady": 10},
            {"Entry":"entry_username",
            "text": "",
                "row": 2, "column": 0,
                    "padx": 0, "pady": 10},
            {"Label":"label_password",
            "text": "Password:",
                "font": "Arial",
                    "size": "12",
                        "row": 3, "column": 0,
                            "padx": 5, "pady": 10},
            {"Entry":"entry_password",
            "text": "",
                "row": 4, "column": 0,
                    "padx": 0, "pady": 10},
            {"Button":"button_forward",
            "text": "Submit", #TODO: add command later
                "row": 5, "column": 0,
                    "padx": 10, "pady": 10},
        ],
        #"Transitions": { # Frame transitions (one dictionary inside a list)
        #    "to_frame": "frame_2_frame",
        #    "on_event": "button_forward_click" #TODO: define event types
        #},

        },
    ],
}

#TODO: Schetch out functions needed to manipulate this file
#TODO: Create functions to read and write to this file
#TODO: Create functions to convert between json and python dictionary
#TODO: Create functions to add, remove, and edit elements in this file
