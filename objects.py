import pygame as pg
from pygame.locals import *
from setting import *

#オブジェクトクラス
class Goal(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_SIZE,PLAYER_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+2,y+2]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = 10
        self.counter = 0
                
    def update(self):
        pass