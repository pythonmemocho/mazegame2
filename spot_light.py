import pygame as pg
from pygame.locals import *
from _setting import *

class Spot_light:
    def __init__(self) -> None:
        self.surface = pg.Surface((WIDTH,HEIGHT))
        self.surface.set_colorkey(WHITE)
        self.surface.set_alpha(240)

    def draw(self,player_rect):
        SCREEN.blit(self.surface,(0,0))
        pg.draw.rect(self.surface,(BLACK),(0,0,WIDTH,HEIGHT))
        pg.draw.circle(self.surface,(WHITE),(player_rect[0],player_rect[1]),100)


