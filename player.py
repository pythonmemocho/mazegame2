import pygame as pg
from pygame.locals import *
from setting import *

#プレイヤークラス
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        
        self.image = self.get_sprite_image(PLAYER_SIZE,PLAYER_SIZE,"img/enemy.png",x,y)
        # self.image = pg.image.load('img/left-0.png').convert_alpha()
        self.image = pg.transform.scale(self.image,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = 10
        self.goal = False
        self.speed = 3

    def get_sprite_image(self,width,height,sheet,x,y):
        img = pg.Surface((width,height)).convert_alpha()
        data = pg.image.load(sheet)
        img.blit(data,(x,y))
        return img

    def update(self,data):
        #プレイヤーの移動距離
        dx = 0
        dy = 0

		#プレイヤーのキー操作
        key = pg.key.get_pressed()
        if key[K_LEFT]:
            dx -= self.speed
        if key[K_RIGHT]:
            dx += self.speed
        if key[K_UP]:
            dy -= self.speed
        if key[K_DOWN]:
            dy += self.speed

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
        if self.goal:
            self.kill()