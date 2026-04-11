from mazeengine import MazeEngine
from factoringsystem import FactoringSystem
from assignsystem import AssignSystem
#from scanner import *


#import pygame


class Maze:


    def __init__(
            
            self,
            size: int= 30,
            custom_starting_point: tuple | bool= False,
            custom_starting_direction: str | bool= False,
            print_console: bool= False
            
    ):
        
        #TODO: check for size and print_console aswell
        def checking_arguments(custom_starting_point, custom_starting_direction):

            # Checking custom_starting_point
            try:

                data_type = type(custom_starting_point)


                if data_type in [bool, tuple]:
                
                    if data_type == bool:

                        if custom_starting_point == True:

                            custom_starting_point = False


                        else:

                            pass


                    elif data_type == tuple:

                        inside_tuple_type = type(custom_starting_point[0])
                        
                        
                        if inside_tuple_type == int:

                            pass


                        inside_tuple_type = type(custom_starting_point[1])
                        
                        
                        if inside_tuple_type == int:

                            pass


            except:

                if data_type not in [bool, tuple]:

                    print("\n\n  The custom_starting_point argument must be of type tuple or bool.\n    Disabling custom_starting_point\n\n")
                    

                else:

                    if inside_tuple_type != int:

                        print("\n\n  The custom_starting_point tuple argument must be of type int.\n    Disabling custom_starting_point\n\n")


                custom_starting_point = False


            # Checking custom_starting_direction
            try:

                data_type = type(custom_starting_direction)


                if data_type in [bool, str]:
                
                    if data_type == bool:

                        if custom_starting_direction == True:

                            custom_starting_direction = False


                        else:

                            pass


                    elif data_type == str:

                        length_data_type = len(custom_starting_direction)


                        if length_data_type == 1:
                            
                            pass


                        characters_data_type = custom_starting_direction


                        if characters_data_type in ["l", "r", "u", "d"]:
                            
                            pass


            except:

                if data_type not in [bool, str]:

                    print("\n\n  The custom_starting_direction argument must be of type str or bool.\n    Disabling custom_starting_direction\n\n")
                    

                else:

                    if length_data_type != 1:

                        print("\n\n  The custom_starting_direction argument must be a single character string.\n    Disabling custom_starting_direction\n\n")


                    elif characters_data_type not in ["l", "r", "u", "d"]:

                        print("\n\n  The custom_starting_direction argument must be either 'l', 'r', 'u' or 'd'.\n    Disabling custom_starting_direction\n\n")


                custom_starting_direction = False


            return custom_starting_point, custom_starting_direction


        self.custom_starting_point, self.custom_starting_direction = checking_arguments(custom_starting_point, custom_starting_direction)


        self.mazeEngine = MazeEngine(
            
            object_maze= self,
            size= size,
            custom_starting_point= self.custom_starting_point,
            custom_starting_direction= self.custom_starting_direction,
            print_console= print_console,
            object_factoringSystem= FactoringSystem(), 
            object_assignSystem= AssignSystem()
            
            )


        #self.available_directions = ["l", "r", "u", "d"]
        #self.random_direction = None


        # These tuples are based on how grid is being iterated in / how it was created
        # self.directions = {

        #     'l': (0, -1),
        #     'r': (0, 1),
        #     'u': (-1, 0),
        #     'd': (1, 0)

        # }


        # self.scores = {

        #     'topside': 0,
        #     'bottomside': 0,
        #     'rightside':0,
        #     'leftside': 0

        # }


        # self.total_assignments = 0
        # self.assignments = {}


        # self.arrows = {

        #    "l": "←",
        #    "r": "→",
        #    "u": "↑",
        #    "d": "↓"

        # }

        #########################################################
        # checking_arguments()


        # self.mazeEngine = MazeEngine(
            
        #     object_maze= self,
        #     size= size,
        #     custom_starting_point= custom_starting_point,
        #     custom_starting_direction= custom_starting_direction,
        #     print_console= print_console,
        #     object_factoringSystem= FactoringSystem(), 
        #     object_assignSystem= AssignSystem()
            
        #     )
        #########################################################

        # self.factoring = Factoring()

        # self.assignor = Assignment(self, self.print_console)

        # #self.scanner = Scanner(self)


        # self.grid = self.create_grid(self.size)


        # self._chosen_cell_pos = ()
        # self._selected_cell_info = []


        # self.first_assignment_and_direction_completed = self.set_first_assingment_and_direction(

        #     # Custom Starting point (tuple)
        #     tuple_pos= False,

        #     # Direction specifier (str)
        #     direction= "r",

        #     # Console printing (bool)
        #     print_console = self.print_console

        # )


        # self.maze_completed = False
        # self.maze = self.create_maze()




    def print_maze(self):

        for row in self.mazeEngine.maze:

            for col in row:

                print(col, end= " ")


            print()
        

        print()





#Maze(20).print_grid()
#a.set_first_assingment_and_direction((4, 10))
#Maze(50).print_maze()
#a = Maze(25)
#a.print_grid()
Maze(30, False).print_maze()

