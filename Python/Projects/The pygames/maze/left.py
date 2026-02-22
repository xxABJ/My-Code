class Left:


    class l1:

        def __init__(self, left_factory):

            self.left_factory = left_factory

        
        def assign(self):

            grid = self.left_factory.maze.grid[:]
            previous_assignment = self.left_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 2):

                grid[previous_pos[0]][previous_pos[1] - assignments] = "l"
                
                
                updated_previous_pos = (
                    previous_pos[0],
                    previous_pos[1] - (assignments - 1)
                )
                

                self.left_factory.maze.log_assignments(

                    direction= "l",
                    previous_pos= updated_previous_pos

                )


                self.left_factory.maze.score_calculator(

                    direction= "l",
                    state= ""

                )
                #print(assignments)


            self.left_factory.maze.grid = grid


    class l2:

        def __init__(self, left_factory):

            self.left_factory = left_factory

        
        def assign(self):

            grid = self.left_factory.maze.grid[:]
            previous_assignment = self.left_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 3):

                grid[previous_pos[0]][previous_pos[1] - assignments] = "l"
                
                
                updated_previous_pos = (
                    previous_pos[0],
                    previous_pos[1] - (assignments - 1)
                )
                

                self.left_factory.maze.log_assignments(

                    direction= "l",
                    previous_pos= updated_previous_pos

                )


                self.left_factory.maze.score_calculator(

                    direction= "l",
                    state= ""

                )
                #print(assignments)


            self.left_factory.maze.grid = grid


    class l3:

        def __init__(self, left_factory):

            self.left_factory = left_factory

        
        def assign(self):

            grid = self.left_factory.maze.grid[:]
            previous_assignment = self.left_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 4):

                grid[previous_pos[0]][previous_pos[1] - assignments] = "l"
                
                
                updated_previous_pos = (
                    previous_pos[0],
                    previous_pos[1] - (assignments - 1)
                )
                

                self.left_factory.maze.log_assignments(

                    direction= "l",
                    previous_pos= updated_previous_pos

                )


                self.left_factory.maze.score_calculator(

                    direction= "l",
                    state= ""

                )
                #print(assignments)


            self.left_factory.maze.grid = grid


    def __init__(self, maze):
        
        self.maze = maze


        self.direction = ""
        self.alternative_directions = ["u", "d"]


        self.assignment = {
            1: Left.l1(self),
            2: Left.l2(self),
            3: Left.l3(self)
        }


    def check(self):
        
        score = self.maze.scores.get('leftside')


        if score >= 3:
            
            self.assign(3)
            print('   l3 - assigned')


        elif score == 2:
            
            self.assign(2)
            print('  l2 - assigned')


        elif score == 1:
            
            self.assign(1)
            print(' l1 - assigned')


        else:
            
            return self.alternative_directions


    def assign(self, num):
        
        return self.assignment.get(num).assign()