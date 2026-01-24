import pygame, sys, random

class Game:


    CELL_SIZE = 40; CELL_ROW = 15
    bGRID = [[0 for col in range(15)] for row in range(15)]
    GRID = (CELL_ROW, CELL_ROW)
    WIDTH = CELL_SIZE*CELL_ROW; HEIGHT = CELL_SIZE*CELL_ROW
    SCORE_SURFACE_SIZE = CELL_SIZE
    COLOURS = {
        'green': (74, 182, 55),
        'dark_green': (34, 99, 31),
        'red': (226, 47, 47),
        'white': (255, 255, 255)
    }
    MAX_GAME_SPEED = 10
    SNAKE_SPEED = 4
    PLAYING_SPEED =  int((MAX_GAME_SPEED - SNAKE_SPEED)*60)


    pygame.init()
    pygame.display.set_caption("Abj's Snake Game :p")
    CANVAS = pygame.Surface((WIDTH, HEIGHT))
    PLAYING = pygame.USEREVENT; pygame.time.set_timer(PLAYING, PLAYING_SPEED)
    clock = pygame.time.Clock()


    class Apple:

        
        def __init__(self):
            self.apple_pos = self.spawn_apple()

            self.apple_rect = pygame.Rect((self.apple_pos.x * Game.CELL_SIZE), ((self.apple_pos.y * Game.CELL_SIZE) - Game.SCORE_SURFACE_SIZE),
                                          Game.CELL_SIZE - 5, Game.CELL_SIZE - 5)
            

        def spawn_apple(self):
            apple_pos = pygame.Vector2(random.randint(0, Game.CELL_ROW - 1),
                                       random.randint(0, Game.CELL_ROW - 1))
            return apple_pos


        def draw(self, window):
            pygame.draw.rect(window, Game.COLOURS['red'], self.apple_rect, 0, 8)


    class Snake:


        def __init__(self):
            self.moving_direction = "up"
            
            self.snake_body_pos = [     # Starting size: 3
                pygame.Vector2(10, 12), 
                pygame.Vector2(10, 11),
                pygame.Vector2(10, 10)  # Head
            ]


        def draw(self, window):
            self.snake_rects = [

                pygame.Rect((body.x * Game.CELL_SIZE), ((body.y * Game.CELL_SIZE) - Game.SCORE_SURFACE_SIZE), Game.CELL_SIZE - 0, Game.CELL_SIZE - 0)
                for body in self.snake_body_pos

                ]


            for rect in self.snake_rects:
                pygame.draw.rect(window, Game.COLOURS['dark_green'], rect, 0, 7)


        def snake_movements(self, direction = "default"):
            
            
            def move_left():
                if not self.moving_direction == 'right':
                    whole_body = self.snake_body_pos[:]

                    head_pos = whole_body[-1]; new_head_pos = pygame.Vector2(head_pos.x - 1, head_pos.y)
                    whole_body.append(new_head_pos)

                    self.snake_body_pos = whole_body[1:]
                    self.moving_direction = "left"


            def move_right():
                if not self.moving_direction == 'left':
                    whole_body = self.snake_body_pos[:]

                    head_pos = whole_body[-1]; new_head_pos = pygame.Vector2(head_pos.x + 1, head_pos.y)
                    whole_body.append(new_head_pos)

                    self.snake_body_pos = whole_body[1:]
                    self.moving_direction = "right"


            def move_up():
                if not self.moving_direction == 'down':
                    whole_body = self.snake_body_pos[:]

                    head_pos = whole_body[-1]; new_head_pos = pygame.Vector2(head_pos.x, head_pos.y - 1)
                    whole_body.append(new_head_pos)

                    self.snake_body_pos = whole_body[1:]
                    self.moving_direction = "up"


            def move_down():
                if not self.moving_direction == 'up':
                    whole_body = self.snake_body_pos[:]

                    head_pos = whole_body[-1]; new_head_pos = pygame.Vector2(head_pos.x, head_pos.y + 1)
                    whole_body.append(new_head_pos)

                    self.snake_body_pos = whole_body[1:]
                    self.moving_direction = "down"


            def default_moving():
                whole_body = self.snake_body_pos[:]

                head_pos = whole_body[-1]
                match self.moving_direction:
                    case 'left':
                        new_head_pos = pygame.Vector2(head_pos.x - 1, head_pos.y)
                    case 'right':
                        new_head_pos = pygame.Vector2(head_pos.x + 1, head_pos.y)
                    case 'up':
                        new_head_pos = pygame.Vector2(head_pos.x, head_pos.y - 1)
                    case 'down':
                        new_head_pos = pygame.Vector2(head_pos.x, head_pos.y + 1)
                whole_body.append(new_head_pos)

                self.snake_body_pos = whole_body[1:]

            
            match direction:
                case 'left':
                    if not self.moving_direction == 'left':
                        move_left()

                case 'right':
                    if not self.moving_direction == 'right':
                        move_right()

                case 'up':
                    if not self.moving_direction == 'up':
                        move_up()

                case 'down':
                    if not self.moving_direction == 'down':
                        move_down()
                        
                case 'default':
                    default_moving()


    class GameLogic:


        SCORE = 0


        def __init__(self, apple_obj, snake_obj):
            self.apple_pos = apple_obj.apple_pos
            self.snake_body_pos = snake_obj.snake_body_pos
            
            self.font = pygame.font.Font(None, (Game.SCORE_SURFACE_SIZE - (Game.SCORE_SURFACE_SIZE//10)))
            

        def draw(self, window):
            score_text = self.font.render(str(Game.GameLogic.SCORE),
                                       True, Game.COLOURS['white'])
            
            window.blit(score_text, (Game.WIDTH // 2, (Game.SCORE_SURFACE_SIZE // 2) // 2))


        def wall_collision(self):
            snake_head_pos = (self.snake_body_pos[-1].x, self.snake_body_pos[-1].y)

            if snake_head_pos[0] < 0 or snake_head_pos[0] > Game.WIDTH:
                return True
            elif snake_head_pos[1] < 0 or snake_head_pos[1] > Game.HEIGHT:
                return True

            return False
            

        def eat_collision(self):
            apple_pos = self.apple_pos
            snake_head_pos = (self.snake_body_pos[-1].x, self.snake_body_pos[-1].y)

            if apple_pos == snake_head_pos:
                return True
            
            return False
            

        def eat_apple(self, snake_obj):
            whole_body = self.snake_body_pos[:]
            
            new_body = whole_body[-1]
            match snake_obj.moving_direction:
                case 'left':
                    new_body = pygame.Vector2(new_body.x - 1, new_body.y)
                case 'right':
                    new_body = pygame.Vector2(new_body.x + 1, new_body.y)
                case 'up':
                    new_body = pygame.Vector2(new_body.x, new_body.y - 1)
                case 'down':
                    new_body = pygame.Vector2(new_body.x, new_body.y + 1)
            whole_body.append(new_body)

            snake_obj.snake_body_pos = whole_body
            Game.GameLogic.SCORE += 1
            

        # Don't forget Game.GameLogic.SCORE_SURFACE_SIZE
        def hit_wall(self):
            pass



    def __init__(self):
        #for row in Game.GRID:
        #    for column in Game.GRID:
        #        pass
        #    print(row, end='\n')
        self.screen = pygame.display.set_mode(Game.CANVAS.get_size())
        self.canvas = Game.CANVAS
        
        self.apple = Game.Apple()
        self.snake = Game.Snake()


    def run(self):
        while True:
            game_logic = Game.GameLogic(self.apple, self.snake)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                # Game physics & Key inputs 
                if event.type == Game.PLAYING:
                    self.snake.snake_movements("default")
                
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LEFT:
                        self.snake.snake_movements('left')
                    
                    if event.key == pygame.K_RIGHT:
                        self.snake.snake_movements('right')
                    
                    if event.key == pygame.K_UP:
                        self.snake.snake_movements('up')
                    
                    if event.key == pygame.K_DOWN:
                        self.snake.snake_movements('down')


            # Game mehcanics  
            if game_logic.eat_collision():
                game_logic.eat_apple(self.snake)
                self.apple = Game.Apple()

            if game_logic.hit_wall():# or self.game_logic.hit_self():
                pass


            # Game rendering
            self.screen.fill(Game.COLOURS['dark_green'])
            self.screen.blit(self.canvas, (0, Game.SCORE_SURFACE_SIZE))
            self.canvas.fill(Game.COLOURS['green'])
            self.apple.draw(self.canvas)
            self.snake.draw(self.canvas)
            game_logic.draw(self.screen)

            pygame.display.update()
            Game.clock.tick(60)


Game().run()