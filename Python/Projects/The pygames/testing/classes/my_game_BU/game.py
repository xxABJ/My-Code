import pygame
from abc import ABC, abstractmethod
from colours import Colours


width = 600; height = 800


class Game(ABC):


    def __init__(self):
        self.gravity = 10
        self.velocity = 10

            #self.player = Player()

    #def spawn_player(self):
    #    pass

    def controls(self):
        pass

    def player_movements(key):
        pass

    def get_player_position(self, id):
        #print(f"x: {self.player_body.x} y: {self.player_body.y}")
        return [self.player_body.x, self.player_body.y]

    @abstractmethod
    def draw(self, window):
        pass

