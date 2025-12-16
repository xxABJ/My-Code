import pygame, sys

CLOSEWINDOW = pygame.USEREVENT + 1
KEYBOARD = pygame.USEREVENT + 2
MOUSE = pygame.USEREVENT + 3

def post_events(self, event_type):
    if event_type == pygame.QUIT:
        pygame.event.post(pygame.event.Event(CLOSEWINDOW))
    if event_type == pygame.KEYDOWN:
        pygame.event.post(pygame.event.Event(KEYBOARD))
    
    #mouse
    if pygame.mouse.get_visible() and pygame.mouse.get_pressed():
        pygame.event.post(pygame.event.Event(MOUSE))

def handle_events(self, event_type):
    if event_type in EVENTS

def closewindow(self, event_type):
    pygame.quit()
    sys.exit()

def keyboard(self, event_type):
    self.interact(event_type)

def mouse(self, event_type):
    self.mouse()