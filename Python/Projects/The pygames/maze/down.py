class Down:


    class assigner:

        def __init__(self, assignSystem, num: int= 0) -> None:

            self.assignSystem = assignSystem
            self.print_console = assignSystem.print_console


            if num >= 0:

                self.amount_of_moves = num



        def assign(self) -> None | bool:

            # Invalid number of moves -> False
            if self.amount_of_moves == 0:

                if self.print_console:

                    print(f"┌─── down.py.Down.assigner.assign()")
                    print("│")
                    print(f"│ self.amount_of_moves: {self.amount_of_moves}")
                    print("│")


                return False


            grid = self.assignSystem.mazeEngine.grid
            current_direction = "d"


            for assignments in range(1, 1 + (self.amount_of_moves)):

                # Getting the previous assignment info
                previous_assignment = self.assignSystem.mazeEngine.previous_assignment()
                length_of_assignments = previous_assignment[0][0]
                previous_direction_data = previous_assignment[0][1]
                previous_pos = previous_assignment[1]


                # Accounting for changed direction logged key
                if len(previous_direction_data) != 1:

                    previous_direction = previous_direction_data[-1]


                else:

                    previous_direction = previous_direction_data

                # THIS WILL BREAK THE CODE LATER!!!!!!!
                # Can be possible -- TODO: skipping logic or method so it won't be possible
                if grid[previous_pos[0]][previous_pos[1] + 1] == "S":

                    # Getting the factored condition and value
                    # Choosing a cell
                    # Setting selected cell info
                    # Assigning the arrow to the chosen cell
                    # Calculating the score after the assignment

                    return print("SKIPPING LOGIC REQUIRED: down.py.Down.assigner.assign()")


                else:

                    if self.print_console:

                        if assignments == 1:

                            print("┌───      down.py.Down.assigner.assign()")
                            print("│")


                        else:

                            print("│")
                            print("├───      down.py.Down.assigner.assign()")
                            print("│")


                        print(f"├ previous_assignment: {previous_assignment}")
                        print(f"├ previous_pos: {previous_pos}")
                        print(f"├ previous_direction_data: {previous_direction_data}")
                        print(f"├ previous_direction: {previous_direction}")
                        print("│")


                        print("│")
                        print("├ Getting factored condition and value for DOWN CLASS:")
                        
                        
                        # Getting the factored condition and value
                        factored_direction_data, factoring_value = self.assignSystem.mazeEngine.factoringSystem.check_condition(

                                previous_direction= previous_direction,
                                current_direction= current_direction,
                                print_console= self.print_console

                        )                
                        
                        
                        print(f"├ factored_direction_data: {factored_direction_data}", end= " ")
                        print(f" >> factoring_value: {factoring_value}  ✅")
                        print("│")
                        print("│")


                        print(f"│ OLD self.assignSystem.mazeEngine.get_chosen_cell_pos(): {self.assignSystem.mazeEngine.get_chosen_cell_pos()}")


                        print("│ choosing global selected cell (factoring!) . . .", end= " ")


                        # Choosing a cell
                        self.assignSystem.mazeEngine.pick_selected_cell(

                            previous_pos[0] + factoring_value[0],
                            previous_pos[1] + factoring_value[1]

                        )
                        chosen_row, chosen_col = self.assignSystem.mazeEngine.get_chosen_cell_pos()


                        print(f" >> ✅ chosen_row: {chosen_row}", end= " ")
                        print(f" >> ✅ chosen_col: {chosen_col}")


                        print(f"│ NEW self.assignSystem.mazeEngine.get_chosen_cell_pos(): {self.assignSystem.mazeEngine.get_chosen_cell_pos()}")
                        print("│")


                        print("│")
                        print("│ DOWN previous direction", end= "  ")


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
                        print("│")


                        # Loop cycle value
                        print(f"├─ loop: {assignments}")


                        # Account for the first move after first initial assignment
                        if length_of_assignments == 1:

                            print(f"├ SECOND - global chosen cell: {(chosen_row, chosen_col)}")
                            print("├ SECOND - ", end= "")


                        else:

                            print(f"├ global chosen cell: {(chosen_row, chosen_col)}")
                            print("├ ", end= "")


                        print(f"* DOWN CLASS * inserting in grid: {self.assignSystem.arrows.get(current_direction)}", end= " ")
                        
                        
                        print(" >> Setting selected cell", end= " ")


                        # Setting selected cell info
                        self.assignSystem.mazeEngine.set_selected_cell_info(current_direction)


                        print("✅", end= " ")


                        print(" >> Assigning the arrow in the grid", end= " ")


                        # Assigning the arrow to the chosen cell
                        grid[ chosen_row ][ chosen_col ] = self.assignSystem.arrows.get(current_direction)


                        print("✅ >> DONE!")


                        print(f"├─ self.assignSystem.mazeEngine.get_selected_cell_info(): {self.assignSystem.mazeEngine.get_selected_cell_info()}")
                        print("│")


                        # Logging the assignment
                        self.assignSystem.mazeEngine.log_assignments(

                            current_direction= current_direction,
                            previous_pos= previous_pos,
                            factored_direction_data= factored_direction_data,
                            factoring_value= factoring_value,
                            print_console= self.print_console

                        )          


                        # Calculating the score after the assignment
                        self.assignSystem.mazeEngine.score_calculator(

                            current_direction= current_direction,
                            state= "",
                            factored_direction_data= factored_direction_data,
                            print_console= self.print_console

                        )


                        if assignments != self.amount_of_moves:

                            print(f"├{'─'*30}┘")


                        else:

                            print(f"└{'─'*30}┘")


                        # Printing grid progression
                        self.assignSystem.mazeEngine.print_grid()


                        # Setting the updated grid to the maze
                        self.assignSystem.mazeEngine.grid = grid


                    else:

                        # Getting the factored condition and value
                        factored_direction_data, factoring_value = self.assignSystem.mazeEngine.factoringSystem.check_condition(

                                previous_direction= previous_direction,
                                current_direction= current_direction,
                                print_console= self.print_console

                        )       


                        # Choosing a cell
                        self.assignSystem.mazeEngine.pick_selected_cell(

                            previous_pos[0] + factoring_value[0],
                            previous_pos[1] + factoring_value[1]

                        )
                        chosen_row, chosen_col = self.assignSystem.mazeEngine.get_chosen_cell_pos()


                        # Setting selected cell info
                        self.assignSystem.mazeEngine.set_selected_cell_info(current_direction)


                        # Assigning the arrow to the chosen cell
                        grid[ chosen_row ][ chosen_col ] = self.assignSystem.arrows.get(current_direction)

                    
                        # Logging the assignment
                        self.assignSystem.mazeEngine.log_assignments(

                            current_direction= current_direction,
                            previous_pos= previous_pos,
                            factored_direction_data= factored_direction_data,
                            factoring_value= factoring_value,
                            print_console= self.print_console

                        )          


                        # Calculating the score after the assignment
                        self.assignSystem.mazeEngine.score_calculator(

                            current_direction= current_direction,
                            state= "",
                            factored_direction_data= factored_direction_data,
                            print_console= self.print_console

                        )


                        # Setting the updated grid to the maze
                        self.assignSystem.mazeEngine.grid = grid


    # Maybe useful for cache system designing
    def __init__(self, assignSystem):
        
        self.assignSystem = assignSystem


        self.down_assigner = None
        self.down_cache = None


        # self.direction = ""


    def assign(self):
        
        return self.down_assigner.assign()
    
