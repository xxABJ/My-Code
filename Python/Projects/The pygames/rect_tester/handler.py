import pygame


class Handler:


    def __init__(self, main):
        
        self.main = main


    def get_inputs(self, event):

        self.mouse_inputs(event)
        self.keyboard_inputs(event)



    def mouse_inputs(self, event):

        def mouseclick_createmenu():
            
            def minus():

                if self.main.rendering.surfaces:

                    for key, value in self.main.rendering.surfaces.items():
                        
                        if (key[0] + 5 <= pygame.mouse.get_pos()[0] <= (key[0] + 25)) and ((key[1] + 80) - 40 <= pygame.mouse.get_pos()[1] <= (key[1] + 80) - 20):

                            self.main.createmenu.minus_amount()


                            self.main.rendering.surfaces = {}


                            menu_surface = self.main.creat_menu()
                            self.main.rendering.add_surfaces([key, menu_surface])


            def add():

                if self.main.rendering.surfaces:

                    for key, value in self.main.rendering.surfaces.items():
                        
                        if (key[0] + value.get_width() - 25 <= pygame.mouse.get_pos()[0] <= (key[0] + value.get_width() - 5)) and ((key[1] + 80) - (20) - 20 <= pygame.mouse.get_pos()[1] <= (key[1] + 80) - (20)):

                            self.main.createmenu.add_amount()


                            self.main.rendering.surfaces = {}


                            menu_surface = self.main.creat_menu()
                            self.main.rendering.add_surfaces([key, menu_surface])

            
            minus()
            add()


        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.mouse_button_check('left'):
                
                mouseclick_createmenu()


            if self.mouse_button_check('middle'):

                print(pygame.mouse.get_pressed())
                print(self.main.mouse.get_mouse_pos())
    

    def mouse_button_check(self, type):

        if type == 'left':
            
            left_mouse_button = pygame.mouse.get_pressed()[0]

            
            return left_mouse_button
        

        if type == 'right':
            
            right_mouse_button = pygame.mouse.get_pressed()[2]

            
            return left_mouse_button
        

        if type == 'middle':
            
            middle_mouse_button = pygame.mouse.get_pressed()[1]

            
            return middle_mouse_button
        

    def keyboard_inputs(self, event):

        def c():

            if not self.main.rendering.surfaces:
                
                mouse_pos = pygame.mouse.get_pos()
                menu_surface = self.main.creat_menu()


                self.main.rendering.add_surfaces([mouse_pos, menu_surface])
             
               
            else:
                
                self.main.createmenu.reset_amount()
                self.main.rendering.surfaces = {}


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_c:
                
                c()