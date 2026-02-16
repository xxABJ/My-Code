from settings import Settings, pygame


class Pong:


    def __init__(self, game, position):

        self.game = game
        self.position = position


        if self.position == 'left':
            x, y = 50, 200
        elif self.position == 'right':
            x, y = 900, 200


        self.pong_rect = pygame.Rect(x, y, 30, 200)
        self.pong_mover = (False, False)


    def valid_move(self):

        if 0 <= self.pong_rect.y and (self.pong_rect.y + self.pong_rect.h) <= Settings.HEIGHT:
                
                return True
        
        
        return False