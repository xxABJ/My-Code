class Colours:
    dark_grey = (16, 21, 30) # 0
    red = (207, 18, 18) # 1
    green = (67, 152, 21) # 2
    yellow = (229, 200, 30) # 3
    blue = (30, 113, 229) # 4
    purple = (136, 69, 213) # 5
    pink = (244, 119, 232) # 6
    white = (231, 224, 214) # 7

    @classmethod
    def get_cell_colours(cls):
        return [cls.dark_grey, cls.red, cls.green, cls.yellow, cls.blue, cls.purple, cls.pink, cls.white]