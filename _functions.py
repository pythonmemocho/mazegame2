import pygame as pg

import _setting

#sprite_sheetから画像を取り出す関数
def get_sprite_image(sheet,count,width,height,y):
    sprite_sheet = pg.image.load(sheet)
    sheet_width = sprite_sheet.get_width()
    image_size = int(sheet_width / count)
    images = []
    for i in range(count):
        images.append(sprite_sheet.subsurface((image_size * i, y, width, height)))
    return images


#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		_setting.SCREEN.blit(text_surface,text_rect)

def image_load_and_scale_func(img, scale_x, scale_y):
    img = pg.image.load(img).convert_alpha()
    img = pg.transform.scale(img, (scale_x, scale_y))
    return img