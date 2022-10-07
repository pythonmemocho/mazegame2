import pygame as pg

from title_screen import *
from game import Game

game = Game()

def main():
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        #マウスカーソルの消去
        pg.mouse.set_visible(False)

        #titleがFalseならメソッドを実行,trueならtitle画面をインスタンス化
        if not game.title:
            game.game_loop()
        else:
            game.title_screen = Title()
            if pg.key.get_pressed()[K_RETURN]:
                game.title = False
                game.game_over = False

        CLOCK.tick(FPS)
        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main()