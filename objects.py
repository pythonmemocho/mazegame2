import pygame as pg
from _setting import *

from _functions import image_load_and_scale_func
#graphics from https://opengameart.org/users/joe-williamson

class Goal(pg.sprite.Sprite):
    images = [
        image_load_and_scale_func("img\door_close.png", CHIP_SIZE,CHIP_SIZE),
        image_load_and_scale_func("img\door_open.png", CHIP_SIZE,CHIP_SIZE)
        ]
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.radius = 10
    
    def update(self):
        self.image = self.images[1]
        return self.image

#keyのクラス
class Key(pg.sprite.Sprite):
    key_image = image_load_and_scale_func('img/key.png',CHIP_SIZE,CHIP_SIZE)
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = self.key_image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = 10
        
