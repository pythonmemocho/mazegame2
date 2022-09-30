import pygame as pg
# from pygame.locals import *
# from setting import *

import random


#Enemyクラス
class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.images = self.get_sprite_image("img/enemy.png", 6, 16, 16, 0)
        self.enemy_size = 30
        self.index = 0
        self.image = self.images[self.index]
        self.image = pg.transform.scale(self.image,(self.enemy_size,self.enemy_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width // 2
        #カウントUP用の変数
        self.counter = 0
        #進行方向設定
        self.direction = self.change_direction()
        #移動速度
        self.speed = 1
        #画像切り替え用のカウンター
        self.index_counter = 20
        #画像の向き設定用の変数
        self.img_direction = True

    #sprite_sheetから画像を取り出すメソッド
    def get_sprite_image(self,sheet,count,width,height,y):
        sprite_sheet = pg.image.load(sheet)
        sheet_width = sprite_sheet.get_width()
        image_size = int(sheet_width / count)
        images = []
        for i in range(count):
            images.append(sprite_sheet.subsurface((image_size * i, y, width, height)))
        return images    
      
    #ランダムで進行方向を変える処理    
    def change_direction(self):
        return random.randint(1,4)

    #毎フレームの更新処理
    def update(self,data):
        #画像の更新処理
        self.index_counter -= 1
        if self.index_counter < 0:
            self.index += 1
            if self.index > len(self.images) - 1:
                self.index = 0
            self.image = self.images[self.index]
            self.image = pg.transform.scale(self.image,(self.enemy_size,self.enemy_size))
            #画像の左右の向きの設定
            if self.img_direction:
                self.image = pg.transform.flip(self.image,True,False)
            #画像切り替えのタイミング設定（nフレーム毎に切り替え）
            self.index_counter = 20

        #移動距離初期化
        dx = 0
        dy = 0

        #nカウントが n毎 に進行方向変える
        if self.counter % 90 == 0:
            self.direction = self.change_direction()
        
        #各数値に該当する向きへ速度をプラスする
        if self.direction == 0:
            dx, dy = 0, 0
        elif self.direction == 1:
            dy -= self.speed
        elif self.direction == 2:
            self.img_direction = True
            dx += self.speed
        elif self.direction == 3:
            dy += self.speed
        elif self.direction == 4:
            self.img_direction = False
            dx -= self.speed
        
        #壁との接触判定
        for tile in data:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        #移動速度を足す
        self.rect.x += dx
        self.rect.y += dy

        #カウントUPさせる
        self.counter += 1