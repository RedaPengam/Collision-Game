import pygame as pg
import random as rd

class Asteroid(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 2
        self.max_health = 2
        self.velocity = 2
        self.image = pg.image.load('data/asteroid.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0
        self.origin_image = self.image
        self.angle = 0

    def initialPosition(self):
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0

    def rotate(self):
        self.angle += 12
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def move1(self):
        self.rect.y += self.velocity
        self.rect.x += self.velocity
        # asteroid off screen
        if (0 > self.rect.y or self.rect.y > 720) or (0 > self.rect.x or self.rect.x > 1280):
            self.initialPosition()

    def move2(self):
        self.rect.y += self.velocity
        self.rect.x -= self.velocity
        # asteroid off screen       
        if (0 > self.rect.y or self.rect.y > 720) or (0 > self.rect.x or self.rect.x > 1280):
            self.initialPosition()

    def remove(self):
        self.asteroid.remove(self)
