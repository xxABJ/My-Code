from game_settings import *
from inputs import INPUTS

import sys

class Game:
    def __init__(self):
        pygame.init()

    def run(self):
        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #if event.type == pygame.KEYDOWN:
                #    print(event, event.key)
                #    print((event.__dict__))
                
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP: 
                    INPUTS(event) # this class will not change unless a new buffer is trying to comunicate

Game().run()