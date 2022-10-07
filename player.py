import pygame as pg
from pygame.locals import *

from _functions import get_sprite_image

#graphics from https://opengameart.org/users/grafxkid

#プレイヤークラス
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        
        self.images = get_sprite_image("img/player.png", 6, 16, 13, 0)
        self.index = 0
        self.player_size = 25
        self.image = self.images[self.index]
        self.image = pg.transform.scale(self.image,(self.player_size,self.player_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = self.width // 2
        #向きの設定
        self.direction = True
        #移動速度の設定
        self.speed = 2
        #画像切り替え用のカウンター
        self.index_counter = 20
        #ゴールしているかのチェック
        self.goal = False

    #毎フレームの更新処理
    def update(self,data):
        #画像の更新処理
        self.index_counter -= 1
        if self.index_counter < 0:
            self.index += 1
            if self.index > len(self.images) - 1:
                self.index = 0
            self.image = self.images[self.index]
            self.image = pg.transform.scale(self.image,(self.player_size,self.player_size))
            #画像の左右の向きの設定
            if self.direction:
                self.image = pg.transform.flip(self.image,True,False)
            #画像切り替えのタイミング設定（nフレーム毎に切り替え）
            self.index_counter = 20

        #プレイヤーの移動距離
        dx = 0
        dy = 0

		#プレイヤーのキー操作
        key = pg.key.get_pressed()
        if key[K_a]:
            self.direction = False
            dx -= self.speed
        if key[K_d]:
            self.direction = True
            dx += self.speed
        if key[K_w]:
            dy -= self.speed
        if key[K_s]:
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
               
        # #ゴールした場合の処理
        # if self.goal:
        #     #killでグループから自身を削除
        #     self.kill()