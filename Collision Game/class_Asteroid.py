import pygame as pg
import random as rd

class Asteroid(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 2
        self.max_health = 2
<<<<<<< HEAD
        self.velocity = 1
=======
        self.velocity = 0.1
>>>>>>> 08fb1eabc35aaf6a773ed0e3f2f3a098d7069293
        self.image = pg.image.load('data/asteroid.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0
        self.origin_image = self.image
        self.angle = 0

<<<<<<< HEAD
    def initialPosition(self):
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0

=======
>>>>>>> 08fb1eabc35aaf6a773ed0e3f2f3a098d7069293
    def rotate(self):
        self.angle += 12
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect)

    def move(self):
<<<<<<< HEAD
        self.rect.y += self.velocity
        self.rect.x += self.velocity
        self.rotate

=======
        self.rotate
        self.rect.y += self.velocity
        self.rect.x -= self.velocity
    
>>>>>>> 08fb1eabc35aaf6a773ed0e3f2f3a098d7069293
    def remove(self):
        self.asteroid.remove(self)
