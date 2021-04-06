import pygame as pg

class Joueur:

    def __init__(pg.sprite.Sprite):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 5