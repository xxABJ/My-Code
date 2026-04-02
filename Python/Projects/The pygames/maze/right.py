import random


class Right:


    class assigner:

        def __init__(self, right_factory, num = False):

            self.right_factory = right_factory


            if num >= 0:

                self.amount_of_moves = num


        def _factoring(self, direction= str, print_console= bool) -> None:
            pass


        def assign(self, print_console: bool = False):

            if print_console and self.amount_of_moves == 0:
                print(f"┌─── right.py.Right.assigner.assign()")
                print("│")
                print(f"│ self.amount_of_moves: {self.amount_of_moves}")
                print("│")
                return False


            grid = self.right_factory.maze.grid[:]


            loop = 0
            for assignments in range(1, 1 + (self.amount_of_moves)):

                previous_assignment = self.right_factory.maze.previous_assignment()
                length_of_assignments = previous_assignment[0][0]
                previous_direction = previous_assignment[0][1]
                previous_pos = previous_assignment[1]

                if print_console:
                        if assignments == 1:
                            print(f"┌─── right.py.Right.assigner.assign()")
                            print("│")
                        else:
                            print("│")
                            print(f"├─── right.py.Right.assigner.assign()")
                            print("│")
                            print(f"├ full_previous_assignment: {previous_assignment}")
                            print(f"├ previous_direction: {previous_direction}")
                            print("│")

                current_selected_cell = (previous_pos[0], previous_pos[1])

                # Should not be possible
                if grid[previous_pos[0]][previous_pos[1] + 1] == "S":

                    #updated_previous_pos = (
                    #    current_selected_cell[0],
                    #    current_selected_cell[1]
                    #)
                    print("WTF IS THIS")
                    pass


                else:

                    if previous_direction == "r":


                        # Choosing the cell
                        self.right_factory.maze.choose_selected_cell(

                            previous_pos[0],
                            previous_pos[1] + 1

                        )


                        chosen_row = self.right_factory.maze.get_chosen_cell_pos()[0]
                        chosen_col = self.right_factory.maze.get_chosen_cell_pos()[1]


                        # Accounting for the first move
                        if print_console:

                            print(f"│ RIGHT prev r: {previous_pos}")
                            print("│")
                            print(f"├─ loop:", loop + 1)
                            print("│")


                            if length_of_assignments == 1:

                                print(f"├ FIRST - current_chosen_cell: {(chosen_row, chosen_col)}")

                                # Assigning the arrow to the chosen cell
                                print("├ FIRST - RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("r"), end="")
                                self.right_factory.maze.set_selected_cell_info("r")
                                grid[chosen_row][chosen_col] = self.right_factory.maze.arrows.get("r")
                                print(" . . . Setting selected cell . . . DONE!")


                            else:

                                print(f"├ current_chosen_cell: {(chosen_row, chosen_col)}")

                                # Assigning the arrow to the chosen cell
                                print("├ RIGHT CLASS inserting in grid:", self.right_factory.maze.arrows.get("r"), end="")
                                self.right_factory.maze.set_selected_cell_info("r")
                                grid[chosen_row][chosen_col] = self.right_factory.maze.arrows.get("r")
                                print(" . . . Setting selected cell . . . DONE!")

                        
                        else:

                            self.right_factory.maze.set_selected_cell_info("r")
                            grid[chosen_row][chosen_col] = self.right_factory.maze.arrows.get("r")


                        # pre = r
                        updated_previous_pos = (
                            chosen_row,
                            chosen_col
                        )

                        
                        # Logging the assignment
                        self.right_factory.maze.log_assignments(

                            direction= "r",
                            previous_pos= previous_pos,
                            print_console = print_console

                        )
                                

                    elif previous_direction == "d":
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
                        

                    elif previous_direction == "u":
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
                        

                    elif previous_direction == "l":
                    #case self.right_factory.maze.arrows.get("l"):
                    #case "←":
                    #case "l":
                    # should not be possible

                        print(f"invalid prev l: {previous_pos}")

                        if len(self.right_factory.maze.assignments) == 1:
                            updated_previous_pos = False


                        else:
                            updated_previous_pos = False


                self.right_factory.maze.score_calculator(

                    direction= "r",
                    state= "",
                    print_console = print_console

                )

                if assignments != self.amount_of_moves:
                    print(f"├{'─'*30}┘")
                else:
                    print(f"└{'─'*30}┘")

                loop += 1



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


    def assign(self, print_console: bool = False):
        
        return self.right_assigner.assign(print_console)
    

