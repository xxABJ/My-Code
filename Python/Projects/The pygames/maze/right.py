class Right:


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


    def __init__(self, maze):
        
        self.maze = maze


        self.direction = ""
        self.alternative_directions = ["u", "d"]


        self.assignment = {
            1: Right.r1(self),
            2: Right.r2(self),
            3: Right.r3(self)
        }


    def check(self):
        
        score = self.maze.scores.get('rightside')


        if score >= 3:
            
            self.assign(3)
            print('   r3 - assigned')


        elif score == 2:
            
            self.assign(2)
            print('  r2 - assigned')


        elif score == 1:
            
            self.assign(1)
            print(' r1 - assigned')


        else:
            
            return self.alternative_directions


    def assign(self, num):
        
        return self.assignment.get(num).assign()