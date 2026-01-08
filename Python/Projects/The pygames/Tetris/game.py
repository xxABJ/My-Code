from blocks import *
from grid import Grid
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        random_block = random.choice(self.blocks)
        self.blocks.remove(random_block)
        return random_block
    
    def draw(self, window):
        self.grid.draw(window)
        self.current_block.draw(window)
        
    def move_left(self):
        self.current_block.move(0, -1)

    def move_right(self):
        self.current_block.move(0, 1)

    def move_down(self):
        self.current_block.move(1, 0)
