import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.image = pg.image.load('data/joueur1.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()