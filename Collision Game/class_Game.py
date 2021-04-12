import pygame as pg
from class_Player import Player
from class_Asteroid import Asteroid

class Game:

    def __init__(self):
        # players creation
        self.all_players = pg.sprite.Group()
        self.player1 = Player(self)
        self.player2 = Player(self)
        self.all_players.add(self.player1)
        self.all_players.add(self.player2)
        # corrects the player2 initial position
        self.player2.rect.x = 1160
        self.player2.rect.y = 400
        self.player2.image = pg.image.load('data/joueur2.png')
        self.player2.image = pg.transform.scale(self.player2.image, (100, 70))
        # keys currently pressed
        self.pressed = {}
        # asteroids creation
        self.all_asteroids =pg.sprite.Group()
        self.asteroid1 = Asteroid(self)        
        self.asteroid2 = Asteroid(self)
        self.asteroid3 = Asteroid(self)        
        self.asteroid4 = Asteroid(self)
        self.all_asteroids.add(self.asteroid1, self.asteroid2, self.asteroid3, self.asteroid4)
    
    def check_collision (self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)




