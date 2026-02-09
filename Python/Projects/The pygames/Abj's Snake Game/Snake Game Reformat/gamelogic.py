from settings import Settings


import pygame, random


class GameLogic:

    
    def __init__(self, game):

        self.game = game


        self.apple_positions = []
        self.bodypart_insert_queue = []
        
        
        self.vectors =  {
            "left": pygame.Vector2(-1, 0),
            "right": pygame.Vector2(1, 0),
            "up": pygame.Vector2(0, -1),
            "down": pygame.Vector2(0, 1)
        }


        self.reset_queue = False


        self.paused_moving_direction = ""
        self.paused = False


        self.create_snake()
        self.create_apple()


    def get_logic(self, event):

        def check_collisions():

            if not self.game.collisions.check():

                return
            

            if self.game.collisions.check() == 'eat_collision':
            
                self.eat_apple()
            
            
            elif self.game.collisions.check() == 'wall_collision':
            
                self.game.snake.moving_direction = 'collision'
                self.end_game()


            elif self.game.collisions.check() == 'self_collision':
            
                self.game.snake.moving_direction = 'collision'
                self.end_game()

        
        def check_eat_queue():

            if not self.apple_positions:
                
                return
            

            snake_full_body = self.game.snake.snake_body_pos
            snake_tail = snake_full_body[-1]
            old_apple_pos = self.apple_positions[0]


            if snake_tail == old_apple_pos:

                try:

                    new_snake_body = self.bodypart_insert_queue[0]
                    self.game.snake.snake_body_pos.append(new_snake_body)
                    
                    
                    self.apple_positions.pop(0)
                    self.bodypart_insert_queue.pop(0)


                    print("\nNew body added!")
                    print(f" in the game! ({self.game.get_game_score() - len(self.bodypart_insert_queue)})\n")


                except Exception as e:

                    pass
                    #print('Exception?: {e} how?')
                

        if event.type == Settings.PLAYING_UE:
        
            if self.game.get_game_state() == "":
            
                self.game.set_game_state('resume_game')
                self.start_game()


            elif self.game.get_game_state() != "":
            
                #print(self.game.snake.moving_direction)
                self.move(self.game.snake.moving_direction)


            check_collisions()
            check_eat_queue()


    def get_inputs(self, event):

        if not event.type == pygame.KEYDOWN:

            return
        

        direction = self.game.snake.moving_direction


        if direction == 'collision':

            self.game.tick = pygame.time.set_timer(Settings.RESTARTING_UE, Settings.RESTARTING_SPEED)


            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_r:
                    
                    self.restart_game()


        elif event.type == pygame.KEYDOWN:

            if not self.paused:

                if event.key == pygame.K_UP and direction != 'down':

                    direction = 'up'


                if event.key == pygame.K_DOWN and direction != 'up':

                    direction = 'down'


                if event.key == pygame.K_RIGHT and direction != 'left':

                    direction = 'right'


                if event.key == pygame.K_LEFT and direction != 'right':

                    direction = 'left'


                # Pause
                if event.key == pygame.K_ESCAPE and not self.paused:

                    print("- PAUSED -")
                    self.paused_moving_direction = direction
                    self.paused = True


                    direction = 'stop'


            else:

                # Unpause
                if event.key == pygame.K_ESCAPE:

                    print("- RESUMING -")
                    self.paused = False


        self.game.snake.moving_direction = direction


    def move(self, direction):

        movements = {"left", "right", "up", "down", "collision"}
        

        # Pause logic
        if direction not in movements:
            
            if self.paused:

                self.pause_game()
            
            
            else:

                self.resume_game()


                self.game.snake.moving_direction = self.paused_moving_direction
                self.paused = False
        

        elif direction == 'collision':
            
            return


        else:

            snake_full_body = self.game.snake.snake_body_pos
            snake_head = snake_full_body[0]
            new_snake_head = pygame.Vector2(int(snake_head.x + self.vectors[direction].x),
                                            int(snake_head.y + self.vectors[direction].y))


            snake_full_body.insert(0, new_snake_head)
            self.game.grid.grid[int(snake_full_body[-1].x)][int(snake_full_body[-1].y)] = Settings.GRIDCELL_EMPTY
            snake_full_body.pop()


            self.game.snake.snake_body_pos = snake_full_body
            self.game.snake.moving_direction = direction
            

            self.place_snake()


    def start_game(self):
    
        self.game.set_game_state('resume_game')

    
    def pause_game(self):

        self.game.set_game_state('pause_game')


    def resume_game(self):

        self.game.set_game_state('resume_game')

    
    def restart_game(self):

        print('- RESTARTING -')
        self.game.set_game_state('restart_game')


    def end_game(self):

        self.game.set_game_state('end_game')


    def create_snake(self):

        snake_full_body = []


        random_snake_part = pygame.Vector2(random.randint(3, Settings.CELL_ROW - 3), 
                                        random.randint(10, Settings.CELL_ROW - 3))
        

        for part in range(3):

            snake_body_part = pygame.Vector2(random_snake_part.x, random_snake_part.y + part)
            snake_full_body.append(snake_body_part)

        
        self.game.snake.snake_body_pos = snake_full_body
        self.place_snake()


    def place_snake(self):

        for vector in self.game.snake.snake_body_pos:
            
            if 0 <= vector.x < Settings.CELL_ROW and 0 <= vector.y < Settings.CELL_ROW:
                
                self.game.grid.grid[int(vector.x)][int(vector.y)] = Settings.GRIDCELL_SNAKE


    def create_apple(self):

        apple_pos = pygame.Vector2(random.randint(1, Settings.CELL_ROW - 1),
                                random.randint(1, Settings.CELL_ROW - 1))
        
    
        while self.game.grid.grid[int(apple_pos.x)][int(apple_pos.y)] == Settings.GRIDCELL_SNAKE:
    
            apple_pos = pygame.Vector2(random.randint(1, Settings.CELL_ROW - 1), 
                                    random.randint(1, Settings.CELL_ROW - 1))
            
    
        self.game.apple.apple_pos = apple_pos
        self.place_apple()


    def place_apple(self):

        apple_pos = self.game.apple.apple_pos
        self.game.grid.grid[int(apple_pos.x)][int(apple_pos.y)] = Settings.GRIDCELL_APPLE


    def eat_apple(self):

        inverse_movement = {
            "left": "right",
            "right": "left",
            "up": "down",
            "down": "up"
        }


        apple_pos = self.game.apple.apple_pos
        opposite_direction = inverse_movement.get(self.game.snake.moving_direction)
        new_snake_body = pygame.Vector2(int(apple_pos.x + self.vectors[opposite_direction].x),
                                        int(apple_pos.y + self.vectors[opposite_direction].y))
        

        self.apple_positions.append(apple_pos)
        self.bodypart_insert_queue.append(new_snake_body)


        self.game.increase_game_score()
        self.create_apple()

