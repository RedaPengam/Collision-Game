import pygame as pg
import random as rd
class Asteroid(pg.sprite.Sprite):

    def __init__(self, class_Player):
        super().__init__()
        self.class_Player = class_Player
        self.health = 2
        self.max_health = 2
        self.damage = 10
        self.velocity = 2
        self.image = pg.image.load('data/asteroid.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0
        self.origin_image = self.image
        self.angle = 0
    
    def damage(self,amount):
        #infliger les dégats
        self.health-= amount
        # if self.health <= 0 :
        #     self.remove()

    def initialPosition(self):
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0

    def rotate1(self):
        self.angle += rd.randint(1, 5)
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def rotate2(self):
        self.angle -= rd.randint(5, 10)
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def move1(self):
        self.rect.y += rd.randint(2, 4)
        self.rect.x += rd.randint(1, 3)
        # asteroid off screen
        if (0 > self.rect.y or self.rect.y > 720) or (0 > self.rect.x or self.rect.x > 1280):
            self.initialPosition()
            
        # # verifier si l'asteroid entre en collision avec un joueur    
        # for player in self.class_Player.game.check_collision(self, self.class_Player.game.all_players):
            
        #     #suprimer l'asteroid
        #     self.remove()
            
        #     #infliger des degats aux joueurs
        #     player.damage(self.damage)
            
    def move2(self):
        self.rect.y += rd.randint(2, 4)
        self.rect.x -= rd.randint(1, 3)
        # asteroid off screen       
        if (0 > self.rect.y or self.rect.y > 720) or (0 > self.rect.x or self.rect.x > 1280):
            self.initialPosition()

    def remove(self):
        self.asteroid.remove(self)
