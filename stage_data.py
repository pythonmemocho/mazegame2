import pygame as pg
from pygame.locals import *
from player import Player 
from setting import *
from enemy import *
from objects import *

#ステージクラス       
class Stage():
	def __init__(self, data):
		self.enemySprite = pg.sprite.Group()
		self.keySprite = pg.sprite.Group()
		#空のリストを用意
		self.tile_list = []
		#のちに用意するstageの番号1を地面とし、リストに位置とサイズ情報を格納していく
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == "P":
					self.player = Player(col_count * CHIP_SIZE,row_count * CHIP_SIZE)
					self.playerSprite = pg.sprite.GroupSingle(self.player)
				if tile == 1:
					self.img = pg.image.load("img/aisle.png").convert_alpha()
					self.img = pg.transform.scale(self.img,(CHIP_SIZE,CHIP_SIZE))
					img_rect = self.img.get_rect()
					img_rect.x = col_count * CHIP_SIZE
					img_rect.y = row_count * CHIP_SIZE
					tile = (self.img, img_rect)
					self.tile_list.append(tile) 
				if tile == "E":
					self.enemy = Enemy(col_count * CHIP_SIZE,row_count * CHIP_SIZE)
					self.enemySprite.add(self.enemy)
				if tile == "G":
					self.goal = Goal(col_count * CHIP_SIZE,row_count * CHIP_SIZE)
					self.goalSprite = pg.sprite.GroupSingle(self.goal)
				if tile == "K":
					self.key = Key(col_count * CHIP_SIZE,row_count * CHIP_SIZE)
					self.keySprite.add(self.key)
				col_count += 1
			row_count += 1
        
		

	#上で得たリスト情報を元にスクリーンに描画する	
	def draw(self,screen):
		for tile in self.tile_list:
            #tile[0]には画像、tile[1]にはrectサイズの情報が入っている。
			screen.blit(tile[0],tile[1])
	
		
