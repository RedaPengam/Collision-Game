import pygame as pg
from class_Player import Player
from class_Asteroid import Asteroid

class Game:

    def __init__(self):
        # players creation
        self.player1 = Player()
        self.player2 = Player()
        # corrects the player2 initial position
        self.player2.rect.x = 1160
        self.player2.rect.y = 520
        self.player2.image = pg.image.load('data/joueur2.png')
        self.player2.image = pg.transform.scale(self.player2.image, (100, 70)) 
        # keys currently pressed
        self.pressed = {}
        # asteroids creation
        self.asteroid1 = Asteroid()        
        self.asteroid2 = Asteroid()
        self.asteroid3 = Asteroid()        
        self.asteroid4 = Asteroid()





