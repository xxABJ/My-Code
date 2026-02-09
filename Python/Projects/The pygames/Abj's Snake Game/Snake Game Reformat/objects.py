from grid import *
from snake import *
from apple import *
from collisions import *
from rendering import *
from gamelogic import *


class Objects:

    
    @staticmethod
    def get_object(game, text):

        if text == 'grid':
            return Grid()
        

        elif text == 'snake':
            return Snake()
        

        elif text == 'apple':
            return Apple()
        

        elif text == 'collisions':
            return Collisions(game)
        

        elif text == 'rendering':
            return Rendering(game)
        

        elif text == 'gamelogic':
            return GameLogic(game)
        
        
        else:
            raise ValueError(f"Unknown object type: {text}")