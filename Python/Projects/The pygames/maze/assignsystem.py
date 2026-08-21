from up import Up
from down import Down
from right import Right
from left import Left

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




    # 2.1
    def _get_amount_of_assignments(self, chosen_direction):

        if self.print_console:

            print(f"╠{'═'*19}")
            print(f"╠════ assignsystem.py.AssignSystem._get_amount_of_assignments()")


            score = self.mazeEngine.get_scores()


            next_boundary = self.mazeEngine.boundarySystem.get_next_boundary(

                current_direction= chosen_direction,
                print_console= self.print_console

            )


            boundary_after_next_boundary = self.mazeEngine.boundarySystem.get_any_boundary(

                current_direction= chosen_direction,
                amount_of_assignments= 1,
                print_console= False

            )


            print("║")
            print(f"╠ next_boundary: {next_boundary}")
            print(f"╠ boundary_after_next_boundary: {boundary_after_next_boundary}")


            match chosen_direction:

                case "l":

                    border_distance = score.get(self.score_direction_translated.get("l"))


                case "r":
                
                    border_distance = score.get(self.score_direction_translated.get("r"))


                case "u":

                    border_distance = score.get(self.score_direction_translated.get("u"))


                case "d":

                    border_distance = score.get(self.score_direction_translated.get("d"))

            
            print(f"╠ border_distance: {border_distance}")
            print("║")


            # This is for if next boundary is in ["R", "|"] which means it is False and an invalid move
            if type(next_boundary) == list:

                print("║")
                print(f"║   BORDER_DIS == {border_distance} ")
                print(f"║   next_boundary: {next_boundary[1]}")
                print("║")
                print("║")
                print(f"║   ❌self.mazeEngine.boundarySystem.get_next_boundary(chosen_direction)")

                self.mazeEngine.boundarySystem.get_next_boundary(

                    current_direction= chosen_direction,
                    print_console= self.print_console,
                    
                    )

                print(f"║   ❌{self.mazeEngine.boundarySystem.get_next_boundary(current_direction= chosen_direction, print_console= False)}")


                amount_of_assignments = 0


                print("║")
                print(f"╠{'═'*9}")
                #input()
                return amount_of_assignments


            # This is for next boundary is O or G and the one after is in ["R", "|"] which means it is False and an invalid move
            elif next_boundary in ["O", "G"] and type(boundary_after_next_boundary) == list:

                print("║")
                print(f"║   BORDER_DIS == {border_distance} ")
                print(f"║   next_boundary: {next_boundary}")
                print(f"║   the boundary after that: {boundary_after_next_boundary[1]}")
                print("║")
                print("║")
                print(f"║   ❌self.mazeEngine.boundarySystem.get_any_boundary(chosen_direction, 1)")

                self.mazeEngine.boundarySystem.get_any_boundary(
                    
                    current_direction= chosen_direction,
                    amount_of_assignments= 1,
                    print_console= self.print_console
                    
                    )

                print(f"║   ❌{self.mazeEngine.boundarySystem.get_any_boundary(current_direction= chosen_direction, amount_of_assignments= 1, print_console= False)}")


                amount_of_assignments = 0


                print("║")
                print(f"╠{'═'*9}")
                #input()
                return amount_of_assignments


            elif border_distance > 4:
                
                choices = [1, 2, 3, 4]


            elif border_distance > 3:

                choices = [1, 2, 3]


            elif border_distance > 2:

                choices = [1, 2]


            elif 2 >= border_distance >= 1:

                choices = [1]


            while True:

                amount_of_assignments = random.choice(choices)
                print(f"╠ amount_of_assignments: {amount_of_assignments}")
                print("║")


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_any_boundary(

                    current_direction= chosen_direction,
                    amount_of_assignments= amount_of_assignments,
                    print_console= self.print_console

                )


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:

                    break


                else:
                    
                    print(f"║     FAILED - amount_of_assignments: {amount_of_assignments} is not valid")
                    choices.pop(choices.index(amount_of_assignments))


                if len(choices) == 0:

                    print("║")
                    print("║ All choices failed, returning amount_of_assignments = 0")
                    print("║")
                    amount_of_assignments = 0
                    break

            
            print(f"╠{'═'*19}")
            return amount_of_assignments
        

        else:

            score = self.mazeEngine.get_scores()


            next_boundary = self.mazeEngine.boundarySystem.get_next_boundary(

                current_direction= chosen_direction,
                print_console= self.print_console

            )


            boundary_after_next_boundary = self.mazeEngine.boundarySystem.get_any_boundary(

                current_direction= chosen_direction,
                amount_of_assignments= 1,
                print_console= False

            )


            match chosen_direction:

                case "l":

                    border_distance = score.get(self.score_direction_translated.get("l"))


                case "r":
                
                    border_distance = score.get(self.score_direction_translated.get("r"))


                case "u":

                    border_distance = score.get(self.score_direction_translated.get("u"))


                case "d":

                    border_distance = score.get(self.score_direction_translated.get("d"))


            # This is for if next boundary is in ["R", "|"] which means it is False and an invalid move
            if type(next_boundary) == list:

                # self.mazeEngine.boundarySystem.get_next_boundary(

                #     current_direction= chosen_direction,
                #     print_console= self.print_console,
                    
                #     )
                

                amount_of_assignments = 0
                return amount_of_assignments


            # This is for next boundary is O or G and the one after is in ["R", "|"] which means it is False and an invalid move
            elif next_boundary in ["O", "G"] and type(boundary_after_next_boundary) == list:

                # self.mazeEngine.boundarySystem.get_any_boundary(
                    
                #     current_direction= chosen_direction,
                #     amount_of_assignments= 1,
                #     print_console= self.print_console
                    
                #     )


                amount_of_assignments = 0
                return amount_of_assignments


            elif border_distance > 4:
                
                choices = [1, 2, 3, 4]


            elif border_distance > 3:

                choices = [1, 2, 3]


            elif border_distance > 2:

                choices = [1, 2]


            elif 2 >= border_distance >= 1:

                choices = [1]


            while True:

                amount_of_assignments = random.choice(choices)


                VALID_AMOUNT_OF_ASSIGNMENTS = self.mazeEngine.boundarySystem.get_any_boundary(

                    current_direction= chosen_direction,
                    amount_of_assignments= amount_of_assignments,
                    print_console= self.print_console

                )


                if type(VALID_AMOUNT_OF_ASSIGNMENTS) != list:

                    break


                else:
                    
                    choices.pop(choices.index(amount_of_assignments))


                if len(choices) == 0:

                    amount_of_assignments = 0
                    break


            return amount_of_assignments


    # 2.2
    def _get_direction_classes(self, direction) -> object:

        if direction == "l":

            return Left(self)


        elif direction == "r":

            return Right(self)


        elif direction == "u":

            return Up(self)


        elif direction == "d":

            return Down(self)


    # 2.
    def assign(self, confirmed_directions, index) -> tuple[bool, str]:

        assignment_state = None


        if self.print_console:
                

            print(f"╔{"═"*5} @MazeEngine.assignSystem.AssignSystem.assign()")
            print("║")


            if len(confirmed_directions) > 1:

                chosen_direction = random.choice(confirmed_directions)


            else:

                chosen_direction = confirmed_directions[0]


            print(f"╠ chosen_direction: {chosen_direction}")
            print("║")


            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                
            )


            print("║")
            print(f"╠ amount_of_assignments: {amount_of_assignments}")
            print("║")


            match chosen_direction:

                case "u":

                    UP = self._get_direction_classes("u")


                    UP.up_assigner = UP.assigner(self, amount_of_assignments)


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Up moves - assigned")
                    print("║")
                    print(f"╚{"═"*30}╝\n")


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

                    DOWN = self._get_direction_classes("d")


                    DOWN.down_assigner = DOWN.assigner(self, amount_of_assignments)


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Down moves - assigned")
                    print("║")
                    print(f"╚{"═"*30}╝\n")


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

                    RIGHT = self._get_direction_classes("r")


                    RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Right moves - assigned")
                    print("║")
                    print(f"╚{"═"*30}╝\n")


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

                    LEFT = self._get_direction_classes("l")


                    LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)


                    print(f"║ {" "*amount_of_assignments}{amount_of_assignments} Left moves - assigned")
                    print("║")
                    print(f"╚{"═"*30}╝\n")


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

            if len(confirmed_directions) > 1:

                chosen_direction = random.choice(confirmed_directions)


            else:

                chosen_direction = confirmed_directions[0]


            amount_of_assignments = self._get_amount_of_assignments(
                
                chosen_direction= chosen_direction,
                
            )


            match chosen_direction:

                case "u":

                    UP = self._get_direction_classes("u")


                    UP.up_assigner = UP.assigner(self, amount_of_assignments)


                    if UP.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    UP.up_assigner = None


                case "d":

                    DOWN = self._get_direction_classes("d")


                    DOWN.down_assigner = DOWN.assigner(self, amount_of_assignments)


                    if DOWN.assign() == False:

                        assignment_state = False 
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    DOWN.down_assigner = None


                case "r":

                    RIGHT = self._get_direction_classes("r")


                    RIGHT.right_assigner = RIGHT.assigner(self, amount_of_assignments)


                    if RIGHT.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    RIGHT.right_assigner = None


                case "l":

                    LEFT = self._get_direction_classes("l")


                    LEFT.left_assigner = LEFT.assigner(self, amount_of_assignments)


                    if LEFT.assign() == False:

                        assignment_state = False
                        return assignment_state, chosen_direction
                    

                    else:

                        assignment_state = True


                    LEFT.left_assigner = None


            return assignment_state, chosen_direction
        


    def get_cached_directions(self, latest_direction) -> dict[tuple, tuple]:

        match latest_direction:
            
            case "u":

                direction = "UP"
                

            case "d":

                direction = "DOWN"
                
            
            case "r":

                direction = "RIGHT"
                
            
            case "l":

                direction = "LEFT"


        direction_class = self._get_direction_classes(latest_direction)
  

        if self.print_console:

            print("\n")
            print(f"┌{'─'*15} {direction} CLASS CACHE {'─'*17}┐")


            k = 0
            for key, value in direction_class.cached_directions.items():

                if k != key[0]:
                    print(f"│\n├─ BATCH {key[0]}:\n│  assignment No. {str(key[1][0]): <3} , {str(key[1][1]): >3}  {"•grid_pos:": >10} {value}")
                    k = key[0]


                elif k == key[0]:
                    print(f"│  assignment No. {str(key[1][0]): <3} , {str(key[1][1]): >3}  {"•grid_pos:": >10} {value}")


            print("│")
            print(f"└{'─'*50}┘")
            print("\n")


        return self._get_direction_classes(latest_direction).cached_directions

