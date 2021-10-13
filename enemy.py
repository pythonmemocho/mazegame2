import pygame as pg
from pygame.locals import *
from setting import *
import random


#敵クラス
class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/slime.png')
        self.image = pg.transform.scale(self.image,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+2,y+2]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.direction = self.change_direction()
        self.counter = 0
        
    def change_direction(self):
        return random.randint(0,4)

    def update(self,data):
        dx = 0
        dy = 0

        if self.counter % 80 == 0:
            self.direction = self.change_direction()
        
        if self.direction == 0:
            dx,dy = 0,0
        elif self.direction == 1:
            dy -= 5
        elif self.direction == 2:
            dx += 5
        elif self.direction == 3:
            dy += 5
        elif self.direction == 4:
            dx -= 5
        
        #壁との接触判定
        for tile in data:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        #移動速度を足す
        self.rect.x += dx
        self.rect.y += dy

        self.counter += 1