import pygame, sys
from events import *
from game import *
from background import Background
from ground import Ground
from player import Player
#from colours import Colours


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Testing :p")

clock = pygame.time.Clock()


#classes = [
#    Background(3),
#    Ground(),
#    Player(1, 10, 20)
#]

bg = Background(1)
g = Ground()
p1 = Player(1, 10, 20)

while True:

    py_events([p1])


    #draw

    bg.draw(screen)
    g.draw(screen)
    p1.draw(screen)
    #p1.get_player_position(1)

    #for c in classes:
    #    c.draw(screen)
    #b.draw(screen)
    #g.draw(screen)

    pygame.display.update()

    clock.tick(60)