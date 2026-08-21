from imports import *

class Settings:


    WIDTH = 800
    HEIGHT = 600
    CANVAS = pygame.Surface((WIDTH, HEIGHT))


    DECK_1 = [
        {"spades":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"hearts":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"clubs":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"diamonds":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
    ]

    DECK_2 = [
        {"spades":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"hearts":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"clubs":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {"diamonds":[1,2,3,4,5,6,7,8,9,10,11,12,13]},
    ]


    # Backgrounds
    @staticmethod
    def bg_randomizor():
    
        return (random.randint(110, 220), random.randint(110, 220), random.randint(110, 220))
    
    
    COLOURS = {
        'bg': bg_randomizor(),
        #'screen_background': (146, 215, 224),
        # 'cell_green': (95, 129, 63),
        # 'grid_border': (79, 89, 31),
        # 'snake_green': (66, 102, 12),
        # 'apple_red': (187, 29, 29),
        # 'white': (255, 255, 255)
    }


    BG_SPEED = 1000
    BG_UE = pygame.USEREVENT

