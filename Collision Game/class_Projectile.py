#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:23:16 2021

@author: maxinegravier
"""
import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self,class_Player):
        super().__init__()
        self.class_Player=class_Player
        self.velocity =5
        self.image=pg.image.load('data/laser.png')
        self.image=pg.transform.scale(self.image, (50,50))
        self.rect=self.image.get_rect()
        self.rect.x=class_Player.rect.x
        self.rect.y=class_Player.rect.y
    
    def remove(self):
        self.class_Player.all_projectiles.remove(self)
        
    def move(self):
        #on fait se déplacer le projectile
        self.rect.x +=self.velocity
        #le projectile sort de l'écran: on le supprime
        if self.rect.x>1080:
            self.remove()
