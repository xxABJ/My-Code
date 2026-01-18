from game import *


class Ground(Game):


    def __init__(self):
        super().__init__()
        self.ground = pygame.rect.Rect(0, height*0.8, width, 10)


    def draw(self, window):
        #Background.draw(self, window)
        pygame.draw.rect(window, "grey", self.ground)
