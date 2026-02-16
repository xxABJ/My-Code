from grid import Grid


import pygame, sys


class Maze:


    def __init__(self, size):
        
        # Big enough to not break logic: 7+ (7x7)
        self.grid = Grid(size)