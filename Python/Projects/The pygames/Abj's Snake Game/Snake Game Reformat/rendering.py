from settings import Settings


import pygame


class Rendering:
    

    def __init__(self, game):
        
        self.game = game


        self.restart_render_done = False


        self.gamescore_font = pygame.font.Font(None, (Settings.SCORE_SURFACE_SIZE - (Settings.SCORE_SURFACE_SIZE//10)))
        self.start_font1 = pygame.font.Font(None, 80)
        self.start_font2 = pygame.font.Font(None, 50)
        self.pause_font1 = pygame.font.Font(None, 100)
        self.end_font1 = pygame.font.Font(None, 80)
        self.end_font2 = pygame.font.Font(None, 50)
        self.end_font3 = pygame.font.Font(None, 65)
        self.end_reason_font = pygame.font.Font(None, 35)


    def update(self):
    
        def end_game():

            self.game.screen.fill(Settings.COLOURS['screen_background'])
            self.game.canvas.fill(Settings.COLOURS['screen_background'])


            end_text1 = "GAME OVER"
            end_text2 = f"Your score is:   {str(self.game.get_game_score())}"
            end_text3 = "-  Press ( R ) to restart !  -"
            

            end_surface1 = self.end_font1.render(end_text1, True, Settings.COLOURS['white'])
            end_surface2 = self.end_font2.render(end_text2, True, 'red')
            end_surface3 = self.end_font3.render(end_text3, True, 'gold')


            self.game.canvas.blit(end_surface1, ((self.game.screen.get_width() // 2) - (end_surface1.get_width() // 2),
            (self.game.screen.get_height() // 2) - ((end_surface1.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) - (200)))

            self.game.canvas.blit(end_surface2, ((self.game.screen.get_width() // 2) - (end_surface2.get_width() // 2),
            (self.game.screen.get_height() // 2) - ((end_surface2.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) - (100)))
            

            match self.game.collisions.collision_reason:
                case "wall_collision":
                    
                    end_reason = "You hit the wall :p"


                    end_reason_surface = self.end_reason_font.render(end_reason, True, 'green')


                    self.game.canvas.blit(end_reason_surface, ((self.game.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25),
                    (self.game.screen.get_height() // 2) - ((end_surface2.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) + (0)))


                case "self_collision":
                    
                    end_reason = "You hit yourself :p"


                    end_reason_surface = self.end_reason_font.render(end_reason, True, 'green')


                    self.game.canvas.blit(end_reason_surface, ((self.game.screen.get_width() // 2) - (end_surface2.get_width() // 2) + (25),
                    (self.game.screen.get_height() // 2) - ((end_surface2.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) + (0)))
            

            self.game.canvas.blit(end_surface3, ((self.game.screen.get_width() // 2) - (end_surface3.get_width() // 2),
            (self.game.screen.get_height() // 2) - ((end_surface3.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) + (150)))

            self.game.screen.blit(self.game.canvas, (0, Settings.SCORE_SURFACE_SIZE))


        def resume_game():

            def score_render():
                
                gamescore_text = str(self.game.get_game_score())


                gamescore_surface = self.gamescore_font.render(gamescore_text, True, Settings.COLOURS['white'])


                self.game.screen.blit(gamescore_surface, ((self.game.screen.get_width() // 2) - (gamescore_surface.get_width() // 2) + (0),
                (Settings.SCORE_SURFACE_SIZE // 2) - (gamescore_surface.get_height()// 2) + (0)))


            self.game.screen.fill(Settings.COLOURS['screen_background'])
            self.game.canvas.fill(Settings.COLOURS['grid_border'])


            cell_border = Settings.SQUARE_BORDER_WIDTH
            cell_size = Settings.CELL_SIZE


            cell_types = {
                'empty': Settings.GRIDCELL_EMPTY,
                'apple': Settings.GRIDCELL_APPLE,
                'snake': Settings.GRIDCELL_SNAKE
            }


            for row in range(len(self.game.grid.grid)):
                
                for col in range(len(self.game.grid.grid[row])):
                    
                    cell = self.game.grid.grid[row][col]
                    cell_pos = pygame.Vector2(row, col)


                    if cell == cell_types['empty']:

                        empty_cell_rect = pygame.Rect(cell_pos.x * cell_size + (cell_border//2),
                                                      cell_pos.y * cell_size + (cell_border//2), 
                                                      cell_size - (cell_border),
                                                      cell_size - (cell_border))
                        

                        pygame.draw.rect(self.game.canvas, Settings.COLOURS['cell_green'], empty_cell_rect, 0, 3)
        

                    elif cell == cell_types['apple']:

                        apple_cell_rect = pygame.Rect(cell_pos.x * cell_size + (cell_border),
                                                      cell_pos.y * cell_size + (cell_border),
                                                      cell_size - (cell_border+2),
                                                      cell_size - (cell_border+2))
        
        
                        pygame.draw.rect(self.game.canvas, Settings.COLOURS['apple_red'], apple_cell_rect, 0, 13)


                    elif cell == cell_types['snake']:

                        snake_cell_rect = pygame.Rect(cell_pos.x * cell_size + (cell_border), 
                                                      cell_pos.y * cell_size + (cell_border), 
                                                      cell_size - (cell_border+2), 
                                                      cell_size - (cell_border+2))
        
        
                        pygame.draw.rect(self.game.canvas, Settings.COLOURS['snake_green'], snake_cell_rect, 0, 7)


            score_render()
            self.game.screen.blit(self.game.canvas, (0, Settings.SCORE_SURFACE_SIZE))


        def pause_game():

            pause_text = f"PAUSED"
            

            pause_surface = self.end_font1.render(pause_text, True, Settings.COLOURS['white'])


            self.game.canvas.blit(pause_surface, ((self.game.screen.get_width() // 2) - (pause_surface.get_width() // 2), 
            (self.game.screen.get_height() // 2) - ((pause_surface.get_height() + Settings.SCORE_SURFACE_SIZE) // 2) - (25)))

            self.game.screen.blit(self.game.canvas, (0, Settings.SCORE_SURFACE_SIZE))


        def restart_game():

            restart_text1 = ".  RESTARTING  ."
            restart_text2 = ".  .  RESTARTING  .  ."
            restart_text3 = ".  .  .  RESTARTING  .  .  ."


            restart_texts = [restart_text1, restart_text2, restart_text3]
            restart_font = pygame.font.Font(None, 50)


            for text in restart_texts:

                self.game.screen.fill(Settings.COLOURS['screen_background'])


                restart_surface = restart_font.render(text, True, 'gold')


                self.game.screen.blit(restart_surface, ((self.game.screen.get_width()//2) - (restart_surface.get_width()//2),
                ((self.game.screen.get_height()//2) - (restart_surface.get_height()//2))))


                pygame.display.update()
                pygame.time.delay(Settings.RESTARTING_SPEED*2)


            self.game.new_game()


        match self.game.get_game_state():
            case 'start_game':
                
                resume_game()

            case 'resume_game':
                
                resume_game()

            case 'end_game':
                
                end_game()

            case 'pause_game':
                
                pause_game()

            case 'restart_game':

                restart_game()


        pygame.display.update()
        self.game.clock.tick(60)

