import pygame, sys, random

class Game:


    CELL_SIZE = 40; CELL_ROW = 15
    WIDTH = CELL_SIZE*CELL_ROW; HEIGHT = CELL_SIZE*CELL_ROW
    SCORE_SURFACE_SIZE = CELL_SIZE
    SQUARE_BORDER_WIDTH = 2
    COLOURS = {
        'cell_green': (95, 129, 63),
        'grid_border': (79, 89, 31),
        'snake_green': (66, 102, 12),
        'apple_red': (187, 29, 29),
        'white': (255, 255, 255)
    }
    MAX_GAME_SPEED = 10
    SNAKE_SPEED = 4
    PLAYING_SPEED =  int((MAX_GAME_SPEED - SNAKE_SPEED)*60)


    pygame.init()
    pygame.display.set_caption("Abj's Snake Game (w/ grid obj) :p")
    CANVAS = pygame.Surface((WIDTH, HEIGHT))
    PLAYING = pygame.USEREVENT; pygame.time.set_timer(PLAYING, PLAYING_SPEED)
    clock = pygame.time.Clock()


    class Grid:


        def __init__(self):

            self.grid = [[0 for col in range(Game.CELL_ROW)] for row in range(Game.CELL_ROW)]


        def draw(self, window):

            def draw_empty_cell(row, col):

                    empty_cell_pos = pygame.Vector2(row, col)
                    empty_cell_rect = pygame.Rect(empty_cell_pos.x * cell_size, empty_cell_pos.y * cell_size,
                                                  cell_size - cell_border, cell_size - cell_border)
                    

                    pygame.draw.rect(window, Game.COLOURS['cell_green'], empty_cell_rect, 0, 3)


            cell_border = Game.SQUARE_BORDER_WIDTH; cell_size = Game.CELL_SIZE


            for rows in range(len(self.grid)):

                for columns in range(len(self.grid[rows])):

                    draw_empty_cell(rows, columns)


                    # Apple cell
                    if self.grid[rows][columns] == 1:

                        apple_cell_pos = pygame.Vector2(rows, columns)
                        apple_cell_rect = pygame.Rect(apple_cell_pos.x * cell_size + (cell_border//2),
                                                      apple_cell_pos.y * cell_size + (cell_border//2),
                                                      cell_size - (cell_border+2),
                                                      cell_size - (cell_border+2))
                        

                        pygame.draw.rect(window, Game.COLOURS['apple_red'], apple_cell_rect, 0, 13)


                    # Snake cell
                    elif self.grid[rows][columns] == 2:

                        snake_cell_pos = pygame.Vector2(rows, columns)
                        snake_cell_rect = pygame.Rect(snake_cell_pos.x * cell_size + (cell_border),
                                                      snake_cell_pos.y * cell_size + (cell_border),
                                                      cell_size - (cell_border+4),
                                                      cell_size - (cell_border+4))
                        

                        pygame.draw.rect(window, Game.COLOURS['snake_green'], snake_cell_rect, 0, 7)


        def print(self):
            
            for row in self.grid:

                for col in row:

                    print("", col, end="")
                

                print()


    class Snake:


        def __init__(self, grid_obj):

            self.grid = grid_obj


            self.moving_direction = "up"
      

            self.snake_body_pos = [     # Starting size: 3
                pygame.Vector2(10, 10), # Head
                pygame.Vector2(10, 11),
                pygame.Vector2(10, 12)
            ]


        def place(self):
        
            for vector in self.snake_body_pos:
            
                self.grid.grid[int(vector.x)][int(vector.y)] = 2


        def snake_movements(self, direction = "default"):
            
            def move_left():

                if not self.moving_direction == 'right':

                    whole_body = self.snake_body_pos[:]
                    head_pos = whole_body[0]; new_head_pos = pygame.Vector2(head_pos.x - 1, head_pos.y)
                    whole_body.insert(0, new_head_pos)


                    self.snake_body_pos = whole_body[:len(whole_body)-1]
                    self.grid.grid[int(whole_body[-1].x)][int(whole_body[-1].y)] = 0
                    self.moving_direction = "left"


            def move_right():

                if not self.moving_direction == 'left':

                    whole_body = self.snake_body_pos[:]
                    head_pos = whole_body[0]; new_head_pos = pygame.Vector2(head_pos.x + 1, head_pos.y)
                    whole_body.insert(0, new_head_pos)


                    self.snake_body_pos = whole_body[:len(whole_body)-1]
                    self.grid.grid[int(whole_body[-1].x)][int(whole_body[-1].y)] = 0
                    self.moving_direction = "right"


            def move_up():

                if not self.moving_direction == 'down':

                    whole_body = self.snake_body_pos[:]
                    head_pos = whole_body[0]; new_head_pos = pygame.Vector2(head_pos.x, head_pos.y - 1)
                    whole_body.insert(0, new_head_pos)


                    self.snake_body_pos = whole_body[:len(whole_body)-1]
                    self.grid.grid[int(whole_body[-1].x)][int(whole_body[-1].y)] = 0
                    self.moving_direction = "up"


            def move_down():

                if not self.moving_direction == 'up':

                    whole_body = self.snake_body_pos[:]
                    head_pos = whole_body[0]; new_head_pos = pygame.Vector2(head_pos.x, head_pos.y + 1)
                    whole_body.insert(0, new_head_pos)


                    self.snake_body_pos = whole_body[:len(whole_body)-1]
                    self.grid.grid[int(whole_body[-1].x)][int(whole_body[-1].y)] = 0
                    self.moving_direction = "down"


            def default_moving():

                whole_body = self.snake_body_pos[:]
                head_pos = whole_body[0]


                match self.moving_direction:
                    case 'left':
                        new_head_pos = pygame.Vector2(head_pos.x - 1, head_pos.y)

                    case 'right':
                        new_head_pos = pygame.Vector2(head_pos.x + 1, head_pos.y)

                    case 'up':
                        new_head_pos = pygame.Vector2(head_pos.x, head_pos.y - 1)

                    case 'down':
                        new_head_pos = pygame.Vector2(head_pos.x, head_pos.y + 1)


                whole_body.insert(0, new_head_pos)
                self.snake_body_pos = whole_body[:len(whole_body)-1]
                self.grid.grid[int(whole_body[-1].x)][int(whole_body[-1].y)] = 0

            
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
    
    
    class Apple:

        
        def __init__(self, grid_obj):

            self.grid = grid_obj


            self.apple_pos = self.spawn_apple()
            

        def spawn_apple(self):

            apple_pos = pygame.Vector2(random.randint(1, Game.CELL_ROW - 1),
                                       random.randint(1, Game.CELL_ROW - 1))
            

            while self.grid.grid[int(apple_pos.x)][int(apple_pos.y)] == 2:

                apple_pos = pygame.Vector2(random.randint(1, Game.CELL_ROW - 1), 
                                           random.randint(1, Game.CELL_ROW - 1))
                

            return apple_pos


        def place(self):

            apple_pos = self.apple_pos
            self.grid.grid[int(apple_pos.x)][int(apple_pos.y)] = 1


    class GameLogic:

        
        SCORE = 0
        APPLE_POSITIONS = []
        BODY_PART_INSERT_QUEUE = []


        def __init__(self, grid_obj, apple_obj, snake_obj, screen_obj):

            self.grid = grid_obj
            self.apple = apple_obj
            self.snake = snake_obj
            self.screen = screen_obj


            self.game_logic_endgame_reason = ""
            self.stop = False


            self.score_font = pygame.font.Font(None, (Game.SCORE_SURFACE_SIZE - (Game.SCORE_SURFACE_SIZE//10)))
            self.end_font1 = pygame.font.Font(None, 80)
            self.end_font2 = pygame.font.Font(None, 50)
            self.end_reason_font = pygame.font.Font(None, 35)


        def score_draw(self):

            score_surface = self.score_font.render(str(Game.GameLogic.SCORE), 
                                                   True, Game.COLOURS['white'])
            

            # Those (x, y) coords makes it in the middle, above the grid 
            self.screen.blit(score_surface, (Game.WIDTH // 2, (Game.SCORE_SURFACE_SIZE // 2) // 2))


        def wall_collision(self):

            grid_side_length = Game.CELL_ROW
            snake_wholebody = self.snake.snake_body_pos[:]


            for vector in snake_wholebody:
                   
                if (0 <= vector.x < grid_side_length) & (0 <= vector.y < grid_side_length) :
                        
                    return False
                

                else:
                
                    return True
            

        def self_collision(self):

            snake_head_pos = self.snake.snake_body_pos[0]
            snake_wholebody = self.snake.snake_body_pos[:]


            if snake_wholebody.count(snake_head_pos) != 1:
                
                return True
            

            else:

                return False
            

        def eat_collision(self):
            
            snake_head_pos = self.snake.snake_body_pos[0]
            grid = self.grid.grid[:]


            if grid[int(snake_head_pos.x)][int(snake_head_pos.y)] == 1:
                
                return True
            

            else:
                
                return False
            

        def eat_apple(self):

            def eat_body_queue_inserter(apple_pos, direction):

                match direction: # Opposite spawing of last body-part is required to not self collide
                    case 'left':

                        insert_body_part = pygame.Vector2(apple_pos.x + 1, apple_pos.y)
                
                    case 'right':

                        insert_body_part = pygame.Vector2(apple_pos.x - 1, apple_pos.y)
                
                    case 'up':

                        insert_body_part = pygame.Vector2(apple_pos.x, apple_pos.y + 1)
                
                    case 'down':

                        insert_body_part = pygame.Vector2(apple_pos.x, apple_pos.y - 1)
                    
                
                Game.GameLogic.APPLE_POSITIONS.append(self.apple.apple_pos)
                Game.GameLogic.BODY_PART_INSERT_QUEUE.append(insert_body_part)


            apple_pos = self.apple.apple_pos
            direction = self.snake.moving_direction


            eat_body_queue_inserter(apple_pos, direction)


            Game.GameLogic.SCORE += 1


        def queue_check(self):

            def snake_body_update(whole_body, last_body_part, body_part_insert_queue, apple_positions):

                new_body = body_part_insert_queue[0]
                past_apple_pos = apple_positions[0]


                if last_body_part == past_apple_pos:
                    
                    del Game.GameLogic.APPLE_POSITIONS[0]
                    del Game.GameLogic.BODY_PART_INSERT_QUEUE[0]


                    whole_body.append(new_body)
                    self.snake.snake_body_pos = whole_body


                    # To not skip the amount of body-parts number, when apples are eaten faster than the last body-part reaches that apple's position
                    if len(body_part_insert_queue) < 1:
                        
                        print(f"\nNew bodypart added\n  in the game! ({Game.GameLogic.SCORE})")
                    

                    else:
                        
                        print(f"\nNew bodypart added\n  in the game! ({(Game.GameLogic.SCORE) - (len(body_part_insert_queue))})")


            whole_body = self.snake.snake_body_pos[:]
            last_body_part = whole_body[-1]


            previous_apple_positions = Game.GameLogic.APPLE_POSITIONS
            body_part_insert_queue = Game.GameLogic.BODY_PART_INSERT_QUEUE


            if len(body_part_insert_queue) > 0:

                snake_body_update(whole_body, last_body_part, body_part_insert_queue, previous_apple_positions)
            

        def end_game(self, canvas, reason = ""):

            #self.screen.fill('darkblue')
            #canvas.fill('darkblue')
            #antialias = True
            antialias = False


            end_text1 = "GAME OVER"
            end_text2 = f"Your score is: {str(Game.GameLogic.SCORE)}"
            

            end_surface1 = self.end_font1.render(end_text1, antialias, Game.COLOURS['white'])
            end_surface2 = self.end_font2.render(end_text2, antialias, Game.COLOURS['white'])


            canvas.blit(end_surface1, ((self.screen.get_width() // 2) - (end_surface1.get_width() // 2),
                                       (self.screen.get_height() // 2) - ((end_surface1.get_height() + Game.SCORE_SURFACE_SIZE) // 2) - (200)))
            
            canvas.blit(end_surface2, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2),
                                       (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2)))
            

            match reason:
                case "wall":
                    end_reason = "You hit the wall :p"

                    end_reason_surface = self.end_reason_font.render(end_reason, antialias, Game.COLOURS['white'])


                    canvas.blit(end_reason_surface, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25), 
                                                     (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2) + (175)))

                case "self":
                    end_reason = "You hit yourself :p"

                    end_reason_surface = self.end_reason_font.render(end_reason, antialias, Game.COLOURS['white'])


                    canvas.blit(end_reason_surface, ((self.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25), 
                                                     (self.screen.get_height() // 2) - ((end_surface2.get_height() + Game.SCORE_SURFACE_SIZE) // 2) + (175)))
            
            
            self.screen.blit(canvas, (0, Game.SCORE_SURFACE_SIZE))
            

            pygame.display.update()


    def __init__(self):

        self.screen = pygame.display.set_mode((Game.CANVAS.get_width(), Game.CANVAS.get_height() + Game.SCORE_SURFACE_SIZE))
        self.canvas = Game.CANVAS
        

        self.grid = Game.Grid()
        self.snake = Game.Snake(self.grid)
        self.apple = Game.Apple(self.grid)
        

        self.game_logic = Game.GameLogic(self.grid, self.apple, self.snake, self.screen)


    def run(self):

        while True:

            while not self.game_logic.stop:

                ## Play screen

                # Game engine
                self.game_logic = Game.GameLogic(self.grid, self.apple, self.snake, self.screen)


                # PyGame event handler
                for event in pygame.event.get():

                    # Required window exit button
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

                        
                        # Print the grid !
                        if event.key == pygame.K_p:

                            self.grid.print()


                # Game mehcanics
                self.game_logic.queue_check()                


                # Game mehcanics - Termination logic
                if self.game_logic.wall_collision():
                    
                    print("\nwall collision!")
                    self.game_logic.game_logic_endgame_reason = "wall"
                    self.game_logic.stop = True
                    break


                elif self.game_logic.self_collision():
                    
                    print("\nself collision!")
                    self.game_logic.game_logic_endgame_reason = "self"
                    self.game_logic.stop = True
                    break
            

                # Game mehcanics - Progression logic
                if self.game_logic.eat_collision():

                    self.game_logic.eat_apple()
                    self.apple = Game.Apple(self.grid)


                # Game rendering update
                self.screen.fill('darkblue')
                self.canvas.fill(Game.COLOURS['grid_border'])


                self.snake.place()
                self.apple.place()
                self.grid.draw(self.canvas)
                self.game_logic.score_draw()


                self.screen.blit(self.canvas, (0, Game.SCORE_SURFACE_SIZE))
                
                
                pygame.display.update()


                # Game Framerate cap
                Game.clock.tick(60)


            ## Game-Over screen

            # PyGame event handler
            for event in pygame.event.get():

                # Required window exit button handler
                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    sys.exit()


            # Game rendering update & Framerate cap
            self.game_logic.end_game(self.canvas, self.game_logic.game_logic_endgame_reason)
            Game.clock.tick(60)


Game().run()