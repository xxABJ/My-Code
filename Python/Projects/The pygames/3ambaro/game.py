from settings import *

# ^^ this is for current viewing file, and capabilities.
    # real dependency connections are important in final main RUNNING file.
        # but still imports are required for editorial reasons, can be removed when project is complete but will make all files have errors.


class Game:

    def __init__(self):

        # Pygame
        pygame.init()
        pygame.display.set_caption("3ambaro!")


        self.screen = pygame.display.set_mode(Settings.CANVAS.get_size())
        self.canvas = Settings.CANVAS
        self.clock = pygame.time.Clock()

        self.timer = 0


        # Game Logic
        self.gamelogic = Objects.get_object(self, "gamelogic")

        # Rendering
        self.rendering = Objects.get_object(self, "rendering")


    def run(self):


        self.canvas.fill(Settings.bg_randomizor())
        self.screen.blit(self.canvas, (0, 0))


        while True:

            for event in pygame.event.get():

                # Exit
                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()


                # Game Logic
                self.gamelogic.get_logic(event)


            # Rendering
            self.timer += 1
            print(self.timer)
            self.rendering.update()
            if self.timer == 80:
                self.timer = 0


g = Game()
g.run()