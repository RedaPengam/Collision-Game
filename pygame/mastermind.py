import os, time, sys
import random as rd
import pygame as pg
from moviepy.editor import VideoFileClip
from pathlib import Path

##### game window #####

# Initialize the program & clock
pg.init()
clock = pg.time.Clock()
# title and icon
pg.display.set_caption('Oss Mastermind')
pg.display.set_icon(pg.image.load('data/dujardin32.jpg')) # 32*32 icon
# create the screen : top left O(0,0); (width=x_axis, height=y_axis)
#screen = pg.display.set_mode((1600, 900), pg.RESIZABLE)
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.toggle_fullscreen()
background = pg.image.load('data/play.png').convert()

#### constants ####

font = pg.font.SysFont("calibri.ttf", 32)
input_box = pg.Rect(820, 615, 200, 30)

# Filing rectangle color
color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('dodgerblue2')
color = color_inactive

click = False

#### game fonctions ####

def display_text(txt_instru, xtxt=400, ytxt=800):
    return screen.blit(font.render(txt_instru, True, (255, 255, 80)), (xtxt, ytxt))

def display_text2(txt_instru, xtxt=400, ytxt=800):
    return screen.blit(font.render(txt_instru, True, (0, 0, 0)), (xtxt, ytxt))

def play_sound(sound):
    return pg.mixer.Sound(sound).play()

def play_video(video):
    clip = VideoFileClip(video)
    clip.preview(fps=25)

#### game itself ####

def game():

    while True:
        screen.blit(background, (0, 0))
        display_text('Menu', 20, 20)
        mx, my = pg.mouse.get_pos()
        button = pg.Rect(520, 580, 200, 50)

        # if the user clicked on the play button, start a new game
        if button.collidepoint((mx, my)):
            if click:
                pg.mixer_music.stop()
                game()

        pg.draw.rect(screen, (0, 0, 0), button)
        display_text('Jouer', 590, 594)
        click = False

        for event in pg.event.get():
            # if the user clicked on the cross button, exit game
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                # if the user clicked on 'Space', play mission video
                if event.key == pg.K_SPACE:
                    play_video('data/mission.ts')
                # if the user clicked on 'Enter', start a new game
                if event.key == pg.K_RETURN:
                    pg.mixer_music.stop()
                    game()
                # if the user clicked on 'Echap', leave the game
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        clock.tick(60)

menu()
pg.quit()