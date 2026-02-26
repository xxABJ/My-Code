import random


class Down:


    class assigner:

        def __init__(self,down_factory, num =False):

            self.down_factory = down_factory


            if num >= 0:

                self.amount_of_moves = num

        
        def assign(self):

            print(self.amount_of_moves)
            if self.amount_of_moves == 0:
                return False


            grid = self.down_factory.maze.grid[:]


            for assignments in range(1, 1 + (self.amount_of_moves)):


                print("latest assignment: ", self.down_factory.maze.assignments.get(list(self.down_factory.maze.assignments.keys())[-1]))

                previous_assignment = self.down_factory.maze.previous_assignment()
                previous_pos = previous_assignment[1]
                current_selected_cell = (previous_pos[0], previous_pos[1])


                if grid[current_selected_cell[0] + 1][current_selected_cell[1]] == "S":

                    #updated_previous_pos = (
                    #    current_selected_cell[0],
                    #    current_selected_cell[1]
                    #)
                    pass


                else:

                    match previous_assignment[0][1]:

                        #case self.down_factory.maze.arrows.get("d"):
                        #case "↓":
                        case "d":

                            print(f"d\nDOWN prev d: {previous_pos}")


                            if len(self.down_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0] + 1, previous_pos[1])

                                print("DOWN CLASS inserting in grid:", self.down_factory.maze.arrows.get("d"))
                                grid[current_selected_cell[0]][current_selected_cell[1]] = self.down_factory.maze.arrows.get("d")


                                # pre = d
                                updated_previous_pos = (
                                    previous_pos[0],
                                    previous_pos[1]
                                )


                                print(f"  1# FINAL POS (DOWN prev d):\n  {updated_previous_pos}")


                            else:

                                print("DOWN CLASS inserting in grid:", self.down_factory.maze.arrows.get("d"))
                                grid[previous_pos[0]][previous_pos[1]] = self.down_factory.maze.arrows.get("d")


                                # pre = d
                                updated_previous_pos = (
                                    previous_pos[0],
                                    previous_pos[1]
                                )


                                print(f"  FINAL POS (DOWN prev d):\n  {updated_previous_pos}")


                            self.down_factory.maze.log_assignments(

                                direction= "d",
                                previous_pos= updated_previous_pos

                            )


                        #case self.down_factory.maze.arrows.get("r"):
                        #case "→":
                        case "r":

                            print(f"\nDOWN prev r: {previous_pos}")
                            

                            if len(self.down_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0], previous_pos[1] + 1)

                                print("DOWN CLASS inserting in grid:", self.down_factory.maze.arrows.get("r"))
                                grid[current_selected_cell[0]][current_selected_cell[1]] = self.down_factory.maze.arrows.get("r")


                                # pre = r
                                updated_previous_pos = (
                                    previous_pos[0],
                                    previous_pos[1]
                                )


                                print(f"  1# FINAL POS (DOWN prev r):\n  {updated_previous_pos}")


                            elif len(self.down_factory.maze.assignments) != 1:

                                print("DOWN CLASS inserting in grid:", self.down_factory.maze.arrows.get("r"))
                                grid[previous_pos[0]][previous_pos[1]] = self.down_factory.maze.arrows.get("r")


                                # pre = r
                                updated_previous_pos = (
                                    previous_pos[0],
                                    previous_pos[1]
                                )


                                print(f"  FINAL POS (DOWN prev r):\n  {updated_previous_pos}")

                            

                            self.down_factory.maze.log_assignments(

                                    direction= "d",
                                    previous_pos= updated_previous_pos,
                                    changing_directions = "r>d"

                                )


                        #case self.down_factory.maze.arrows.get("l"):
                        #case "←":
                        case "l":

                            print(f"prev l: {previous_pos}")
                            

                            if len(self.down_factory.maze.assignments) == 1:
                                current_selected_cell = (previous_pos[0], previous_pos[1] - 1)


                            grid[current_selected_cell[0]][current_selected_cell[1]] = self.down_factory.maze.arrows.get("d")


                            # pre = l
                            updated_previous_pos = (
                                current_selected_cell[0],
                                current_selected_cell[1]
                            )


                        #case self.down_factory.maze.arrows.get("u"):
                        #case "↑":
                        case "u":
                            # should not be possible

                            print(f"invalid prev u: {previous_pos}")

                            if len(self.down_factory.maze.assignments) == 1:
                                updated_previous_pos = False


                            else:
                                updated_previous_pos = False
                        

                if not updated_previous_pos:
                    return updated_previous_pos

                

                #self.down_factory.maze.log_assignments(
                #
                #    direction= "d",
                #    previous_pos= updated_previous_pos
                #
                #)


                self.down_factory.maze.score_calculator(

                    direction= "d",
                    state= ""

                )
                #print(assignments)

            self.down_factory.maze.print_grid()


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
    