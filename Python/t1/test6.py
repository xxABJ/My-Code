import json

with open("monitors.json", "r") as f:
    Monitor_list = json.load(f)["Monitors"]

#def read_json_file():
#
# "w" deletes all and re writes back in !
# Deleting all data from file "monitos.json" with the "w" argument, then adding new data obtains from test6.py and inserting it to "monitos.json" with the "w" json file !
# Below command vvv
#with open("monitors.json", "w") as f:
#    json.dump({"Monitors": Monitor_list}, f)
#
#    with open(json_file, "r") as f:
#        Monitor_list = json.load(f)["Monitors"]
#    
#    return Monitor_list    

#def recreate_json_file(Monitor_list):
#
# "w" deletes all and re writes back in !
# Deleting all data from file "monitos.json" with the "w" argument, then adding new data obtains from test6.py and inserting it to "monitos.json" with the "w" json file !
# Below command vvv
#with open("monitors.json", "w") as f:
#    json.dump({"Monitors": Monitor_list}, f)
#
#    with open(json_file, "w") as f:
#        json.dump({"Monitors": Monitor_list}, f)
#
#    return f"\nNew {json_file} has been created!"

def add_monitor():

    while True:
        print("Enter a monitor name (or location):")
        name = input("-> ").lower()

        if len(name) < 1:
            print("Can not be empty.\n")
        elif " " in name:
            print("Can not have spaces.\n")
        else:
            break
    
    while True:
        print("Enter a brand name:")
        brand = input("-> ").lower()

        if len(brand) < 1:
            print("Can not be empty.\n")
        elif " " in brand:
            print("Can not have spaces.\n")
        else:
            break

    while True:
        print("Enter the monitor size:")
        size = input("-> ")

        if size.count(".") > 1:
            print("Can not have more than one decimal point.\n")

        elif not "." in size:
            if size.isdigit() == True:
                float(size)
                break
            elif len(size) < 1:
                print("Can not be empty.\n")
            elif " " in size:
                print("Can not have spaces.\n")
            else:
                print("INVALID, not a number.\n")
                
        else:
            try:
                float(size)
                break
            except:
                print("INVALID, not a number.\n")

    while True:
        print("Enter the monitor year model:")
        model = input("-> ")

        if len(model) < 1:
            print("Can not be empty.\n")
        elif " " in model:
            print("Can not have spaces.\n")
        elif model.isdigit() == False:
            print("INVALID, not a number.\n")
        else:
            int(model)
            break

    New_monitor = {"name": name, "brand": brand, "size": size, "model": model}
    return New_monitor

def display_monitor_list(Monitor_list):

    for i, New_monitor in enumerate(Monitor_list):
        print(i + 1, "~", New_monitor["name"], "|", New_monitor["brand"], "|", New_monitor["size"], "|", New_monitor["model"])

def delete_monitor(Monitor_list):

    print("\n- - - - Current monitor list! - - - -\n")
    display_monitor_list(Monitor_list)
    print("\n- - - - - - - - - - - - - - - - - - -\n")

    if len(Monitor_list) < 1:
        print("No monitor is stored !")
        return
    else:
        pass

    while True:
        print("Which monitor do you want to delete?:")
        number = input("-> ")

        try:
            number = int(number)
            if not 0 < number <= len(Monitor_list):
                print("INVALID ANSWER, no monitor with that number.")
            else:
                break
        except:
            print("INVALID ANSWER, not a number.")

    for i, New_monitor in enumerate(Monitor_list):
        if i == number:
            Monitor_list.pop(number - 1)
            print("\nMonitor has been deleted!\n")
            return

def search_for_monitor(Monitor_list):

    print("\n- - - - Search menu! - - - -\n")

    while True:
        search_name = input("Monitor name to search for: ")
        found = False

        for i, New_monitor in enumerate(Monitor_list):
            name = New_monitor["name"]
            if search_name in name:
                name = (New_monitor["name"], New_monitor["brand"], New_monitor["size"], New_monitor["model"])
                print(i + 1, "~",name)
                found = True
        
        if found:
            print("\nMonitor/Monitors found!")
        else:
            print("\nNo monitor name was found.")

        print("\n Do you want to search again?: (y) or (n)")

        while True:
            command = input("-> ").lower()
            if command == "y":
                break
            elif command == "n":
                return
            else:
                print("INVAILD answer. please type 'y' or 'n'.\n")

def main_menu_ui():
    
    print("\n- - - - - - - - - - - - - - - - - -")
    print("|            Main Menu            |")
    print("- - - - - - - - - - - - - - - - - -")
    print("|                                 |")
    print("| -(1)-  Assign a new monitor.    |")
    print("|                                 |")
    print("| -(2)-  Delete a monitor.        |")
    print("|                                 |")
    print("| -(3)-  List of monitors.        |")
    print("|                                 |")
    print("| -(4)-  Search for monitor.      |")
    print("|                                 |")
    print("| -(5)-  Exit.                    |")
    print("|                                 |")
    print("- - - - - - - - - - - - - - - - - -")
    print("|    Total number of monitors:",len(Monitor_list)," |")
    print("- - - - - - - - - - - - - - - - - -\n")

def main_menu():

    main_menu_ui()

    while True:
        main_menu_option = input("-> ")
        
        flag = False
        try:
            main_menu_option = int(main_menu_option)
            main_menu_option == 0 < int(main_menu_option) <= 5
            flag = True
        except:
            print("INVALID answer, not a number.\n")

        if flag == True:
            # assign a new monitor
            if main_menu_option == 1:
                New_monitor = add_monitor()
                Monitor_list.append(New_monitor)
                print("\nNew monitor has been added!\n")
                main_menu_ui()

            # delete a monitor
            elif main_menu_option == 2:
                delete_monitor(Monitor_list)
                main_menu_ui()

            # list of monitors
            elif main_menu_option == 3:
                print("\nList of Monitors:\n")
                display_monitor_list(Monitor_list)
                print("\n Return to main menu? (y): ")

                while True:
                    answer = input("-> ").lower()
                    if answer == "y":
                        break
                    else:
                        print("Please type 'y' to return to the main menu.")
                
                main_menu_ui()

            #search for monitor
            elif main_menu_option == 4:
                search_for_monitor(Monitor_list)
                main_menu_ui()

            #exit
            elif main_menu_option == 5:
                with open("monitors.json", "w") as f:
                    json.dump({"Monitors": Monitor_list}, f)
                break

# --

main_menu()