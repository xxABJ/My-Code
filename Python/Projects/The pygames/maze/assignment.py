from up import *
from down import *
from right import *
from left import *

import random    


class Assignment:


    def __init__(self, maze):

        self.maze = maze


        self.converted = {

            "l": "leftside",
            "r": "rightside",
            "u": "topside",
            "d": "bottomside",

        }
        

        self.at_bottom = False
        

    def _get_assignments(self, direction):

        if direction == "l":

            return Left(self)


        elif direction == "r":

            return Right(self)


        elif direction == "u":

            return Up(self)


        elif direction == "d":

            return Down(self)


    def validate_direction(self, previous_assignment):

        previous_direction = previous_assignment[0][1]
        previous_pos = previous_assignment[1]


        #print(previous_direction)
        confirmed_directions = self._get_valid_directions(previous_direction)
        return confirmed_directions


    # 1 brute force complete, with at_bottom indicator, all paths logging
    def _get_valid_directions(self, previous_direction):
        
        def c_topleft(scores) -> bool:
            
            topside = scores.get("topside")
            leftside = scores.get("leftside")

            if topside == 0 and leftside == 0:
            
                return True
            
            else:

                return False
            

        def c_topright(scores) -> bool:
            
            topside = scores.get("topside")
            rightside = scores.get("rightside")

            if topside == 0 and rightside == 0:
            
                return True
            
            else:

                return False
            
            
        def c_bottomleft(scores) -> bool:
            
            bottomside = scores.get("bottomside")
            leftside = scores.get("leftside")

            if bottomside == 0 and leftside == 0:
            
                return True
            
            else:

                return False
            
            
        def c_bottomright(scores) -> bool:
            
            bottomside = scores.get("bottomside")
            rightside = scores.get("rightside")

            if bottomside == 0 and rightside == 0:
            
                return True
            
            else:

                return False


        scores = self.maze.scores
        

        leftside = scores.get("leftside")
        rightside = scores.get("rightside")
        topside = scores.get("topside")
        bottomside = scores.get("bottomside")


        if previous_direction == "l":
            
            # Always check main border_distance first
            if leftside == 0:

                if c_topleft:

                    return ["d"]
                

                # w/brute force method (go to "F" when at_bottom == True), this shouldn't be possible
                elif c_bottomleft:

                    self.at_bottom = True
                    return ["u"]
                

                # c_topright & c_bottomright is not possible


                else:

                    return ["u", "d"]
                

            elif topside == 0:

                 return ["l", "d"]
            

            elif bottomside == 0:

                self.at_bottom = True
                return ["l", "u"]
            

            # checking leftside is not required


            else:


                #@TODO: LOGIC FOR CHECKING A WALL BETWEEN ASSIGNMENTS IS PRESENT


                return ["l", "u", "d"]


        elif previous_direction == "r":
            
            # Always check main side first
            if rightside == 0:

                if c_topright:

                    return ["d"]
                

                # w/brute force method (go to "F" when at_bottom == True), this shouldn't be possible
                elif c_bottomright:

                    self.at_bottom = True
                    return ["u"]
                

                # c_topleft & c_bottomleft is not possible


                else:

                    return ["u", "d"]
                

            elif topside == 0:

                 return ["r", "d"]
            

            elif bottomside == 0:

                self.at_bottom = True
                return ["r", "u"]
            

            # checking leftside is not required


            else:

                return ["r", "u", "d"]

    

        elif previous_direction == "d":
            
            # Always check main side first
            if bottomside == 0:

                self.at_bottom = True


                if c_bottomleft:

                    return ["r"]
                

                elif c_bottomright:

                    return ["l"]
                

                # c_topleft & c_topright is not possible
                
                
                else:

                    return ["l", "r"]
                
            
            elif leftside == 0:

                return ["d", "r"]
            

            elif rightside == 0:

                return ["d", "l"]
            

            # checking topside is not required


            else:

                return ["l", "r", "d"]


        elif previous_direction == "u":
            
            # Always check main side first
            if topside == 0:

                if c_topleft:

                    return ["r"]
                

                elif c_topright:

                    return ["l"]
                

                # c_bottomleft & c_bottomright is not possible
                

                else:

                    return ["l", "r"]
                

            elif leftside == 0:

                return ["u", "r"]
            

            elif rightside == 0:

                return ["u", "l"]


            # checking bottomside is not required


            else:

                return ["l", "r", "u"]



    def _get_amount_of_assignments(self, chosen_direction, previous_pos):

        score = self.maze.scores
        last_direction = -1


        match chosen_direction:
            case "l":

                border_distance = score.get(self.converted.get("l"))

                grid = self.maze.grid[:]
                leftside = self.maze.scores.get("leftside")
                
                for l_distance in range(1, leftside + 1):

                    if grid[previous_pos[0]][previous_pos[1] - l_distance] == self.maze.arrows.get("l"):

                        print(f"last   : {last_direction}")
                        last_direction = (l_distance - 1)
                        print(f"last   : {last_direction}")
                        break



            case "r":

                border_distance = score.get(self.converted.get("r"))

                grid = self.maze.grid[:]
                rightside = self.maze.scores.get("rightside")
                
                for r_distance in range(1, rightside + 1):

                    if grid[previous_pos[0]][previous_pos[1] + r_distance] == self.maze.arrows.get("r"):

                        print(f"last   : {last_direction}")
                        last_direction = (r_distance - 1)
                        print(f"last   : {last_direction}")
                        break


            case "u":

                border_distance = score.get(self.converted.get("u"))

                grid = self.maze.grid[:]
                topside = self.maze.scores.get("topside")
                
                for u_distance in range(1, topside + 1):

                    if grid[previous_pos[0] - u_distance][previous_pos[1]] == self.maze.arrows.get("u"):

                        print(f"last   : {last_direction}")
                        last_direction = (u_distance - 1)
                        print(f"last   : {last_direction}")
                        break


            case "d":

                border_distance = score.get(self.converted.get("d"))

                grid = self.maze.grid[:]
                bottomside = self.maze.scores.get("bottomside")
                print(f"bottomside: {bottomside}")
                
                #for d_distance in range(1, bottomside + 1):
                #
                #    #print(d_distance)
                #    if grid[previous_pos[0] + d_distance][previous_pos[1]] == self.maze.arrows.get("d"):
                #
                #        print(f"last   : {last_direction}")
                #        last_direction = (d_distance)
                #        print(f"last   : {last_direction}")
                #
                #        print(self.maze.print_grid())
                #
                #        break


        print(f"border_distance: {border_distance}")
        print(f"last_direction: {last_direction}")


        if last_direction == -1:

            if border_distance > 4:
                
                amount_of_assignments = random.choice([2, 4])


            elif border_distance > 2:
                
                amount_of_assignments = random.choice([2])
                #amount_of_assignments = 2

            elif border_distance == 2:

                amount_of_assignments = 1


            #elif border_distance == 2:
            #    
            #    amount_of_assignments = random.randint(1, 2)
            #    #amount_of_assignments = 1
            #
            #elif border_distance == 1:
            #
            #    amount_of_assignments = 1


            #@TODO: LOGIC FOR CHANGING DIRECTION REQUIRED
            else:

                print("\nBORDER_DIS == 0 ?\n")


                #print(self.maze.print_assignments())
                #print(self.maze.print_grid())
                amount_of_assignments = 0

            #elif border_distance == 3:
            #    
            #    amount_of_assignments = random.randint(1, 3)
            #    #amount_of_assignments = 2
            #
            #
            #elif border_distance == 2:
            #    
            #    amount_of_assignments = random.randint(1, 2)
            #    #amount_of_assignments = 1
            #
            #elif border_distance == 1:
            #
            #    amount_of_assignments = 1
            #
            #
            ## Not sure if border_distance == 0 check is required
            #else:
            #
            #    print("\nBORDER_DIS == 0 ?\n")
            #
            #
            #    #print(self.maze.print_assignments())
            #    #print(self.maze.print_grid())
            #    amount_of_assignments = 0
        
        else:

            print("CLOSE TO OLDER ASSIGNMENT !!!!!")
            amount_of_assignments = 0
            #if border_distance >= 4 and last_direction == 3 or last_direction == 0:
            #    
            #    amount_of_assignments = random.randint(1, 3)
            #
            #
            #elif border_distance == 3 and last_direction == 2 or last_direction == 0:
            #    
            #    amount_of_assignments = random.randint(1, 2)
            #    #amount_of_assignments = 2
            #
            #elif border_distance == 2 and last_direction == 1 or last_direction == 0:
            #    
            #    amount_of_assignments = 1
            #    #amount_of_assignments = 2
            #
            #
            #elif border_distance == 1 and last_direction == 0:
            #    
            #    amount_of_assignments = 1
            #
            #
            ## Not sure if border_distance == 0 check is required
            #else:
            #
            #    if last_direction == 0:
            #        print("\nLAST_DIRECTION == 0\n")
            #        
            #    else:
            #        print("\nw last BORDER_DIS == 0 ?\n")
            #        print(border_distance)
            #        amount_of_assignments = 0
            #
            #    #print(self.maze.print_assignments())
            #    #print(self.maze.print_grid())
            #
            #    #amount_of_assignments = 0




        return amount_of_assignments


    def assign(self, confirmed_directions, previous_assignments, index):

        chosen_direction = random.choice(confirmed_directions)
        previous_pos = previous_assignments[1]
        print(chosen_direction)
        amount_of_assignments = self._get_amount_of_assignments(chosen_direction, previous_pos)
        print(amount_of_assignments)

        match chosen_direction:
            case "l":

                LEFT = self._get_assignments("l")

                LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Left moves - assigned")

                if LEFT.assign() == False:
                    return False

                LEFT.left_assigner = None


            case "r":

                RIGHT = self._get_assignments("r")

                RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Right moves - assigned")

                if RIGHT.assign() == False:
                    return False

                RIGHT.right_assigner = None


            case "u":

                UP = self._get_assignments("u")

                UP.up_assigner = UP.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Up moves - assigned")

                if UP.assign() == False:
                    return False

                UP.up_assigner = None


            case "d":

                DOWN = self._get_assignments("d")

                DOWN.down_assigner = DOWN.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Down moves - assigned")

                if DOWN.assign() == False:
                    return False

                DOWN.down_assigner = None


        #if self.maze.scores.get("bottomside") == 0:
        #
        #    self.at_bottom = True


        print(f" ♦ Successful Assignment No.{index+1}\n     direction: {chosen_direction}\n\n{"-"*20}")





    # 2 return a 3x3 grid info where center cell is row & col and returns list of validated directions - for now just uses scores

    # also can make it contain more logic, such as does not intersect, rewind to cause of intersection direction, check for specific score to move specifically, right paths logging only
    def get_cell_info(self, previous_direction, row, col):
        
        def c_topleft(scores) -> bool:
            
            topside = scores.get("topside")
            leftside = scores.get("leftside")

            if topside == 0 and leftside == 0:
            
                return True
            
            else:

                return False
            

        def c_topright(scores) -> bool:
            
            topside = scores.get("topside")
            rightside = scores.get("rightside")

            if topside == 0 and rightside == 0:
            
                return True
            
            else:

                return False
            
            
        def c_bottomleft(scores) -> bool:
            
            bottomside = scores.get("bottomside")
            leftside = scores.get("leftside")

            if bottomside == 0 and leftside == 0:
            
                return True
            
            else:

                return False
            
            
        def c_bottomright(scores) -> bool:
            
            bottomside = scores.get("bottomside")
            rightside = scores.get("rightside")

            if bottomside == 0 and rightside == 0:
            
                return True
            
            else:

                return False


        scores = self.maze.scores
        

        leftside = scores.get("leftside")
        rightside = scores.get("rightside")
        topside = scores.get("topside")
        bottomside = scores.get("bottomside")


        if previous_direction == "l":
            
            pass


        elif previous_direction == "r":
            
            pass
    

        elif previous_direction == "d":
            
            if leftside == 0:

                if c_bottomleft:
                    
                    self.at_bottom  = True
                    return ["r"]
                

                else:

                    return ["r", "d"]
            

            elif rightside == 0:

                if c_bottomright:
                    
                    self.at_bottom  = True
                    return ["l"]
                

                else:

                    return ["l", "d"]
                
            
            else:

                return ["l", "r", "d"]


        elif previous_direction == "u":
            
            if topside == 0:

                if c_topleft:

                    return ["r"]
                

                elif c_topright:

                    return ["l"]
                

                else:

                    return ["l", "r"]
                
            else:

                return ["l", "r", "u"]


        return


