import pygame, random


#from menu


from gamelogic import GameLogic


#from ingame


from rendering import Rendering


class Objects:

    @staticmethod
    def get_object(game, text):


        if text == "gamelogic":

            return GameLogic(game)


        elif text == "rendering":

            return Rendering(game)


#class GameLogic_Objects:
        #def get_gamelogic_object(game, text):