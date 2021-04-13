import pygame as pg
import sys, time
from class_Player import Player
from class_Game import Game
from class_Asteroid import Asteroid
from class_Projectile import Projectile

pg.init()
clock = pg.time.Clock()

# Création de la fenêtre et de l'écran
pg.display.set_caption('Collision Game') # labels the window
pg.display.set_icon(pg.image.load('data/icon.png')) # creates the icon for the window (has to be 32*32 px)

screen = pg.display.set_mode((1280, 720), pg.RESIZABLE) # creates the screen : top left O(0,0); (width=x_axis, height=y_axis)

# loads the game class
game = Game(screen)

while True:
    # Affiche le fond d'écran pour l'écran
    screen.blit(game.background, (0, 0))
        
    # Affiche l'écran de jeu si en jeu
    if game.is_playing :
        game.ingame_screen(screen, Projectile)
    # Affiche l'écran de menu sinon
    else :
        game.menu_screen(screen)
    # Affiche l'écran Game Over 2 si le joueur 2 meurt
    if game.player2.health <= 0:
        game.gameover2_screen(screen, Projectile)
    # Affiche l'écran Game Over 1 si le joueur 1 meurt
    elif game.player1.health <= 0:
        game.gameover1_screen(screen, Projectile)
        
    # refreshes the screen
    pg.display.update()
    clock.tick(60) # fps

    # looks for key pressed every 1/fps sec
    for event in pg.event.get():
        # if the player hits the cross window button
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            print("Quitting game")

        # detects if the player hit a key from the mouse
        elif event.type == pg.MOUSEBUTTONDOWN:
            # if the mouse is on the play button 
            if game.play_button_rect.collidepoint(event.pos) :
                # starts the game
                game.is_playing = True
            
            elif game.replay_button_rect.collidepoint(event.pos) :
                game.player1.rect.y = 320 
                game.player1.health = game.player1.health.max_health 
                game.player1.rect.y = 320 
                game.player1.health = game.player1.health.max_health

        # detects if the player hit a key from the keyboard
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True
            
            if event.key == pg.K_SPACE:
                game.player1.launch_projectile1()
                
            if event.key == pg.K_RETURN:
                game.player2.launch_projectile2()
        
        # detects if the player releases a key from the keyboard
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
    