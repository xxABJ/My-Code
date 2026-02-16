import pygame


class CreateMenu:


    amount = 1


    def __init__(self):

        self.font = pygame.font.Font(None, 30)


    def add_amount(self):

        CreateMenu.amount += 1


    def minus_amount(self):

        if CreateMenu.amount > 1:

            CreateMenu.amount -= 1

    
    def print(self):
        print(CreateMenu.amount)


    def reset_amount(self):

        CreateMenu.amount = 1


    def menu_surface(self):

        menu_surface = pygame.Surface((60, 80))
        menu_surface.fill('grey')


        # add amount
        top = 15
        add_amount_text = f"{str(CreateMenu.amount)}"
        add_amount_surface = self.font.render(add_amount_text, True, 'black')
        menu_surface.blit(add_amount_surface, ((menu_surface.get_width()//2) - (add_amount_surface.get_width()//2), top))


        # buttons
        side = 5
        bottom = 20
        add_button_surface = pygame.Surface((20, 20))
        add_button_surface.fill('darkgreen')

        minus_button_surface = pygame.Surface((20, 20))
        minus_button_surface.fill('darkred')
        
        add_text = "+"
        add_text_surface = self.font.render(add_text, True, 'green')
        add_button_surface.blit(add_text_surface, ((add_button_surface.get_width()//2) - (add_text_surface.get_width()//2), (add_button_surface.get_height()//2) - (add_text_surface.get_height()//2)))
        menu_surface.blit(add_button_surface, (menu_surface.get_width() - (add_button_surface.get_width() + side), menu_surface.get_height() - (add_button_surface.get_height() + bottom)))

        minus_text = "-"
        minus_text_surface = self.font.render(minus_text, True, 'red')
        minus_button_surface.blit(minus_text_surface, ((minus_button_surface.get_width()//2) - (minus_text_surface.get_width()//2), (minus_button_surface.get_height()//2) - (minus_text_surface.get_height()//2)))
        menu_surface.blit(minus_button_surface, (side, menu_surface.get_height() - (minus_button_surface.get_height() + bottom)))


        return menu_surface
