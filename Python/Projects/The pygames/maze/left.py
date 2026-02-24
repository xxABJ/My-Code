import random


class Left:


    class assigner:

        def __init__(self, left_factory, num =False):

            self.left_factory = left_factory


            if num >= 0:

                self.amount_of_moves = num

        
        def assign(self):

            print(self.amount_of_moves)
            if self.amount_of_moves == 0:
                return False


            grid = self.left_factory.maze.grid[:]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                previous_assignment = self.left_factory.maze.previous_assignment()
                previous_pos = previous_assignment[1]
                current_selected_cell = (previous_pos[0], previous_pos[1])


                if grid[previous_pos[0]][previous_pos[1] - 1] == "S":

                    updated_previous_pos = (
                        current_selected_cell[0],
                        current_selected_cell[1]
                    )


                else:

                    match previous_assignment[0][1]:

                        #case self.left_factory.maze.arrows.get("l"):
                        #case "←":
                        case "l":

                            print(f"prev l: {previous_pos}")
                            

                            if len(self.left_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0], previous_pos[1] - 1)

                                grid[current_selected_cell[0]][current_selected_cell[1]] = self.left_factory.maze.arrows.get("l")


                                # pre = l
                                updated_previous_pos = (
                                    current_selected_cell[0],
                                    current_selected_cell[1] + 1
                                )
                                


                            else:

                                grid[current_selected_cell[0]][current_selected_cell[1]] = self.left_factory.maze.arrows.get("l")


                                # pre = l
                                updated_previous_pos = (
                                    current_selected_cell[0],
                                    current_selected_cell[1]
                                )
                                

                        #case self.left_factory.maze.arrows.get("d"):
                        #case "↓":
                        case "d":

                            print(f"prev d: {previous_pos}")
                            

                            if len(self.left_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0] + 1, previous_pos[1])


                            else:
                                pass


                            grid[current_selected_cell[0]][current_selected_cell[1]] = self.left_factory.maze.arrows.get("l")


                            # pre = d
                            updated_previous_pos = (
                                current_selected_cell[0],
                                current_selected_cell[1]
                            )
                        

                        #case self.left_factory.maze.arrows.get("u"):
                        #case "↑":
                        case "u":

                            print(f"prev u: {previous_pos}")

                            
                            if len(self.left_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0] - 1, previous_pos[1])


                            else:
                                pass


                            grid[current_selected_cell[0]][current_selected_cell[1]] = self.left_factory.maze.arrows.get("l")


                            # pre = u
                            updated_previous_pos = (
                                current_selected_cell[0],
                                current_selected_cell[1]
                            )
                        

                        #case self.left_factory.maze.arrows.get("r"):
                        # case "←":
                        case "r":
                            # should not be possible

                            print(f"invalid prev r: {previous_pos}")


                            if len(self.left_factory.maze.assignments) == 1:
                                updated_previous_pos = False


                            else:
                                updated_previous_pos = False
                

                if not updated_previous_pos:
                    return updated_previous_pos
                

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
    

    