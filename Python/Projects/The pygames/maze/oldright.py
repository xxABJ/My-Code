
class r1:

    def __init__(self, right_factory):

        self.right_factory = right_factory

    
    def assign(self):

        grid = self.right_factory.maze.grid[:]
        previous_assignment = self.right_factory.maze.previous_assignment()
        previous_pos = previous_assignment[1]


        for assignments in range(1, 2):

            grid[previous_pos[0]][previous_pos[1] + assignments] = "r"
            
            
            updated_previous_pos = (
                previous_pos[0],
                previous_pos[1] + (assignments - 1)
            )
            

            self.right_factory.maze.log_assignments(

                direction= "r",
                previous_pos= updated_previous_pos

            )


            self.right_factory.maze.score_calculator(

                direction= "r",
                state= ""

            )
            #print(assignments)


        self.right_factory.maze.grid = grid


class r2:

    def __init__(self, right_factory):

        self.right_factory = right_factory

    
    def assign(self):

        grid = self.right_factory.maze.grid[:]
        previous_assignment = self.right_factory.maze.previous_assignment()
        previous_pos = previous_assignment[1]


        for assignments in range(1, 3):

            grid[previous_pos[0]][previous_pos[1] + assignments] = "r"
            
            
            updated_previous_pos = (
                previous_pos[0],
                previous_pos[1] + (assignments - 1)
            )
            

            self.right_factory.maze.log_assignments(

                direction= "r",
                previous_pos= updated_previous_pos

            )


            self.right_factory.maze.score_calculator(

                direction= "r",
                state= ""

            )
            #print(assignments)


        self.right_factory.maze.grid = grid


class r3:

    def __init__(self, right_factory):

        self.right_factory = right_factory

    
    def assign(self):

        grid = self.right_factory.maze.grid[:]
        previous_assignment = self.right_factory.maze.previous_assignment()
        previous_pos = previous_assignment[1]


        for assignments in range(1, 4):

            grid[previous_pos[0]][previous_pos[1] + assignments] = "r"
            
            
            updated_previous_pos = (
                previous_pos[0],
                previous_pos[1] + (assignments - 1)
            )
            

            self.right_factory.maze.log_assignments(

                direction= "r",
                previous_pos= updated_previous_pos

            )


            self.right_factory.maze.score_calculator(

                direction= "r",
                state= ""

            )
            #print(assignments)


        self.right_factory.maze.grid = grid
