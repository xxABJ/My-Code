import pygame, sys
from scripts.utility import load_image
from scripts.entity import PhysicsEntity

class Game:
    
    
    def __init__(self):
        
        #PyGame base
        pygame.init()
        pygame.display.set_caption("Game testing")
        self.screen = pygame.display.set_mode((700, 700))
        self.clock = pygame.time.Clock()


        self.player = PhysicsEntity(self, 'player', (140, 210), (16, 16))


        self.assets = {
            'player' : load_image('Main Characters/player.png')
        }

    
    def run(self):
        while True:


            self.screen.fill((82, 183, 220))

            #self.player.update(self)

            self.player.render(self)
            
            #self.img_pos[0] += (self.horizontal_movement[1] - self.horizontal_movement[0]) * 3
            #self.img_pos[1] += (self.vertical_movement[1] - self.vertical_movement[0]) * 3
            #
            #self.screen.blit(self.img, self.img_pos)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                

                # Remember this event will execute once, even if you keep holding!
                if event.type == pygame.KEYDOWN:                        # |
                                                                        # |
                    if event.key == pygame.K_UP:                        # |
                        #self.player.vertical_movement[0] = True        # |
                        self.player.update(self, v = [True, False])     # |
                        #pass
                    if event.key == pygame.K_DOWN:                      # |
                        #self.player.vertical_movement[1] = True        # |
                        self.player.update(self, v = [False, True])     # |
                        #pass
                                                                        # |
                    if event.key == pygame.K_RIGHT:                     # |
                        #self.horizontal_movement[1] = True             # |
                        self.player.update(self, h = [False, True])     # |
                    if event.key == pygame.K_LEFT:                      # |
                        #self.horizontal_movement[0] = True             # |
                        self.player.update(self, h = [True, False])     # |
                                                                        # |
                                                                        # V
                # So you use this, with a boolean indicator system to simulate continuity.
                if event.type == pygame.KEYUP:
                
                    if event.key == pygame.K_UP:
                        #self.vertical_movement[0] = False
                        self.player.update(self, v = [False, False])
                        #pass
                    if event.key == pygame.K_DOWN:
                        #self.vertical_movement[1] = False
                        self.player.update(self, v = [False, False])
                        #pass
                        
                    if event.key == pygame.K_RIGHT:
                        #self.horizontal_movement[1] = False
                        self.player.update(self, h = [False, False])
                    if event.key == pygame.K_LEFT:
                        #self.horizontal_movement[0] = False
                        self.player.update(self, h = [False, False])

                
            pygame.display.update()
            self.clock.tick(60)
        

Game().run()