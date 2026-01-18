from game import *


class Background(Game):
    
    
    def __init__(self, tile_amount = 5):
        super().__init__()
        self.tile_amount = tile_amount
        self.background = self.get_background()
       

    def get_background(self):
        colour_list = Colours.get_colours(self.tile_amount)
        background_rect_list = []
        background_rect_size = height//self.tile_amount
        y_adjust = 0
        for tiles in range(self.tile_amount):
            tile = pygame.rect.Rect(0, 0 + y_adjust, width, background_rect_size)
            background_rect_list.append(tile)
            y_adjust += background_rect_size
        return [background_rect_list, colour_list]


    def draw(self, window):
        for rect in self.background[0]:
            pygame.draw.rect(window, self.background[1][self.background[0].index(rect)], rect)
