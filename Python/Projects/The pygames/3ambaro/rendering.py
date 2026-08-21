from settings import *


class Rendering:

    def __init__(self, game):

        self.game = game


    def update(self):

        if self.game.timer == 80:

            self.game.canvas.fill(Settings.bg_randomizor())
            self.game.screen.blit(self.game.canvas, (0, 0))

            
        pygame.display.update()
        self.game.clock.tick(60)

        # self.game.canvas.fill(Settings.COLOURS['bg'])
        # self.game.screen.blit(self.game.canvas, (0, 0))

        # pygame.display.update()
        # self.game.clock.tick(60)