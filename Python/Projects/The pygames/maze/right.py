import random


class Right:


    class assigner:

        def __init__(self, right_factory, num = False):

            self.right_factory = right_factory


            if num >= 0:

                self.amount_of_moves = num


        def assign(self):

            print(self.amount_of_moves)
            if self.amount_of_moves == 0:
                return False


            grid = self.right_factory.maze.grid[:]

            round = 0
            for assignments in range(1, 1 + (self.amount_of_moves)):

                #if previous_assignment and previous_pos:
                #    print("old_previous_assignment:", previous_assignment)
                #    print("old_beginning_pos:", previous_pos)

                print("latest assignment: ", self.right_factory.maze.assignments.get(list(self.right_factory.maze.assignments.keys())[-1]))

                previous_assignment = self.right_factory.maze.previous_assignment()
                previous_pos = previous_assignment[1]

                print("new_previous_assignment:", previous_assignment)
                print("new_beginning_pos:", previous_pos)
                current_selected_cell = (previous_pos[0], previous_pos[1])


                if grid[previous_pos[0]][previous_pos[1] + 1] == "S":

                    #updated_previous_pos = (
                    #    current_selected_cell[0],
                    #    current_selected_cell[1]
                    #)
                    print("WTF IS THIS")
                    pass


                else:

                    if previous_assignment[0][1] == "r":
                    #case self.right_factory.maze.arrows.get("r"):
                    #case "→":
                    #case "r":

                        print(f"\nRIGHT prev r: {previous_pos}")

                        if len(self.right_factory.maze.assignments) == 1:
                            current_selected_cell = (previous_pos[0], previous_pos[1] + 1)

                            print("RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("r"))
                            grid[current_selected_cell[0]][current_selected_cell[1]] = self.right_factory.maze.arrows.get("r")


                            # pre = r
                            updated_previous_pos = (
                                previous_pos[0],
                                previous_pos[1]
                            )

                            print("round:",round)
                            print(f"  1# FINAL POS (RIGHT prev r):\n  {updated_previous_pos}")


                        else:


                            print("RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("r"))
                            grid[previous_pos[0]][previous_pos[1]] = self.right_factory.maze.arrows.get("r")


                            # pre = r
                            updated_previous_pos = (
                                previous_pos[0],
                                previous_pos[1]
                            )


                            print("round:",round)
                            print(f"  FINAL POS (RIGHT prev r):\n  {updated_previous_pos}")


                        self.right_factory.maze.log_assignments(

                            direction= "r",
                            previous_pos= updated_previous_pos,

                        )
                                

                    elif previous_assignment[0][1] == "d":
                    #case self.right_factory.maze.arrows.get("d"):
                    #case "↓":
                    #case "d":

                        print(f"\nRIGHT prev d: {previous_pos}")


                        if len(self.right_factory.maze.assignments) == 1:
                            current_selected_cell = (previous_pos[0] + 1, previous_pos[1])

                            print("RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("d"))
                            grid[current_selected_cell[0]][current_selected_cell[1]] = self.right_factory.maze.arrows.get("d")


                            # pre = d
                            updated_previous_pos = (
                                previous_pos[0],
                                previous_pos[1]
                            )

                            print(f"  1# FINAL POS (RIGHT prev d):\n  {updated_previous_pos}")


                        elif len(self.right_factory.maze.assignments) != 1:
                        
                            print("RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("d"))
                            grid[previous_pos[0]][previous_pos[1]] = self.right_factory.maze.arrows.get("d")


                            # pre = d
                            updated_previous_pos = (
                                previous_pos[0],
                                previous_pos[1]
                            )

                            print(f"  FINAL POS (RIGHT prev d):\n  {updated_previous_pos}")


                            self.right_factory.maze.log_assignments(

                                direction= "r",
                                previous_pos= updated_previous_pos,
                                changing_directions = "d>r"

                            )
                        

                    elif previous_assignment[0][1] == "u":
                    #case self.right_factory.maze.arrows.get("u"):
                    #case "↑":
                    #case "u":

                        print(f"prev u: {previous_pos}")


                        if len(self.right_factory.maze.assignments) == 1:
                            current_selected_cell = (previous_pos[0] - 1, previous_pos[1])


                        else:
                            pass
                        
                        
                        grid[current_selected_cell[0]][current_selected_cell[1]] = self.right_factory.maze.arrows.get("r")


                        # pre = u
                        updated_previous_pos = (
                            current_selected_cell[0],
                            current_selected_cell[1]
                        )
                        

                    elif previous_assignment[0][1] == "l":
                    #case self.right_factory.maze.arrows.get("l"):
                    #case "←":
                    #case "l":
                    # should not be possible

                        print(f"invalid prev l: {previous_pos}")

                        if len(self.right_factory.maze.assignments) == 1:
                            updated_previous_pos = False


                        else:
                            updated_previous_pos = False


                print("   UPP:   ",updated_previous_pos)
                if updated_previous_pos == False:
                    return updated_previous_pos


                print("   UPP:   ",updated_previous_pos)
                #self.right_factory.maze.log_assignments(
                #
                #    direction= "r",
                #    previous_pos= updated_previous_pos
                #
                #)


                self.right_factory.maze.score_calculator(

                    direction= "r",
                    state= ""

                )
                #print(assignments)

                round += 1

            self.right_factory.maze.print_grid()


            self.right_factory.maze.grid = grid


        
        def assign_old(self):

            if self.amount_of_moves == 0:
                return False

            grid = self.right_factory.maze.grid[:]
            previous_assignment = self.right_factory.maze.previous_assignment()
            previous_pos = previous_assignment[1]


            for assignments in range(1, 1 + (self.amount_of_moves)):

                if grid[previous_pos[0]][previous_pos[1] + assignments] == "S":
                    
                    pass
                
                
                else:

                    grid[previous_pos[0]][previous_pos[1] + assignments] = self.right_factory.maze.arrows.get("r")
                
                
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
    

