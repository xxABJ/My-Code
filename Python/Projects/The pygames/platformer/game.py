import pygame, sys
from settings import *
from level import Level
from text import Text

pygame.USEREVENT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)); pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()

        self.index = 0
        self.bgc = BACKGROUNDCOLOURS[self.index]
        self.binds = [
            [self.enter(), "enter"], [self.lalt(), "alt"], [self.w(), "w"], [self.s(), "s"], [self.a(), "a"], [self.d(), "d"], [self.esc(), "esc"], [self.space(), "space"],
            [self.up(), "up"], [self.down(), "down"], [self.left(), "left"], [self.right(), "right"]
        ]

        self.player = True
        self.level = Level(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # specifing keys
                if event.type == pygame.KEYDOWN:
                    self.interact(event.key)

            # mouse
            self.mouse()

            # drawing the window
            self.screen.fill(BACKGROUNDCOLOURS[self.index])
            self.level.draw()

            # updating the window
            #pygame.display.update()
            self.clock.tick(FPS)

    def mouse(self):
        self.leftclick(); self.rightclick(); self.middleclick()

    def leftclick(self):
        if pygame.mouse.get_visible() and pygame.mouse.get_pressed()[0]:
            
            
            return print(f"left click: {pygame.mouse.get_pos()}\n")
        
    def rightclick(self):
        if pygame.mouse.get_visible() and pygame.mouse.get_pressed()[2]:


            return print(f"right click: {pygame.mouse.get_pos()}\n")

    def middleclick(self):
        if pygame.mouse.get_visible() and pygame.mouse.get_pressed()[1]:


            return print(f"middle button click: {pygame.mouse.get_pos()}\n")

    def interact(self, event_key=None):
        if self.player:
            for index, value in enumerate(self.binds):
                if event_key == value[0] and value[1] == "enter":
                    if self.index == len(BACKGROUNDCOLOURS) - 1:
                        self.index = 0
                        print(f"\nResetting self.index to 0")
                    if len(BACKGROUNDCOLOURS) - 1 > self.index:
                        self.index += 1
                        print(f"self.index: {self.index}")
                    print(f"\nself.binds index: {index}")
                    print(f"value: {value}")
                elif event_key == value[0]:
                    print(f"\nself.binds index: {index}")
                    print(f"value: {value}")
            return print(f"event_key: {event_key}")
        
    def text(self, text, size=int, colour=tuple, x=int, y=int, orientation=None, dynamic_var=None, font=None):
        return Text(self, text, size, colour, x, y, orientation, dynamic_var, font)

    def enter(self):
        return 13
    
    def lalt(self):
        return 1073742050

    def up(self):
        return 1073741906

    def down(self):
        return 1073741905

    def left(self):
        return 1073741904

    def right(self):
        return 1073741903
    
    def w(self):
        return 119
    
    def s(self):
        return 115
    
    def a(self):
        return 97
    
    def d(self):
        return 100
    
    def esc(self):
        return 27
    
    def space(self):
        return 32

if __name__ == "__main__":
    g = Game()
    g.run()