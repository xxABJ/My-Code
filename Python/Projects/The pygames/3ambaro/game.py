import pygame

from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.MAIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.windowcaption = pygame.display.set_caption(("3ambaroo"))
        self.clock = pygame.time.Clock()

        self.running = True

    def reset_keys(self):
        self.ESCAPE_KEY = False
        self.ENTER_KEY = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.BACKSPACE_KEY = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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
    
    def game_loop(self):
        self.clock.tick(FPS)
        self.check_events()
        if self.BACKSPACE_KEY:
            pygame.QUIT

        self.MAIN.fill("blue")
        self.reset_keys()

a = Game()
while a.running:
    a.game_loop()