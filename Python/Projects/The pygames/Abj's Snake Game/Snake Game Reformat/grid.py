from settings import Settings


class Grid:


    def __init__(self):

        self.grid = [[0 for col in range(Settings.CELL_ROW)] for row in range(Settings.CELL_ROW)]


    def print(self):
        
        for row in self.grid:

            for col in row:

                print("", col, end="")


            print()

