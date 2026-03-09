class Scanner:


    def __init__(self, maze):
        
        self.maze = maze


        self.translator = {

            "l": "leftside",
            "r": "rightside",
            "u": "topside",
            "d": "bottomside"

        }


        self.directions = {

            'l': (0, -1),
            'r': (0, 1),
            'u': (-1, 0),
            'd': (1, 0)

        }

        self.debug = 0


    def scan(self, row= bool, col= bool, print_console= bool) -> None:
        
        def operator(logic, value):
            
            if logic == "+":

                return +value
            

            elif logic == "-":
                
                return -value


        grid = self.maze.grid
        previous_assignment = self.maze.previous_assignment()
        previous_coordinates = (previous_assignment[1][1])
        previous_direction = previous_assignment[1][0]


        pending_direction = self.maze.random_direction


        match previous_direction:
            case "l":
                factor = self.directions.get(pending_direction)
            
            case "r":
                factor = self.directions.get(pending_direction)

            case "u":
                factor = self.directions.get(pending_direction)
            
            case "d":
                factor = self.directions.get(pending_direction)
                

        accounted_coordinates = tuple(

            a + b for a, b in zip(

                previous_coordinates,
                factor

                ))
        
        
        # New score is accounted for in "accounted_coordinates"
        available_cellcheck_amount = self.maze.scores.get(self.translator.get(pending_direction))
        pending_assignment = ( pending_direction, available_cellcheck_amount )
        

        ROW = accounted_coordinates[0]
        COL = accounted_coordinates[1]


        if row:

            if pending_direction == "u":
                
                logic = "+"


            elif pending_direction == "d":
                
                logic = "-"


            for row_cell in range(available_cellcheck_amount):

                cell = grid[ROW + operator(logic, row_cell)][COL]


                if cell == " ":

                    continue


                elif cell == "|":

                    pass
                    #TODO: implement chosen accounting logic


                elif cell != " ":

                    current_rowcell = ROW + operator(logic, row_cell)
                    #TODO: implement chosen accounting logic


        if col:

            if pending_direction == "r":
                
                logic = "+"


            elif pending_direction == "l":
                
                logic = "-"
            

            for col_cell in range(available_cellcheck_amount):

                cell = grid[ROW][COL + operator(logic, col_cell)]


                if cell == " ":

                    continue


                elif cell == "|":

                    print("    |  wall")
                    self.debug = COL + operator(logic, col_cell)
                    break
                    #TODO: implement chosen accounting logic


                elif cell != " ":

                    print("    D  direction")
                    current_colcell = COL + operator(logic, col_cell)
                    self.debug = COL + operator(logic, col_cell)
                    break
                    #TODO: implement chosen accounting logic


    def result(self):
        
        print(f"self.debug: {self.debug}")