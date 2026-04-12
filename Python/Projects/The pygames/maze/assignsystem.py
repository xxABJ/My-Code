from up import *
from down import *
from right import *
from left import *

import random    


class AssignSystem:


    def __init__(self, object_mazeEWngine):

        self.mazeEngine = object_mazeEWngine
        self.print_console = self.mazeEngine.print_console


        self.arrows = self.mazeEngine.arrows
        self.score_direction_translated = self.mazeEngine.score_direction_translated
        

        self.at_bottom = False
        




    # brute force complete, with at_bottom indicator, all paths logging
    # 1.1
    def _get_valid_directions(self, previous_direction):
        
        def c_topleft(scores) -> bool:
            
            topside = scores.get(self.score_direction_translated.get("u"))
            leftside = scores.get(self.score_direction_translated.get("l"))


            if topside == 0 and leftside == 0:
            
                return True
            

            else:

                return False
            

        def c_topright(scores) -> bool:
            
            topside = scores.get(self.score_direction_translated.get("u"))
            rightside = scores.get(self.score_direction_translated.get("r"))


            if topside == 0 and rightside == 0:
            
                return True
            

            else:

                return False
            
            
        def c_bottomleft(scores) -> bool:
            
            bottomside = scores.get(self.score_direction_translated.get("d"))
            leftside = scores.get(self.score_direction_translated.get("l"))


            if bottomside == 0 and leftside == 0:
            
                return True
            

            else:

                return False
            
            
        def c_bottomright(scores) -> bool:
            
            bottomside = scores.get(self.score_direction_translated.get("d"))
            rightside = scores.get(self.score_direction_translated.get("r"))


            if bottomside == 0 and rightside == 0:
            
                return True
            
            
            else:

                return False




        scores = self.mazeEngine.get_scores()
        

        leftside = scores.get(self.score_direction_translated.get("l"))
        rightside = scores.get(self.score_direction_translated.get("r"))
        topside = scores.get(self.score_direction_translated.get("u"))
        bottomside = scores.get(self.score_direction_translated.get("d"))


        if previous_direction == "l":
            
            # Always check main border_distance first
            if leftside == 0:

                if c_topleft(scores):

                    return ["d"]
                

                # w/brute force method (go to "F" when at_bottom == True), this shouldn't be possible
                elif c_bottomleft(scores):

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
            

            # checking rightside is not required


            else:


                #@TODO: LOGIC FOR CHECKING A WALL BETWEEN ASSIGNMENTS IS PRESENT


                return ["l", "u", "d"]


        elif previous_direction == "r":
            
            # Always check main side first
            if rightside == 0:

                if c_topright(scores):

                    return ["d"]
                

                # w/brute force method (go to "F" when at_bottom == True), this shouldn't be possible
                elif c_bottomright(scores):

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


                if c_bottomleft(scores):

                    return ["r"]
                

                elif c_bottomright(scores):

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

                if c_topleft(scores):

                    return ["r"]
                

                elif c_topright(scores):

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

    # 1.
    def validate_direction(self):

        previous_direction = self.mazeEngine.previous_assignment()[0][1]


        confirmed_directions = self._get_valid_directions(previous_direction)


        return confirmed_directions





    # TODO: WTF IS THIS MESS, DELETE!
    # OR REMAKE USING C1, C2, C3 CONCEPTS
    # 2.1
    def _get_amount_of_assignments(self, chosen_direction):

        score = self.mazeEngine.get_scores()
        #last_direction = -1
        

        if self.print_console:

            print(f"╠{'═'*7}")
            print(f"╠═══ assignsystem.py.AssignSystem._get_amount_of_assignments()")


        match chosen_direction:

            case "l":

                border_distance = score.get(self.score_direction_translated.get("l"))

                # grid = self.maze.grid[:]
                # leftside = self.maze.scores.get("leftside")
                
                # for l_distance in range(1, leftside + 1):

                #     if grid[previous_pos[0]][previous_pos[1] - l_distance] == self.maze.arrows.get("l"):

                #         print(f"last   : {last_direction}")
                #         last_direction = (l_distance - 1)
                #         print(f"last   : {last_direction}")
                #         break


            case "r":
            
                border_distance = score.get(self.score_direction_translated.get("r"))
            

                #grid = self.maze.grid[:]
                #rightside = self.maze.scores.get(self.converted.get("r"))
                #for r_distance in range(1, rightside + 1):
                #
                #    if grid[previous_pos[0]][previous_pos[1] + r_distance] == self.maze.arrows.get("r"):
                #
                #        print(f"last   : {last_direction}")
                #        last_direction = (r_distance - 1)
                #        print(f"last   : {last_direction}")
                #        break


            case "u":

                border_distance = score.get(self.score_direction_translated.get("u"))

                # grid = self.maze.grid[:]
                # topside = self.maze.scores.get("topside")
                
                # for u_distance in range(1, topside + 1):

                #     if grid[previous_pos[0] - u_distance][previous_pos[1]] == self.maze.arrows.get("u"):

                #         print(f"last   : {last_direction}")
                #         last_direction = (u_distance - 1)
                #         print(f"last   : {last_direction}")
                #         break


            case "d":

                border_distance = score.get(self.score_direction_translated.get("d"))

                # grid = self.maze.grid[:]
                # bottomside = self.maze.scores.get("bottomside")
                # print(f"bottomside: {bottomside}")
                
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


        if self.print_console:
            
            print(f"║   border_distance: {border_distance}")
            #print(f"last_direction: {last_direction}")


        #if last_direction == -1:
        if border_distance > 4:
            
            amount_of_assignments = random.choice([1, 2, 3, 4])


        elif border_distance > 3:
            
            amount_of_assignments = random.choice([1, 2, 3])


        elif border_distance > 2:
            
            amount_of_assignments = random.choice([1, 2])


        elif border_distance == 2:

            amount_of_assignments = 1


        #@TODO: LOGIC FOR CHANGING DIRECTION REQUIRED
        else:

            if self.print_console:

                print("║   BORDER_DIS == 1 ?")


            amount_of_assignments = 0

        
        #else:
        
        #    print("CLOSE TO OLDER ASSIGNMENT !!!!!")
        #    amount_of_assignments = 0


            if self.print_console:

                print(f"╠{'═'*7}")


        return amount_of_assignments

    # 2.2
    def _get_assignments(self, direction) -> object:

        if direction == "l":

            return Left(self)


        elif direction == "r":

            return Right(self)


        elif direction == "u":

            return Up(self)


        elif direction == "d":

            return Down(self)


    # 2.
    def assign(
            
            self,
            confirmed_directions,
            index,
            
        ) -> tuple[bool, str]:

        assignment_state = None


        if self.print_console:
                

            print(f"╔{"═"*5} @MazeEngine.assignSystem.AssignSystem.assign()")
            print("║")


            chosen_direction = random.choice(confirmed_directions)
            print(f"╠ chosen_direction: {chosen_direction}")
            print("║")
            previous_pos = self.mazeEngine.previous_assignment()[1]


            # TODO: Last direction concept (cache?, recalling?)
            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                #previous_pos= previous_pos
                
            )



            print("║")
            print(f"╠ amount_of_assignments: {amount_of_assignments}")
            print("║")


            match chosen_direction:

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


                    #DOWN.down_cache = ""


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Down moves - assigned")
                    print("║")
                    print(f"╚{"═"*20}╝\n")


                    if DOWN.assign() == False:

                        print("│")
                        print(f"│ DOWN ASSIGNMENT FAILED")
                        print(f"│ Amount of assignments: {amount_of_assignments}")
                        print("│")
                        print(f"└{'─'*20}┘\n")


                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    DOWN.down_assigner = None


                case "r":

                    RIGHT = self._get_assignments("r")


                    RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)


                    #RIGHT.right_cache = ""


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Right moves - assigned")
                    print("║")
                    print(f"╚{"═"*20}╝\n")


                    if RIGHT.assign() == False:

                        print("│")
                        print(f"│ RIGHT ASSIGNMENT FAILED")
                        print(f"│ Amount of assignments: {amount_of_assignments}")
                        print("│")
                        print(f"└{'─'*20}┘\n")


                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    RIGHT.right_assigner = None


                case "l":

                    LEFT = self._get_assignments("l")


                    LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments, self.print_console)
                    print(f"{" "*amount_of_assignments}{amount_of_assignments} Left moves - assigned")


                    if LEFT.assign() == False:
                        assignment_state = False
                        return assignment_state, chosen_direction
                    
                    else:
                        assignment_state = True


                    LEFT.left_assigner = None


            print(f"╔═════ @MazeEngine.assignSystem.AssignSystem.assign()   -    TESTING LOOP No.{index+1}\n╚═          direction: {chosen_direction}\n")


            return assignment_state, chosen_direction
    

        else:

            chosen_direction = random.choice(confirmed_directions)
            previous_pos = self.mazeEngine.previous_assignment()[1]


            #TODO: Last direction concept (cache?, recalling?)
            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                previous_pos= previous_pos
                
            )


            match chosen_direction:

                case "u":

                    pass


                case "d":

                    DOWN = self._get_assignments("d")


                    DOWN.down_assigner = DOWN.assigner(self, amount_of_assignments)


                    #DOWN.down_cache = ""


                    if DOWN.assign() == False:

                        assignment_state = False 
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    DOWN.down_assigner = None


                case "r":

                    RIGHT = self._get_assignments("r")


                    RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments, self.print_console)


                    #RIGHT.right_cache = ""


                    if RIGHT.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    RIGHT.right_assigner = None


                case "l":

                    pass


            return assignment_state, chosen_direction