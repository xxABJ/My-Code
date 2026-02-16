import pygame


class Rendering:


    def __init__(self, main):
        
        self.main = main


        self.surfaces = {}




    def update(self):

        self.main.window.fill('lightgreen')


        if self.surfaces != None:

            for key, value in self.surfaces.items():

                self.main.window.blit(value, key)


        pygame.display.update()

    
    def add_surfaces(self, surface):

        self.surfaces[surface[0]] = surface[1]


    def remove_surfaces(self, surface):

        if surface in self.surfaces:

            self.surfaces.remove(surface)