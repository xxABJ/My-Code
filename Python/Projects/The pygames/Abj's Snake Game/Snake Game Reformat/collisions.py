from settings import Settings


class Collisions:


    def __init__(self, game):
        
        self.game = game


        self.collision_reason = ""

    
    def check(self):

        def check_wall_collision():

            for vector in self.game.snake.snake_body_pos:

                if not (0 <= vector.x < Settings.CELL_ROW) or not (0 <= vector.y < Settings.CELL_ROW):

                    return 'wall_collision'
                

            return False


        def check_self_collision():

            for vector in self.game.snake.snake_body_pos:

                if self.game.snake.snake_body_pos.count(vector) > 1:

                    return 'self_collision'
                

            return False


        def check_eat_collision():

            snake_head = self.game.snake.snake_body_pos[0]


            if snake_head == self.game.apple.apple_pos:

                return 'eat_collision'
            

            return False


        wall_collision = check_wall_collision()
        self_collision = check_self_collision()
        eat_collision = check_eat_collision()


        if wall_collision != False:

            self.collision_reason = wall_collision
            return wall_collision
        

        if self_collision != False:

            self.collision_reason = self_collision
            return self_collision
        

        if eat_collision != False:

            self.collision_reason = eat_collision
            return eat_collision

