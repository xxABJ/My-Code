import pygame, sys, random


class Settings:

    WIDTH = 1000
    HEIGHT = 600
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


    COLOURS = {
        'green1': (55, 99, 36),
        'green2':(46, 91, 58),
        'ball': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        'bg': (8, 12, 14)
    }


class Window:

    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Abj's Ping Pong!")
        
        
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        self.clock = pygame.time.Clock()


    def render(self, objects):

        self.screen.fill(Settings.COLOURS['bg'])


        for object in objects:
            
            if object.position == 'left':

                pygame.draw.rect(self.screen, Settings.COLOURS['green1'], object.pong_rect)
            

            elif object.position == 'right':

                pygame.draw.rect(self.screen, Settings.COLOURS['green2'], object.pong_rect)


        pygame.display.update()


from pong import *