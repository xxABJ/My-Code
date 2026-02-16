import pygame, random


class Maze:


    def __init__(self, size):
        
        self.size = size


        self.available_directions = ["l", "r", "u", "d"]
        self.random_direction = random.choice(self.available_directions)
        
        
        self.directions = {
            'l': pygame.Vector2(-1, 0),
            'r': pygame.Vector2(1, 0),
            'u': pygame.Vector2(0, -1),
            'd': pygame.Vector2(0, 1)
        }


        self.assignments = {

        }


        self.scores = {
            'topside': 0,
            'bottomside': 0,
            'leftside': 0,
            'rightside':0
        }
        #self.topside_score = 0
        #self.bottomside_score = 0
        #self.leftside_score = 0
        #self.rightside_score = 0





        self.grid = self.create_grid(self.size)


        self.maze_completed = False
        self.maze = self.create_maze(self.grid[:])


    def scanner(growx, gcoly, i_d, size):


        #for rows in grid:
        #
        #    #if rows == 0 or rows == len(grid)-1:
        #    #    continue
        #
        #    for col in rows:
        #
        #        #if col == 0 or col == len(rows)-1:
        #        #    continue
        #
        #        if col == "S":
        #            choices = ['down', 'right', 'left']
        #
        #            if random.choice(choices) == 'down':
        #
        #
        #                #if not self.done:
        #                x_start_point = grid[grid.index(rows)+1][rows.index(col)]
        #                y_start_point = rows.index(col)
        #                # logic for dynamic size setting + logic for alternative size setting when required
        #                scangrid_size = (len(rows) - rows.index(col))
        #                scanner(x_start_point, y_start_point, 'down', scangrid_size)
        #
        #
        #            elif random.choice(choices) == 'right':
        #                start_point = grid[grid.index(rows)][rows.index(col)-1]
        #
        #
        #            elif random.choice(choices) == 'left':
        #                start_point = grid[grid.index(rows)][rows.index(col)+1]


        directions = ['l', 'r', 'u', 'd']
        

        row_marker = 0
        col_marker = 0
        for s_row in range(size):

            for s_col in range(size):

                try:

                    d = random.choice(directions)

                    # Start=down
                    if i_d == 'down':
                        
                        x, y = 1, 0


                        if d == 'l':

                            if s_row + row_marker == 0 and s_col == 0:
                                
                                grid[x + s_row][y + s_col] = d
                                continue


                            else:

                                if grid[x + s_row][y + s_col-1] != "|":

                                    if grid[x + s_row][y + s_col-1] == 'l':
                                        
                                        grid[x + s_row][y + s_col-2] = d
                                        continue


                                    elif grid[x + s_row][y + s_col-1] == 'r' or grid[x + s_row][y + s_col-1] == 'u' or grid[x + s_row][y + s_col-1] == 'd':

                                        continue


                                else:

                                    continue


                        elif d == 'r':

                            if s_row == 0 and s_col == 0:
                                
                                grid[x + s_row][y + s_col] = d
                                continue


                            else:

                                if grid[x + s_row][y + s_col+1] != "|":

                                    if grid[x + s_row][y + s_col-1] == 'r':
                                        
                                        grid[x + s_row][y + s_col] = d
                                        continue


                                    elif grid[x + s_row][y + s_col-1] == 'l' or grid[x + s_row][y + s_col-1] == 'u' or grid[x + s_row][y + s_col-1] == 'd':
                                        
                                        break


                                elif grid[x + s_row][y + s_col+1] == "|":

                                    while d == 'r' or d == 'l':

                                        d = random.choice(directions)


                                        if grid[x + s_row-1][y + s_col] == "|" and d == 'u':
                                            
                                            d = random.choice(directions)
                                            continue
                                        
                                        
                                        # intersection inevitable
                                        # also WHAT ABOUT (S_ROW -2 == an assigned direction) when 'u' is a forced next assignment, because path got cornered :'(( !!!!
                                        # or solution: go left until finish XD, then execute random walls w/ skipping pathing
                                        elif grid[x + s_row+1][y + s_col] == "|" and d == 'd':
                                            
                                            d = random.choice(directions)
                                            continue


                                        continue
                                    

                                    grid[x + s_row][y + s_col] = d
                                    continue


                        elif d == 'u':

                            if s_row + row_marker == 0 and s_col == 0:
                                
                                while d == 'u':
                                    
                                    d = random.choice(directions)
                                    grid[x + s_row + row_marker][y + s_col] = d
            
                                continue


                            else:

                                if grid[x + s_row + row_marker][y + s_col-1] != "|":

                                    if grid[x + s_row + row_marker][y + s_col-1] == 'r':
                                        
                                        grid[x + s_row + row_marker][y + s_col] = d
                                        continue


                                    elif grid[x + s_row + row_marker][y + s_col-1] == 'l':

                                        if grid[x + s_row + row_marker][y + s_col-2] != "|":
                                            
                                            grid[x + s_row + row_marker][y + s_col-2] = d
                                            continue

                                    
                                    elif grid[x + s_row + row_marker][y + s_col-1] == 'u':
                                        
                                        row_marker -= 1
                                        
                                        if grid[x + s_row + row_marker-1][y + s_col-1] != "|":
                                        
                                            grid[x + s_row + row_marker][y + s_col-1] == d
                                            row_marker += 1
                                            continue


                                        elif grid[x + s_row + row_marker][y + s_col-1] != "|":
                                            grid[x + s_row + row_marker][y + s_col-1] == d
                                            continue


                                        else:

                                            while d == 'u':
                                                
                                                d = random.choice(directions)
                                                if grid[x + s_row][y + s_col-1] == "|" and d == 'l':
                                                    d = random.choice(directions)
                                                    continue

                                                elif grid[x + s_row][y + s_col+1] == "|" and d == 'r':
                                                    d = random.choice(directions)
                                                    continue
                                            
                                            grid[x + s_row + row_marker][y + s_col] = d

                                            row_marker += 1
                                            continue


                                    elif grid[x + s_row + row_marker][y + s_col-1] == 'd':

                                        continue


                                else:

                                    continue


                        elif d == 'd':

                            if s_row + row_marker == 0 and s_col == 0:

                                grid[x + s_row + row_marker][y + s_col] = d
                                continue


                            else:

                                if grid[x + s_row + row_marker][y + s_col-1] != "|":

                                    if grid[x + s_row + row_marker][y + s_col-1] == 'r':
                                        
                                        grid[x + s_row + row_marker][y + s_col] = d
                                        continue


                                    elif grid[x + s_row + row_marker][y + s_col-1] == 'l':

                                        if grid[x + s_row + row_marker][y + s_col-2] != "|":
                                            
                                            grid[x + s_row + row_marker][y + s_col-2] = d
                                            continue

                                    
                                    elif grid[x + s_row + row_marker][y + s_col-1] == 'd':

                                        row_marker += 1
                                        
                                        if grid[x + s_row + row_marker][y + s_col+2] != "|":
                                        
                                            grid[x + s_row + row_marker][y + s_col-1] == d
                                            row_marker += 1
                                            continue




                    #Start=right
                    elif i_d == 'right':

                        x, y = 0, 1

                        if d == 'l':


                            continue


                        elif d == 'r':


                            continue


                        elif d == 'u':


                            continue


                        elif d == 'd':


                            continue


                    
                    
                    #Start=left
                    elif i_d == 'left':

                        x, y = 0, -1

                        if d == 'l':


                            continue


                        elif d == 'r':


                            continue


                        elif d == 'u':


                            continue


                        elif d == 'd':


                            continue


                except:
                    continue

                row_marker += 1


    def score_assessment(self, choice) -> list:

        if len(self.assignments) > 0:

            last_assignment_key = list(self.assignments.keys())[-1]
            last_assignment_value = list(self.assignments.values())[-1]
            #pending_assignment = self.grid[last_assignment_value.x + self.directions[choice].x][last_assignment_value.y + self.directions[choice].y]
            pending_assignment = (last_assignment_value.x + self.directions[choice].x, last_assignment_value.y + self.directions[choice].y)


            top_side = last_assignment_value.x
            bottom_side = len(self.grid) - last_assignment_value.x
            left_side = last_assignment_value.y
            right_side = len(self.grid) - last_assignment_value.y


            self.topside_score = top_side
            self.bottomside_score = bottom_side
            self.leftside_score = left_side
            self.rightside_score = right_side

            return pending_assignment
        
        return False


    def create_maze(self, grid):

        while not self.maze_completed:

            pending_assessment = self.score_assessment(self.random_direction)
            

            # Assigning the first direction
            if pending_assessment == False:

                print(f"\n{"-"*20}\npending_assessment: {pending_assessment}\n")


                for row in range(len(grid)):
                    
                    # Break after assigning the first direction
                    if len(self.assignments) > 0:
                        
                        break

                    
                    # Skip if at horizontal side-border
                    if row == 0 or row == len(grid) - 1:
                        
                        print(f"row:{row} horizontal side-borders")
                        continue
                    

                    print("in")
                    for col in range(len(grid)):

                        # Skip if at vertical side-borders
                        if col == 0 or col == len(grid) - 1:
                            
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

                                #print('can both')
                                available_directions = ("l", "r", "d")


                            else:

                                # Cannot assign to the left
                                if grid[row][col - 1] == "|":
                                    
                                    available_directions = ("r", "d")
                                    #available_directions.pop(0)
                                    #print('can not left')


                                # Cannot assign to the right
                                elif grid[row][col + 1] == "|":

                                    available_directions = ("l", "d")
                                    #available_directions.pop(1)
                                    #print('can not right')


                            # Starting point
                            self.random_direction = random.choice(available_directions)


                            # Assigning direction. The vectors ([pygame] .x, .y) below are reversed when indexing, due to the grid's iteration method.
                            grid[row + int(self.directions[self.random_direction].y)][col + int(self.directions[self.random_direction].x)] = self.random_direction


                            # Logging assignments
                            self.assignments[self.random_direction] = tuple(
                               
                                a + b for a, b in zip(
                                    ( row, col ),
                                    ( (row + int(self.directions[self.random_direction].y) - row, (col + int(self.directions[self.random_direction].x) - col)) )
                                    
                                ))
                            

                            break


                break
            #else:
                #self.maze_completed = true


        self.print_assignments()
        return grid


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


#Maze(20).print_grid()
Maze(30).print_maze()

