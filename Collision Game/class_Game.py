import pygame as pg
from class_Player import Player
from class_Asteroid import Asteroid

class Game:

    def __init__(self, screen):
        # création des fonds d'écran
        self.background = pg.image.load('data/background.jpg').convert() # creates the background picture variable that will be printed on the screen
        self.background = pg.transform.scale(self.background, (1280, 720))

        self.banner = pg.image.load('data/banner.png') # creates the banner that will be printed on the screen
        self.banner = pg.transform.scale(self.banner, (800,500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = screen.get_width()/5 -10

        self.gameover1_banner = pg.image.load('data/gameover1.png') # creates the banner that will be printed on the screen if the player 1 wins
        self.gameover1_banner = pg.transform.scale(self.gameover1_banner, (800,500))
        self.gameover1_banner_rect = self.gameover1_banner.get_rect()
        self.gameover1_banner_rect.x = screen.get_width()/5 -10

        self.gameover2_banner = pg.image.load('data/gameover2.png') # creates the banner that will be printed on the screen if the player 2 wins
        self.gameover2_banner = pg.transform.scale(self.gameover2_banner, (800,500))
        self.gameover2_banner_rect = self.gameover2_banner.get_rect()
        self.gameover2_banner_rect.x = screen.get_width()/5 -10

        # création du bouton play
        self.play_button = pg.image.load('data/button.png')
        self.play_button = pg.transform.scale(self.play_button, (200,100))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = screen.get_width()/2.5
        self.play_button_rect.y = screen.get_height()/1.2
        
        # création des joueurs
        self.all_players = pg.sprite.Group()
        self.player1 = Player(self)
        self.player2 = Player(self)
        self.all_players.add(self.player1)
        self.all_players.add(self.player2)

        # corrige la position initiale du joueur 2
        self.player2.rect.x = 1160
        self.player2.rect.y = 400
        self.player2.image = pg.image.load('data/joueur2.png')
        self.player2.image = pg.transform.scale(self.player2.image, (100, 70))

        # création des astéroïdes
        self.all_asteroids = pg.sprite.Group()
        self.asteroid1 = Asteroid(self)        
        self.asteroid2 = Asteroid(self)
        self.asteroid3 = Asteroid(self)        
        self.asteroid4 = Asteroid(self)
        self.all_asteroids.add(self.asteroid1, self.asteroid2, self.asteroid3, self.asteroid4)
        
        # création du dictionnaire des touches pressées en live
        self.pressed = {}

        # définit si le jeu est lancé ou non
        self.is_playing = False
    
    def check_collision (self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def ingame_screen(self, screen, Projectile):
        # affichage des sprites à l'écran
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

        # action du joueur 1 à l'enfoncement de ses touches de commande
        if self.pressed.get(pg.K_z) and self.player1.rect.y > 20 :
            self.player1.move_up()
            self.player1.update_health_bar(screen)      
        elif self.pressed.get(pg.K_s) and self.player1.rect.y < 630 :
            self.player1.move_down()            
            self.player1.update_health_bar(screen)
        
        # action du joueur 2 à l'enfoncement de ses touches de commande
        if self.pressed.get(pg.K_UP) and self.player2.rect.y > 20 :
            self.player2.move_up()
            self.player2.update_health_bar(screen)
        elif self.pressed.get(pg.K_DOWN) and self.player2.rect.y < 630 :
            self.player2.move_down()
            self.player2.update_health_bar(screen)

        # mise en mouvement des astéroïdes
        self.asteroid1.move1()
        self.asteroid1.rotate1()
        self.asteroid2.move2()
        self.asteroid2.rotate2()
        self.asteroid3.move1()
        self.asteroid3.rotate2()
        self.asteroid4.move2()
        self.asteroid4.rotate1()

    def menu_screen(self, screen):
        screen.blit(self.banner, self.banner_rect)
        screen.blit(self.play_button, self.play_button_rect)

    def gameover1_screen(self, screen, Projectile): 
        self.is_playing = False
        # affiche l'écran gameover1
        screen.blit(self.gameover1_banner, self.gameover1_banner_rect)
        screen.blit(self.play_button, self.play_button_rect)
        # retire tous les sprites de l'écran
        for projectile in self.player1.all_projectiles:
            Projectile.remove(projectile)
        for projectile in self.player2.all_projectiles:
            Projectile.remove(projectile)
        for asteroide in self.all_asteroids:
            Asteroid.remove(asteroide)

    def gameover2_screen(self, screen, Projectile):        
        self.is_playing = False        
        # affiche l'écran gameover2
        screen.blit(self.gameover2_banner, self.gameover2_banner_rect)
        screen.blit(self.play_button, self.play_button_rect)
        # retire tous les sprites de l'écran
        for projectile in self.player1.all_projectiles:
            Projectile.remove(projectile)
        for projectile in self.player2.all_projectiles:
            Projectile.remove(projectile)
        for asteroide in self.all_asteroids:
            Asteroid.remove(asteroide)