from factoring import *
from assignment import *
from scanner import *



import pygame, random


class Maze:


    def __init__(self, size, print_console: bool= False):
        
        self.size = size
        self.print_console = print_console


        #self.available_directions = ["l", "r", "u", "d"]
        self.random_direction = None


        # These tuples are based on how grid is being iterated in / how it was created
        self.directions = {

            'l': (0, -1),
            'r': (0, 1),
            'u': (-1, 0),
            'd': (1, 0)

        }


        self.scores = {

            'topside': 0,
            'bottomside': 0,
            'rightside':0,
            'leftside': 0

        }


        self.total_assignments = 0
        self.assignments = {}


        self.arrows = {

           "l": "←",
           "r": "→",
           "u": "↑",
           "d": "↓"

        }

        self.factoring = Factoring()
        self.scanner = Scanner(self)
        self.assignor = Assignment(self, self.print_console)


        self.grid = self.create_grid(self.size)


        self._chosen_cell_pos = ()
        self._selected_cell_info = []


        self.first_assignment_and_direction_completed = self.set_first_assingment_and_direction(

            # Custom Starting point (tuple)
            tuple_pos= False,

            # Direction specifier (str)
            direction= "r",

            # Console printing (bool)
            print_console = self.print_console

        )


        self.maze_completed = False
        self.maze = self.create_maze()


    def pick_selected_cell(self, row, col):

        self._chosen_cell_pos = (row, col)

    def get_chosen_cell_pos(self):

        return self._chosen_cell_pos
    

    def set_selected_cell_info(self, direction):

        self._selected_cell_info = [self._chosen_cell_pos, direction]

    def get_selected_cell_info(self):

        return self._selected_cell_info




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
        
        new_total_assignments = self.total_assignments + 1


        # Logging the assignments
        if print_console:

            # Accounting for all assignments
            if previous_pos:

                starting_row = previous_pos[0]
                starting_col = previous_pos[1]


                print("│")
                print(f"├{"─"*10}  LOGGING (self.log_assignments)")
                print("│")


                # SAFETY MEASURES, Shouldn't be required, due to available arguments in function
                if not factoring_value:

                    print("\n\n\nWARNING: No factoring value argument passed in with previous position in self.log_assignments() function, calculating factoring value . . .\n\n\n")


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

                print(f"┌{"─"*10}  LOGGING (self.log_assignments)")
                print("│")


                # SAFETY MEASURES
                if not factoring_value:

                    print("\n\n\nWARNING: No factoring value argument passed in with previous position in self.log_assignments() function, calculating factoring value . . .\n\n\n")


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
            self.assignments[(new_total_assignments, factored_direction_data)] = tuple(
                
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
            self.assignments[(new_total_assignments, factored_direction_data)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( starting_row, starting_col ),
                    ( factoring_value[0], factoring_value[1] )
                    
            ))


        self.total_assignments = new_total_assignments




    def score_calculator(
            
            self,
            direction: str,
            starting_row: int= None,
            starting_col: int= None,
            state: str = None,
            print_console: bool= False
            
        ) -> None:

        size = self.size


        if print_console:

            # (Row, Col) is from self.set_first_assignment()
            if state == "first_assignment":

                # Printing old scores
                print(f"┌{'─'*10}  CALCULATING SCORES (self.score_calculator)")
                print("│")
                print(f"│ OLD")
                print(f"│ Assignment No.{self.total_assignments}")
                print("│")
                self.print_scores()


                # (Row, Col) are the pos of 'S'
                if direction == 'd':

                    calculated_scores = {

                        'topside': starting_row,
                        'bottomside': (size - 2) - starting_row - 1,
                        'rightside': (size - 2) - starting_col,
                        'leftside': starting_col - 1
                    
                    }


                elif direction == 'u':

                    calculated_scores = {

                        'topside': starting_row - 2,
                        'bottomside': (size - 2) - starting_row + 1,
                        'rightside': (size - 2) - starting_col,
                        'leftside': starting_col - 1
                    
                    }
                

                elif direction == 'l':

                    calculated_scores = {
                        
                        'topside': starting_row - 1,
                        'bottomside': (size - 2) - starting_row,
                        'rightside': (size - 2) - starting_col + 1,
                        'leftside': starting_col - 2
                    
                    }
                
                
                elif direction == 'r':

                    calculated_scores = {

                        'topside': starting_row - 1,
                        'bottomside': (size - 2) - starting_row,
                        'rightside': (size - 2) - starting_col - 1,
                        'leftside': starting_col
                    
                    }


                self.scores = calculated_scores


                # Printing new scores
                print("│")
                print("│")
                print(f"│ NEW")
                print(f"│ Assignment No.{self.total_assignments + 1}")
                print("│")
                self.print_scores()
                print("│")
                print(f"└{'─'*30}┘")


            else:
                
                # Printing old scores
                print("│")
                print(f"├{'─'*10}  CALCULATING SCORES (self.score_calculator)")
                print("│")
                print(f"│ OLD")
                print(f"│ Assignment No.{self.total_assignments}")
                print("│")
                self.print_scores()


                scores = self.scores


                if direction == 'd':

                    new_topside_score = scores.get('topside') + 1
                    new_bottomside_score = scores.get('bottomside') - 1


                    self.scores['topside'] = new_topside_score
                    self.scores['bottomside'] = new_bottomside_score


                elif direction == 'u':

                    new_topside_score = scores.get('topside') - 1
                    new_bottomside_score = scores.get('bottomside') + 1


                    self.scores['topside'] = new_topside_score
                    self.scores['bottomside'] = new_bottomside_score


                elif direction == 'r':

                    new_rightside_score = scores.get('rightside') - 1
                    new_leftside_score = scores.get('leftside') + 1


                    self.scores['rightside'] = new_rightside_score
                    self.scores['leftside'] = new_leftside_score


                elif direction == 'l':

                    new_rightside_score = scores.get('rightside') + 1
                    new_leftside_score = scores.get('leftside') - 1


                    self.scores['rightside'] = new_rightside_score
                    self.scores['leftside'] = new_leftside_score   


                # Printing new scores
                print("│")
                print("│")
                print(f"│ NEW")
                print(f"│ Assignment No.{self.total_assignments + 1}")
                print("│")
                self.print_scores()
                print("│")
                #print(f"├{'─'*30}")


        else:

            # (Row, Col) is from self.set_first_assignment()
            if state == "first_assignment":

                # (Row, Col) are the pos of 'S'
                if direction == 'd':

                    calculated_scores = {

                        'topside': starting_row,
                        'bottomside': (size - 2) - starting_row - 1,
                        'rightside': (size - 2) - starting_col,
                        'leftside': starting_col - 1
                    
                    }


                elif direction == 'u':

                    calculated_scores = {

                        'topside': starting_row - 2,
                        'bottomside': (size - 2) - starting_row + 1,
                        'rightside': (size - 2) - starting_col,
                        'leftside': starting_col - 1
                    
                    }
                

                elif direction == 'l':

                    calculated_scores = {
                        
                        'topside': starting_row - 1,
                        'bottomside': (size - 2) - starting_row,
                        'rightside': (size - 2) - starting_col + 1,
                        'leftside': starting_col - 2
                    
                    }
                
                
                elif direction == 'r':

                    calculated_scores = {

                        'topside': starting_row - 1,
                        'bottomside': (size - 2) - starting_row,
                        'rightside': (size - 2) - starting_col - 1,
                        'leftside': starting_col
                    
                    }


                self.scores = calculated_scores


            else:

                scores = self.scores


                if direction == 'd':

                    new_topside_score = scores.get('topside') + 1
                    new_bottomside_score = scores.get('bottomside') - 1


                    self.scores['topside'] = new_topside_score
                    self.scores['bottomside'] = new_bottomside_score


                elif direction == 'u':

                    new_topside_score = scores.get('topside') - 1
                    new_bottomside_score = scores.get('bottomside') + 1


                    self.scores['topside'] = new_topside_score
                    self.scores['bottomside'] = new_bottomside_score


                elif direction == 'r':

                    new_rightside_score = scores.get('rightside') - 1
                    new_leftside_score = scores.get('leftside') + 1


                    self.scores['rightside'] = new_rightside_score
                    self.scores['leftside'] = new_leftside_score


                elif direction == 'l':

                    new_rightside_score = scores.get('rightside') + 1
                    new_leftside_score = scores.get('leftside') - 1


                    self.scores['rightside'] = new_rightside_score
                    self.scores['leftside'] = new_leftside_score   



    #@@@@@  TODO: USE self._chosen_cell_pos and self._selected_cell_info 
    def set_first_assingment_and_direction(
            
            self,
            tuple_pos: tuple | bool= False,
            direction: str | bool= False,
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
                
                ROW = tuple_pos[0]
                COL = tuple_pos[1]
                AVAILABLE_DIRECTIONS = _get_direction_validation(ROW, COL)

                self.change_starting(

                    row= ROW,
                    col= COL
                
                )

                if print_console:
                    print(f"~ 'S' at: (ROW: {ROW}, COL: {COL})")


            elif custom_start == False:


                if print_console:
                    print("~ self.set_first_assignment()")


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
                    print(f"\n~ Located state point\n  'S' at: (ROW: {ROW}, COL: {COL})")


            # Starting direction
            if custom_direction == True:
            
                RANDOM_VALID_DIRECTION = direction


                if print_console:
                    print(f"~ Selected direction: {RANDOM_VALID_DIRECTION}")


            elif custom_direction == False:

                RANDOM_VALID_DIRECTION = random.choice(AVAILABLE_DIRECTIONS)


                if print_console:
                    print(f"\n~ AVAILABLE_DIRECTIONS: {AVAILABLE_DIRECTIONS}")
                    print(f"~ RANDOMLY SELECTED DIRECTION: {RANDOM_VALID_DIRECTION}")


            if print_console:
                print()
            

            return size, grid, RANDOM_VALID_DIRECTION, ROW, COL


        size = self.size
        grid = self.grid


        if print_console:

            print(f"\n{"♦"*50}\n{"♦"*12} FIRST ASSIGNMENT PRINTING {"♦"*11}\n{"♦"*50}")
            print(f"tuple_pos: {tuple_pos}\ndirection: {direction}\nprint_console: {print_console}\n")


            # Determining conditions for first assignment
            if tuple_pos and direction:

                Conditions = (True, True)


            elif tuple_pos:

                Conditions = (True, False)


            elif direction:

                Conditions = (False, True)

            
            else:

                Conditions = (False, False)


            size, grid, RANDOM_VALID_DIRECTION, ROW, COL = first_assignment(Conditions[0], Conditions[1])


            # All of these should be = FALSE, due to the self.assignments being empty
            previous_assignment = self.previous_assignment()

            try:
                
                previous_direction = previous_assignment[0][1]
                previous_pos = previous_assignment[1]
            

            except:
                
                previous_direction = False
                previous_pos = False


            print(f"previous_direction: {previous_direction}")
            print(f"previous_pos: {previous_pos}")


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


            # Assigning direction.
            print(f"\n• ASSIGNING: {factored_direction_data}", end=" ")
            grid[ chosen_row ][ chosen_col ] = self.arrows.get(factored_direction_data)
            print("✅ >> DONE!\n")


            # Logging assignments
            print(f"\n• LOGGING: {factored_direction_data}\n")
            self.log_assignments(

                current_direction= RANDOM_VALID_DIRECTION,
                starting_row= ROW,
                starting_col= COL,
                previous_pos= previous_pos,
                factoring_value= factoring_value,
                factored_direction_data= factored_direction_data,
                print_console= print_console

            )
            print("✅ >> DONE!\n")


            # Calculating scores for the first assignment
            print(f"\n• CALCULATING SCORE FOR: {factored_direction_data}\n")
            self.score_calculator(

                direction= factored_direction_data,
                starting_row= ROW,
                starting_col= COL,
                state= "first_assignment",
                print_console= print_console

            )
            print("✅ >> DONE!\n")


            # Last assignment log
            print(f"\n• PREVIOUS LOGGED ASSIGNMENT: {self.previous_assignment()}\n")
            

            self.print_grid()


            print(f"\n{"♦"*50}\n{"♦"*50}\n{"♦"*50}\n")


        else:

            # Determining conditions for first assignment
            if tuple_pos and direction:

                Conditions = (True, True)


            elif tuple_pos:

                Conditions = (True, False)


            elif direction:

                Conditions = (False, True)

            
            else:

                Conditions = (False, False)


            size, grid, RANDOM_VALID_DIRECTION, ROW, COL = first_assignment(Conditions[0], Conditions[1])


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


            # Assigning direction.
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

                direction= factored_direction_data,
                starting_row= ROW,
                starting_col= COL,
                state= "first_assignment",
                print_console= print_console

            )





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
        
            confirmed_directions = self.assignor.validate_direction()
            # TESTING
            confirmed_directions = random.choice(["r"])
        

            # This is not stable, remake
            assignment_state, final_direction = self.assignor.assign(
                
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






    def change_starting(self, row= int, col= int) -> None:
        
        for rows in range(self.size):
            
            if rows == 0:
                continue

            for cols in range(self.size):

                if cols == 0 or cols == self.size - 1:
                    continue

                self.grid[rows][cols] = " "

            break

        self.grid[row][col] = "S"


    def create_grid(self, size):

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




    def print_assignments(self):

        print("\n--- ALL ASSIGNMENTS | MAZE SOLUTION @Maze().assignments ---\n")


        total_directions = 1
        for key, value in self.assignments.items():

            print(f"  •{total_directions: <10} {"   ->   "} •direction: ({key})  •grid_pos: {value}")
            total_directions += 1
        
        
        print()


    def print_scores(self):
        for key, value in self.scores.items():
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


    def print_maze(self):

        for row in self.maze:

            for col in row:

                print(col, end= " ")


            print()
        

        print()


    def previous_assignment(self) -> dict | bool:

        if len(self.assignments) > 0:

            last_assignment_key = list(self.assignments.keys())[-1]
            last_assignment_value = list(self.assignments.values())[-1]
            previous_assignment = [last_assignment_key, (last_assignment_value[0], last_assignment_value[1])]


            return previous_assignment
        

        return False



    def reset_all(self):

        self.available_directions = ["l", "r", "u", "d"]
        self.random_direction = random.choice(self.available_directions)
        self.total_assignments = 0
        self.assignments = {}
        self.scores = {
            'topside': 0,
            'bottomside': 0,
            'leftside': 0,
            'rightside':0
        }
        self.grid = self.create_grid(self.size)
        self.assignor = Assignment(self)
        self.first_direction_completed = False
        return




#Maze(20).print_grid()
#a.set_first_assingment_and_direction((4, 10))
#Maze(50).print_maze()
#a = Maze(25)
#a.print_grid()
Maze(30, False).print_maze()

