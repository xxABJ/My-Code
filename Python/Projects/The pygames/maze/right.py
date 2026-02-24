import random


class Right:


    class assigner:

        def __init__(self, right_factory, num = False):

            self.right_factory = right_factory


            if num:

                self.amount_of_moves = num

        
        def assign(self):

            grid = self.right_factory.maze.grid[:]
            previous_assignment = self.right_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                grid[previous_pos[0]][previous_pos[1] + assignments] = "→"
                
                
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


        self.right_assigner = None


    def check(self):
        
        score = self.maze.scores.get('rightside')


        if score >= 3:
            
            num = random.randint(1, 3)


        elif score == 2:
            
            num = random.randint(1, 2)


        elif score == 1:
            
            num = 1


        elif score == 0:
            
            return self.alternative_directions


        self.right_assigner = Right.assigner(self, num)
        print(f"{" "*num}{num} right moves - assigned")
        self.assign()


        self.right_assigner = None
        return False


    def assign(self):
        
        return self.right_assigner.assign()
    

