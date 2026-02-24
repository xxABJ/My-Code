from assignment import *


import pygame, random


class Maze:


    def __init__(self, size):
        
        self.size = size

        self.arrows = {

           "l": "←",
           "r": "→",
           "u": "↑",
           "d": "↓"

        }


        self.available_directions = ["l", "r", "u", "d"]
        self.random_direction = random.choice(self.available_directions)
        
        # These tuples are based on how grid is being iterated in / how it was created
        self.directions = {
            'l': (0, -1),
            'r': (0, 1),
            'u': (-1, 0),
            'd': (1, 0)
        }

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
        #self.right = Right(self)
        #self.left = Left(self)
        #self.up = Up(self)
        #self.down = Down(self)


        self.first_direction_completed = False
        self.maze_completed = False
        self.maze = self.create_maze(self.size)
        

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


    def previous_assignment(self) -> list:

        if len(self.assignments) > 0:

            last_assignment_key = list(self.assignments.keys())[-1]
            last_assignment_value = list(self.assignments.values())[-1]
            previous_assignment = [last_assignment_key, (last_assignment_value[0], last_assignment_value[1])]


            return previous_assignment
        

        return False


    #TODO: ADD SPECIAL LOGIC FOR ASSIGNMENT AFTER CHANGING DIRECTION
    # (AFTER THE ASIIGNMENT [i.e → > ↓ ] = Normally it's logger = (0, 1) for concurring same direction, but for changing directions ..
    # It should be: *ADDITIONAL additional_logger = logger(i.e for → > ↓) = (1, 0)
    def log_assignments(self, direction, row= None, col= None, previous_pos= False):
        
        new_total_assignments = self.total_assignments + 1


        if previous_pos:
            
            row = previous_pos[0]
            col = previous_pos[1]


            print("logger:", (row, col))
            print("logger2:", ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col ))

            self.assignments[(new_total_assignments, direction)] = tuple(
                
                a + b for a, b in zip(
                    
                    ( row, col ),
                    ( row + self.directions[direction][0] - row, col + self.directions[direction][1] - col )
                    
                    ))
        
        
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


        # Accounting for maze border walls
        if state == 'first':

            size = self.size


            if direction == 'd':

                calculated_scores = {

                    'topside': row,
                    'bottomside': (size - 2) - row - 1,
                    'leftside': col - 1,
                    'rightside': (size - 2) - col
                
                }
            

            elif direction == 'l':

                calculated_scores = {
                    
                    'topside': row - 1,
                    'bottomside': (size - 2) - row,
                    'leftside': col - 2,
                    'rightside': (size - 2) - col + 1
                
                }
            
            
            elif direction == 'r':

                calculated_scores = {

                    'topside': row - 1,
                    'bottomside': (size - 2) - row,
                    'leftside': col,
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



    def create_maze(self, size):

        grid = self.grid

        #while True:

            #grid = self.create_grid(self.size)

        while not self.first_direction_completed:

            previous_assignment = self.previous_assignment()
            
            self.change_starting(1, self.size // 2) ### TESTING
            #self.change_starting(self.size - 2) ### TESTING

            # Assigning the first direction
            if previous_assignment == False:

                print(f"\n{"-"*20}\nprevious_assignment: {previous_assignment}\n")


                for row in range(size):
                    
                    # Break after assigning the first direction
                    if len(self.assignments) > 0:
                        
                        self.first_direction_completed = True
                        break

                    
                    # Skip if at horizontal side-border
                    #if row < 5 or row == size - 1:
                    if row == 0 or row == size - 1:
                        
                        print(f"row:{row} horizontal side-borders")
                        continue
                    

                    print("in")
                    for col in range(size):

                        # Skip if at vertical side-borders
                        if col == 0 or col == size - 1:
                            
                            print(f"{" "*5}col:{col} vertical side-borders")
                            continue


                        # Skip if not at the starting point
                        elif grid[row][col] != "S":
                            
                            print(f"{" "*5}col:{col} not 'S'")
                            continue


                        else:

                            print(f"{" "*5}col:{col} found 'S'")
                            #available_directions = ["l", "r", "d"]


                            # Can assign any direction opposite the starting area (exclude 'u' direction, if "S" is at top / exclude 'd' direction, if "S" is at bottom) @Maze().create_grid()
                            if grid[row][col - 1] != "|" and grid[row][col + 1] != "|":

                                available_directions = ["l", "r", "d"]
                                #print('can both')


                            else:

                                # Cannot assign to the left
                                if grid[row][col - 1] == "|":
                                    
                                    available_directions = ["r", "d"]
                                    #print('can not left')


                                # Cannot assign to the right
                                elif grid[row][col + 1] == "|":

                                    available_directions = ["l", "d"]
                                    #print('can not right')


                            # Starting point
                            self.random_direction = random.choice(available_directions)
                            #self.random_direction = "d" ### TESTING


                            # Assigning direction. (Opposites due to how it is iterated into)
                            print(f"\nassigning: {self.random_direction}\n")
                            grid[ row + self.directions[self.random_direction][0] ][ col + self.directions[self.random_direction][1] ] = self.arrows.get(self.random_direction)


                            # Logging assignments
                            self.log_assignments(

                                direction= self.random_direction,
                                row= row,
                                col= col,

                            )


                            # Updating scores
                            print(" • FIRST ASSIGNMENT")
                            self.score_calculator(self.random_direction, row= row, col= col, state= 'first')


                            break


            #self.random_direction = random.choice(self.available_directions)
            
            
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



        #num_of_assignments = 1
        #num_of_tries = 0
        #while not self.assignor.at_bottom:
        #
        #    previous_assignment = self.previous_assignment()
        #
        #    confirmed_directions = self.assignor.validate_direction(previous_assignment)
        #    
        #    while self.assignor.assign(confirmed_directions, previous_assignment, num_of_assignments) == False:
        #
        #        if num_of_tries > 100 or num_of_assignments > 1000:
        #            break
        #
        #        num_of_tries +=1
        #        self.assignor.assign(confirmed_directions, previous_assignment, num_of_assignments)
        #
        #        continue
        #
        #
        #    num_of_assignments += 1
        #
        #    if num_of_tries > 100:
        #        #self.reset_all()
        #        break
        #
        #
        #    elif num_of_assignments > 1000:
        #        #self.reset_all()
        #        break
        #
        #
        #if len(self.assignments) > 500 or num_of_tries > 100 or num_of_assignments > 1000 or self.assignor.at_bottom != True:
        #    print(f"{"\n"*10}RESET{"\n"*10}")
        #    self.reset_all()
        #    continue
        #
        #else:
        #
        #    break

        
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

        for row in self.grid:

            for col in row:

                print(col, end= " ")


            print()


    def print_maze(self):

        for row in self.maze:

            for col in row:

                print(col, end= " ")


            print()
        

        print()


#Maze(20).print_grid()
Maze(20).print_maze()
#Maze(50).print_maze()

