class Monitor:

    def __init__(self, name: str, brand: str, size: float, model: int, brightness: int) -> None:

        self.name = name
        self.brand = brand
        self.size = size
        self.model = model
        self.brightness = brightness
        
        self.turned_on: bool = False

    #def assign_monitor_number():
    #
    #    Monitor_number += 1
    #    return Monitor_number

    def turn_off(self) -> None:

        if self.turned_on == False:
            print(f"The Monitor ({self.name}, Brand: {self.brand}) is already turned OFF.")
        
        else:
            self.turned_on = False
            print(f"The Monitor ({self.name}, Brand: {self.brand}) is turning OFF now.")

    def turn_on(self) -> None:

        if self.turned_on == True:
            print(f"The Monitor ({self.name}, Brand: {self.brand}) is already turned ON.")
        
        else:
            self.turned_on = True
            print(f"The Monitor ({self.name}, Brand: {self.brand}) is turning ON now.")

    def brightness_level_check(self) -> None:

        print(f"\nThe brigtness of the monitor ({self.name}, Brand: {self.brand}) is: {self.brightness}%\n")

    def brightness_level_change(self) -> None:

        print("\nWelcome, entering brightness level configuration.")
        print(f"The current brightness level of the monitor ({self.name}, Brand: {self.brand}) is: {self.brightness}%")

        while True:

            print("\n= = = = = = = = = = = = = = = = = = =")
            print("=   Brightness Configuration menu   =")
            print("= = = = = = = = = = = = = = = = = = =\n")
            print("(1) Increase the brightness level.")
            print("(2) Decrease the brightness level.")
            print("(3) Check your current brightness level.")
            print("(4) Exit.\n")
            print("Please type your option below:")
            menu_option: str = input("-> ")

            if menu_option.isdigit():
                
                menu_option = int(menu_option)

                if menu_option == 1:

                    while True:

                        print("\nHow much do you want to increase the brightness level of the monitor?")
                        amount: str = input("-> ")

                        if amount.isdigit():

                            amount = int(amount)
                            self.brightness = int(self.brightness)

                            if self.brightness + amount <= 100:

                                self.brightness += amount
                                print("\n- - - - - - - - - - - - - - - - -")
                                print("Changing the brightness level . . .")
                                print("- - - - - - - - - - - - - - - - -\n")
                                print("Done.")

                                break

                            if self.brightness + amount > 100:

                                while True:

                                    print("\nThe brightness level of the monitor can only go up to 100%,\n")
                                    print("Do you want to increase the brightness to the maximum?")
                                    print("Type: 'y' or 'n' below to proceed.")
                                    maximum_level: str = input("-> ")

                                    if maximum_level.lower() == "y":

                                        self.brightness = 100
                                        print("\nYou have answered yes. (y)")
                                        print("\n- - - - - - - - - - - - - - - - -")
                                        print("Changing the brightness level . . .")
                                        print("- - - - - - - - - - - - - - - - -\n")
                                        print("Done.")

                                        break

                                    elif maximum_level.lower() == "n":

                                        print("\nYou have answered no. (n)\n")
                                        print("Do you still want to change the brightness level?")
                                        print("Type: 'y' or 'n' below to proceed.")
                                        change_level: str = input("-> ")

                                        if change_level.lower() == "y":

                                            break

                                        elif change_level.lower() == "n":

                                            break

                                        else:

                                            print(f"INVALID answer,\n")

                                    else:

                                        print(f"INVALID answer,\n")   

                        else:

                            print("INVALID answer,\n")

                        if (maximum_level.lower() == "y") or (change_level.lower() == "n"):
                             
                             break

                elif menu_option == 2:

                    while True:

                        print("\nHow much do you want to decrease the brightness level of the monitor?")
                        amount: str = input("-> ")
                        
                        if amount.isdigit():
                        
                            amount = int(amount)
                            self.brightness = int(self.brightness)
                            
                            if self.brightness - amount >= 0:
                            
                                self.brightness -= amount
                                print("\n- - - - - - - - - - - - - - - - -")
                                print("Changing the brightness level . . .")
                                print("- - - - - - - - - - - - - - - - -\n")
                                print("Done.")

                                break
                            
                            if self.brightness < 0:
                                
                                while True:
                                    
                                    print("\nThe brightness level of the monitor can only go down to 0%,\n")
                                    print("Do you want to decrease the brightness to the minimum?")
                                    print("Type: 'y' or 'n' below to proceed.")
                                    minimum_level: str = input("-> ")
    
                                    if minimum_level.lower() == "y":
                                    
                                        self.brightness = 0
                                        print("\nYou have answered yes. (y)")
                                        print("\n- - - - - - - - - - - - - - - - -")
                                        print("Changing the brightness level . . .")
                                        print("- - - - - - - - - - - - - - - - -\n")
                                        print("Done.")
                                        
                                        break
                                    
                                    elif minimum_level.lower() == "n":
                                    
                                        print("\nYou have answered no. (n)")
                                        print("\nDo you still want to change the brightness level?")
                                        print("Type: 'y' or 'n' below to proceed.")
                                        change_level: str = input("-> ")
    
                                        if change_level.lower() == "y":
                                             
                                            break
                                        
                                        elif change_level.lower() == "n":
                                             
                                            break
                                        
                                        else:
                                        
                                            print(f"INVALID answer,\n")
    
                                    else:
                                    
                                        print(f"INVALID answer,\n")   
                        
                        else:
                        
                            print(f"INVALID answer,\n")

                        if (minimum_level.lower() == "y") or (change_level.lower() == "n"):
                             
                             break

                elif menu_option == 3:

                    print("\nAlright,")
                    print(f"The current brightness level of the monitor ({self.name}, Brand: {self.brand}) is: {self.brightness}%\n")

                elif menu_option == 4:
                        
                    print("Alright,")

                    break

                else:

                    print("INVALID answer,\n")

            else:

                print("INVALID answer,\n")

        print("\nExiting brightness level configuration . . .")
        print("Done.\n")

def assign_monitor_specifications():

    print("\nenter a monitor name (or location?):")
    name: str = input("-> ")

    print("\nenter a brand name:")
    brand: str = input("-> ")

    print("\nenter monitor size:")
    size: str = input("-> ")
    size = float(size)

    print("\nenter a year model:")
    model: str = input("-> ")
    model = int(model)

    print("\nenter a brightness level:")
    brightness: str = input("-> ")
    brightness = int(brightness)

    total = "Monitor "+str(len(Monitor_specification + 1))+"#"

    return (str(total) + Monitor(name, brand, size, model, brightness)).append(Monitor_specification)

Monitor_specification = []

def check_monitor_list():

    return print(Monitor_list)

def total_number_of_monitors():

    return print(len(Monitor_specification))

def main_menu():

    print("\n- - - - - - - - - - - - - - - - - -")
    print("|            Main Menu            |")
    print("- - - - - - - - - - - - - - - - - -")
    print("|                                 |")
    print("| -(1)-  Assign a new monitor.    |")
    print("|                                 |")
    print("| -(2)-  Monitor configuration.   |")
    print("|                                 |")
    print("| -(3)-  List of monitors.        |")
    print("|                                 |")
    print("| -(4)-  Total monitor number     |")
    print("|                                 |")
    print("| -(5)-  Exit.                    |")
    print("|                                 |")
    print("- - - - - - - - - - - - - - - - - -\n")
    
    while True:
        main_menu_option = input("-> ")

        flag = False
        try:
            main_menu_option == 0 < main_menu_option.isdigit() <= 5
            main_menu_option = int(main_menu_option)
            flag = True
        except:
            print("INVALID answer,\n")

        if flag == True:
            return main_menu_option

def main_menu_option_1 ():

    print("\n- - - - - - - - - - - - - - - - - -")
    print("|      Assign a new monitor.      |")
    print("- - - - - - - - - - - - - - - - - -\n")
    print("assigning a new monitor .  .  .")
    assign_monitor_specifications()
        
    

#def main_menu_option_2 ():
#
#def main_menu_option_3 ():
#
#def main_menu_option_4 ():


#Left_Monitor: Monitor = Monitor('Left Monitor', 'Acer', '27.1', '2016', '20')

#print(abj)
#print(abj.name)
#print(abj.brand)
#print(abj.size)
#print(abj.model)
#abj.turn_on()
#abj.turn_off()
#abj.turn_off()
#abj.turn_on()
#abj.turn_on()
#Left_Monitor.turn_off()
#Left_Monitor.turn_on()
#Left_Monitor.turn_on()
#Left_Monitor.brightness_level_change()
#print(Left_Monitor.name)

#assign_monitor()

main_menu()
print(main_menu)