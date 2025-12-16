import pygame, json
from menu import *

# gameclass - https://www.youtube.com/@CDcodes

# make a menu class that generates a menu on the pygame window.
# make a button class that generates buttons on the menu/other.
# make a game class? (prob have to draw the actual game.. maybe)

class Game:
    def __init__(self):
        pygame.init()
        #self.load_json = self.load_setting()

        self.running, self.playing = True, False
        self.ESCAPE_KEY, self.ENTER_KEY, self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPACE_KEY = False, False, False, False, False, False, False

        self.player1_alive = False
        self.player2_alive = False
        self.player3_alive = False
        self.player4_alive = False

        self.player1_trigger = False
        self.player2_trigger = False
        self.player3_trigger = False
        self.player4_trigger = False

        self.player1_cell = None
        self.player2_cell = None
        self.player3_cell = None
        self.player4_cell = None

        self.scale = 1
        self.cellsize = 80
        self.cellcount = 12
        self.bordersize = 4 # even works better .. (see lines 333-547)
        self.boardlength = (self.cellsize * self.cellcount)
        self.center_adjustment = self.cellsize - self.bordersize / 2
        self.boardplacement_adjustment = self.cellsize

        self.boardplacement =[
{(100, 0): [(self.boardplacement_adjustment + self.cellsize*1, self.boardplacement_adjustment), []], (99, 0): [(self.boardplacement_adjustment + self.cellsize*2, self.boardplacement_adjustment), []], (98, 0): [(self.boardplacement_adjustment + self.cellsize*3, self.boardplacement_adjustment), []], (97, 0): [(self.boardplacement_adjustment + self.cellsize*4, self.boardplacement_adjustment), []], (96, 0): [(self.boardplacement_adjustment + self.cellsize*5, self.boardplacement_adjustment), []], (95, 0): [(self.boardplacement_adjustment + self.cellsize*6, self.boardplacement_adjustment), []], (94, 0): [(self.boardplacement_adjustment + self.cellsize*7, self.boardplacement_adjustment), []], (93, 0): [(self.boardplacement_adjustment + self.cellsize*8, self.boardplacement_adjustment), []], (92, 0): [(self.boardplacement_adjustment + self.cellsize*9, self.boardplacement_adjustment), []], (91, 0): [(self.boardplacement_adjustment + self.cellsize*10, self.boardplacement_adjustment), []]},#dict 0

{(90, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize)), []], (89, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize)), []], (88, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize)), []], (87, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize)), []], (86, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize)), []], (85, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize)), []], (84, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize)), []], (83, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize)), []], (82, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize)), []], (81, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize)), []]},#dict 1
        
{(80, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*2)), []], (79, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*2)), []], (78, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*2)), []], (77, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*2)), []], (76, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*2)), []], (75, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*2)), []], (74, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*2)), []], (73, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*2)), []], (72, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*2)), []], (71, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*2)), []]},#dict 2

{(70, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*3)), []], (69, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*3)), []], (68, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*3)), []], (67, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*3)), []], (66, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*3)), []], (65, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*3)), []], (64, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*3)), []], (63, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*3)), []], (62, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*3)), []], (61, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*3)), []]},#dict 3
        
{(60, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*4)), []], (59, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*4)), []], (58, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*4)), []], (57, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*4)), []], (56, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*4)), []], (55, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*4)), []], (54, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*4)), []], (53, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*4)), []], (52, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*4)), []], (51, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*4)), []]},#dict 4
        
{(50, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*5)), []], (49, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*5)), []], (48, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*5)), []], (47, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*5)), []], (46, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*5)), []], (45, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*5)), []], (44, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*5)), []], (43, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*5)), []], (42, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*5)), []], (41, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*5)), []]},#dict 5

{(40, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*6)), []], (39, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*6)), []], (38, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*6)), []], (37, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*6)), []], (36, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*6)), []], (35, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*6)), []], (34, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*6)), []], (33, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*6)), []], (32, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*6)), []], (31, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*6)), []]},#dict 6

{(30, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*7)), []], (29, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*7)), []], (28, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*7)), []], (27, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*7)), []], (26, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*7)), []], (25, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*7)), []], (24, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*7)), []], (23, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*7)), []], (22, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*7)), []], (21, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*7)), []]},#dict 7

{(20, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*8)), []], (19, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*8)), []], (18, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*8)), []], (17, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*8)), []], (16, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*8)), []], (15, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*8)), []], (14, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*8)), []], (13, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*8)), []], (12, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*8)), []], (11, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*8)), []]},#dict 8

{(10, 0): [(self.boardplacement_adjustment + self.cellsize*10, (self.boardplacement_adjustment + self.cellsize*9)), []], (9, 0): [(self.boardplacement_adjustment + self.cellsize*9, (self.boardplacement_adjustment + self.cellsize*9)), []], (8, 0): [(self.boardplacement_adjustment + self.cellsize*8, (self.boardplacement_adjustment + self.cellsize*9)), []], (7, 0): [(self.boardplacement_adjustment + self.cellsize*7, (self.boardplacement_adjustment + self.cellsize*9)), []], (6, 0): [(self.boardplacement_adjustment + self.cellsize*6, (self.boardplacement_adjustment + self.cellsize*9)), []], (5, 0): [(self.boardplacement_adjustment + self.cellsize*5, (self.boardplacement_adjustment + self.cellsize*9)), []], (4, 0): [(self.boardplacement_adjustment + self.cellsize*4, (self.boardplacement_adjustment + self.cellsize*9)), []], (3, 0): [(self.boardplacement_adjustment + self.cellsize*3, (self.boardplacement_adjustment + self.cellsize*9)), []], (2, 0): [(self.boardplacement_adjustment + self.cellsize*2, (self.boardplacement_adjustment + self.cellsize*9)), []], (1, 0): [(self.boardplacement_adjustment + self.cellsize*1, (self.boardplacement_adjustment + self.cellsize*9)), []]}]#dict 9
  #0                    #1                   #2                   #3                   #4                   #5                   #6                   #7                   #8                   #9

        cellnumber = 100
        saved = self.boardplacement_adjustment
        for dictionary in self.boardplacement:
            for assign in range(len(dictionary)):
                if list(dictionary.keys())[assign][0] == cellnumber:
                    exec(f"self.cell_{cellnumber} = {cellnumber}; self.pos_{cellnumber} = list(dictionary.values())[assign][0]")
                    cellnumber -= 1
            #print("next dict")
        self.boardplacement_adjustment = saved

        self.vertical = pygame.Surface((self.bordersize, self.cellsize))
        self.horizontal = pygame.Surface((self.cellsize, self.bordersize))
        self.cell_pale = pygame.Surface((self.cellsize - self.bordersize, self.cellsize - self.bordersize))
        self.cell_brown = pygame.Surface((self.cellsize - self.bordersize, self.cellsize - self.bordersize))
        #self.ladder_vertical = pygame.Surface((self.))
        #self.ladder_horizontal = pygame.Surface((self.))

        self.video_resolution = [(self.boardlength, self.boardlength), (1000, 1000), (1024, 760), (1280, 720)]
        self.DISPLAY_W, self.DISPLAY_H = self.video_resolution[0]
        self.MAIN = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.menucolours = [(80, 110, 100), (255, 190, 140), (220, 110, 255), (0, 0, 0)]
        self.HIGHLIGHTED, self.MENUCOLOUR, self.WHITE, self.BORDERCOLOUR, self.PALE, self.BROWN = (120, 170, 60), self.menucolours[0], (255, 255, 255), (0, 0, 0), (210, 150, 60), (115, 70, 20)

        #self.player1 = Player1(self)

        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.videosettings_menu = VideoSettings(self)
        self.coloursettings_menu = MenuColourSettings(self)
        self.board = Board(self)
        self.current_menu = self.main_menu

    def load_setting(self):
        with open("game.json", "r") as file:
            return json.load(file)

    def save_settings(self):
            with open("game.json", "w") as file:
                json.dump(self, file)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_menu_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACKSPACE_KEY = True
    
    def draw_character(self):

        for lst in range(len(self.boardplacement)):
            for cell in range(int(self.boardplacement)):
                if cell == 1:
                    pass
                if cell == 2:
                    pass
                if cell == 3:
                    pass
                if cell == 4:
                    pass
  
    def reset_keys(self):
        self.ESCAPE_KEY, self.ENTER_KEY, self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPACE_KEY = False, False, False, False, False, False, False

    def game_loop(self):
        while self.playing:
            #self.load_json = self.load_setting()
            self.check_events()
            if self.ESCAPE_KEY:
                self.playing = False
            self.window.fill(self.MENUCOLOUR)

            #Check Player Placement
            #self.check_player_position_logic() #checks if alive
            #self.set_player_position_logic() #sets variable to position and updates board logic

            #Draw Board
            self.draw_cells()

            #Draw cell numbers
            self.draw_cellnumbers()

            #Draw board elements
            #self.draw_boardelements()

            # cell list
            #print(self.pos_1)

            self.MAIN.blit(self.window, (self.center_adjustment, self.center_adjustment))
            pygame.display.update()
            self.reset_keys()

            #print(f"len(self.boardplacement): {len(self.boardplacement)}")
            #print(f"\nself.cell_100: {self.cell_100}\nself.pos_100: {self.pos_100}\n")
            #print(f"\nself.cell_91: {self.cell_91}\nself.pos_91: {self.pos_91}\n")
            #print(f"\nself.cell_90: {self.cell_90}\nself.pos_90: {self.pos_90}\n")
            #print(f"\nself.cell_81: {self.cell_81}\nself.pos_81: {self.pos_81}\n")
            #print(f"\nself.cell_80: {self.cell_80}\nself.pos_80: {self.pos_80}\n")
            #print(f"\nself.cell_71: {self.cell_71}\nself.pos_71: {self.pos_71}\n")
            #print(f"\nself.cell_70: {self.cell_70}\nself.pos_70: {self.pos_70}\n")
            #print(f"\nself.cell_61: {self.cell_61}\nself.pos_61: {self.pos_61}\n")
            #print(f"\nself.cell_60: {self.cell_60}\nself.pos_60: {self.pos_60}\n")
            #print(f"\nself.cell_51: {self.cell_51}\nself.pos_51: {self.pos_51}\n")
            #print(f"\nself.cell_50: {self.cell_50}\nself.pos_50: {self.pos_50}\n")
            #print(f"\nself.cell_41: {self.cell_41}\nself.pos_41: {self.pos_41}\n")
            #print(f"\nself.cell_40: {self.cell_40}\nself.pos_40: {self.pos_40}\n")
            #print(f"\nself.cell_31: {self.cell_31}\nself.pos_31: {self.pos_31}\n")
            #print(f"\nself.cell_30: {self.cell_30}\nself.pos_30: {self.pos_30}\n")
            #print(f"\nself.cell_21: {self.cell_21}\nself.pos_21: {self.pos_21}\n")
            #print(f"\nself.cell_20: {self.cell_20}\nself.pos_20: {self.pos_20}\n")
            #print(f"\nself.cell_11: {self.cell_11}\nself.pos_11: {self.pos_11}\n")
            #print(f"\nself.cell_10: {self.cell_10}\nself.pos_10: {self.pos_10}\n")
            #print(f"\nself.cell_1: {self.cell_1}\nself.pos_1: {self.pos_1}\n")

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_colourtext(self, text, size, x, y, colour):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)
    
    def draw_boardtext(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_highlighted_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.HIGHLIGHTED)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    #pygame.draw.lines

    def draw_ladder(self):
        pass

    def draw_cells(self):
        x_vertical, y_vertical = 0, 0
        x_horizontal, y_horizontal = 0, 0
        cellsize_adjustment = int(self.cellsize - self.bordersize / 2)
        row_adjustment = 0

        self.MAIN.fill(self.MENUCOLOUR)
        self.vertical.fill(self.BORDERCOLOUR)
        self.horizontal.fill(self.BORDERCOLOUR)
        self.cell_pale.fill(self.PALE)
        self.cell_brown.fill(self.BROWN)

        mod = 0
        for rows in range(11):
            mod += 1
            for cells in range(10):
                old_x_vertical = x_vertical
                x_vertical += cellsize_adjustment
                new_x_vertical = x_vertical
                self.window.blit(self.vertical, (old_x_vertical, y_vertical))
                self.window.blit(self.vertical, (new_x_vertical, y_vertical))

                old_y_horizontal = y_horizontal
                y_horizontal += cellsize_adjustment
                new_y_horizontal = y_horizontal
                self.window.blit(self.horizontal, (x_horizontal, old_y_horizontal))
                self.window.blit(self.horizontal, (x_horizontal, new_y_horizontal))

                if mod % 2:
                    self.window.blit(self.cell_pale, (self.bordersize + old_x_vertical, self.bordersize + old_y_horizontal))
                else:
                    self.window.blit(self.cell_brown, (self.bordersize + old_x_vertical, self.bordersize + old_y_horizontal))
                mod += 1

                x_horizontal += cellsize_adjustment
                y_horizontal = old_y_horizontal


            x_vertical, y_vertical = 0, row_adjustment
            x_horizontal, y_horizontal = 0, row_adjustment
            row_adjustment += cellsize_adjustment
            
    def draw_cellnumbers(self):
        text_size = self.cellsize // 5
        text_placement = self.boardlength // 200
        required_adjustion = self.cellsize
        vertical_adjustion = required_adjustion
        saved = required_adjustion

        # Row 1
        self.draw_boardtext("100", text_size, self.bordersize + text_placement, self.bordersize + text_placement)
        self.draw_boardtext("99", text_size, required_adjustion + self.bordersize - int(self.bordersize/2) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("98", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*2) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("97", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*3) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("96", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*4) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("95", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*5) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("94", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*6) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("93", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*7) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("92", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*8) + text_placement, self.bordersize + text_placement)
        required_adjustion += saved
        self.draw_boardtext("91", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*9) + text_placement, self.bordersize + text_placement)

        # Row 2
        self.draw_boardtext("90", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*9) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("89", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*8) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("88", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*7) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("87", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*6) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("86", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*5) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("85", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*4) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("84", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*3) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("83", text_size, required_adjustion + self.bordersize - int(self.bordersize/2*2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("82", text_size, required_adjustion + self.bordersize - int(self.bordersize/2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))
        required_adjustion -= saved
        self.draw_boardtext("81", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2))

        # Row 3
        vertical_adjustion += saved
        self.draw_boardtext("80", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion = saved
        self.draw_boardtext("79", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("78", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("77", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("76", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("75", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("74", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("73", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("72", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)
        required_adjustion += saved
        self.draw_boardtext("71", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*2)

        # Row 4
        vertical_adjustion += saved
        self.draw_boardtext("70", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("69", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("68", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("67", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("66", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("65", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("64", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("63", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("62", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)
        required_adjustion -= saved
        self.draw_boardtext("61", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*3)

        # Row 5
        vertical_adjustion += saved
        self.draw_boardtext("60", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion = saved
        self.draw_boardtext("59", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("58", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("57", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("56", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("55", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("54", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("53", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("52", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)
        required_adjustion += saved
        self.draw_boardtext("51", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*4)

        # Row 6
        vertical_adjustion += saved
        self.draw_boardtext("50", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("49", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("48", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("47", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("46", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("45", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("44", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("43", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("42", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)
        required_adjustion -= saved
        self.draw_boardtext("41", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*5)

        # Row 7
        vertical_adjustion += saved
        self.draw_boardtext("40", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion = saved
        self.draw_boardtext("39", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("38", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("37", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("36", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("35", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("34", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("33", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("32", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)
        required_adjustion += saved
        self.draw_boardtext("31", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*6)

        # Row 8
        vertical_adjustion += saved
        self.draw_boardtext("30", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("29", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("28", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("27", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("26", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("25", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("24", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("23", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("22", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)
        required_adjustion -= saved
        self.draw_boardtext("21", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*7)

        # Row 9
        vertical_adjustion += saved
        self.draw_boardtext("20", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion = saved
        self.draw_boardtext("19", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("18", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("17", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("16", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("15", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("14", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("13", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("12", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)
        required_adjustion += saved
        self.draw_boardtext("11", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*8)

        # Row 10
        vertical_adjustion += saved
        self.draw_boardtext("10", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*9 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("9", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*8 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("8", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*7 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("7", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*6 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("6", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*5 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("5", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*4 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("4", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*3 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("3", text_size, required_adjustion + self.bordersize - int(self.bordersize//2)*2 + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("2", text_size, required_adjustion + self.bordersize - int(self.bordersize//2) + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)
        required_adjustion -= saved
        self.draw_boardtext("1", text_size, self.bordersize + text_placement, vertical_adjustion + self.bordersize + text_placement - int(self.bordersize//2)*9)

    #def check_player_position_logic(self):
    #    player_types = list(self.load_json["Settings"]["Players"].keys())
    #    
    #    for player in player_types:
    #        if player == "cat":
    #            self.player1_alive = True
    #        elif player == "dog":
    #            self.player2_alive = True
    #        elif player == "sheep":
    #            self.player3_alive = True
    #        elif player == "fly":
    #            self.player4_alive = True

    #def move_player_position(self):
    #    player_types = list(self.load_json["Settings"]["Players"].keys())
    #
    #
    #
    #    pass

    def set_player_position_logic(self):
        player_position = list(self.load_json["Game"]["Players"]["Positions"].values())
        playerlist = []
        turns = []

        if self.player1_alive:
            playerlist.append(self.player1_cell)
        if self.player2_alive:
            playerlist.append(self.player2_cell)
        if self.player3_alive:
            playerlist.append(self.player3_cell)
        if self.player4_alive:
            playerlist.append(self.player4_cell)

        for player in playerlist:
            if player == self.player1_cell:
                self.player1_cell = player_position[0]
                turns.append(self.player1_trigger)
            elif player == self.player2_cell:
                self.player2_cell = player_position[1]
                turns.append(self.player2_trigger)
            elif player == self.player3_cell:
                self.player3_cell = player_position[2]
                turns.append(self.player3_trigger)
            elif player == self.player4_cell:
                self.player4_cell = player_position[3]
                turns.append(self.player4_trigger)
        
        # here should be function call to update the trigger variable and draw movement on screen


        #print()
        #print(f"self.player1_cell: {self.player1_cell}")
        #print(f"self.player2_cell: {self.player2_cell}")
        #print(f"self.player3_cell: {self.player3_cell}")
        #print(f"self.player4_cell: {self.player4_cell}")
        #print()

        # Move trigger for adjusting the logic board
        for player in turns:
            if player:
                for dictionary in self.boardplacement:
                    for key, value in dictionary.items():
                        if self.player1_pos == key[0]:
                            key[1] += 1
                        elif self.player2_pos == key[0]:
                            key[1] += 1
                        elif self.player3_pos == key[0]:
                            key[1] += 1
                        elif self.player4_pos == key[0]:
                            key[1] += 1
                player = False
            
    def check_players(self):
        pass

class Board(Game):
    def __init__(self, game):
        #Game.__init__(self, game)
        self.game = game
        self.boxborder_horizontal = pygame.Rect(0, 0, 5, 5)
        self.boxborder_vertical = pygame.Rect(0, 0, 5, 5)
        self.BOXBORDERCOLOUR = (0, 0, 0)
        self.boxw, self.boxh = self.game.DISPLAY_W/12, self.game.DISPLAY_H/12
        pygame.Vector2(0,1)
        self.box_count = [12, 12]
        self.position_player1 = None
        self.position_player2 = None
        self.position_player3 = None
        self.position_player4 = None

    def blit_board(self):
        self.game.window.blit(self.game.display_surface, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_boxes(self):
        for row in range(self.box_count[0]):
            r = pygame.draw.rect(self.game.display_surface, self.BOXBORDERCOLOUR, self.boxborder_vertical)
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.window.blit(self.game.display_surface, r)
            pygame.display.update()
            self.boxborder_vertical.x += self.boxh
            for column in range(self.box_count[1]):
                pygame.draw.rect(self.game.display_surface, self.BOXBORDERCOLOUR, self.boxborder_vertical)
                self.boxborder_vertical.y += self.boxw

    def draw_board(self):
        self.draw_boxes()
