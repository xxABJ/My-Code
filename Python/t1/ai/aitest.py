import pygame
import random

pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set display dimensions
dis_width = 800
dis_height = 600

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('2D Platformer by GitHub Copilot')

clock = pygame.time.Clock()
player_size = 50
player_speed = 5
gravity = 1
jump_strength = 15

font_style = pygame.font.SysFont(None, 50)

# Load images
background_img = pygame.image.load('background.png')
player_img = pygame.image.load('player.png')
platform_img = pygame.image.load('platform.png')

class Player:
    def __init__(self):
        self.rect = pygame.Rect(dis_width // 2, dis_height - player_size, player_size, player_size)
        self.image = pygame.transform.scale(player_img, (player_size, player_size))
        self.vel_y = 0
        self.jumping = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def apply_gravity(self):
        self.vel_y += gravity
        self.rect.y += self.vel_y

    def jump(self):
        if not self.jumping:
            self.vel_y = -jump_strength
            self.jumping = True

    def draw(self):
        dis.blit(self.image, self.rect.topleft)

    def check_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > dis_width:
            self.rect.right = dis_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > dis_height:
            self.rect.bottom = dis_height
            self.vel_y = 0
            self.jumping = False

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(platform_img, (width, height))

    def draw(self):
        dis.blit(self.image, self.rect.topleft)

def generate_platforms(level):
    platforms = []
    platform_count = 5 + level  # Increase the number of platforms with each level
    for i in range(platform_count):
        x = random.randint(0, dis_width - 200)
        y = dis_height - (i * 100) - 50
        platforms.append(Platform(x, y, 200, 10))
    return platforms

def gameLoop():
    game_over = False
    level = 1

    player = Player()
    platforms = generate_platforms(level)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player_speed, 0)
        if keys[pygame.K_RIGHT]:
            player.move(player_speed, 0)

        player.apply_gravity()
        player.check_boundaries()

        for platform in platforms:
            if player.rect.colliderect(platform.rect) and player.vel_y > 0:
                player.rect.bottom = platform.rect.top
                player.vel_y = 0
                player.jumping = False

        dis.blit(background_img, (0, 0))
        player.draw()
        for platform in platforms:
            platform.draw()
        pygame.display.update()

        # Check if player reached the top of the screen to advance to the next level
        if player.rect.top <= 0:
            level += 1
            platforms = generate_platforms(level)
            player.rect.topleft = (dis_width // 2, dis_height - player_size)
            player.vel_y = 0
            player.jumping = False

        clock.tick(30)

    pygame.quit()
    quit()

gameLoop()
