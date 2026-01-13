from ground import *

class Player(Ground):
    def __init__(self, id, w, h):
        super().__init__()
        self.id = id
        self.w = w
        self.h = h
        self.player_body = self.get_player_body()
        self.player_body_colour = Colours.get_colour()
    
    def get_player_body(self):
        player_rect = pygame.Rect(width//2, height//2, self.w, self.h)
        return player_rect
    
    def draw(self, window): #blitting surface
        #player_surface = pygame.Surface((self.body.w, self.body.h), 0, Colours.get_colour())
        #window.blit(player_surface, (width//2, height//2))

        pygame.draw.rect(window, self.player_body_colour, self.player_body)