class BoundarySystem:


    def __init__(self, mazeEngine):

        self.mazeEngine = mazeEngine

        self.forward_cell_factor = {

            "u": [(-1, 0), "u"],
            "d": [(1, 0), "d"],
            "r": [(0, 1), "r"],
            "l": [(0, -1), "l"],

        }


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

    
    def get_next_boundary_type(self, current_direction, amount_of_assignments=0, print_console1= False, print_console2= False):

        if print_console1:
            #print("║")
            print(f"╠{'═'*2}")
            print(f"╠═ │ boundarysystem.py.BoundarySystem.get_next_boundary_type()")
            print("║  │")

        grid = self.mazeEngine.grid


        previous_chosen_cell = self.mazeEngine.get_chosen_cell_pos()
        row = previous_chosen_cell[0]
        col = previous_chosen_cell[1]



        if amount_of_assignments != 0 and print_console1:

            print(f"╠  │ previous_chosen_cell: {previous_chosen_cell}")
            print(f"╠  │ current_direction: {current_direction}")
            

        previous_direction = self.mazeEngine.previous_assignment()[0][1]


        if amount_of_assignments != 0 and print_console1:

            print(f"╠  │ previous_direction: {previous_direction}")
            print("║  │")


        if len(previous_direction) > 1:

            previous_direction = previous_direction[-1]


        # Getting the factored condition and value
        factored_direction_data, factoring_value = self.mazeEngine.factoringSystem.check_condition(

            previous_direction= previous_direction,
            current_direction= current_direction,
            print_console= False

        )


        if amount_of_assignments == 0:

            if print_console1:
                print(f"╠  │ amounts_of_assignments: {amount_of_assignments}")
                print("║  │")
                print(f"║  │ returning: {grid[row + factoring_value[0]][col + factoring_value[1]]}")
                print(f"╠{'═'*2}")

            return grid[row + factoring_value[0]][col + factoring_value[1]]


        else:

            if print_console2:

                print("║  │ Checking if amount of assignments do not fail the boundary check...")
                print("║  │ will it hit a   R   or a   |  ?   (ok / not ok)")
                print(f"╠  │ amounts_of_assignments: {amount_of_assignments}")

                row = row + factoring_value[0]
                col = col + factoring_value[1]


                forward_cell_factoring_data = self.forward_cell_factor[current_direction]
                forward_cell_factoring_value = forward_cell_factoring_data[0]
                forward_cell_factoring_direction = forward_cell_factoring_data[1]


                for forward_cell in range(1, amount_of_assignments + 1):

                    print("║  │")
                    print(f"║  │   forward_cell: {forward_cell}")
                    print("║  │")

                    if forward_cell == 1:

                        if forward_cell == amount_of_assignments:

                            if grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]] not in ["|", "R"]:

                                match forward_cell_factoring_direction:

                                    case "u":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: ok {grid[row - 1][col]} {row - 1, col}")
                                        print(f"╠{'═'*2}")


                                    case "d":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: ok {grid[row + 1][col]} {row + 1, col}")
                                        print(f"╠{'═'*2}")

                                    
                                    case "r":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: ok {grid[row][col + 1]} {row, col + 1}")
                                        print(f"╠{'═'*2}")


                                    case "l":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: ok {grid[row][col - 1]} {row, col - 1}")
                                        print(f"╠{'═'*2}")


                                return grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]
                            

                            else:

                                match forward_cell_factoring_direction:

                                    case "u":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: not ok {grid[row - 1][col]} {row - 1, col}")
                                        print(f"╠{'═'*2}")

                                    
                                    case "d":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: not ok {grid[row + 1][col]} {row + 1, col}")
                                        print(f"╠{'═'*2}")


                                    case "r":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: not ok {grid[row][col + 1]} {row, col + 1}")
                                        print(f"╠{'═'*2}")


                                    case "l":

                                        print(f"║  │     next_boundary: ok {grid[row][col]} {row, col}")
                                        print(f"║  │     boundary_after_next_boundary: not ok {grid[row][col - 1]} {row, col - 1}")
                                        print(f"╠{'═'*2}")


                                return [False, grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]]
                            
                    
                        if grid[row][col] not in ["|", "R"]:

                            print(f"║  │     ok {grid[row][col]} {row, col}")  
                            
                            
                            continue


                        else:

                            print(f"║  │     not ok {grid[row][col]} {row, col}")
                            print(f"╠{'═'*2}")


                            return [False, grid[row][col]]
                        

                    # Due to factored value ... can be changed
                    forward_cell = forward_cell - 1


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


                print(f"╠{'═'*2}")


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

                row = row + factoring_value[0]
                col = col + factoring_value[1]


                forward_cell_factoring_data = self.forward_cell_factor[current_direction]
                forward_cell_factoring_value = forward_cell_factoring_data[0]
                forward_cell_factoring_direction = forward_cell_factoring_data[1]


                for forward_cell in range(1, amount_of_assignments + 1):

                    if forward_cell == 1:

                        if forward_cell == amount_of_assignments:

                            if grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]] not in ["|", "R"]:

                                return grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]
                            
                            else:

                                return [False, grid[row + forward_cell_factoring_value[0]][col + forward_cell_factoring_value[1]]]
                            
                    
                        if grid[row][col] not in ["|", "R"]:

                            continue


                        else:

                            return [False, grid[row][col]]
                        

                    # Due to factored value ... can be changed
                    forward_cell = forward_cell - 1


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