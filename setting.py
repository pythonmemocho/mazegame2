import pygame as pg

#画面サイズの設定
WIDTH  =  570
HEIGHT =  570

#１マスのサイズ設定
CHIP_SIZE = 30 

#FPS設定
CLOCK = pg.time.Clock()
FPS = 60

SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Maze_Game')

#使いそうな色の設定
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GRAY = (210,210,210)
ORANGE = (255,165,0)

#keyの個数の設定
number_of_keys = 5

#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		SCREEN.blit(text_surface,text_rect)