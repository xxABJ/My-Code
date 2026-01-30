import pygame, sys, random

class Game:


    CELL_SIZE = 40; CELL_ROW = 15
    WIDTH = CELL_SIZE*CELL_ROW; HEIGHT = CELL_SIZE*CELL_ROW
    SCORE_SURFACE_SIZE = CELL_SIZE
    SQUARE_BORDER_WIDTH = 2
    COLOURS = {
        'green': (30, 90, 30),
        'mid_green': (110, 110, 50),
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


        BODY_PART_INSERT_QUEUE = []

        
        def __init__(self):

            self.apple_pos = self.spawn_apple()


            self.apple_rect = pygame.Rect((self.apple_pos.x * Game.CELL_SIZE), ((self.apple_pos.y * Game.CELL_SIZE) - Game.SCORE_SURFACE_SIZE),
                                          Game.CELL_SIZE - 0, Game.CELL_SIZE - 0)
            

        def spawn_apple(self):

            apple_pos = pygame.Vector2(random.randint(1, Game.CELL_ROW - 1),
                                       random.randint(1, Game.CELL_ROW - 1))
            

            return apple_pos


        def draw(self, canvas):

            pygame.draw.rect(canvas, Game.COLOURS['red'], self.apple_rect, 0, 40)


    class Snake:


        def __init__(self):

            self.moving_direction = "up"
            

            self.snake_body_pos = [     # Starting size: 3
                pygame.Vector2(10, 12), 
                pygame.Vector2(10, 11),
                pygame.Vector2(10, 10)  # Head
            ]


        def draw(self, canvas):
            
            self.snake_rects = [

                pygame.Rect((body.x * Game.CELL_SIZE) + 2, ((body.y * Game.CELL_SIZE) - Game.SCORE_SURFACE_SIZE) + 2, Game.CELL_SIZE - 4, Game.CELL_SIZE - 4)
                for body in self.snake_body_pos

                ]


            for rect in self.snake_rects:

                pygame.draw.rect(canvas, Game.COLOURS['green'], rect, 0, 5)


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
        RECT_PLACEMENT_ADJUSTER = 2
        APPLE_POSITIONS = []


        def __init__(self, apple_obj, snake_obj, screen):

            self.apple = apple_obj
            self.snake = snake_obj
            
            
            self.screen = screen
            self.screen_width = self.screen.get_width()
            self.screen_height = self.screen.get_height()


            self.game_logic_endgame_reason = ""
            self.stop = False


            self.score_font = pygame.font.Font(None, (Game.SCORE_SURFACE_SIZE - (Game.SCORE_SURFACE_SIZE//10)))
            self.end_font1 = pygame.font.Font(None, 80)
            self.end_font2 = pygame.font.Font(None, 50)
            self.end_reason_font = pygame.font.Font(None, 35)


        def draw(self, canvas):

            self.draw_grid(canvas)
            

            score_surface = self.score_font.render(str(Game.GameLogic.SCORE), 
                                                   True, Game.COLOURS['white'])
            

            self.screen.blit(score_surface, (Game.WIDTH // 2, (Game.SCORE_SURFACE_SIZE // 2) // 2))


        def draw_grid(self, canvas):

            cell_row = Game.CELL_ROW; cell_size = Game.CELL_SIZE
            x_adjuster = 0; y_adjuster = 0; rect_placement_adjuster = Game.SQUARE_BORDER_WIDTH
            

            for row in range(cell_row):

                for col in range(cell_row):

                    single_grid_rect = pygame.Rect(((rect_placement_adjuster // 2) + x_adjuster), ((rect_placement_adjuster // 2) + y_adjuster),
                                                   (cell_size) - (rect_placement_adjuster),
                                                   (cell_size) - (rect_placement_adjuster))
                    

                    pygame.draw.rect(canvas, Game.COLOURS['mid_green'], single_grid_rect)
                    

                    x_adjuster += cell_size
                

                x_adjuster = 0
                y_adjuster += cell_size


        def wall_collision(self):

            snake_head_pos = (self.snake.snake_body_pos[-1].x * Game.CELL_SIZE, self.snake.snake_body_pos[-1].y * Game.CELL_SIZE)


            if (snake_head_pos[0] < 0) or (snake_head_pos[0] == self.screen_width):
                return True
            

            elif (snake_head_pos[1] < Game.SCORE_SURFACE_SIZE) or (snake_head_pos[1] == self.screen_height):
                return True


            return False
            

        def self_collision(self):

            snake_head_pos = (self.snake.snake_body_pos[-1].x, self.snake.snake_body_pos[-1].y)


            body_parts = []
            for body_part in self.snake.snake_body_pos:
                body_part = (body_part.x, body_part.y)
                body_parts.append(body_part)


            if body_parts.count(snake_head_pos) != 1:
                return True
            

            return False
            

        def eat_collision(self):
            
            apple_pos = self.apple.apple_pos
            snake_head_pos = (self.snake.snake_body_pos[-1].x, self.snake.snake_body_pos[-1].y)


            if apple_pos == snake_head_pos:
                return True
            

            return False
            

        def eat_apple(self):

            def eat_queue_inserter(lastbody, direction):

                match direction:
                    case 'left': 
                        insert_body_part = pygame.Vector2(lastbody.x, lastbody.y)

                    case 'right':
                        insert_body_part = pygame.Vector2(lastbody.x, lastbody.y)

                    case 'up':
                        insert_body_part = pygame.Vector2(lastbody.x, lastbody.y)

                    case 'down':
                        insert_body_part = pygame.Vector2(lastbody.x, lastbody.y)
                    
                
                Game.GameLogic.APPLE_POSITIONS.append(self.apple.apple_pos)
                Game.Apple.BODY_PART_INSERT_QUEUE.append(insert_body_part)


            whole_body = self.snake.snake_body_pos[:]
            last_body_part = whole_body[-1]


            eat_queue_inserter(last_body_part, self.snake.moving_direction)
            Game.GameLogic.SCORE += 1


        def queue_check(self):

            def snake_body_update(wholebody, lastbody, bodypart_insert_queue, apple_positions):

                newbody = bodypart_queue[0]


                if lastbody == apple_positions[0]:
                    
                    del Game.GameLogic.APPLE_POSITIONS[0]
                    del Game.Apple.BODY_PART_INSERT_QUEUE[0]


                    wholebody.insert(0, newbody)
                    self.snake.snake_body_pos = wholebody
                    print(f"\nnew bodypart added\n  in the game! ({Game.GameLogic.SCORE})")


            whole_body = self.snake.snake_body_pos[:]
            last_body_part = whole_body[0]


            previous_apple_positions = Game.GameLogic.APPLE_POSITIONS
            body_part_insert_queue = Game.Apple.BODY_PART_INSERT_QUEUE


            if len(body_part_insert_queue) > 0:

                snake_body_update(whole_body, last_body_part, body_part_insert_queue, previous_apple_positions)
            

        def end_game(self, canvas, reason = ""):

            self.screen.fill('darkblue')
            canvas.fill('darkblue')


            end_text1 = "GAME OVER"
            end_text2 = f"Your score is: {str(Game.GameLogic.SCORE)}"
            

            end_surface1 = self.end_font1.render(end_text1, True, Game.COLOURS['white'])
            end_surface2 = self.end_font2.render(end_text2, True, Game.COLOURS['white'])


            canvas.blit(end_surface1, ((self.screen.get_width() // 2) - (end_surface1.get_width() // 2),
                                       (self.screen.get_height() // 2) - ((end_surface1.get_height() + Game.SCORE_SURFACE_SIZE) // 2) - (200)))
            
            canvas.blit(end_surface2, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2),
                                       (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2)))
            

            match reason:
                case "wall":
                    end_reason = "You hit the wall :p"

                    end_reason_surface = self.end_reason_font.render(end_reason, True, Game.COLOURS['white'])


                    canvas.blit(end_reason_surface, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25), 
                                                     (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2) + (175)))

                case "self":
                    end_reason = "You hit yourself :p"

                    end_reason_surface = self.end_reason_font.render(end_reason, True, Game.COLOURS['white'])


                    canvas.blit(end_reason_surface, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25), 
                                                     (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2) + (175)))
            
            
            self.screen.blit(canvas, (0, Game.SCORE_SURFACE_SIZE))
            

            pygame.display.update()


    def __init__(self):

        self.screen = pygame.display.set_mode((Game.CANVAS.get_width(), Game.CANVAS.get_height() + Game.SCORE_SURFACE_SIZE))
        self.canvas = Game.CANVAS
        

        self.apple = Game.Apple()
        self.snake = Game.Snake()
        

        self.game_logic = Game.GameLogic(self.apple, self.snake, self.screen)


    def run(self):

        while True:

            while not self.game_logic.stop:

                # Game engine
                self.game_logic = Game.GameLogic(self.apple, self.snake, self.screen)


                # PyGame event handler
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


                    # Game physics
                    if event.type == Game.PLAYING:

                        self.snake.snake_movements("default")


                    # Key inputs
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
                self.game_logic.queue_check()                


                if self.game_logic.eat_collision():

                    self.game_logic.eat_apple()
                    self.apple = Game.Apple()


                elif self.game_logic.wall_collision():
                    
                    print("\nwall collision!")
                    self.game_logic.game_logic_endgame_reason = "wall"
                    self.game_logic.stop = True
                    break


                elif self.game_logic.self_collision():
                    
                    print("\nself collision!")
                    self.game_logic.game_logic_endgame_reason = "self"
                    self.game_logic.stop = True
                    break

    
                # Game rendering update
                self.screen.fill('darkblue')
                self.canvas.fill(Game.COLOURS['dark_green'])


                self.game_logic.draw(self.canvas)
                self.snake.draw(self.canvas)
                self.apple.draw(self.canvas)


                self.screen.blit(self.canvas, (0, Game.SCORE_SURFACE_SIZE))
                
                
                pygame.display.update()


                # Game Framerate cap
                Game.clock.tick(60)


            # Game-Over screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            # Game rendering update & Framerate cap
            self.game_logic.end_game(self.canvas, self.game_logic.game_logic_endgame_reason)
            Game.clock.tick(60)


Game().run()