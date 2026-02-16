from settings import *


class Game(Window):


    def __init__(self):
        
        super().__init__()


        self.left = Pong(self, 'left')
        self.right = Pong(self, 'right')

        self.move_vel = 20

        self.move_left_player = False
        self.move_right_player = False

        self.keys = None


    def run(self):

        while True:

            for event in pygame.event.get():

                self.exit(event)

                self.get_inputs(event)

            if self.keys:
                if self.keys[pygame.K_UP]:
                    #print('up')
                    self.right_movement('up')

                elif self.keys[pygame.K_DOWN]:
                    #print('down')
                    self.right_movement('down')

            self.left_movement()


            self.render([self.left, self.right])
            self.clock.tick(60)


    def get_inputs(self, event):

        def player_left_press():

            if event.key == pygame.K_w:
                
                self.left.pong_mover = (True, False)
                self.move_left_player = True


            if event.key == pygame.K_s:

                self.left.pong_mover = (False, True)
                self.move_left_player = True


        def player_left_release():

            self.left.pong_mover = (False, False)
            self.move_left_player = False


        def player_right_press():

            if event.key == pygame.K_UP:

                self.right.pong_mover = (True, False)
                self.move_right_player = True
                self.keys = pygame.key.get_pressed()


            if event.key == pygame.K_DOWN:

                self.right.pong_mover = (False, True)
                self.move_right_player = True
                self.keys = pygame.key.get_pressed()


        def player_right_release():

            self.right.pong_mover = (False, False)
            self.move_right_player = False
            self.keys = None


        if event.type == pygame.KEYDOWN:

            player_left_press()
            player_right_press()

        
        if event.type == pygame.KEYUP:

            player_left_release()
            player_right_release()


    def left_movement(self):

        up = (True, False)
        down = (False, True)


        if self.move_left_player:
            
            if self.left.pong_mover == up:
                if self.left.pong_rect.y != 0:

                    if self.left.valid_move():
                        self.move_vel = 10
                        self.left.pong_rect.y -= self.move_vel


                    else:
                        self.move_vel = 0
                        self.left.pong_rect.y = 0


            if self.left.pong_mover == down:
                if self.left.pong_rect.y != (Settings.HEIGHT - self.left.pong_rect.h):

                    if self.left.valid_move():
                        self.move_vel = 10
                        self.left.pong_rect.y += self.move_vel
                    

                    else:
                        self.move_vel = 0
                        self.left.pong_rect.y = (Settings.HEIGHT - self.left.pong_rect.h)

        else:
            pass


    def right_movement(self, direction):

        up = (True, False)
        down = (False, True)


        if self.move_right_player and direction == 'up':

            if self.right.pong_mover == up:

                if self.right.pong_rect.y != 0:

                    if self.right.valid_move():

                        self.move_vel = 10
                        self.right.pong_rect.y -= self.move_vel


                    else:

                        self.move_vel = 0
                        self.right.pong_rect.y = 0


        else:

            if self.right.pong_mover == down:

                if self.right.pong_rect.y != (Settings.HEIGHT - self.right.pong_rect.h):

                    if self.right.valid_move():

                        self.move_vel = 10
                        self.right.pong_rect.y += self.move_vel


                    else:

                        self.move_vel = 0
                        self.right.pong_rect.y = (Settings.HEIGHT - self.right.pong_rect.h)

                        


    def exit(self, event):
        
        if event.type == pygame.QUIT:
                
            pygame.quit()
            sys.exit()


Game().run()