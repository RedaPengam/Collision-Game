import os, time, sys
import random as rd
import pygame as pg
from pathlib import Path
from class_Player import Player
from class_Game import Game

##### path #####

L = str(__file__) # gets the full path & the name of the current file (.../mastermind.py)
print(L[0:-13]) # L[0:-13] ONLY gets the full path of the current file (.../)
#os.chdir(L[0:-13])

##### game window #####

# Initialize the program & clock

pg.init()
clock = pg.time.Clock()

# window and screen

pg.display.set_caption('Collision Game') # labels the window
pg.display.set_icon(pg.image.load('data/icon.png')) # creates the icon for the window (has to be 32*32 px)

screen = pg.display.set_mode((1280, 720), pg.RESIZABLE) # creates the screen : top left O(0,0); (width=x_axis, height=y_axis)

background = pg.image.load('data/background.jpg').convert() # creates the background picture variable that will be printed on the screen
background = pg.transform.scale(background, (1280, 720))

# charger notre jeu
game = Game()

#### constants ####

font = pg.font.SysFont("calibri.ttf", 32)
input_box = pg.Rect(820, 615, 200, 30)

color_inactive = pg.Color('lightskyblue3') # Filing rectangle color
color_active = pg.Color('dodgerblue2')
color = color_inactive

xtxt = 100
ytxt = 100

click = False

#### game fonctions ####

def display_text(txt_instru, xtxt=400, ytxt=800):
    return screen.blit(font.render(txt_instru, True, (150, 2, 76)), (xtxt, ytxt))

def display_text2(txt_instru, xtxt=400, ytxt=800):
    return screen.blit(font.render(txt_instru, True, (0, 0, 0)), (xtxt, ytxt))

def play_sound(sound):
    return pg.mixer.Sound(sound).play()

#### game itself ####

while True:
    # GUI
    screen.blit(background, (0, 0)) # prints the background
    display_text('Game', 20, 20) # prints text info
    mx, my = pg.mouse.get_pos() # gets mouse position
    button = pg.Rect(520, 580, 200, 50) # draws a button

    # sprites positioning
    screen.blit(Player().image, Player().rect)

    for event in pg.event.get():
        # if the user clicked on the cross button, exit game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

            # if the user clicked on 'Echap', leave the game
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pg.display.update()
    clock.tick(60)



