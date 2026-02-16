import pygame


class RECT:


    ID = 0


    def __init__(self, x= 0, y= 0, width= 20, height= 20):
        
        self.id = RECT.ID
        RECT.ID += 1


        self.rect = pygame.Rect(x, y, width, height)