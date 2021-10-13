import pygame as pg

# WIDTH  =  475
# HEIGHT =  475 
WIDTH  =  625
HEIGHT =  625

CHIP_SIZE = 25 
PLAYER_SIZE = 20
CLOCK = pg.time.Clock()
FPS = 60

SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('MAZE')
    
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)


#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		SCREEN.blit(text_surface,text_rect)