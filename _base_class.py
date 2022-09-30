import pygame as pg
from os import path

class BaseClass(pg.sprite.Sprite):
    _file_dir = path.dirname(__file__)
    _img_dir = path.join(_file_dir,'img')
       
    def __init__(self, pos_x, pos_y,_img_dir,img_ind):
        pg.sprite.Sprite.__init__(self)
        self._image_sprite = [
            path.join(_img_dir, 'player.png'),
            path.join(_img_dir, 'enemy.png'),
            path.join(_img_dir, 'key.png'),
            path.join(_img_dir, 'door_close.png'),
            path.join(_img_dir, 'door_open.png')
        ]
        self.img_ind = img_ind

        

    #sprite_sheetから画像を取り出すメソッド
    def get_sprite_image(self,count,width,height,y):
        sprite_sheet = pg.image.load(self._image_sprite[self.img_ind]).convert_alpha()
        sheet_width = sprite_sheet.get_width()
        image_size = int(sheet_width / count)
        images = [sprite_sheet.subsurface((image_size * i, y, width, height)) \
            for i in range(count)]
        return images