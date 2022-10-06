import pygame as pg
from pygame.locals import *
from _setting import *

#graphics from https://opengameart.org/users/joe-williamson

#goal(door)のクラス
class Goal(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.images = ["img\door_close.png","img\door_open.png"]
        self.image = pg.image.load(self.images[0])
        self.image = pg.transform.scale(self.image,(CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = 10
    
    def update(self):
        self.image = pg.image.load(self.images[1])
        self.image = pg.transform.scale(self.image,(CHIP_SIZE,CHIP_SIZE))
                
            
#keyのクラス
class Key(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/key.png')
        self.image = pg.transform.scale(self.image,(CHIP_SIZE,CHIP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = 10
        self.get_all_keys = False
        
