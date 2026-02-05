from settings import *


class Game:


    def __init__(self):

        # Pygame
        pygame.init()
        pygame.display.set_caption("Abj's Snake Game :p")

        
        self.screen = pygame.display.set_mode((Settings.CANVAS.get_width(),
        Settings.CANVAS.get_height() + Settings.SCORE_SURFACE_SIZE))
        self.canvas = Settings.CANVAS
        self.tick = pygame.time.set_timer(Settings.PLAYING_UE, Settings.PLAYING_SPEED)
        self.clock = pygame.time.Clock()
       

        # Game variables
        self._game_state = ""
        self._game_score = 0


        # Object assignments
        self.grid = Grid()
        self.snake = Snake()
        self.apple = Apple()


        # Collisions 
        self.collisions = Collisions(self)


        # Rendering
        self.rendering = Rendering(self)


        # Game logic
        self.gamelogic = GameLogic(self)


    def run(self):

        while True:
                
            for event in pygame.event.get():
            
                # Required exit logic
                self.exit(event)


                # Inputs
                self.gamelogic.get_inputs(event)
                

                # Gametick & Collisions
                self.gamelogic.get_logic(event)


            # Rendering & Framecap
            self.rendering.update()


    def restart(self):
        
        Game().run()


    def exit(self, event):
        
        if event.type == pygame.QUIT:
                
            pygame.quit()
            sys.exit()


    def get_game_state(self):

        return self._game_state


    def set_game_state(self, game_state):
        
        self._game_state = game_state


    def get_game_score(self):

        return self._game_score


    def increase_game_score(self):
        
        self._game_score += 1


Game().run()

