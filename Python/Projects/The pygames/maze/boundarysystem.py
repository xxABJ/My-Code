class BoundarySystem:


    def __init__(self, mazeEngine):

        self.mazeEngine = mazeEngine


    def establish_boundaries(self):

        grid = self.mazeEngine.grid
        #size = self.mazeEngine.size


        for rows in range(len(grid)):

            # Top & Bottom rows
            if rows == 0 or rows == len(grid) - 1:
                
                continue


            for cols in range(len(grid)):

                # Left & Right side columns
                if cols == 0 or cols == len(grid) - 1:

                    continue


                if grid[rows][cols] in ["S", "F"]:

                    continue


                if grid[rows - 1][cols] in ["O", " "] or grid[rows + 1][cols] in ["O", " "] or grid[rows][cols - 1] in ["O", " "] or grid[rows][cols + 1] in ["O", " "]:

                    grid[rows][cols] = "G"


                    if grid[rows - 1][cols] == "|" or grid[rows + 1][cols] == "|" or grid[rows][cols - 1] == "|" or grid[rows][cols + 1] == "|":

                        grid[rows][cols] = "O"


        print("Boundaries established")
        self.mazeEngine.print_grid()


    def set_boundaries(self):

        grid = self.mazeEngine.grid


        for rows in range(len(grid)):

            # Top & Bottom rows
            if rows == 0 or rows == len(grid) - 1:
                
                continue


            for cols in range(len(grid)):

                # Left & Right side columns
                if cols == 0 or cols == len(grid) - 1:

                    continue


                cell = grid[rows][cols]


                if cell in ["↑", "↓", "→", "←"]:

                    if cell == "↑":

                        # BEHIND red boundary
                        if grid[rows + 1][cols] not in ["|", "R", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows + 1][cols] = "R"


                            # BEHIND orange boundary
                            if grid[rows + 2][cols] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 2][cols] = "O"

                        
                        # BEHIND bottom-right angle red boundary
                        if grid[rows + 1][cols + 1] not in ["|", "R", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows + 1][cols + 1] = "R"


                            # BEHIND bottom-right 3-corner-angle orange boundary
                            if grid[rows + 2][cols + 1] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 2][cols + 1] = "O" #LEFT

                            
                            if grid[rows + 2][cols + 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 2][cols + 2] = "O" #CORNER

                            
                            if grid[rows + 1][cols + 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 1][cols + 2] = "O" #TOP

                        
                        # BEHIND bottom-left angle red boundary
                        if grid[rows + 1][cols - 1] not in ["|", "R", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows + 1][cols - 1] = "R"


                            # BEHIND bottom-left 3-corner-angle orange boundary
                            if grid[rows + 2][cols - 1] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 2][cols - 1] = "O" #RIGHT


                            if grid[rows + 2][cols - 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 2][cols - 2] = "O" #CORNER


                            if grid[rows + 1][cols - 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows + 1][cols - 2] = "O" #TOP

                        
                        # RIGHT red boundary
                        if grid[rows][cols + 1] not in ["|", "R", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows][cols + 1] = "R"


                            # RIGHT orange boundary
                            if grid[rows][cols + 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows][cols + 2] = "O"


                        # LEFT red boundary
                        if grid[rows][cols - 1] not in ["|", "R", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows][cols - 1] = "R"

                        
                            # LEFT orange boundary
                            if grid[rows][cols - 2] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                                grid[rows][cols - 2] = "O"

                        
                        # INFRONT right orange boundary
                        if grid[rows - 1][cols + 1] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows - 1][cols + 1] = "O"

                        
                        # INFRONT left orange boundary
                        if grid[rows - 1][cols - 1] not in ["|", "R", "O", "S", "F", "↑", "↓", "→", "←"]:

                            grid[rows - 1][cols - 1] = "O"


                    elif cell == "↓":

                        # BEHIND red boundary
                        if grid[rows - 1][cols] not in ["|", "R", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows - 1][cols] = "R"


                            # BEHIND orange boundary
                            if grid[rows - 2][cols] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 2][cols] = "O"


                        
                        # BEHIND top-right angle red boundary
                        if grid[rows - 1][cols + 1] not in ["|", "R", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows - 1][cols + 1] = "R"


                            # BEHIND top-right 3-corner-angle orange boundary
                            if grid[rows - 2][cols + 1] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 2][cols + 1] = "O" #LEFT

                            
                            if grid[rows - 2][cols + 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 2][cols + 2] = "O" #CORNER

                            
                            if grid[rows - 1][cols + 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 1][cols + 2] = "O" #BOTTOM

                        
                        # BEHIND top-left angle red boundary
                        if grid[rows - 1][cols - 1] not in ["|", "R", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows - 1][cols - 1] = "R"


                            # BEHIND top-left 3-corner-angle orange boundary
                            if grid[rows - 2][cols - 1] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 2][cols - 1] = "O" #RIGHT


                            if grid[rows - 2][cols - 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 2][cols - 2] = "O" #CORNER


                            if grid[rows - 1][cols - 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows - 1][cols - 2] = "O" #BOTTOM

                        
                        # RIGHT red boundary
                        if grid[rows][cols + 1] not in ["|", "R", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows][cols + 1] = "R"


                            # RIGHT orange boundary
                            if grid[rows][cols + 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows][cols + 2] = "O"


                        # LEFT red boundary
                        if grid[rows][cols - 1] not in ["|", "R", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows][cols - 1] = "R"


                            # LEFT orange boundary
                            if grid[rows][cols - 2] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                                grid[rows][cols - 2] = "O"


                        # INFRONT right orange boundary
                        if grid[rows + 1][cols + 1] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows + 1][cols + 1] = "O"

                        
                        # INFRONT left orange boundary
                        if grid[rows + 1][cols - 1] not in ["|", "R", "O", "S", "F", "↓", "↑", "→", "←"]:

                            grid[rows + 1][cols - 1] = "O"

                        
                    elif cell == "→":

                        # BEHIND red boundary
                        if grid[rows][cols - 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows][cols - 1] = "R"


                            # BEHIND orange boundary
                            if grid[rows][cols - 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows][cols - 2] = "O"


                        # BEHIND top-left angle red boundary
                        if grid[rows - 1][cols - 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols - 1] = "R"


                            # BEHIND top-left 3-corner-angle orange boundary
                            if grid[rows - 2][cols - 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols - 1] = "O" #RIGHT


                            if grid[rows - 2][cols - 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols - 2] = "O" #CORNER


                            if grid[rows - 1][cols - 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 1][cols - 2] = "O" #BOTTOM

                        
                        # BEHIND bottom-left angle red boundary
                        if grid[rows + 1][cols - 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows + 1][cols - 1] = "R"


                            # BEHIND bottom-left 3-corner-angle orange boundary
                            if grid[rows + 2][cols - 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols - 1] = "O" #RIGHT


                            if grid[rows + 2][cols - 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols - 2] = "O" #CORNER


                            if grid[rows + 1][cols - 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 1][cols - 2] = "O" #TOP


                        # UP red boundary
                        if grid[rows - 1][cols] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols] = "R"


                            # UP orange boundary
                            if grid[rows - 2][cols] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols] = "O"

                        
                        # DOWN red boundary
                        if grid[rows + 1][cols] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows + 1][cols] = "R"


                            # DOWN orange boundary
                            if grid[rows + 2][cols] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols] = "O"


                        # INFRONT top orange boundary
                        if grid[rows - 1][cols + 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols + 1] = "O"

                        
                        # INFRONT bottom orange boundary
                        if grid[rows + 1][cols + 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:
                            
                            grid[rows + 1][cols + 1] = "O"
                        
                    
                    elif cell == "←":

                        # BEHIND red boundary
                        if grid[rows][cols + 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows][cols + 1] = "R"


                            # BEHIND orange boundary
                            if grid[rows][cols + 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows][cols + 2] = "O"

                        
                        # BEHIND top-right angle red boundary
                        if grid[rows - 1][cols + 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols + 1] = "R"


                            # BEHIND top-right 3-corner-angle orange boundary
                            if grid[rows - 2][cols + 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols + 1] = "O" #LEFT

                            
                            if grid[rows - 2][cols + 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols + 2] = "O" #CORNER

                            
                            if grid[rows - 1][cols + 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 1][cols + 2] = "O" #BOTTOM


                        # BEHIND bottom-right angle red boundary
                        if grid[rows + 1][cols + 1] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows + 1][cols + 1] = "R"


                            # BEHIND bottom-right 3-corner-angle orange boundary
                            if grid[rows + 2][cols + 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols + 1] = "O" #LEFT

                            
                            if grid[rows + 2][cols + 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols + 2] = "O" #CORNER

                            
                            if grid[rows + 1][cols + 2] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 1][cols + 2] = "O" #TOP

                        
                        # UP red boundary
                        if grid[rows - 1][cols] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols] = "R"


                            # UP orange boundary
                            if grid[rows - 2][cols] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows - 2][cols] = "O"

                        # DOWN red boundary
                        if grid[rows + 1][cols] not in ["|", "R", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows + 1][cols] = "R"


                            # DOWN orange boundary
                            if grid[rows + 2][cols] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                                grid[rows + 2][cols] = "O"

                        
                        # INFRONT top orange boundary
                        if grid[rows - 1][cols - 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows - 1][cols - 1] = "O"


                        # INFRONT bottom orange boundary
                        if grid[rows + 1][cols - 1] not in ["|", "R", "O", "S", "F", "→", "←", "↓", "↑"]:

                            grid[rows + 1][cols - 1] = "O"


                else:

                    continue


        print("\nSet Boundaries Done")

                    


    def _system_variables(self, current_direction):

        grid = self.mazeEngine.grid
        previous_direction = self.mazeEngine.previous_assignment()[0][1]


        if len(previous_direction) > 1:

            previous_direction = previous_direction[-1]


        previous_chosen_cell = self.mazeEngine.get_chosen_cell_pos()
        row = previous_chosen_cell[0]
        col = previous_chosen_cell[1]


        # Getting the factored condition and value
        factored_direction_data, factoring_value = self.mazeEngine.factoringSystem.check_condition(

            previous_direction= previous_direction,
            current_direction= current_direction,
            print_console= False

        )


        return grid, previous_direction, previous_chosen_cell, row, col, factored_direction_data, factoring_value


    def get_next_boundary(self, current_direction, print_console= False):
        
        if print_console:

            grid, previous_direction, previous_chosen_cell, row, col, factored_direction_data, factoring_value = self._system_variables(current_direction)


            print(f"╠{'═'*2}")
            print(f"╠═ │ boundarysystem.py.BoundarySystem.get_next_boundary()")
            print("║  │")
            print(f"╠  │ previous_chosen_cell: {previous_chosen_cell}")
            print(f"╠  │ current_direction: {current_direction}")
            print(f"╠  │ previous_direction: {previous_direction}")
            print("║  │")
            print(f"║  │ returning: {grid[row + factoring_value[0]][col + factoring_value[1]]}")
            print(f"╠{'═'*2}")


            if grid[row + factoring_value[0]][col + factoring_value[1]] not in ["|", "R"]:

                return grid[row + factoring_value[0]][col + factoring_value[1]]
            

            else:

                return [False, grid[row + factoring_value[0]][col + factoring_value[1]]]


        else:

            grid, previous_direction, previous_chosen_cell, row, col, factored_direction_data, factoring_value = self._system_variables(current_direction)


            if grid[row + factoring_value[0]][col + factoring_value[1]] not in ["|", "R"]:

                return grid[row + factoring_value[0]][col + factoring_value[1]]
            

            else:

                return [False, grid[row + factoring_value[0]][col + factoring_value[1]]]


    def get_any_boundary(self, current_direction, amount_of_assignments, print_console= False):

        if print_console:

            print(f"╠{'═'*2}")
            print(f"╠═ │ boundarysystem.py.BoundarySystem.get_any_boundary()")


            grid, previous_direction, previous_chosen_cell, row, col, factored_direction_data, factoring_value = self._system_variables(current_direction)


            # Required factoring value for the cell
            row = row + factoring_value[0]
            col = col + factoring_value[1]


            # Getting the factored condition and value for the loop's forward cell variable
            forward_cell_factoring_direction, forward_cell_factoring_value = self.mazeEngine.factoringSystem.check_condition(

                previous_direction= False,
                current_direction= current_direction,
                print_console= False

            )


            for forward_cell in range(amount_of_assignments + 1):

                print("║  │")
                print(f"╠  │ forward_cell: {forward_cell} , MOVE: {forward_cell+1} , direction {forward_cell_factoring_direction}")

                # The first iteration of the loop
                if forward_cell == 0:

                    # Checking if initial argument amount to return boundaries is just one
                    if forward_cell + 1 == amount_of_assignments:

                        if grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]] not in ["|", "R"]:

                            print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                            print(f"║  │     boundary_after_next_boundary: ok {grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]} {row + forward_cell_factoring_value[0], col + forward_cell_factoring_value[1]}")
                            print(f"╠{'═'*2}")

                            return grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]
                        

                        else:

                            print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                            print(f"║  │     boundary_after_next_boundary: not ok {grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]} {row + forward_cell_factoring_value[0], col + forward_cell_factoring_value[1]}")
                            print(f"╠{'═'*2}")

                            return [False, grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]]


                match forward_cell_factoring_direction:

                    case "u":

                        if grid[row - forward_cell][col] not in ["|", "R"]:

                            print(f"║  │     ok {grid[row - forward_cell][col]} {row - forward_cell, col}")
                            continue


                        else:

                            print(f"║  │     not ok {grid[row - forward_cell][col]} {row - forward_cell, col}")
                            print(f"╠{'═'*2}")
                            return [False, grid[row - forward_cell][col]]
                        
                    
                    case "d":

                        if grid[row + forward_cell][col] not in ["|", "R"]:

                            print(f"║  │     ok {grid[row + forward_cell][col]} {row + forward_cell, col}")
                            continue

                        
                        else:

                            print(f"║  │     not ok {grid[row + forward_cell][col]} {row + forward_cell, col}")
                            print(f"╠{'═'*2}")
                            return [False, grid[row + forward_cell][col]]
                        

                    case "r":

                        if grid[row][col + forward_cell] not in ["|", "R"]:

                            print(f"║  │     ok {grid[row][col + forward_cell]} {row, col + forward_cell}")
                            continue


                        else:

                            print(f"║  │     not ok {grid[row][col + forward_cell]} {row, col + forward_cell}")
                            print(f"╠{'═'*2}")
                            return [False, grid[row][col + forward_cell]]
                        

                    case "l":

                        if grid[row][col - forward_cell] not in ["|", "R"]:

                            print(f"║  │     ok {grid[row][col - forward_cell]} {row, col - forward_cell}")
                            continue


                        else:

                            print(f"║  │     not ok {grid[row][col - forward_cell]} {row, col - forward_cell}")
                            print(f"╠{'═'*2}")
                            return [False, grid[row][col - forward_cell]]
                            
                
            match forward_cell_factoring_direction:

                case "u":

                    return grid[row - forward_cell][col]
                

                case "d":

                    return grid[row + forward_cell][col]
                

                case "r":

                    return grid[row][col + forward_cell]
                

                case "l":

                    return grid[row][col - forward_cell]


        
        else:

            grid, previous_direction, previous_chosen_cell, row, col, factored_direction_data, factoring_value = self._system_variables(current_direction)


            # Required factoring value for the cell
            row = row + factoring_value[0]
            col = col + factoring_value[1]


            # Getting the factored condition and value for the loop's forward cell variable
            forward_cell_factoring_direction, forward_cell_factoring_value = self.mazeEngine.factoringSystem.check_condition(

                previous_direction= False,
                current_direction= current_direction,
                print_console= False

            )


            for forward_cell in range(amount_of_assignments + 1):

                # The first iteration of the loop
                if forward_cell == 0:

                    # Checking if initial argument amount to return boundaries is just one
                    if forward_cell + 1 == amount_of_assignments:

                        if grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]] not in ["|", "R"]:

                            return grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]
                        

                        else:

                            return [False, grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]]


                match forward_cell_factoring_direction:

                    case "u":

                        if grid[row - forward_cell][col] not in ["|", "R"]:

                            continue


                        else:

                            return [False, grid[row - forward_cell][col]]
                        
                    
                    case "d":

                        if grid[row + forward_cell][col] not in ["|", "R"]:

                            continue

                        
                        else:

                            return [False, grid[row + forward_cell][col]]
                        

                    case "r":

                        if grid[row][col + forward_cell] not in ["|", "R"]:

                            continue


                        else:

                            return [False, grid[row][col + forward_cell]]
                        

                    case "l":

                        if grid[row][col - forward_cell] not in ["|", "R"]:

                            continue


                        else:

                            return [False, grid[row][col - forward_cell]]
                            
                
            match forward_cell_factoring_direction:

                case "u":

                    return grid[row - forward_cell][col]
                

                case "d":

                    return grid[row + forward_cell][col]
                

                case "r":

                    return grid[row][col + forward_cell]
                

                case "l":

                    return grid[row][col - forward_cell]

