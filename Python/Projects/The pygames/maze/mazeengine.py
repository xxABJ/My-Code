from factoringsystem import FactoringSystem
from assignsystem import AssignSystem

import random


class MazeEngine:


    def __init__(
            
            self,
            object_maze: object,
            size: int,
            custom_starting_point: tuple | bool,
            custom_starting_direction: str | bool,
            print_console: bool,
            
        ):
        
        self.arrows = {

           "u": "↑",
           "d": "↓",
           "r": "→",
           "l": "←"

        }
        

        self.score_direction_translated = {

            "u": "topside",
            "d": "bottomside",
            "r": "rightside",
            "l": "leftside"

        }


        self._scores = {

            'topside': 0,
            'bottomside': 0,
            'rightside':0,
            'leftside': 0

        }


        self._total_assignments = 0
        self._assignments = {}
        self._chosen_cell_pos = ()
        self._selected_cell_info = []


        self.maze = object_maze
        self.size = size
        self.custom_starting_point = custom_starting_point
        self.custom_starting_direction = custom_starting_direction
        self.print_console = print_console

        
        self.factoringSystem = FactoringSystem()
        self.assignSystem =  AssignSystem(self)


        self.grid = self.create_grid(self.size)


        self.set_first_assingment_and_direction(

            # Custom Starting point (tuple)
            custom_starting_point= self.custom_starting_point,

            # Direction specifier (str)
            custom_starting_direction= self.custom_starting_direction,

            # Console printing (bool)
            print_console = self.print_console

        )


        self.maze = self.create_maze()


        self.maze_completed = False




    def create_grid(self, size: int) -> list:

        grid = []
        for rows in range(size):

            row = []
            for col in range(size):

                if (rows == 0 or rows == size-1) or (col == 0 or col == size-1):
                    
                    col = "|"


                else:
                    
                    col = " "

                
                row.append(col)
            

            if rows == 1:
                
                random_index = random.randint(1, size-2)
                row.pop(random_index)
                row.insert(random_index, "S")


            elif rows == size-2:
                
                random_index = random.randint(1, size-2)
                row.pop(random_index)
                row.insert(random_index, "F")


            grid.append(row)

        
        return grid
    



    def set_first_assingment_and_direction(
            
            self,
            custom_starting_point: tuple | bool= False,
            custom_starting_direction: str | bool= False,
            print_console: bool= False
            
        ) -> None:

        def first_assignment(custom_start, custom_direction):

            def _get_direction_validation(row, col):

                # Can assign any direction
                if grid[row][col - 1] != "|" and grid[row][col + 1] != "|" and grid[row - 1][col] != "|" and grid[row + 1][col] != "|":
                
                    available_directions = ["l", "r", "d", "u"]


                else:
                
                    # Cannot assign left
                    if grid[row][col - 1] == "|":
                    
                    
                        #c_topleft
                        if grid[row - 1][col - 1] == "|":
                        
                            available_directions = ["r", "d"]


                        #c_bottomleft
                        elif grid[row + 1][col - 1] == "|":
                        
                            available_directions = ["r", "u"]


                    # Cannot assign right
                    elif grid[row][col + 1] == "|":
                    
                        #c_topright
                        if grid[row - 1][col + 1] == "|":
                        
                            available_directions = ["l", "d"]


                        #c_bottomright
                        elif grid[row + 1][col + 1] == "|":
                        
                            available_directions = ["l", "u"]


                    # Cannot assign up
                    elif grid[row - 1][col] == "|":
                    
                        available_directions = ["l", "r", "d"]


                    # Cannot assign down
                    elif grid[row + 1][col] == "|":
                    
                        available_directions = ["l", "r", "u"]


                return available_directions


            if print_console:

                print()


            # Starting Assignment
            if custom_start == True:
                
                ROW = custom_starting_point[0]
                COL = custom_starting_point[1]
                AVAILABLE_DIRECTIONS = _get_direction_validation(ROW, COL)

                self.change_starting(

                    row= ROW,
                    col= COL
                
                )


                if print_console:

                    print(f"~ 'S' at: (ROW: {ROW}, COL: {COL})")


            elif custom_start == False:


                if print_console:

                    print("~ Locating starting point . . .", end=" ")


                # Starting-point Locator
                for row in range(size):

                    # Skip if at horizontal side-border
                    if row == 0 or row == size - 1:
                        
                        #print(f"row:{row} horizontal side-borders")
                        continue
                    
                    else:

                        #print(f"row:{row}")
                        pass


                    for col in range(size):

                        # Skip if at vertical side-borders
                        if col == 0 or col == size - 1:
                            
                            #print(f"{" "*5}col:{col} vertical side-borders")
                            continue


                        # Skip if not at the state point
                        elif grid[row][col] != "S":
                            
                            #print(f"{" "*5}col:{col} not 'S'")
                            continue


                        else:

                            #print(f"row:{row}")
                            #print(f"{" "*5}col:{col} found 'S'")
                            #pass


                            ROW = row
                            COL = col
                            AVAILABLE_DIRECTIONS = _get_direction_validation(ROW, COL)
                            break

                
                if print_console:

                    print(f" DONE!✅\n  'S' at: (ROW: {ROW}, COL: {COL})")


            # Starting direction
            if custom_direction == True:
            
                RANDOM_VALID_DIRECTION = custom_starting_direction


                if print_console:

                    print(f"~ Selected direction: {RANDOM_VALID_DIRECTION}")


            elif custom_direction == False:

                RANDOM_VALID_DIRECTION = random.choice(AVAILABLE_DIRECTIONS)


                if print_console:

                    print(f"\n\n~ AVAILABLE_DIRECTIONS: {AVAILABLE_DIRECTIONS}")
                    print(f"~ RANDOMLY SELECTED DIRECTION: {RANDOM_VALID_DIRECTION}")


            if print_console:
                
                print()
            

            return size, grid, RANDOM_VALID_DIRECTION, ROW, COL


        size = self.size
        grid = self.grid


        if print_console:

            print(f"\n{"♦"*50}\n{"♦"*12} FIRST ASSIGNMENT PRINTING {"♦"*11}\n{"♦"*50}")
            print(f"tuple_pos: {custom_starting_point}\ndirection: {custom_starting_direction}\nprint_console: {print_console}\n")


            # Determining conditions for first assignment
            if custom_starting_point and custom_starting_direction:

                Conditions = (True, True)


            elif custom_starting_point:

                Conditions = (True, False)


            elif custom_starting_direction:

                Conditions = (False, True)

            
            else:

                Conditions = (False, False)


            size, grid, RANDOM_VALID_DIRECTION, ROW, COL = first_assignment(Conditions[0], Conditions[1])


            # ???
            # All of these should be = FALSE, due to the self.assignments being empty
            previous_assignment = self.previous_assignment()

            try:
                
                previous_direction = previous_assignment[0][1]
                previous_pos = previous_assignment[1]
            

            except:
                
                previous_direction = False
                previous_pos = False


            print(f"    previous_direction: {previous_direction}")
            print(f"    previous_pos: {previous_pos}")



            # Getting the factored condition and value
            print("\n\n• CALCULATING FACTORING CONDITION\n")
            factored_direction_data, factoring_value = self.factoringSystem.check_condition(

                previous_direction= previous_direction,
                current_direction= RANDOM_VALID_DIRECTION,
                print_console= print_console

            )
            print(f" >> factored_direction_data: {factored_direction_data}", end= " ")
            print(f" >> factoring_value: {factoring_value}", end= " ")
            print("✅ DONE!")


            print(f"\n\n~ OLD self.get_chosen_cell_pos(): {self.assignSystem.mazeEngine.get_chosen_cell_pos()}")


            # Choosing a cell
            print("~ Choosing global selected cell (factoring!) . . .", end= " ")
            self.pick_selected_cell(

                ROW + factoring_value[0],
                COL + factoring_value[1]

            )
            chosen_row, chosen_col = self.get_chosen_cell_pos()
            print(f" >> ✅ chosen_row: {chosen_row}", end= " ")
            print(f" >> ✅ chosen_col: {chosen_col}")
            print(f"~ NEW self.get_chosen_cell_pos(): {self.assignSystem.mazeEngine.get_chosen_cell_pos()}")


            print(f"\n• Inserting in grid:   {self.arrows.get(factored_direction_data)}", end= " ")         


            # Setting selected cell info
            print("   >> Setting selected cell", end= " ")
            self.set_selected_cell_info(factored_direction_data)
            print("✅")


            # Assigning direction
            print(f"\n\n• ASSIGNING: {factored_direction_data}", end=" ")
            grid[ chosen_row ][ chosen_col ] = self.arrows.get(factored_direction_data)
            print("✅ DONE!")


            # Logging assignments
            print(f"\n\n• LOGGING: {factored_direction_data}\n")
            self.log_assignments(

                current_direction= RANDOM_VALID_DIRECTION,
                starting_row= ROW,
                starting_col= COL,
                previous_pos= previous_pos,
                factoring_value= factoring_value,
                factored_direction_data= factored_direction_data,
                print_console= print_console

            )
            print("✅ DONE!")


            # Calculating scores for the first assignment
            print(f"\n\n• CALCULATING SCORE FOR: {factored_direction_data}\n")
            self.score_calculator(

                current_direction= factored_direction_data,
                starting_row= ROW,
                starting_col= COL,
                state= "first_assignment",
                factored_direction_data= factored_direction_data,
                print_console= print_console

            )
            print("✅ DONE!")


            # Last assignment log
            print(f"\n\n• PREVIOUS LOGGED ASSIGNMENT: {self.previous_assignment()}\n")
            

            # Updating grid
            self.grid = grid


            self.print_grid()


            print(f"\n{"♦"*50}\n{"♦"*50}\n{"♦"*50}\n")


        else:

            # Determining conditions for first assignment
            if custom_starting_point and custom_starting_direction:

                Conditions = (True, True)


            elif custom_starting_point:

                Conditions = (True, False)


            elif custom_starting_direction:

                Conditions = (False, True)

            
            else:

                Conditions = (False, False)


            size, grid, RANDOM_VALID_DIRECTION, ROW, COL = first_assignment(Conditions[0], Conditions[1])


            # ???
            # All of these should be = FALSE, due to no assignments has been logged yet.
            previous_assignment = self.previous_assignment()

            try:
                
                previous_direction = previous_assignment[0][1]
                previous_pos = previous_assignment[1]
            

            except:
                
                previous_direction = False
                previous_pos = False



            # Getting the factored condition and value
            factored_direction_data, factoring_value = self.factoring.check_condition(

                previous_direction= previous_direction,
                current_direction= RANDOM_VALID_DIRECTION,
                print_console= print_console

            )


            # Choosing a cell
            self.pick_selected_cell(

                ROW + factoring_value[0],
                COL + factoring_value[1]

            )
            chosen_row, chosen_col = self.get_chosen_cell_pos()


            # Setting selected cell info
            self.set_selected_cell_info(RANDOM_VALID_DIRECTION)


            # Assigning direction
            grid[ ROW + factoring_value[0] ][ COL + factoring_value[1] ] = self.arrows.get(factored_direction_data)


            # Logging assignments
            self.log_assignments(

                current_direction= RANDOM_VALID_DIRECTION,
                starting_row= ROW,
                starting_col= COL,
                previous_pos= previous_pos,
                factoring_value= factoring_value,
                factored_direction_data= factored_direction_data,
                print_console= print_console

            )


            # Calculating scores for the first assignment
            self.score_calculator(

                current_direction= factored_direction_data,
                starting_row= ROW,
                starting_col= COL,
                state= "first_assignment",
                factored_direction_data= factored_direction_data,
                print_console= print_console

            )


            # Updating grid
            self.grid = grid




    def change_starting(self, row: int, col: int) -> None:

        for rows in range(self.size):
            
            if rows == 0 or rows == self.size - 1:
                
                continue


            for cols in range(self.size):

                if cols == 0 or cols == self.size - 1:
                    
                    continue


                self.grid[rows][cols] = " "


            break


        self.grid[row][col] = "S"




    def previous_assignment(self) -> dict | bool:

        if self.get_total_assignments() > 0:

            last_assignment_key = list(self._assignments.keys())[-1]
            last_assignment_value = list(self._assignments.values())[-1]
            
            
            previous_assignment = [last_assignment_key, (last_assignment_value[0], last_assignment_value[1])]


            return previous_assignment
        

        return False




    def pick_selected_cell(self, row: int, col: int) -> None:

        self._chosen_cell_pos = (row, col)


    def get_chosen_cell_pos(self) -> tuple:

        return self._chosen_cell_pos
    

    def set_selected_cell_info(self, direction: str) -> None:

        self._selected_cell_info = [self._chosen_cell_pos, direction]


    def get_selected_cell_info(self) -> list:

        return self._selected_cell_info




    def set_total_assignments(self, value: int) -> None:

        self._total_assignments = value


    def get_total_assignments(self) -> int:

        return self._total_assignments




    def log_assignments(
            
            self,
            current_direction: str,
            starting_row: int= None,
            starting_col: int= None,
            previous_pos: tuple= False,
            factoring_value: tuple= None,
            factored_direction_data: str | bool= False,
            print_console: bool= False

        ) -> None:
        
        new_total_assignments = self.get_total_assignments() + 1


        # Logging the assignments
        if print_console:

            # Accounting for all assignments
            if previous_pos:

                starting_row = previous_pos[0]
                starting_col = previous_pos[1]


                print("│")
                print(f"├{"─"*10}  LOGGING (@MazeEngine.log_assignments)")
                print("│")


                # SAFETY MEASURES, Shouldn't be required, due to available arguments in function
                if not factoring_value:

                    print("\n\n\nWARNING: No factoring value argument passed in with previous position in @MazeEngine.log_assignments() function, calculating factoring value . . .\n\n\n")


                    if factored_direction_data:

                        if len(factored_direction_data) != 1:

                            previous_direction = factored_direction_data[-1]


                        else:

                            previous_direction = factored_direction_data


                    else:

                        previous_direction = self.previous_assignment()[0][1]


                        # Accounting for changed directrion logged key
                        if len(previous_direction) != 1:

                            # TODO: CHECK if order is correct
                            previous_direction = previous_direction[-1]


                    # Getting the factored condition and value
                    factored_direction_data, factoring_value = self.factoring.check_condition(

                            previous_direction= previous_direction,
                            current_direction= current_direction,
                            print_console= print_console

                    )


            # Accounting for first assignment log where no previous_pos and factoring_value arguments available
            else:

                print(f"┌{"─"*10}  LOGGING (@MazeEngine.log_assignments)")
                print("│")


                # SAFETY MEASURES
                if not factoring_value:

                    print("\n\n\nWARNING: No factoring value argument passed in with previous position in @MazeEngine.log_assignments() function, calculating factoring value . . .\n\n\n")


                    if factored_direction_data:

                        previous_direction = factored_direction_data


                    else:

                        # This should = FALSE, due to the self.assignments being empty
                        previous_direction = self.previous_assignment()[0][1]


                    # Getting the factored condition and value
                    factored_direction_data, factoring_value = self.factoring.check_condition(

                            previous_direction= previous_direction,
                            current_direction= current_direction,
                            print_console= print_console

                    )


            print(f"│ logger:")
            print(f"│   direction: {current_direction}")     
            print(f"│   row: {starting_row}")
            print(f"│   col: {starting_col}")
            print(f"│   previous_pos: {previous_pos}")
            print(f"│   factoring_value: {factoring_value}")


            if factored_direction_data:
                
                print(f"│   factored_direction_data: {factored_direction_data}")
            
            
            else:
                
                print(f"│   No factored_direction_data, factored_direction_data: {factored_direction_data}")


            print("│")


            # Debugging before and after factoring in required calculations
            print(f"│ before logger edit: {(starting_row, starting_col)}")
            print(f"│ logger edit: {(factoring_value[0], factoring_value[1])}")
            print("│ after logger edit:", tuple(

                a + b for a, b in zip(

                    ( starting_row, starting_col ),
                    ( factoring_value[0], factoring_value[1] )

            )))
            print("│")


            # Conditioning type of factored_direction_data for logging
            match factored_direction_data:

                case "r>r":

                    factored_direction_data = "r"


                case "l>l":

                    factored_direction_data = "l"

                case "u>u":


                    factored_direction_data = "u"

                case "d>d":

                    factored_direction_data = "d"


                case _:
                    
                    pass


            # Adding new data log to the global variable
            self._assignments[(new_total_assignments, factored_direction_data)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( starting_row , starting_col ),
                    ( factoring_value[0] , factoring_value[1] )
                    
            ))


            if previous_pos:

                print(f"├{'─'*30}┘")


            else:

                print(f"└{'─'*30}┘")
            

        else:

            # Accounting for all assignments logging
            if previous_pos:

                starting_row = previous_pos[0]
                starting_col = previous_pos[1]


                # SAFETY MEASURES, Shouldn't be required, due to available arguments in function
                if not factoring_value:

                    if factored_direction_data:

                        if len(factored_direction_data) != 1:

                            previous_direction = factored_direction_data[-1]


                        else:

                            previous_direction = factored_direction_data


                    else:

                        previous_direction = self.previous_assignment()[0][1]


                        # Accounting for changed directrion logged key
                        if len(previous_direction) != 1:

                            # TODO: CHECK if order is correct
                            previous_direction = previous_direction[-1]


                    # Getting the factored condition and value
                    factored_direction_data, factoring_value = self.factoring.check_condition(

                            previous_direction= previous_direction,
                            current_direction= current_direction,
                            print_console= print_console

                    )


            # Accounting for first assignment logging where no previous_pos argument is available
            else:

                # SAFETY MEASURES
                if not factoring_value:


                    if factored_direction_data:

                        previous_direction = factored_direction_data


                    else:

                        # This should = FALSE, due to the self.assignments being empty
                        previous_direction = self.previous_assignment()[0][1]


                    # Getting the factored condition and value
                    factored_direction_data, factoring_value = self.factoring.check_condition(

                            previous_direction= previous_direction,
                            current_direction= current_direction,
                            print_console= print_console

                    )


            # Conditioning type of factored_direction_data for logging
            match factored_direction_data:

                case "r>r":

                    factored_direction_data = "r"


                case "l>l":

                    factored_direction_data = "l"

                case "u>u":


                    factored_direction_data = "u"

                case "d>d":

                    factored_direction_data = "d"


                case _:

                    pass


            # Adding new data log to the global variable
            self._assignments[(new_total_assignments, factored_direction_data)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( starting_row, starting_col ),
                    ( factoring_value[0], factoring_value[1] )
                    
            ))


        self.set_total_assignments(new_total_assignments)


    def get_assignments(self):

        return self._assignments


    def print_assignments(self):

        print("\n--- ALL ASSIGNMENTS | MAZE SOLUTION @MazeEngine()._assignments ---\n")
        
        
        total_directions = 1
        for key, value in self.get_assignments().items():

            print(f" •{total_directions: <3}  ->   │ assignment:  {str(key[0]): <3} , {str(key[1]): >3} │ {"•grid_pos:": >12} {value}")


            total_directions += 1
        
        
        print()




    def score_calculator(
            
            self,
            current_direction: str,
            starting_row: int= None,
            starting_col: int= None,
            state: str= None,
            factored_direction_data: str= None,
            print_console: bool= False
            
        ) -> None:

        size = self.size


        if print_console:

            # (Row, Col) is from self.set_first_assignment()
            if state == "first_assignment":

                # Printing old scores
                print(f"┌{'─'*10}  CALCULATING SCORES (@MazeEngine.score_calculator)")
                print("│")
                print(f"│ factored_direction_data: {factored_direction_data}")
                print("│")
                print(f"│ OLD")
                print(f"│ Assignment No.0")
                print("│")
                self.print_scores()


                print("│")
                print(f"├ EXTRA SPECIAL calculating condition for first assignment ! (due to factored_direction_data: {factored_direction_data}),")


                # (Row, Col) are the pos of 'S'
                if current_direction == 'd':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row - 1,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col,
                        f'{self.score_direction_translated.get("l")}': starting_col - 1
                        
                    }


                elif current_direction == 'u':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row - 2,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row + 1,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col,
                        f'{self.score_direction_translated.get("l")}': starting_col - 1
                    
                    }
                

                elif current_direction == 'l':

                    calculated_scores = {
                        
                        f'{self.score_direction_translated.get("u")}': starting_row - 1,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col + 1,
                        f'{self.score_direction_translated.get("l")}': starting_col - 2
                    
                    }
                
                
                elif current_direction == 'r':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row - 1,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col - 1,
                        f'{self.score_direction_translated.get("l")}': starting_col
                    
                    }


                self._scores = calculated_scores


                # Printing new scores
                print("│")
                print(f"│ NEW")
                print(f"│ Assignment No.1")
                print("│")
                self.print_scores()
                print("│")
                print(f"└{'─'*30}┘")


            else:
                
                # Printing old scores
                print("│")
                print(f"├{'─'*10}  CALCULATING SCORES (@MazeEngine.score_calculator)")
                print("│")
                print(f"│ factored_direction_data: {factored_direction_data}")
                print("│")
                print(f"│ OLD")
                print(f"│ Assignment No.{self.get_total_assignments()}")
                print("│")
                self.print_scores()


                scores = self.get_scores()


                if factored_direction_data[0] == factored_direction_data[-1]:

                    print("│")
                    print(f"├ No special calculating condition (due to factored_direction_data: {factored_direction_data})")
                    print("│   Updating scores depending on the:")
                    print("│         ♦ current direction assigned")


                    if current_direction in ["d", "u"]:

                        old_topside_score = scores.get(self.score_direction_translated.get("u"))
                        old_bottomside_score = scores.get(self.score_direction_translated.get("d"))


                        if current_direction == 'd':

                            new_topside_score = old_topside_score + 1
                            new_bottomside_score = old_bottomside_score - 1


                        elif current_direction == 'u':

                            new_topside_score = old_topside_score - 1
                            new_bottomside_score = old_bottomside_score + 1


                        self._scores[self.score_direction_translated.get("u")] = new_topside_score
                        self._scores[self.score_direction_translated.get("d")] = new_bottomside_score


                    elif current_direction in ["r", "l"]:

                        old_rightside_score = scores.get(self.score_direction_translated.get("r"))
                        old_leftside_score = scores.get(self.score_direction_translated.get("l"))


                        if current_direction == 'r':

                            new_rightside_score = old_rightside_score - 1
                            new_leftside_score = old_leftside_score + 1


                        elif current_direction == 'l':

                            new_rightside_score = old_rightside_score + 1
                            new_leftside_score = old_leftside_score - 1


                        self._scores[self.score_direction_translated.get("r")] = new_rightside_score
                        self._scores[self.score_direction_translated.get("l")] = new_leftside_score   

                
                else:

                    print("│")
                    print(f"├ Special calculating condition (due to factored_direction_data: {factored_direction_data}),")
                    print("│   Updating scores depending on:")
                    print("│         ♦ current direction assigned")
                    print("│         ♦ previous direction")


                    old_topside_score = scores.get(self.score_direction_translated.get("u"))
                    old_bottomside_score = scores.get(self.score_direction_translated.get("d"))
                    old_rightside_score = scores.get(self.score_direction_translated.get("r"))
                    old_leftside_score = scores.get(self.score_direction_translated.get("l"))


                    previous_direction = factored_direction_data[0]


                    if current_direction in ["d", "u"]:

                        new_topside_score = old_topside_score
                        new_bottomside_score = old_bottomside_score

                        if previous_direction == "r":

                            new_rightside_score = old_rightside_score - 1
                            new_leftside_score = old_leftside_score + 1


                        elif previous_direction == "l":

                            new_rightside_score = old_rightside_score + 1
                            new_leftside_score = old_leftside_score - 1


                    elif current_direction in ["r", "l"]:

                        new_rightside_score = old_rightside_score
                        new_leftside_score = old_leftside_score


                        if previous_direction == "d":

                            new_topside_score = old_topside_score + 1
                            new_bottomside_score = old_bottomside_score - 1


                        elif previous_direction == "u":

                            new_topside_score = old_topside_score - 1
                            new_bottomside_score = old_bottomside_score + 1


                    self._scores[self.score_direction_translated.get("u")] = new_topside_score
                    self._scores[self.score_direction_translated.get("d")] = new_bottomside_score
                    self._scores[self.score_direction_translated.get("r")] = new_rightside_score
                    self._scores[self.score_direction_translated.get("l")] = new_leftside_score


                # Printing new scores
                print("│")
                print(f"│ NEW")
                print(f"│ Assignment No.{self.get_total_assignments() + 1}")
                print("│")
                self.print_scores()
                print("│")
                #print(f"├{'─'*30}")


        else:

            # (Row, Col) is from self.set_first_assignment()
            if state == "first_assignment":

                # (Row, Col) are the pos of 'S'
                if current_direction == 'd':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row - 1,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col,
                        f'{self.score_direction_translated.get("l")}': starting_col - 1
                    
                    }


                elif current_direction == 'u':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row - 2,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row + 1,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col,
                        f'{self.score_direction_translated.get("l")}': starting_col - 1
                    
                    }
                

                elif current_direction == 'l':

                    calculated_scores = {
                        
                        f'{self.score_direction_translated.get("u")}': starting_row - 1,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col + 1,
                        f'{self.score_direction_translated.get("l")}': starting_col - 2
                    
                    }
                
                
                elif current_direction == 'r':

                    calculated_scores = {

                        f'{self.score_direction_translated.get("u")}': starting_row - 1,
                        f'{self.score_direction_translated.get("d")}': (size - 2) - starting_row,
                        f'{self.score_direction_translated.get("r")}': (size - 2) - starting_col - 1,
                        f'{self.score_direction_translated.get("l")}': starting_col
                    
                    }


                self._scores = calculated_scores


            else:

                scores = self.get_scores()


                if current_direction in ["d", "u"]:

                    old_topside_score = scores.get(self.score_direction_translated.get("u"))
                    old_bottomside_score = scores.get(self.score_direction_translated.get("d"))


                    if current_direction == 'd':

                        new_topside_score = old_topside_score + 1
                        new_bottomside_score = old_bottomside_score - 1


                    elif current_direction == 'u':

                        new_topside_score = old_topside_score - 1
                        new_bottomside_score = old_bottomside_score + 1


                    self._scores[self.score_direction_translated.get("u")] = new_topside_score
                    self._scores[self.score_direction_translated.get("d")] = new_bottomside_score


                elif current_direction in ["r", "l"]:

                    old_rightside_score = scores.get(self.score_direction_translated.get("r"))
                    old_leftside_score = scores.get(self.score_direction_translated.get("l"))


                    if current_direction == 'r':

                        new_rightside_score = old_rightside_score - 1
                        new_leftside_score = old_leftside_score + 1


                    elif current_direction == 'l':

                        new_rightside_score = old_rightside_score + 1
                        new_leftside_score = old_leftside_score - 1


                    self._scores[self.score_direction_translated.get("r")] = new_rightside_score
                    self._scores[self.score_direction_translated.get("l")] = new_leftside_score


    def get_scores(self):
        
        return self._scores


    def print_scores(self):

        for key, value in self.get_scores().items():
            
            print("│ ", f"{key: <10}", f"{value: >7}")




    def print_grid(self):

        print()

        
        for _ in range(self.size):
            
            if _ > 9:

                print(f" {_}", end="")


            else:

                print(f"  {_}", end="")
        
        
        print()


        for row in range(self.size):

            print(f"{str(row): >2}", end= "")


            for col in range(self.size):

                print(self.grid[row][col], end= "  ")


            print()


        print()




    def create_maze(self):

        grid = self.grid
            
        # #TEMP Unable to go 'u' after first direction has been assigned
        # while self.random_direction == 'u' and len(self.assignments) == 1:
    
        #     self.random_direction = random.choice(self.available_directions)
        #     continue


        ### TESTING
        if self.print_console:

            print(f"\n ☻ LOOPING ASSIGNMENTS\n")


        for _ in range(5):
        
            confirmed_directions = self.assignSystem.validate_direction()
            # TESTING
            confirmed_directions = random.choice(["r", "d"])
        

            # This is not stable, remake
            assignment_state, final_direction = self.assignSystem.assign(
                
                confirmed_directions= confirmed_directions,
                index= _,
                
            )
            
            if self.print_console:

                if assignment_state == False:

                    print(f"{"*"*5}\nINVALID assignment No.{_+1}\n\nassignment_state:  {assignment_state}\nfinal_direction:   {final_direction}\n{"*"*5}\n")

            
                else:

                    print(f"{"-"*5}\nSUCCESSFUL assignment No.{_+1}\n\nassignment_state:  {assignment_state}\nfinal_direction:   {final_direction}\n{"-"*5}\n")
            


        self.maze_completed = True


        if self.print_console:

            print(f"self.maze_completed: {self.maze_completed}")




        print()
        self.print_assignments()
        return grid




