import pygame
from settings import *

class Text:
    def __init__(self, game, text, size=int, colour=tuple, x=int, y=int, orientation=None, dynamic_var=None, font=None):
        self.game = game
        self.text = text
        #self.textclass = Textfield(self)
        self.limit = WIDTH - 50

        if type(self.text) == list:
            self.indicator = True
            #print("list")
        else:
            self.indicator = False
            #print("string")
        input_text = self.text

        self.size = size
        self.colour = colour
        self.x = x
        self.y = y
        self.orientation = orientation
        self.dynamic_var = dynamic_var
        self.font = font if font != None else pygame.font.get_default_font()

        #self.game.canvas.fill(self.colour)
        #self.game.game.clock.tick(FPS**FPS)
        if not self.indicator:
            if len(self.text) < 40:
                # draw the text in the initialiser
                font = pygame.font.Font(self.font, self.size)
                text_surface = font.render(input_text, True, self.colour)
                self.text_rect = text_surface.get_rect()
                self.orientations()
            
            else:
                print("limittt")
                self.limit_text = self.text[:]
                #self.text = self.limit_text
                font = pygame.font.Font(self.font, self.size)
                text_surface = font.render(self.limit_text, True, self.colour)
                self.text_rect = text_surface.get_rect()
                self.orientations()

            #self.game.canvas.fill(self.colour)
            self.game.canvas.blit(text_surface, self.text_rect)
            #self.dynamic_var += text_rect.size[1]
            
        else:
            size = self.size
            rectx = 0
            recty = 0
            saved2 = size
            #print(input_text)
            
            for string in input_text:

                font = pygame.font.Font(self.font, self.size)
                text_surface = font.render(string, True, 'white')
                self.text_rect = text_surface.get_rect()
                self.text_rect.center = (self.x, self.y - size)

                self.game.canvas.blit(text_surface, self.text_rect)
                size -= saved2
                rectx += self.text_rect.size[0]
                recty += self.text_rect.size[1]
            
            #print(rectx, recty)
            #self.dynamic_var += recty

        #self.game.game.clock.tick(FPS)
        #print(dynamic_var)
    
    def orientations(self):
        if self.orientation == None:
            self.text_rect.topleft = (self.x, self.y)
        elif self.orientation == "ot_center":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.center = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_bottomleft":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.bottomleft = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_bottomright":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.bottomright = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_midbottom":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.midbottom = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_midleft":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.midleft = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_midright":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.midright = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_midtop":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.midtop = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_topleft":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.topleft = (self.x, self.y + self.dynamic_var)
        elif self.orientation == "ot_topright":
            self.dynamic_var += self.text_rect.size[1]
            self.text_rect.topright = (self.x, self.y + self.dynamic_var)

        else:
            if self.orientation == "top":
                self.text_rect.top = (self.x, self.y)
            elif self.orientation == "topright":
                self.text_rect.topright = (self.x, self.y)
            elif self.orientation == "topleft":
                self.text_rect.topleft = (self.x, self.y)
            elif self.orientation == "bottom":
                self.text_rect.bottom = (self.x, self.y)
            elif self.orientation == "bottomright":
                self.text_rect.bottomright = (self.x, self.y)
            elif self.orientation == "bottomleft":
                self.text_rect.bottomleft = (self.x, self.y)
            elif self.orientation == "midbottom":
                self.text_rect.midbottom = (self.x, self.y)
            elif self.orientation == "midleft":
                self.text_rect.midleft = (self.x, self.y)
            elif self.orientation == "midright":
                self.text_rect.midright = (self.x, self.y)
            elif self.orientation == "midtop":
                self.text_rect.midtop = (self.x, self.y)
            elif self.orientation == "center":
                self.text_rect.center = (self.x, self.y)
            elif self.orientation == "centerx":
                self.text_rect.centerx = (self.x, self.y)
            elif self.orientation == "centery":
                self.text_rect.centery = (self.x, self.y)
            elif self.orientation == "right":
                self.text_rect.right = (self.x, self.y)
            elif self.orientation == "left":
                self.text_rect.left = (self.x, self.y)
            elif self.orientation == "textfield":
                #self.dynamic_var += self.text_rect.size[1]
                self.text_rect.topleft = (self.x, self.y)

class Textfield(Text):
    def __init__(self):
        Text.__init__(self)
        self.keyboard_input = input(": ")
        self.newtext = self.keyboard_input
        #self.linefieldsurface = self.keyboard_input.get_rect()
        
        self.nl1occupied = False
    def next_line1(self):
        if self.maxchar == WIDTH - 50:
            self.nl1occupied = True
            
            spacing = 0
            nl1 = Text(self, self.newtext, self.size, self.colour, orientation=None, dynamic_var=spacing, font=None);
            nl1.dynamic_var += spacing; self.nl1saved = spacing; spacing += self.nl1saved
            if nl1.maxchar == self.limit:
                nl1_data = nl1.newtext 
                nl1.newtext = nl1_data
                self.nl1limit = True
                self.nl2occupied = True

        self.nl2occupied = False
    def next_line2(self):
        if self.nl2occupied:
            
            spacing += self.nl1saved
            nl2 = Text(self, self.newtext, self.size, self.colour, orientation=None, dynamic_var=spacing, font=None);
            nl2.dynamic_var += spacing; self.nl2saved = spacing; spacing += self.nl2saved
            if nl2.maxchar == self.limit:
                nl2_data = nl2.newtext 
                nl2.newtext = nl2_data
                self.nl2limit = True
                self.nl3occupied = True
        
        self.nl3occupied = False
    def next_line3(self):
        if self.nl3occupied:
            
            letters = [
                ".", "x", "O", "*", "'"
            ]

            spacing += self.nl2saved
            for letter in letters:
                nl3 = Text(self, letter, self.size, self.colour, orientation=self.orientation, dynamic_var=spacing, font=None);
                nl3.dynamic_var += spacing; self.nl3saved = spacing; spacing += self.nl3saved
                if nl3.maxchar == self.limit:
                    nl3_data = nl3.newtext 
                    nl3.newtext = nl3_data
                    self.nl3limit = True
                    self.nl4occupied = True
    
        self.next_line1()
        self.next_line2()
        self.next_line3()
