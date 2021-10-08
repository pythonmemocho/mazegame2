import pygame as pg
from pygame.locals import *
from setting import *
import random


#敵クラス
class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_SIZE,PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        
    def update(self,data):
        dx = 0
        dy = 0
        direction = random.randint(1,4)
        if direction == 1:
            dy -= 5
        elif direction == 2:
            dx += 5
        elif direction == 3:
            dy += 5
        elif direction == 4:
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
