import pygame as pg
import random as rd

class Asteroid(pg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()      
        self.game = game
        self.health = 20
        self.max_health = 20
        self.dommage = 20
        self.velocity = 2
        #self.all_asteroids = pg.sprite.Group()
        self.image = pg.image.load('data/asteroid.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, 1280)
        self.rect.y = 0
        self.origin_image = self.image
        self.angle = 0
    
    def damage(self,amount):
        # infliger les dégats
        self.health-= amount
        
        if self.health <= 0 :
            self.initialPosition()
                 
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
        
        # verifier si l'asteroide entre en collision avec un joueur    
        for aste in self.game.check_collision(self, self.game.all_players):
                        
            # replacer l'asteroide
            self.initialPosition()
            
            # infliger des degats aux joueurs
            aste.damage(self.dommage)
            
    def move2(self):
        self.rect.y += rd.randint(2, 4)
        self.rect.x -= rd.randint(1, 3)
        # asteroid off screen       
        if (0 > self.rect.y or self.rect.y > 720) or (0 > self.rect.x or self.rect.x > 1280):
            self.initialPosition()
           
        # verifier si l'asteroide entre en collision avec un joueur    
        for aste in self.game.check_collision(self, self.game.all_players):
            
            # replacer l'asteroide
            self.initialPosition()
            
            # infliger des degats aux joueurs
            aste.damage(self.dommage)  
        
    def remove(self):
        self.game.all_asteroids.remove(self)
