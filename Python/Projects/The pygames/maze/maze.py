from mazeengine import MazeEngine
#import random

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
            
            )


    def print_maze(self):

        for row in self.mazeEngine.maze:

            for col in row:

                print(col, end= " ")


            print()
        

        print()


Maze(

    size=40,
    custom_starting_point= False,
    custom_starting_direction= False,
    print_console= True,

    ).print_maze()

