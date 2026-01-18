import pygame, sys
from game import *
from keys import Keyboard

pygame.init()

GRAVITY = pygame.USEREVENT
VELOCITY = pygame.USEREVENT

pygame.time.set_timer(GRAVITY, 60)
pygame.time.set_timer(VELOCITY, 60)


def py_events(list_of_players = []):


    def quit():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    def keyboard(list_of_players):
        #k = Keyboard()

        def move_left(list_of_players):
            for player in list_of_players:
                player_id = player.id
                player_pos = player.get_player_position(player_id)
                player_size = (player.w, player.h)
                if player_pos[0] > 0:
                    player.player_body.x -= player.velocity


        def move_right(list_of_players):
            for player in list_of_players:
                player_id = player.id
                player_pos = player.get_player_position(player_id)
                player_size = (player.w, player.h)
                if player_pos[0] + player_size[0] < width:
                    player.player_body.x += player.velocity


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                move_left(list_of_players)

            #if event.key in Keyboard.get_key_pressed(event.key):
            #    
#
            #    #Registered
            #    if Keyboard.get_key_pressed(event.key)[1] == "a":
            #        #pygame.event.post(pygame.event.Event(VELOCITY))
            #        
            #        pressed = k.is_pressed(Keyboard.get_key_pressed(event.key)[1])
            #        k.pressed_keys[Keyboard.get_key_pressed(event.key)[1]] = pressed
#
            #        while pressed:
            #            move_left(list_of_players)
            #            pressed = k.is_pressed(Keyboard.get_key_pressed(event.key)[1])
            #            #if not k.pressed_keys[Keyboard.get_key_pressed(event.key)[1]]:
            #            #    break
            #            #pressed = Keyboard.is_pressed(Keyboard.get_key_pressed(event.key)[1])
            #            #print(pressed)
            #            #Keyboard.reset_pressed()
#
            #            #move_left(list_of_players)
            #            #velocity_left(list_of_players)
#
#
            #    if Keyboard.get_key_pressed(event.key)[1] == "s":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "d":
            #        move_right(list_of_players)
            #    if Keyboard.get_key_pressed(event.key)[1] == "w":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "space":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "enter":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "esc":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "arrow_up":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "arrow_down":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "arrow_right":
            #        return
            #    if Keyboard.get_key_pressed(event.key)[1] == "arrow_left":
            #        return
#
#
            #    # Not registered
            #    else:
            #        print(f"Key pressed: {Keyboard.get_key_pressed(event.key)}")


    def gravity(list_of_players):
        if event.type == GRAVITY:
            for player in list_of_players:
                player_id = player.id
                player_pos = player.get_player_position(player_id)
                player_size = (player.w, player.h)
                if player_pos[1] + player_size[1] <= player.ground.y - 10:
                    player.player_body.y += player.gravity
                    #player.player_body.y = player.ground.y
    
    def velocity_left(list_of_players):
        for player in list_of_players:
            player_id = player.id
            player_pos = player.get_player_position(player_id)
            player_size = (player.w, player.h)
            if player_pos[0] + player_size[0] < width:
                player.player_body.x -= player.velocity


    for event in pygame.event.get():
        quit()
        keyboard(list_of_players)

        if len(list_of_players) != 0:
            gravity(list_of_players)
            #if pygame.event.event_name(VELOCITY):
            #    velocity_left(list_of_players)
