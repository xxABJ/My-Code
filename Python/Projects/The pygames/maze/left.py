import random


class Left:


    class assigner:

        def __init__(self, left_factory, num =False):

            self.left_factory = left_factory


            if num:

                self.amount_of_moves = num

        
        def assign(self):

            grid = self.left_factory.maze.grid[:]
            previous_assignment = self.left_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                grid[previous_pos[0]][previous_pos[1] - assignments] = "←"
                
                
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


        self.left_assigner = None


    def check(self):
        
        score = self.maze.scores.get('leftside')


        if score >= 3:
            
            num = random.randint(1, 3)


        elif score == 2:
            
            num = random.randint(1, 2)


        elif score == 1:
            
            num = 1


        elif score == 0:
            
            return self.alternative_directions


        self.left_assigner = Left.assigner(self, num)
        print(f"{" "*num}{num} left moves - assigned")
        self.assign()


        self.left_assigner = None
        return False


    def assign(self):
        
        return self.left_assigner.assign()
    

    