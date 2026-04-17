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


        print("Set Boundaries Done")
        #self.mazeEngine.print_grid()

    
    def get_next_boundary_type(self, current_direction, amounts_of_assignments=0):

        grid = self.mazeEngine.grid


        previous_chosen_cell = self.mazeEngine.get_chosen_cell_pos()
        row = previous_chosen_cell[0]
        col = previous_chosen_cell[1]


        print(f"╠ previous_chosen_cell: {previous_chosen_cell}")
        print(f"╠ current_direction: {current_direction}")
        

        previous_direction = self.mazeEngine.previous_assignment()[0][1]
        print(f"╠ previous_direction: {previous_direction}")

        if len(previous_direction) > 1:

            previous_direction = previous_direction[-1]

        # Getting the factored condition and value
        factored_direction_data, factoring_value = self.mazeEngine.factoringSystem.check_condition(

            previous_direction= previous_direction,
            current_direction= current_direction,
            print_console= False

        )


        if len(previous_direction) != 1:

            previous_direction = previous_direction[-1]


        if amounts_of_assignments == 0:


            return grid[row + factoring_value[0]][col + factoring_value[1]]


        else:

            match current_direction:

                case "u":

                    for forward_cell in range(1, amounts_of_assignments + 1):
                        
                        if forward_cell == 1:

                            row = row + factoring_value[0]
                            col = col + factoring_value[1]

                            if grid[row - 1][col] not in ["|", "R"]:

                                print("ok")
                                continue


                            else:

                                print("not ok")
                                return [False, grid[row - 1][col]]


                        if grid[row - forward_cell][col] not in ["|", "R"]:

                            print("ok")
                            continue
                        

                        else:

                            print("not ok")
                            return [False, grid[row - forward_cell][col]]
                        

                    return True


                case "d":

                    for forward_cell in range(1, amounts_of_assignments + 1):
                        
                        if forward_cell == 1:

                            row = row + factoring_value[0]
                            col = col + factoring_value[1]

                            if grid[row + 1][col] not in ["|", "R"]:

                                print("ok")
                                continue


                            else:

                                print("not ok")
                                return [False, grid[row + 1][col]]


                        if grid[row + forward_cell][col] not in ["|", "R"]:

                            print("ok")
                            continue
                        

                        else:

                            print("not ok")
                            return [False, grid[row + forward_cell][col]]
                        

                    return True


                case "r":

                    for forward_cell in range(1, amounts_of_assignments + 1):
                        
                        if forward_cell == 1:

                            row = row + factoring_value[0]
                            col = col + factoring_value[1]

                            if grid[row][col + 1] not in ["|", "R"]:

                                print("ok")
                                continue


                            else:

                                print("not ok")
                                return [False, grid[row][col + 1]]


                        if grid[row][col + forward_cell] not in ["|", "R"]:

                            print("ok")
                            continue
                        

                        else:

                            print("not ok")
                            return [False, grid[row][col + forward_cell]]
                        

                    return True


                case "l":

                    for forward_cell in range(1, amounts_of_assignments + 1):
                        
                        if forward_cell == 1:

                            row = row + factoring_value[0]
                            col = col + factoring_value[1]

                            if grid[row][col - 1] not in ["|", "R"]:

                                print("ok")
                                continue


                            else:

                                print("not ok")
                                return [False, grid[row][col - 1]]


                        if grid[row][col - forward_cell] not in ["|", "R"]:

                            print("ok")
                            continue
                        

                        else:

                            print("not ok")
                            return [False, grid[row][col - forward_cell]]
                        

                    return True