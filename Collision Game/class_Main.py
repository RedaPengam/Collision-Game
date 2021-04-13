import pygame as pg
import sys, time
from class_Player import Player
from class_Game import Game
from class_Asteroid import Asteroid
from class_Projectile import Projectile

pg.init()
clock = pg.time.Clock()

# création de la fenêtre et de l'écran
pg.display.set_caption('Collision Game') # nomme la fenêtre
pg.display.set_icon(pg.image.load('data/icon.png')) # crée une icône pour la fenêtre

screen = pg.display.set_mode((1280, 720), pg.RESIZABLE) # crée l'écran avec la taille en pixel

# crée une instance de jeu 
game = Game(screen)

while True:
    # affiche le fond d'écran
    screen.blit(game.background, (0, 0))  
    # affiche l'écran de jeu si le jeu est lancé
    if game.is_playing :
        game.ingame_screen(screen, Projectile)
    # affiche l'écran de menu sinon
    else :
        game.menu_screen(screen)
    # affiche l'écran gameover2 si le joueur 2 meurt
    if game.player2.health <= 0:
        game.gameover2_screen(screen, Projectile)
    # affiche l'écran gameover1 si le joueur 1 meurt
    elif game.player1.health <= 0:
        game.gameover1_screen(screen, Projectile)
        
    # rafraichit l'écran à 60 fps
    pg.display.update()
    clock.tick(60) # fps

    # boucle d'évènements clavier
    for event in pg.event.get():
        # action au touché de la croix de fenêtre
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            print("Quitting game")

        # actions au clic de la souris
        elif event.type == pg.MOUSEBUTTONDOWN:
            # si on clique sur le bouton play, lancement du jeu
            if game.play_button_rect.collidepoint(event.pos):
                game.is_playing = True
                # réinitialise la vie et la position des joueurs         
                game.player1.rect.y = 320 
                game.player1.health = game.player1.max_health 
                game.player1.rect.y = 320 
                game.player1.health = game.player1.max_health

        # actions à l'enfoncement d'une touche clavier
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True
            # touche espace : tir du joueur 1
            if event.key == pg.K_SPACE:
                game.player1.launch_projectile1()
            # touche entrée : tir du joueur 2
            if event.key == pg.K_RETURN:
                game.player2.launch_projectile2()
        
        # actions au relachement d'une touche clavier
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
    