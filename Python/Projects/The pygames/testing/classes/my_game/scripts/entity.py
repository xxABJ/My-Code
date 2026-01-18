import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.horizontal_movement = [False, False]
        self.vertical_movement = [False, False]



    def update(self, game, h = [None, None], v = [None, None]):
        # Update movement states if provided
        if h != [None, None]:
            self.horizontal_movement = h
        if v != [None, None]:
            self.vertical_movement = v
        
        # Calculate and apply movement
        horizontalframe_movements = self.horizontal_movement[1] - self.horizontal_movement[0]
        verticalframe_movements = self.vertical_movement[1] - self.vertical_movement[0]
        
        self.pos[0] += horizontalframe_movements
        self.pos[1] += verticalframe_movements




    def render(self, game):


        asset = self.game.assets[self.type]
        self.game.screen.blit(asset, self.pos)