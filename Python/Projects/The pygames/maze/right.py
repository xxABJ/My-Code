import random


class Right:


    class assigner:

        def __init__(
                
                self,
                right_factory,
                num: int= 0,
                print_console: bool= False
                
            ) -> None:

            self.right_factory = right_factory
            self.print_console = print_console


            if num >= 0:

                self.amount_of_moves = num



        def assign(self) -> None | bool:

            # Invalid number of moves -> False
            if self.amount_of_moves == 0:

                if self.print_console:

                    print(f"┌─── right.py.Right.assigner.assign()")
                    print("│")
                    print(f"│ self.amount_of_moves: {self.amount_of_moves}")
                    print("│")


                return False


            grid = self.right_factory.maze.grid[:]
            current_direction = "r"


            for assignments in range(1, 1 + (self.amount_of_moves)):

                # Getting the previous assignment info
                previous_assignment = self.right_factory.maze.previous_assignment()
                length_of_assignments = previous_assignment[0][0]
                previous_direction_data = previous_assignment[0][1]
                previous_pos = previous_assignment[1]


                # Accounting for changed direction logged key
                if len(previous_direction_data) != 1:

                    previous_direction = previous_direction_data[-1]


                else:

                    previous_direction = previous_direction_data


                # Can be possible -- TODO: skipping logic or method so it won't be possible
                if grid[previous_pos[0]][previous_pos[1] + 1] == "S":

                    # Getting the factored condition and value
                    # Choosing a cell
                    # Setting selected cell info
                    # Assigning the arrow to the chosen cell
                    # Calculating the score after the assignment

                    return print("SKIPPING LOGIC REQUIRED: right.py.Right.assigner.assign()")


                else:

                    if self.print_console:

                        if assignments == 1:

                            print("┌─── right.py.Right.assigner.assign()")
                            print("│")


                        else:

                            print("│")
                            print("├─── right.py.Right.assigner.assign()")
                            print("│")


                        print(f"├ previous_assignment: {previous_assignment}")
                        print(f"├ previous_pos: {previous_pos}")
                        print(f"├ previous_direction_data: {previous_direction_data}")
                        print(f"├ previous_direction: {previous_direction}")
                        print("│")


                        print("├─ Getting factored condition and value for RIGHT CLASS:", end= " ")
                        
                        
                        # Getting the factored condition and value
                        factored_direction_data, factoring_value = self.right_factory.maze.factoring.check_condition(

                                previous_direction= previous_direction,
                                current_direction= current_direction,
                                print_console= self.print_console

                        )                
                        
                        
                        print(f" >> ✅ factored_direction_data: {factored_direction_data}", end= " ")
                        print(f" >> ✅ factoring_value: {factoring_value}\n")
                        print("│")


                        print(f"│ OLD self.right_factory.maze.get_chosen_cell_pos(): {self.right_factory.maze.get_chosen_cell_pos()}")
                        print("│")


                        print("│ choosing global selected cell . . .", end= " ")


                        # Choosing a cell
                        self.right_factory.maze.pick_selected_cell(

                            previous_pos[0] + factoring_value[0],
                            previous_pos[1] + factoring_value[1]

                        )
                        chosen_row, chosen_col = self.right_factory.maze.get_chosen_cell_pos()


                        print(f" >> ✅ chosen_row: {chosen_row}", end= " ")
                        print(f" >> ✅ chosen_col: {chosen_col}")
                        print("│")


                        print(f"│ NEW self.right_factory.maze.get_chosen_cell_pos(): {self.right_factory.maze.get_chosen_cell_pos()}")
                        print("│")


                        print("│ RIGHT previous direction", end= "  ")


                        match previous_direction: 

                            case "r":

                                print("r", end= "  : ")


                            case "d":

                                print("d", end= "  : ")


                            case "u":

                                print("u", end= "  : ")


                            # Shouldn't be possible
                            case "l":

                                print("l", end= "  : ")


                        print(previous_pos)
                        print("│")


                        # Loop cycle value
                        print(f"├─ loop: {assignments}")
                        print("│")


                        # Account for the first move after first initial assignment
                        if length_of_assignments == 1:

                            print(f"├ SECOND - global chosen cell: {(chosen_row, chosen_col)}")
                            print("├ SECOND - ", end= "")


                        else:

                            print(f"├ global chosen cell: {(chosen_row, chosen_col)}")
                            print("├ ", end= "")


                        print(f"* RIGHT CLASS * inserting in grid: {self.right_factory.maze.arrows.get(current_direction)}", end= " ")
                        
                        
                        print(" >> Setting selected cell", end= " ")


                        # Setting selected cell info
                        self.right_factory.maze.set_selected_cell_info(current_direction)


                        print("✅", end= " ")


                        print(" >> Assigning the arrow in the grid", end= " ")


                        # Assigning the arrow to the chosen cell
                        grid[ chosen_row ][ chosen_col ] = self.right_factory.maze.arrows.get(current_direction)


                        print("✅ >> DONE!")
                        print("│")


                        print(f"│ self.right_factory.maze.get_selected_cell_info(): {self.right_factory.maze.get_selected_cell_info()}")
                        print("│")


                        # Logging the assignment
                        self.right_factory.maze.log_assignments(

                            current_direction= current_direction,
                            previous_pos= previous_pos,
                            factored_direction_data= factored_direction_data,
                            factoring_value= factoring_value,
                            print_console= self.print_console

                        )          


                        # Calculating the score after the assignment
                        self.right_factory.maze.score_calculator(

                            direction= current_direction,
                            state= "",
                            print_console= self.print_console

                        )


                        if assignments != self.amount_of_moves:

                            print(f"├{'─'*30}┘")


                        else:

                            print(f"└{'─'*30}┘")


                        # Printing grid progression
                        self.right_factory.maze.print_grid()


                        # Setting the updated grid to the maze
                        self.right_factory.maze.grid = grid


                    else:

                        # Getting the factored condition and value
                        factored_direction_data, factoring_value = self.right_factory.maze.factoring.check_condition(

                                previous_direction= previous_direction,
                                current_direction= current_direction,
                                print_console= self.print_console

                        )       


                        # Choosing a cell
                        self.right_factory.maze.pick_selected_cell(

                            previous_pos[0] + factoring_value[0],
                            previous_pos[1] + factoring_value[1]

                        )
                        chosen_row, chosen_col = self.right_factory.maze.get_chosen_cell_pos()


                        # Setting selected cell info
                        self.right_factory.maze.set_selected_cell_info(current_direction)


                        # Assigning the arrow to the chosen cell
                        grid[ chosen_row ][ chosen_col ] = self.right_factory.maze.arrows.get(current_direction)

                    
                        # Logging the assignment
                        self.right_factory.maze.log_assignments(

                            current_direction= current_direction,
                            previous_pos= previous_pos,
                            factored_direction_data= factored_direction_data,
                            factoring_value= factoring_value,
                            print_console= self.print_console

                        )          


                        # Calculating the score after the assignment
                        self.right_factory.maze.score_calculator(

                            direction= current_direction,
                            state= "",
                            print_console= self.print_console

                        )


                        # Setting the updated grid to the maze
                        self.right_factory.maze.grid = grid


    # Maybe useful for cache system designing
    def __init__(self, maze):
        
        self.maze = maze


        self.direction = ""
        self.alternative_directions = ["u", "d"]


        self.right_assigner = None



    def assign(self):
        
        return self.right_assigner.assign()
    

