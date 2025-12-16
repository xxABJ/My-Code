from imports import tk, ttk, messagebox, lbry

class dynamic_root_window_frames:
    def __init__(self, window_title="No Title"):
        self.window_variable = tk.Tk()
        self.window_variable.geometry("800x600")
        self.window_title = window_title
        self.window_variable.title(self.window_title)

        self.property_list = library_extractor().property_list
        #print(f"property_list:\n{self.property_list[0]}\n\n{self.property_list[1]}\n")

    def create_window(self):
        property_list = self.property_list[:]
        #print(property_list[0])
        #print()
        #print(property_list[1])

        active_frame = []
        for property in property_list:
            if property[0][0] == "Frame":
                for frame in property:
                    frame_type = frame[0]
                    frame_props = {}
                    for prop in frame[1:]:
                        key = prop[0]
                        value = prop[1]
                        frame_props[key] = value
                    print(f"Creating frame with properties: {frame_props}\n")
                    frame = tk.Frame(master=frame_props.get("master"), bg=frame_props.get("bg"))
                active_frame.append(frame)
            
            elif property[0] == "Widgets":
                for widget in property[1:]:
                    print(f"widget: {widget}")
                    widget_type = widget[0][0]
                    widget_props = {}
                    for prop in widget[1]:
                        key = prop[0]
                        value = prop[1]
                        widget_props[key] = value
                    
                    print(f"Creating widget of type '{widget_type}' with properties: {widget_props}\n")
                    # Here you can add code to create the widget based on widget_type and widget_props
                    
                    if widget_type == "Label":
                        label = tk.Label(active_frame[0], text=widget_props.get("text"), font=(widget_props.get("font"), widget_props.get("size")))
                        label.grid(row=widget_props.get("row"), column=widget_props.get("column"), padx=widget_props.get("padx"), pady=widget_props.get("pady"))
                    elif widget_type == "Entry":
                        if not widget[0][1] == "entry_password":
                            entry = tk.Entry(active_frame[0])
                            entry.grid(row=widget_props.get("row"), column=widget_props.get("column"), padx=widget_props.get("padx"), pady=widget_props.get("pady"))
                        else:
                            entry = tk.Entry(active_frame[0], show="*")
                            entry.grid(row=widget_props.get("row"), column=widget_props.get("column"), padx=widget_props.get("padx"), pady=widget_props.get("pady"))
                    elif widget_type == "Button":
                        if not widget[0][1] == "button_forward":
                            button = tk.Button(active_frame[0], text=widget_props.get("text"))
                            button.grid(row=widget_props.get("row"), column=widget_props.get("column"), padx=widget_props.get("padx"), pady=widget_props.get("pady"))
                        else:
                            button = tk.Button(active_frame[0], text=widget_props.get("text"), command=lambda: messagebox.showinfo("Info", "Submit button clicked!"))
                            button.grid(row=widget_props.get("row"), column=widget_props.get("column"), padx=widget_props.get("padx"), pady=widget_props.get("pady"))

            #self.window_variable.update_idletasks()
        active_frame[0].pack(pady=20)

    def start_window(self):
        self.create_window()

        #print(f"frame: {self.window_variable.winfo_geometry()}\n")
        #print(f"{self.window_variable.wm_geometry(f'{self.window_variable.winfo_screenwidth()-500}x{self.window_variable.winfo_screenheight()-500}+-5+-10')}")
        #print(f"{self.window_variable.wm_frame()}")

        self.window_variable.mainloop()


class library_extractor:
    def __init__(self, widget_library=lbry):
        self.property_list = self.library_extractor()


    def __repr__(self):
        frame_properties = list()
        widget_properties = list()

        elements = []
        for element in lbry.elements:
            elements.append(element)

        for element_name in elements:
            element_data = lbry.elements[element_name][0]
            if "Frame" in element_data:
                print(f"| Element '{element_name}' is a frame:")
                print()
                temp_element_keys = []; temp_element_values = []
                temp_element_tuple = ()
                
                element_info = []
                for key in element_data.keys():
                    temp_element_keys.append(key)
                for value in element_data.values():
                    temp_element_values.append(value)
                for key, value in zip(temp_element_keys, temp_element_values):
                    print(f" *  {key , value}")
                    temp_element_tuple += ((key, value),) # Nice way to create tuple of tuples
                element_info.append(temp_element_tuple)
                print()

                #print(element_info)
                for type in element_info:
                    element_type = str(type[0][0])
                    element_props = list(type[:][1:])
                    print(f"~ Creating widget of type '{element_type}'")
                    print(f"~ with properties: {element_props}")

                    frame_properties.append((element_type,(element_props)))
                    """func of widget creation"""

                print("\n- - - Final frame_properties to create - - -")
                print(frame_properties)
                print()

            elif "Widgets" in element_data:
                for key, value in element_data.items():
                    print(f"| Element '{element_name}' contains widgets:")
                    for widget in value:
                        print(f"|  {widget}")
                
                print()
                widget_info = []
                for key, value in element_data.items():
                    for widgets in value:
                        temp_widget = []; temp_data = []
                        temp_widget_tuple = ()
                        for _ in widgets.keys():
                            temp_widget.append(_)
                        for _ in widgets.values():
                            temp_data.append(_)
                        for widget, data in zip(temp_widget, temp_data):
                            print(f" *  {widget , data}")
                            temp_widget_tuple += ((widget, data),) # Nice way to create tuple of tuples
                        widget_info.append(temp_widget_tuple)
                        print()
                
                #print(widget_info)
                for type in widget_info:
                    widget_type = (str(type[0][0]), str(type[0][1]))
                    widget_props = list(type[:][1:])
                    print(f"~ Creating widget of type '{widget_type}'")
                    print(f"~   with properties: {widget_props}")

                    widget_properties.append((widget_type,(widget_props)))

                print("\n- - - Final widget_properties to create - - -")
                print(widget_properties)
                print()

        #return print(f"elements:\n{elements}\n\nframe_properties:\n{frame_properties}\n\nwidget properties:\n{widget_properties}\n")
        return print(f"elements:\n{elements}\n\nframe_properties:\n{frame_properties}\n\nwidget_properties:\n{widget_properties}\n")


    def library_extractor(self):
        frame_properties = list()
        widget_properties = list()

        elements = []
        for element in lbry.elements:
            elements.append(element)

        for element_name in elements:
            element_data = lbry.elements[element_name][0]
            if "Frame" in element_data:
                temp_element_keys = []; temp_element_values = []
                temp_element_tuple = ()
                element_info = []
                for _ in element_data.keys():
                    temp_element_keys.append(_)
                for _ in element_data.values():
                    temp_element_values.append(_)
                for key, value in zip(temp_element_keys, temp_element_values):
                    temp_element_tuple += ((key, value),) # Nice way to create tuple of tuples
                element_info.append(temp_element_tuple)

                for type in element_info:
                    element_type = str(type[0][0])
                    element_props = list(type[:][1:])
                    frame_properties.append((element_type,(element_props)))
                    """func of widget creation"""

            elif "Widgets" in element_data:
                widget_info = []
                for key, value in element_data.items():
                    for widgets in value:
                        temp_widget = []; temp_data = []
                        temp_widget_tuple = ()
                        for _ in widgets.keys():
                            temp_widget.append(_)
                        for _ in widgets.values():
                            temp_data.append(_)
                        for widget, data in zip(temp_widget, temp_data):
                            temp_widget_tuple += ((widget, data),) # Nice way to create tuple of tuples
                        widget_info.append(temp_widget_tuple)
                
                for type in widget_info:
                    widget_type = (str(type[0][0]), str(type[0][1]))
                    widget_props = list(type[:][1:])
                    widget_properties.append((widget_type,(widget_props)))
                widget_properties.insert(0, ("Widgets"))

        properties = [frame_properties, widget_properties]
        return properties


test = dynamic_root_window_frames("Dynamic Window Title")
test.start_window()


#widget_props = {k: v for k, v in widget_info.items() if k != "type"}
#print(f"| Creating widget of type '' with properties: {widget_props}\n")
# Here you can add code to create the widget based on widget_type and widget_props
# For example:
# if widget_type == "Label":
#     label = tk.Label(self.window_variable, **widget_props)
#     label.pack()