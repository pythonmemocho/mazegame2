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
        self.stage = Stage(stage_data)
        
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
            self.stage.playerSprite.draw(SCREEN)
            #ゴールを描画
            self.stage.goalSprite.draw(SCREEN)
            #敵を描画
            self.stage.enemySprite.draw(SCREEN)
            self.stage.keySprite.draw(SCREEN)
            
            #playerとenemyの衝突判定
            pg.sprite.groupcollide(self.stage.playerSprite, self.stage.enemySprite, True, False)
            #playerとkeyの衝突判定
            pg.sprite.groupcollide(self.stage.playerSprite, self.stage.keySprite, False, True)

            #playerのupdateメソッド呼び出し
            self.stage.playerSprite.update(self.stage.tile_list)
            #enemyのupdateメソッド呼び出し
            self.stage.enemySprite.update(self.stage.tile_list)
            #playerとgoalの接触判定
            if pg.sprite.collide_circle(self.stage.player,self.stage.goal):
                self.stage.player.goal = True

            #ゴール時の処理（テキスト描画）
            if self.stage.player.goal:
                draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), BLUE)
                
            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()