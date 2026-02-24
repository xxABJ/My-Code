import random


class Down:


    class assigner:

        def __init__(self,down_factory, num =False):

            self.down_factory = down_factory


            if num:

                self.amount_of_moves = num

        
        def assign(self):

            grid = self.down_factory.maze.grid[:]
            previous_assignment = self.down_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                grid[previous_pos[0] + assignments][previous_pos[1]] = "↓"
                
                
                updated_previous_pos = (

                    previous_pos[0] + (assignments - 1),
                    previous_pos[1]

                )
                

                self.down_factory.maze.log_assignments(

                    direction= "d",
                    previous_pos= updated_previous_pos

                )


                self.down_factory.maze.score_calculator(

                    direction= "d",
                    state= ""

                )
                #print(assignments)


            self.down_factory.maze.grid = grid


    def __init__(self, maze):
        
        self.maze = maze


        self.direction = ""
        self.alternative_directions = ["l", "r"]


        self.down_assigner = None


    def check(self):
        
        score = self.maze.scores.get('bottomside')


        if score >= 3:
            
            num = random.randint(1, 3)


        elif score == 2:
            
            num = random.randint(1, 2)


        elif score == 1:
            
            num = 1


        elif score == 0:
            
            return self.alternative_directions


        self.down_assigner = Down.assigner(self, num)
        print(f"{" "*num}{num} Down moves - assigned")
        self.assign()


        self.down_assigner = None
        return False


    def assign(self):
        
        return self.down_assigner.assign()
    