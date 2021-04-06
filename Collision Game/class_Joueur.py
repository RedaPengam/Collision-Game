import pygame as pg

class Joueur(pg.sprite.Sprite):

    def __init__(self, numero):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.numero = numero
        self.image = pg.image.load('data/joueur{}.png'.format(self.numero))
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
