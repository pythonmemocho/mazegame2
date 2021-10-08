import pygame as pg
from pygame.locals import * 
from setting import *
from enemy import *

#ステージクラス       
class Stage():
	def __init__(self, data):
		#空のリストを用意
		self.tile_list = []
		#のちに用意するstageの番号1を地面とし、リストに位置とサイズ情報を格納していく
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					self.img = pg.image.load("img/aisle.png").convert_alpha()
					img_rect = self.img.get_rect()
					img_rect.x = col_count * CHIP_SIZE
					img_rect.y = row_count * CHIP_SIZE
					tile = (self.img, img_rect)
					self.tile_list.append(tile) 
				if tile == 2:
					self.enemy = Enemy(col_count * CHIP_SIZE,row_count * CHIP_SIZE) 
					
					
				col_count += 1
			row_count += 1
        
	#上で得たリスト情報を元にスクリーンに描画する	
	def draw(self,screen):
		for tile in self.tile_list:
            #tile[0]には画像、tile[1]にはrectサイズの情報が入っている。
			screen.blit(tile[0],tile[1])
	
		
