import random


class Colours:


    @classmethod
    def get_colours(cls, amount_of_colours = 20) -> list:
        colour_list = []
        for colours in range(amount_of_colours):
            colour = (random.randint(20, 230), random.randint(20, 230), random.randint(20, 230))
            colour_list.append(colour)
        return colour_list
    
    @classmethod
    def get_colour(cls) -> tuple:
        colour = (random.randint(20, 230), random.randint(20, 230), random.randint(20, 230))
        return colour
