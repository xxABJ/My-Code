from handler import *
from mouseinput import *
from rects import *
from create import *
from rendering import *


import pygame, sys


class Window:


    def __init__(self, size = (600, 600), title = "test"):
        
        pygame.init()
        pygame.display.set_caption(title)
        self.window = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()


        self.handler = Handler(self)
        self.mouse = MouseInput(self)


        self.createmenu = None


        self.rendering = Rendering(self)


        #self.rect_queue = []


    def run(self):
        
        while True:

            for event in pygame.event.get():

                self.exit(event)

                self.handler.get_inputs(event)


            self.rendering.update()


            self.clock.tick(60)


    def exit(self, event):
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


    def creat_menu(self):

        self.createmenu = CreateMenu()
        return self.createmenu.menu_surface()


Window().run()