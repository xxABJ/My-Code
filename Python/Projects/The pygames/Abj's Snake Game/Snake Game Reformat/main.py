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
        self.grid = Objects.get_object(self, 'grid')
        self.apple = Objects.get_object(self, 'apple')
        self.snake = Objects.get_object(self, 'snake')


        # Collisions 
        self.collisions = Objects.get_object(self, 'collisions')


        # Rendering
        self.rendering = Objects.get_object(self, 'rendering')


        # Game logic
        self.gamelogic = Objects.get_object(self, 'gamelogic')


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


    def new_game(self):

        # RESET: Gametick
        self.tick = pygame.time.set_timer(Settings.PLAYING_UE, Settings.PLAYING_SPEED)
        
        
        # RESET: Game variables
        self._game_state = ""
        self._game_score = 0


        # RESET: Object assignments
        self.grid = Objects.get_object(self, 'grid')
        self.apple = Objects.get_object(self, 'apple')
        self.snake = Objects.get_object(self, 'snake')


        # RESET: Collisions 
        self.collisions = Objects.get_object(self, 'collisions')


        # RESET: Rendering
        self.rendering = Objects.get_object(self, 'rendering')


        # RESET: Game logic
        self.gamelogic = Objects.get_object(self, 'gamelogic')


        self.set_game_state('start_game')


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

