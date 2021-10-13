import pygame as pg
from pygame.locals import *
from setting import *

#オブジェクトクラス
class Goal(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/castledoors.png')
        self.image = pg.transform.scale(self.image,(CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = 10
        self.counter = 0
                
    def update(self):
        pass

class Key(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/key.png')
        self.image = pg.transform.scale(self.image,(CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+2,y+2]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    

