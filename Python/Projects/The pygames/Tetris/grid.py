import pygame
from colours import Colours

class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self.cell_size = 30
        self.grid = [[0 for col in range(self.columns)] for row in range(self.rows)]
        self.colours = Colours.get_cell_colours()

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.columns):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) # Offset for a grid outline
                #cell_rect = pygame.Rect(row*self.cell_size + 1, col*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) # Offset for a grid outline
                pygame.draw.rect(window, self.colours[cell_value], cell_rect)

    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                print(self.grid[row][col], end= " ")
            print()