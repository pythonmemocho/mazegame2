import pygame as pg
from pygame.locals import *
from setting import *

class Title:
    def __init__(self) -> None:
        SCREEN.fill(BLACK)
        draw_text(f'press ENTER to start', 60, WIDTH / 2, int(HEIGHT * 0.45), WHITE)  
    