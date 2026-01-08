from colours import Colours
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cell_size = 30
        self.cells = {}
        self.rotation_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.colours = Colours.get_cell_colours()

    def move(self, rows, coloumns):
        self.row_offset += rows
        self.column_offset += coloumns

    def get_block_positions(self):
        tiles = self.cells[self.rotation_state]
        active_tiles = []
        for tile in tiles:
            position = Position(tile.row + self.row_offset, tile.col + self.column_offset) # move func assigner
            active_tiles.append(position)
        return active_tiles

    def draw(self, window):
        tiles = self.get_block_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) # .row and .col is related to Position class, make sure this reflects on the grid rects
            pygame.draw.rect(window, self.colours[self.id], tile_rect)