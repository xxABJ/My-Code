import random


class Up:


    class assigner:

        def __init__(self, up_factory, num =False):

            self.up_factory = up_factory


            if num:

                self.amount_of_moves = num

        
        def assign(self):

            grid = self.up_factory.maze.grid[:]
            previous_assignment = self.up_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                grid[previous_pos[0] - assignments][previous_pos[1]] = "↑"
                
                
                updated_previous_pos = (

                    previous_pos[0] - (assignments - 1),
                    previous_pos[1]

                )
                

                self.up_factory.maze.log_assignments(

                    direction= "u",
                    previous_pos= updated_previous_pos

                )


                self.up_factory.maze.score_calculator(

                    direction= "u",
                    state= ""

                )
                #print(assignments)


            self.up_factory.maze.grid = grid


    def __init__(self, maze):
        
        self.maze = maze


        self.side_wall_directions = ["l", "r"]


        self.up_assigner = None


    def check(self):
        
        previous_assignment = self.up_factory.maze.previous_assignment()
        score = self.maze.scores.get('topside')


        if score >= 3 and previous_assignment[0][1] != "d":
            
            num = random.randint(1, 3)


        elif score == 2:
            
            num = random.randint(1, 2)


        elif score == 1:
            
            num = 1


        else:
            
            # Opposite directions
            if previous_assignment[0][1] == "d":

                return

            # Side-wall detection
            elif score == 0:
                
                return self.alternative_directions


        self.up_assigner = Up.assigner(self, num)
        print(f"{" "*num}{num} Up moves - assigned")
        self.assign()


        self.up_assigner = None
        return False
    

    def check2(self):
        
        #previous_assignment = self.up_factory.maze.previous_assignment()
        #score = self.maze.scores.get('topside')
        previous_direction = self.up_factory.maze.previous_assignment()[0][1]

        while self.invalid:
            directions = self.get_cell_info2(previous_direction)

        self.assignment(directions)

        
        
        #if score >= 3 and previous_assignment[0][1] != "d":
        #    
        #    num = random.randint(1, 3)
        #
        #
        #elif score == 2:
        #    
        #    num = random.randint(1, 2)
        #
        #
        #elif score == 1:
        #    
        #    num = 1
        #
        #
        #else:
        #    
        #    # Opposite directions
        #    if previous_assignment[0][1] == "d":
        #
        #        return
        #
        #    # Side-wall detection
        #    elif score == 0:
        #        
        #        return self.alternative_directions


        self.up_assigner = Up.assigner(self, num)
        print(f"{" "*num}{num} Up moves - assigned")
        self.assign()


        self.up_assigner = None
        return False


    def assign(self):
        
        return self.up_assigner.assign()

