from up import *
from down import *
from right import *
from left import *

import random    


class Assignment:


    def __init__(self, maze):

        self.maze = maze

        #self.assignments = {
        #
        #    "u": Up(self),
        #    "d": Down(self),
        #    "l": Left(self),
        #    "r": Right(self)
        #
        #}

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


    def _get_amount_of_assignments(self, chosen_direction):

        score = self.maze.scores


        match chosen_direction:
            case "l":

                side = score.get(self.converted.get("l"))


            case "r":

                side = score.get(self.converted.get("r"))


            case "u":

                side = score.get(self.converted.get("u"))


            case "d":

                side = score.get(self.converted.get("d"))


        #if chosen_direction == "l":
        #
        #    side = score.get(self.converted.get("l"))
        #
        #
        #elif chosen_direction == "r":
        #
        #    side = score.get(self.converted.get("r"))
        #
        #
        #elif chosen_direction == "u":
        #
        #    side = score.get(self.converted.get("u"))
        #
        #
        #elif chosen_direction == "d":
        #
        #    side = score.get(self.converted.get("d"))

        print(f"side: {side}")

        if side >= 3:
            
            amount_of_assignments = random.randint(1, 3)


        elif side == 2:
            
            amount_of_assignments = random.randint(1, 2)


        elif side == 1:
            
            amount_of_assignments = 1


        # Not sure if side == 0 check is required
        else:

            print("\nSIDE 0 ?\n")


        return amount_of_assignments


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
            
            # Always check main side first
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


    def assign(self, confirmed_directions):

        chosen_direction = random.choice(confirmed_directions)
        print(chosen_direction)
        amount_of_assignments = self._get_amount_of_assignments(chosen_direction)

        match chosen_direction:
            case "l":

                LEFT = self._get_assignments("l")

                LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Right moves - assigned")

                LEFT.assign()

                LEFT.left_assigner = None


            case "r":

                RIGHT = self._get_assignments("r")

                RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Right moves - assigned")

                RIGHT.assign()

                RIGHT.right_assigner = None


            case "u":

                UP = self._get_assignments("u")

                UP.up_assigner = UP.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Up moves - assigned")

                UP.assign()

                UP.up_assigner = None


            case "d":

                DOWN = self._get_assignments("d")

                DOWN.down_assigner = DOWN.assigner(self, amount_of_assignments)
                print(f"{" "*amount_of_assignments}{amount_of_assignments} Down moves - assigned")

                DOWN.assign()

                DOWN.down_assigner = None

            
        print(f"----\nSUCCESS\n    {chosen_direction}\n----\n")





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


