import pygame as pg
import sys
from class_Player import Player
from class_Game import Game
from class_Asteroid import Asteroid
from class_Projectile import Projectile

pg.init()

# window and screen
pg.display.set_caption('Collision Game') # labels the window
pg.display.set_icon(pg.image.load('data/icon.png')) # creates the icon for the window (has to be 32*32 px)
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE) # creates the screen : top left O(0,0); (width=x_axis, height=y_axis)
background = pg.image.load('data/background.jpg').convert() # creates the background picture variable that will be printed on the screen
background = pg.transform.scale(background, (1280, 720))

# loads the game class
game = Game()

# for later if we use the mouse
click = False

gameIsOn = True
while gameIsOn:
    # applies the background
    screen.blit(background, (0, 0))
    
    # applies sprites
    screen.blit(game.player1.image, game.player1.rect)
    screen.blit(game.player2.image, game.player2.rect)
    screen.blit(game.asteroid.image, game.asteroid.rect)

    # refreshes the screen
    pg.display.flip()

    # ATTENTION A CODER EN QWERTY POUR DE L'AZERTY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # player1 actions if key pressed
    if game.pressed.get(pg.K_w) and game.player1.rect.y > 20 :
        game.player1.move_up()
    elif game.pressed.get(pg.K_s) and game.player1.rect.y < 630 :
        game.player1.move_down()
    
    # player2 actions if key pressed
    if game.pressed.get(pg.K_UP) and game.player2.rect.y > 20 :
        game.player2.move_up()
    elif game.pressed.get(pg.K_DOWN) and game.player2.rect.y < 630 :
        game.player2.move_down()

    # asteroid actions
    game.asteroid.move()
    # asteroid off screen
    if (0 > game.asteroid.rect.y or game.asteroid.rect.y > 720) or (0 > game.asteroid.rect.x or game.asteroid.rect.x > 1280):
        game.asteroid.initialPosition()
    
    # looks for key pressed every 1/60 sec
    for event in pg.event.get():
        # if the player hits the cross window button
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            print("Quitting game")

        # detects if the player hit a key from the mouse
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

        #  detects if the player hit a key from the keyboard
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
    




