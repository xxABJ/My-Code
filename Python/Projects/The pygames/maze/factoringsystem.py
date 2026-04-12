class FactoringSystem:


    changing_directions = {

        # 1. Previous direction
        # 2. Current direction

        "r": {

            "r": "r>r",
            "d": "r>d",
            "u": "r>u",

            ## Should not be possible
            "l": "r>l"

        },

        "l": {

            "l": "l>l",
            "d": "l>d",
            "u": "l>u",

            ## Should not be possible
            "r": "l>r"

        },

        "u": {

            "u": "u>u",
            "r": "u>r",
            "l": "u>l",

            ## Should not be possible
            "d": "u>d"

        },

        "d": {

            "d": "d>d",
            "r": "d>r",
            "l": "d>l",

            ## Should not be possible
            "u": "d>u"

        },

    }


    factoring_in = {

        # Grid movement directions
        'l': (0, -1),
        'r': (0, 1),
        'u': (-1, 0),
        'd': (1, 0),

        # Right factory conditions
        "r>r": (0 , 1),
        "d>r": (1 , 0),
        "u>r": (-1 , 0),
        "l>r": "not possible",

        # Left factory conditions
        "l>l": (0 , -1),
        "d>l": (1 , 0),
        "u>l": (-1 , 0),
        "r>l": "not possible",

        # Down factory conditions
        "d>d": (1 , 0),
        "r>d": (0 , 1),
        "l>d": (0 , -1),
        "u>d": "not possible",

        # Up factory conditions
        "u>u": (-1 , 0),
        "r>u": (0 , 1),
        "l>u": (0 , -1),
        "d>u": "not possible"

    }


    @classmethod
    def check_condition(
        
            cls,
            previous_direction: str | bool= False,
            current_direction: str= None,
            print_console: bool= False
            
        ) -> str | tuple:
        
        def _required_factor(condition: str, print_console: bool= False) -> tuple:

                if print_console:
                    print("├ Checking condition")
                    print(f"├ ✅ condition  {condition}  met")
                    print("│")


                return cls.factoring_in.get(condition)


        if previous_direction:

            inserting_previous_direction = cls.changing_directions.get(previous_direction)
            inserting_current_direction = inserting_previous_direction.get(current_direction)

        else:

            inserting_current_direction = current_direction


        factored_direction_data = inserting_current_direction


        if print_console:

            if not previous_direction:

                print("┌──────────  Calculating factoring value (@MazeEngine.factoringSystem.check_condition)")
                print("│")


            else: 
            
                print("├──────────  Calculating factoring value (@MazeEngine.factoringSystem.check_condition)")
                print("│")


            if previous_direction:

                print(f"│ inserting_previous_direction: {list(inserting_previous_direction.keys())[0]}")


            else:

                print("│ No previous direction")


            print(f"│ inserting_current_direction: {current_direction}")

            
            print(f"│ Result: ", end="")


            if len(factored_direction_data) > 1:

                for char in factored_direction_data:

                    if char == ">":

                        print("->", end=" ")


                    else:
                        
                        print(char, end=" ")

                print()
            

            else:

                print(factored_direction_data)


            print("│")


        factoring_value = _required_factor(
             
            condition= factored_direction_data,
            print_console= print_console

        )


        if print_console:

            if not previous_direction:

                print(f"└{'─'*30}┘")

            else:

                print(f"├{'─'*30}┘")


        return factored_direction_data, factoring_value,


