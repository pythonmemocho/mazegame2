import pygame as pg
from pygame.locals import *  
from setting import *
from get_stage_data import *
from player import *
from stage_data import *
from enemy import *


#メインゲームクラス
class Game():
    def __init__(self):
        pg.init()      

        #各クラスのインスタンス化
        self.player = Player(25,25)
        
        self.playerSprite = pg.sprite.GroupSingle(self.player)

        self.stage = Stage(stage_data)
        
        self.enemySprite = pg.sprite.GroupSingle(self.stage.enemy)
       
    #メインループメソッド
    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            #画面全体を白に
            SCREEN.fill(WHITE)
            #ステージを描画
            self.stage.draw(SCREEN)
            #プレイヤーを描画
            self.playerSprite.draw(SCREEN)
            #敵を描画
            self.enemySprite.draw(SCREEN)
            
            pg.sprite.groupcollide(self.playerSprite, self.enemySprite, True, False)

            #プレイヤーのupdateメソッド呼び出し
            self.playerSprite.update(self.stage.tile_list)
            self.enemySprite.update(self.stage.tile_list)
            
            #ゴール時の処理（テキスト描画）
            if self.player.goal:
                draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), BLUE)
                
            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()