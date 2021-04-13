import pygame as pg
import sys, time
from class_Player import Player
from class_Game import Game
from class_Asteroid import Asteroid
from class_Projectile import Projectile

pg.init()
clock = pg.time.Clock()

# window and screen
pg.display.set_caption('Collision Game') # labels the window
pg.display.set_icon(pg.image.load('data/icon.png')) # creates the icon for the window (has to be 32*32 px)

screen = pg.display.set_mode((1280, 720), pg.RESIZABLE) # creates the screen : top left O(0,0); (width=x_axis, height=y_axis)

background = pg.image.load('data/background.jpg').convert() # creates the background picture variable that will be printed on the screen
background = pg.transform.scale(background, (1280, 720))

banner = pg.image.load('data/banner.png') # creates the banner that will be printed on the screen
banner = pg.transform.scale(banner, (800,500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/5 -10

play_button = pg.image.load('data/button.png')
play_button = pg.transform.scale(play_button, (200,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()/2.5
play_button_rect.y = screen.get_height()/1.2

replay_button = pg.image.load('data/button.png')
replay_button = pg.transform.scale(replay_button, (200,100))
replay_button_rect = replay_button.get_rect()
replay_button_rect.x = screen.get_width()/2.5
replay_button_rect.y = screen.get_height()/1.2

gameover1_banner = pg.image.load('data/gameover1.png') # creates the banner that will be printed on the screen if the player 1 wins
gameover1_banner = pg.transform.scale(gameover1_banner, (800,500))
gameover1_banner_rect = gameover1_banner.get_rect()
gameover1_banner_rect.x = screen.get_width()/5 -10

gameover2_banner = pg.image.load('data/gameover2.png') # creates the banner that will be printed on the screen if the player 2 wins
gameover2_banner = pg.transform.scale(gameover2_banner, (800,500))
gameover2_banner_rect = gameover2_banner.get_rect()
gameover2_banner_rect.x = screen.get_width()/5 -10

# loads the game class
game = Game()

while True:
    # applies the background
    screen.blit(background, (0, 0))
    
    # checks if the game started
    if game.is_playing:
        game.update(screen, Projectile)
    # checks if the game hasn't start yet
    else :
        # add the welcome screen
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # checks if player2 is dead
    if game.player2.health <= 0:
        game.is_playing = False
        screen.blit(gameover1_banner, gameover1_banner_rect)
        screen.blit(replay_button, replay_button_rect)
        for projectile in game.player1.all_projectiles:
            Projectile.remove(projectile)
        for projectile in game.player2.all_projectiles:
            Projectile.remove(projectile)
        for asteroide in game.all_asteroids:
            Asteroid.remove(asteroide)
    
    # checks if player1 is dead
    elif game.player1.health <= 0:
        game.is_playing = False
        screen.blit(gameover2_banner, gameover2_banner_rect)
        screen.blit(replay_button, replay_button_rect)
        for projectile in game.player1.all_projectiles:
            Projectile.remove(projectile)
        for projectile in game.player2.all_projectiles:
            Projectile.remove(projectile)
        for asteroide in game.all_asteroids:
            Asteroid.remove(asteroide)
        
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
            if play_button_rect.collidepoint(event.pos) :
                # starts the game
                game.is_playing = True
            
            elif replay_button_rect.collidepoint(event.pos) :
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
    