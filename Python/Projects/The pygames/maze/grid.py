from assignment import *


import pygame, random


class Maze:


    def __init__(self, size):
        
        self.size = size


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
            'leftside': 0,
            'rightside':0

        }


        self.total_assignments = 0
        self.assignments = {}


        self.arrows = {

           "l": "←",
           "r": "→",
           "u": "↑",
           "d": "↓"

        }


        self.assignor = Assignment(self)


        self.grid = self.create_grid(self.size)
        self.first_assignment_and_direction_completed = self.set_first_assingment_and_direction(

            tuple_pos= False,
            direction= False,
            print_console = False

        )


        self.maze_completed = False
        #self.maze = self.create_maze(self.size)
        


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




    def previous_assignment(self) -> dict | bool:

        if len(self.assignments) > 0:

            last_assignment_key = list(self.assignments.keys())[-1]
            last_assignment_value = list(self.assignments.values())[-1]
            previous_assignment = [last_assignment_key, (last_assignment_value[0], last_assignment_value[1])]


            return previous_assignment
        

        return False




    #TODO: ADD SPECIAL LOGIC FOR ASSIGNMENT AFTER CHANGING DIRECTION
    # (AFTER THE ASIIGNMENT [i.e → > ↓ ] = Normally it's logger = (0, 1) for concurring same direction, but for changing directions ..
    # It should be: *ADDITIONAL additional_logger = logger(i.e for → > ↓) = (1, 0)
    def log_assignments(self, direction, row= None, col= None, previous_pos= False, changing_directions = False):
        
        new_total_assignments = self.total_assignments + 1


        if changing_directions:
            
            row = previous_pos[0]
            col = previous_pos[1]


            if changing_directions == "r>d":

                direction1 = "r"
                direction2 = "d"

                print("2  r>d  logger:", (row, col))
                print("2  r>d  logger2:", ( row + (self.directions[direction1][0]) - row, col + (self.directions[direction1][1]) - col ))


                self.assignments[(new_total_assignments, direction2)] = tuple(
                    
                    a + b for a, b in zip(
                        
                        ( row, col ),
                        ( row + self.directions[direction1][0] - row, col + self.directions[direction1][1] - col )
                        
                        ))
        
            elif changing_directions == "d>r":
                
                direction1 = "d"
                direction2 = "r"

                print("  2  d>r   before logger edit:", (row, col))
                print("  2  d>r   logger edit:", ( row + self.directions[direction1][0] - row, col + self.directions[direction1][1] - col ))

                self.assignments[(new_total_assignments, direction2)] = tuple(
                    
                    a + b for a, b in zip(
                        
                        ( row, col ),
                        ( row + self.directions[direction1][0] - row, col + self.directions[direction1][1] - col )
                        
                        ))
                
                print("  2  d>r   after logger edit:", tuple(
                    
                    a + b for a, b in zip(
                        
                        ( row, col ),
                        ( row + self.directions[direction1][0] - row, col + self.directions[direction1][1] - col )
                        
                        )))



        elif not changing_directions and previous_pos:
            
            row = previous_pos[0]
            col = previous_pos[1]


            print(direction)

            print("  before logger edit:", (row, col))
            print("  logger edit:", ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col ))

            self.assignments[(new_total_assignments, direction)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( row, col ),
                    ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col )
                    
                    ))
            
            print("  after logger edit:", tuple(
                
                a + b for a, b in zip(
                    
                    ( row, col ),
                    ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col )
                    
                    )))

        
        
        else:
            
            
            self.assignments[(new_total_assignments, direction)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( row, col ),
                    ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col )
                    
                    ))


        self.total_assignments = new_total_assignments




    def score_calculator(self, direction, row= None, col= None, state = ''):

        # Printing old scores
        #print()
        #print("-"*20)
        #print(f"-- OLD")
        #print(f"-- Assignment No.{self.total_assignments - 1}")
        #self.print_scores()


        # (Row, Col) is from self.set_first_assignment()
        if state == 'first':

            size = self.size


            if direction == 'd':

                calculated_scores = {

                    'topside': row - 1,
                    'bottomside': (size - 2) - row - 1,
                    'leftside': col - 1,
                    'rightside': (size - 2) - col
                
                }


            elif direction == 'u':

                calculated_scores = {

                    'topside': row - 2,
                    'bottomside': (size - 2) - row,
                    'leftside': col - 1,
                    'rightside': (size - 2) - col
                
                }
            

            elif direction == 'l':

                calculated_scores = {
                    
                    'topside': row - 1,
                    'bottomside': (size - 2) - row,
                    'leftside': col - 2,
                    'rightside': (size - 2) - col
                
                }
            
            
            elif direction == 'r':

                calculated_scores = {

                    'topside': row - 1,
                    'bottomside': (size - 2) - row,
                    'leftside': col - 1,
                    'rightside': (size - 2) - col - 1
                
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


        # Printing new scores
        #print(f"-- NEW")
        #print(f"-- Assignment No.{self.total_assignments}")
        #self.print_scores()
        #print()




    def set_first_assingment_and_direction(self, tuple_pos = False, direction = False, print_console = False):

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


                # Locator
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


                        # Skip if not at the starting point
                        elif grid[row][col] != "S":
                            
                            #print(f"{" "*5}col:{col} not 'S'")
                            continue


                        else:

                            #print(f"row:{row}")
                            #print(f"{" "*5}col:{col} found 'S'")
                            pass


                            ROW = row
                            COL = col
                            AVAILABLE_DIRECTIONS = _get_direction_validation(ROW, COL)
                            break

                
                if print_console:
                    print(f"~ 'S' at: (ROW: {ROW}, COL: {COL})")


            # Starting direction
            if custom_direction == True:
            
                self.random_direction = direction


                if print_console:
                    print(f"~ Selected direction: {direction}")


            elif custom_direction == False:

                self.random_direction = random.choice(AVAILABLE_DIRECTIONS)


                if print_console:
                    print(f"~ AVAILABLE_DIRECTIONS: {AVAILABLE_DIRECTIONS}")


            if print_console:
                print()
            
            
            return size, grid, AVAILABLE_DIRECTIONS, ROW, COL


        if print_console:
            print(f"\n{"♦"*50}")


        size = self.size
        grid = self.grid
        AVAILABLE_DIRECTIONS = str
        ROW = int
        COL = int


        if tuple_pos:

            Conditions = (True, False)


        if direction:

            Conditions = (False, True)


        if tuple_pos and direction:

            Conditions = (True, True)

        
        if not tuple_pos and not direction:

            Conditions = (False, False)



        size, grid, AVAILABLE_DIRECTIONS, ROW, COL = first_assignment(Conditions[0], Conditions[1])



        # Old Score
        if print_console:
            print(f"\n• OLD SCORE FOR: {self.random_direction}")
            self.print_scores()


        # Updating scores
        if print_console:
            print(f"\n• UPDATING SCORE FOR: {self.random_direction}")
        self.score_calculator(self.random_direction, row= ROW, col= COL, state= 'first')
        if print_console:
            self.print_scores()


        # Assigning direction.
        if print_console:
            print(f"\n• ASSIGNING: {self.random_direction}")
        grid[ ROW + self.directions[self.random_direction][0] ][ COL + self.directions[self.random_direction][1] ] = self.arrows.get(self.random_direction)



        # Logging assignments
        if print_console:
            print(f"\n• LOGGING: {self.random_direction}  > > >  ", end="")
        self.log_assignments(

            direction= self.random_direction,
            row= ROW,
            col= COL,

        )
        if print_console:
            print("DONE!")



        # Last assignment log
        if print_console:
            print(f"\n• PREVIOUS LOGGED ASSIGNMENT: {self.previous_assignment()}")

        
        if print_console:
            print(f"\n{"♦"*50}\n")
        
        
        
        Complete = True
        return Complete




    def create_maze(self, size):

        grid = self.grid
            
        #TEMP Unable to go 'u' after first direction has been assigned
        while self.random_direction == 'u' and len(self.assignments) == 1:
    
            self.random_direction = random.choice(self.available_directions)
            continue


        #self.random_direction = "u" ### TESTING
        ### TESTING
        print(f"\n • LOOPING ASSIGNMENTS\n")

        for _ in range(5):
        
            previous_assignment = self.previous_assignment()
        
            confirmed_directions = self.assignor.validate_direction(previous_assignment)
            confirmed_directions = random.choice(["r", "d"])
        
            if self.assignor.assign(confirmed_directions, previous_assignment, _) == False:
                print(f"\nINVALID SUCCESS No.{_+1}\n    {confirmed_directions}\n{"*"*20}\n")

        
            else:
                print(f"SUCCESS No.{_+1}\n    {confirmed_directions}\n{"-"*20}\n")
            #self.print_assignments()
            #self.print_grid()

        
        self.maze_completed = True
        print(f"self.maze_completed: {self.maze_completed}")




        print()
        self.print_assignments()
        return grid




    def change_starting(self, row, col):
        
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
        print("-"*20)
        for key, value in self.scores.items():
            print(key, value)
        print("-"*20)


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


#Maze(20).print_grid()
#a.set_first_assingment_and_direction((4, 10))
#Maze(50).print_maze()
a = Maze(25)
a.print_grid()

