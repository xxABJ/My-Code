import pygame
from settings import *
from text import *

class Level:
    def __init__(self, game):
        self.game = game
        #self.time = time
        self.canvas = pygame.Surface((WIDTH, HEIGHT))
        
        self.input = input(": ")

        self.TL = (WIDTH - WIDTH, HEIGHT - HEIGHT)
        self.TR = (WIDTH, HEIGHT - HEIGHT)
        self.BL = (WIDTH - WIDTH, HEIGHT)
        self.BR = (WIDTH, HEIGHT)

    def ready_canvas(self):
        closeness = 0
        dynamic_size = 0
        orientations = ["ot_center", "ot_midleft", "ot_topleft", "ot_midtop" "ot_topright", "ot_midright", "ot_bottomright", "ot_midbottom", "ot_bottomleft", "ot_midleft", "ot_center"]
        for index, value in enumerate(orientations):
            idx = index

            self.canvas.fill('lightgrey')
            a_1 = Text(self, "||||||||||||", 19, "white", WIDTH/2, HEIGHT/2, value, dynamic_size);

            #print(self.i)
            #print(self.game.game.index)
            #print(idx); print(a_1.text_rect);

            idx += 1; a_2 = Text(self, "||||||||||||", 19, "white", WIDTH/2, HEIGHT/2, orientations[-idx], dynamic_size);

            #print(idx); print(a_1.text_rect)

            idx -= 1
            dynamic_size += a_1.dynamic_var + closeness;# dynamic_size += a_2.dynamic_var + closeness;

            b_1 = Text(self, "||||||||||||", 29, "green", WIDTH/2, HEIGHT/2, value, dynamic_size); idx += 1; b_2 = Text(self, "||||||||||||", 29, "green", WIDTH/2, HEIGHT/2, orientations[-idx], dynamic_size);
            idx -= 1
            dynamic_size = 0; dynamic_size += b_1.dynamic_var + closeness;# dynamic_size = 0; dynamic_size += b_2.dynamic_var + closeness;
            c_1 = Text(self, "||||||||||||", 39, "blue", WIDTH/2, HEIGHT/2, value, dynamic_size); idx += 1; c_2 = Text(self, "||||||||||||", 39, "blue", WIDTH/2, HEIGHT/2, orientations[-idx], dynamic_size);
            idx -= 1
            dynamic_size = 0; dynamic_size += c_1.dynamic_var + closeness;# dynamic_size = 0; dynamic_size += c_2.dynamic_var + closeness;
            d_1 = Text(self, "||||||||||||", 49, "red", WIDTH/2, HEIGHT/2, value, dynamic_size); idx += 1; d_2 = Text(self, "||||||||||||", 49, "red", WIDTH/2, HEIGHT/2, orientations[-idx], dynamic_size);
            idx -= 1
            dynamic_size = 0; dynamic_size += d_1.dynamic_var + closeness;# dynamic_size = 0; dynamic_size += d_2.dynamic_var + closeness;
            e_1 = Text(self, "||||||||||||", 59, "yellow", WIDTH/2, HEIGHT/2, value, dynamic_size); idx += 1; e_2 = Text(self, "||||||||||||", 59, "yellow", WIDTH/2, HEIGHT/2, orientations[-idx], dynamic_size);
            idx -= 1
            dynamic_size = 0; dynamic_size += e_1.dynamic_var + closeness;# dynamic_size = 0; dynamic_size += e_2.dynamic_var + closeness;
    
            #print(f"dynamic_size: {dynamic_size}")
            dynamic_size = 0

    
            if idx % 7:
                Text(self, ["GAME TITLE"], 40, "black", WIDTH/2, HEIGHT/2 - 50, "center")

            if len(self.input) <= 40:
                Text(self, self.input[:40], 30, "brown", 50, 50, "textfield")
                Text(self, self.input[40:], 30, "brown", 50, 50*2, "textfield")
            elif len(self.input) <= 80:
                Text(self, self.input[:40], 30, "brown", 50, 50, "textfield")
                Text(self, self.input[40:80], 30, "brown", 50, 50*2, "textfield")
                Text(self, self.input[80:], 30, "brown", 50, 50*3, "textfield")
            elif len(self.input) <= 120:
                Text(self, self.input[:40], 30, "brown", 50, 50, "textfield")
                Text(self, self.input[40:80], 30, "brown", 50, 50*2, "textfield")
                Text(self, self.input[80:120], 30, "brown", 50, 50*3, "textfield")
                Text(self, self.input[120:], 30, "brown", 50, 50*4, "textfield")
            elif len(self.input) <= 160:
                Text(self, self.input[:40], 30, "brown", 50, 50, "textfield")
                Text(self, self.input[40:80], 30, "brown", 50, 50*2, "textfield")
                Text(self, self.input[80:120], 30, "brown", 50, 50*3, "textfield")
                Text(self, self.input[120:160], 30, "brown", 50, 50*4, "textfield")
                Text(self, self.input[160:200], 30, "brown", 50, 50*5, "textfield")

            self.game.screen.blit(self.canvas, self.TL)
            #pygame.time.wait(int(FPS/2)*3)
            pygame.display.update()
            #get_time = self.game.clock.get_time(); print(f"get_time() : {self.game.clock.get_time()}")
            #get_fps = self.game.clock.get_fps(); print(f"get_fps() : {self.game.clock.get_fps()}")

        self.game.screen.blit(self.canvas, self.TL)
        pygame.display.update()

    def draw(self):
        self.ready_canvas()
        self.game.screen.blit(self.canvas, self.TL)
        pygame.display.update()