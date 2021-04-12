import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self,class_Player):
        super().__init__()
        
        self.class_Player = class_Player
        self.velocity = 5
        self.image = pg.image.load('data/laser.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = class_Player.rect.x + 100
        self.rect.y = class_Player.rect.y
    
    def remove (self):
        self.class_Player.all_projectiles.remove(self)
    
    def move1(self):
        # on fait se déplacer le projectile
        self.rect.x += self.velocity
        
        # verifier si le projectile entre en collision avec un joueur
        for player in self.class_Player.game.check_collision(self, self.class_Player.game.all_players):
            # supprimer le projectile
            self.remove()
            
            # infliger des dégats aux joueurs 
            player.damage(self.class_Player.attack)
            
        for asteroid in self.class_Player.game.check_collision(self, self.class_Player.game.all_asteroids):
            # supprimer le projectile
            self.remove()
            
            # infliger des dégats aux asteroids
            # asteroid.damage(self.class_Player.attack)
            
        # le projectile sort de l'écran : on le supprime
        if self.rect.x > 1280 :
            self.remove()
                   
    def move2(self):
        # on fait se déplacer le projectile
        self.rect.x -= self.velocity
        # le projectile sort de l'écran: on le supprime
        if self.rect.x < -50:
            self.remove()
            
        # verifier si le projectile entre en collision avec un joueur
        for player in self.class_Player.game.check_collision(self, self.class_Player.game.all_players):
            # supprimer le projectile
            self.remove()
            
            # infliger des dégats aux joueurs 
            player.damage(self.class_Player.attack)
            
        for asteroid in self.class_Player.game.check_collision(self, self.class_Player.game.all_asteroids):
            # supprimer le projectile
            self.remove()
            
            # infliger des dégats aux asteroids
            # asteroid.damage(self.class_Player.attack)
            
        # le projectile sort de l'écran : on le supprime
        if self.rect.x > 1280 :
            self.remove()
