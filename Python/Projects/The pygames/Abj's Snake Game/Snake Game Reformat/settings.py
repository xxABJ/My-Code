import json, sys, pygame


class Settings:


    def get_json_file(filename):
        
        try:

            with open(filename, "r") as file:
                
                return json.load(file)
            

        except:
            
            template = {
                "CELL_SIZE": 40,
                "CELL_ROW": 15,
                "SQUARE_BORDER_WIDTH": 2,
                "MAX_GAME_SPEED": 10,
                "SNAKE_SPEED": 6
            }
            
            
            with open(filename, "x") as file:
                
                json.dump(template, file)


            with open(filename, "r") as file:
                
                return json.load(file)
        

    FILE_NAME = "config_file.json"
    cfg = get_json_file(FILE_NAME)


    CELL_SIZE = cfg['CELL_SIZE']
    CELL_ROW = cfg['CELL_ROW']
    WIDTH = CELL_SIZE * CELL_ROW
    HEIGHT = CELL_SIZE * CELL_ROW
    SCORE_SURFACE_SIZE = CELL_SIZE
    SQUARE_BORDER_WIDTH = cfg['SQUARE_BORDER_WIDTH']
    CANVAS = pygame.Surface((WIDTH, HEIGHT))
    SNAKE_STARTING_SIZE = 3


    GRIDCELL_EMPTY = 0
    GRIDCELL_APPLE = 1
    GRIDCELL_SNAKE = 2


    # Bad calculation -.-
    PLAYING_SPEED = int((cfg['MAX_GAME_SPEED'] - cfg['SNAKE_SPEED'])*25)
    PLAYING_UE = pygame.USEREVENT
    

    RESTARTING_SPEED = 250
    RESTARTING_UE = pygame.USEREVENT


    COLOURS = {
        'screen_background': (50, 45, 104),
        'cell_green': (95, 129, 63),
        'grid_border': (79, 89, 31),
        'snake_green': (66, 102, 12),
        'apple_red': (187, 29, 29),
        'white': (255, 255, 255)
    }


from grid import *
from snake import *
from apple import *
from collisions import *
from rendering import *
from gamelogic import *

