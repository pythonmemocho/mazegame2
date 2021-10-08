import pygame as pg
from pygame.locals import *
from setting import *

#プレイヤークラス
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_SIZE,PLAYER_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.goal = False
                
    def update(self,data):
        #プレイヤーの移動距離
        dx = 0
        dy = 0

		#プレイヤーのキー操作
        key = pg.key.get_pressed()
        if key[K_LEFT]:
            dx -= 5
        if key[K_RIGHT]:
            dx += 5
        if key[K_UP]:
            dy -= 5
        if key[K_DOWN]:
            dy += 5

        #壁との接触判定
        for tile in data:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
        
        #移動速度を足す
        self.rect.x += dx
        self.rect.y += dy

        #ゴールした場合の処理
        if self.rect.left > WIDTH:
            self.kill()
            self.goal = True