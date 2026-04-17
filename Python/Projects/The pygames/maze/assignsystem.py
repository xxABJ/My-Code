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

        if len(previous_direction) != 1:

            previous_direction = previous_direction[-1]


        confirmed_directions = self._get_valid_directions(previous_direction)


        return confirmed_directions





    # TODO: WTF IS THIS MESS, DELETE!
    # OR REMAKE USING C1, C2, C3 CONCEPTS
    # 2.1
    def _get_amount_of_assignments(self, chosen_direction):

        score = self.mazeEngine.get_scores()  


        next_boundary = self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction)
        print(f"╠ next_boundary: {next_boundary}")
        #input()


        if self.print_console:

            print(f"╠{'═'*7}")
            print(f"╠═══ assignsystem.py.AssignSystem._get_amount_of_assignments()")


        match chosen_direction:

            case "l":

                border_distance = score.get(self.score_direction_translated.get("l"))



            case "r":
            
                border_distance = score.get(self.score_direction_translated.get("r"))



            case "u":

                border_distance = score.get(self.score_direction_translated.get("u"))



            case "d":

                border_distance = score.get(self.score_direction_translated.get("d"))



        if self.print_console:
            
            print(f"║   border_distance: {border_distance}")


        if next_boundary in ["O", "G"] and type(self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, 1)) == list and self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, 1)[1] in ["R", "|", "↑", "↓", "→", "←"]:

            if self.print_console:

                print("║   BORDER_DIS == 1 ?")


            amount_of_assignments = 0


            if self.print_console:

                print(f"╠{'═'*7}")

            return amount_of_assignments


        elif border_distance > 4:
            
            loops = 0
            while loops < 10:

                amount_of_assignments = random.choice([1, 2, 3, 4])
                print(f"╠ amount_of_assignments: {amount_of_assignments}")


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, amount_of_assignments)


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:

                    break


                loops += 1


            if loops == 10:

                print("loops == 10, returning 0")
                amount_of_assignments = 0


            return amount_of_assignments


        elif border_distance > 3:
            
            loops = 0
            while loops < 10:

                amount_of_assignments = random.choice([1, 2, 3])
                print(f"╠ amount_of_assignments: {amount_of_assignments}")


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, amount_of_assignments)


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:
                    
                    break


                loops += 1


            if loops == 10:

                print("loops == 10, returning 0")
                amount_of_assignments = 0


            return amount_of_assignments


        elif border_distance > 2:
            
            loops = 0
            while loops < 10:

                amount_of_assignments = random.choice([1, 2])
                print(f"╠ amount_of_assignments: {amount_of_assignments}")


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, amount_of_assignments)


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:
                    
                    break


                loops += 1


            if loops == 10:

                print("loops == 10, returning 0")
                amount_of_assignments = 0


            return amount_of_assignments


        elif border_distance == 2:

            print("\n\n\n\n\nNOT POSSIBLEEEEEEEEEE\n\n\n\n\n")


            loops = 0            
            while loops < 10:

                amount_of_assignments = 1
                print(f"╠ amount_of_assignments: {amount_of_assignments}")


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, amount_of_assignments)


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:
                    
                    break


                loops += 1


            if loops == 10:

                print("loops == 10, returning 0")
                amount_of_assignments = 0
                
            return amount_of_assignments
        

        else:

            print("\n\n\n\n\nAFTER FILTERING NEXT NEXT BOUNDARY\n\n\n\n\n")
            print(f"╠ border_distance: {border_distance}")
            print(f"╠ chosen_direction: {chosen_direction}")
            print(f"╠ next_boundary: {next_boundary}")
            print(f"╠ self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, 1): {self.mazeEngine.boundarySystem.get_next_boundary_type(chosen_direction, 1)}")
            input()


            amount_of_assignments = 1
            return amount_of_assignments


        # #@TODO: LOGIC FOR CHANGING DIRECTION REQUIRED
        # else:

        #     if self.print_console:

        #         print("║   BORDER_DIS == 1 ?")


        #     amount_of_assignments = 0


        #     if self.print_console:

        #         print(f"╠{'═'*7}")


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


            # TODO: Last direction concept (cache?, recalling?)
            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                
            )



            print("║")
            print(f"╠ amount_of_assignments: {amount_of_assignments}")
            print("║")


            match chosen_direction:

                case "u":

                    UP = self._get_assignments("u")


                    UP.up_assigner = UP.assigner(self, amount_of_assignments)


                    #UP.up_cache = ""


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Up moves - assigned")
                    print("║")
                    print(f"╚{"═"*20}╝\n")


                    if UP.assign() == False:

                        print("│")
                        print(f"│ UP ASSIGNMENT FAILED")
                        print(f"│ Amount of assignments: {amount_of_assignments}")
                        print("│")
                        print(f"└{'─'*20}┘\n")


                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


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


                    LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)


                    #LEFT.left_cache = ""


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Left moves - assigned")
                    print("║")
                    print(f"╚{"═"*20}╝\n")


                    if LEFT.assign() == False:

                        print("│")
                        print(f"│ LEFT ASSIGNMENT FAILED")
                        print(f"│ Amount of assignments: {amount_of_assignments}")
                        print("│")
                        print(f"└{'─'*20}┘\n")


                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    LEFT.left_assigner = None


            print(f"╔═════ @MazeEngine.assignSystem.AssignSystem.assign()   -    TESTING LOOP No.{index+1}\n╚═          direction: {chosen_direction}\n")


            return assignment_state, chosen_direction
    

        else:

            chosen_direction = random.choice(confirmed_directions)


            #TODO: Last direction concept (cache?, recalling?)
            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                
            )


            match chosen_direction:

                case "u":

                    UP = self._get_assignments("u")


                    UP.up_assigner = UP.assigner(self, amount_of_assignments)


                    #UP.up_cache = ""


                    if UP.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    UP.up_assigner = None


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


                    RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)


                    #RIGHT.right_cache = ""


                    if RIGHT.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    RIGHT.right_assigner = None


                case "l":

                    LEFT = self._get_assignments("l")


                    LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)


                    #LEFT.left_cache = ""


                    if LEFT.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    LEFT.left_assigner = None


            return assignment_state, chosen_direction