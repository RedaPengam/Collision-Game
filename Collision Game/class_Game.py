import pygame as pg
from class_Player import Player
from class_Asteroid import Asteroid

class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
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
        self.all_asteroids = pg.sprite.Group()
        self.asteroid1 = Asteroid(self)        
        self.asteroid2 = Asteroid(self)
        self.asteroid3 = Asteroid(self)        
        self.asteroid4 = Asteroid(self)
        self.all_asteroids.add(self.asteroid1, self.asteroid2, self.asteroid3, self.asteroid4)
    
    def check_collision (self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def update(self, screen, Projectile):
        # applies sprites
        screen.blit(self.player1.image, self.player1.rect)
        screen.blit(self.player2.image, self.player2.rect)
        screen.blit(self.asteroid1.image, self.asteroid1.rect)
        screen.blit(self.asteroid2.image, self.asteroid2.rect)
        screen.blit(self.asteroid3.image, self.asteroid3.rect)
        screen.blit(self.asteroid4.image, self.asteroid4.rect)
        self.player1.all_projectiles.draw(screen)
        self.player2.all_projectiles.draw(screen)

        # actualisation de la barre de vie des deux joueurs
        self.player1.update_health_bar(screen)
        self.player2.update_health_bar(screen)
            
        # déplacement des projectiles
        for projectile in self.player1.all_projectiles:
            Projectile.move1(projectile)
        for projectile in self.player2.all_projectiles:
            Projectile.move2(projectile)

        # player1 actions if key pressed
        if self.pressed.get(pg.K_z) and self.player1.rect.y > 20 :
            self.player1.move_up()            
        elif self.pressed.get(pg.K_s) and self.player1.rect.y < 630 :
            self.player1.move_down()
        
        # player2 actions if key pressed
        if self.pressed.get(pg.K_UP) and self.player2.rect.y > 20 :
            self.player2.move_up()
            self.player2.update_health_bar(screen)
        elif self.pressed.get(pg.K_DOWN) and self.player2.rect.y < 630 :
            self.player2.move_down()
            self.player2.update_health_bar(screen)
            
        # asteroids actions
        self.asteroid1.move1()
        self.asteroid1.rotate1()
        self.asteroid2.move2()
        self.asteroid2.rotate2()
        self.asteroid3.move1()
        self.asteroid3.rotate2()
        self.asteroid4.move2()
        self.asteroid4.rotate1()



