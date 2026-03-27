
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

