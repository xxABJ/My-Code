import pygame


class MouseInput:


    def __init__(self, main):

        self.main = main
        #self.mouse_pos = self.set_mouse_pos()
        

    def get_mouse_pos(self):

        return pygame.mouse.get_pos()


    def set_mouse_pos(self):

        return pygame.mouse.get_pos()