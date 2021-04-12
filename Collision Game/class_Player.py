import pygame as pg
from class_Projectile import Projectile

class Player(pg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 6
        self.all_projectiles = pg.sprite.Group()
        self.image = pg.image.load('data/joueur1.png')
        self.image = pg.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 320
        
    def damage(self,amount):
        # infliger les dégats
        self.health -= amount
        
        # vérifier qu'il lui reste des points de vie 
        if self.health <= 0:
            # réappatraitre comme un nouveau monstre 
            self.rect.y = 320 
            self.health = self.max_health 
    
    def update_health_bar (self, surface):
        # definir une couleur pour notre jauge de vie 
        bar_color = (111, 210, 46)
        
        # definir couleur barre arrière plan 
        back_bar_color = (60, 63, 60)
        
        # definir la position de la jauge de vie sa largeur et son épaisseur
        bar_position = [self.rect.x , self.rect.y-20 , self.health, 5]
        
        # definir la position de la jauge de vie d'arrière plan sa largeur et son épaisseur
        back_bar_position = [self.rect.x , self.rect.y-20 , self.max_health, 5]
        
        # dessiner la barre de vie
        pg.draw.rect(surface, back_bar_color, back_bar_position)
        pg.draw.rect(surface, bar_color, bar_position)
    
    def launch_projectile1(self): 
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def launch_projectile2(self):
        projectile = Projectile(self)
        projectile.rect.x = self.rect.x - 50
        self.all_projectiles.add(projectile)
        projectile.image =pg.image.load('data/laser2.png')
        projectile.image = pg.transform.scale(projectile.image, (50, 50))

    def move_up(self):
        self.rect.y -= self.velocity 

    def move_down(self):
        self.rect.y += self.velocity
       
