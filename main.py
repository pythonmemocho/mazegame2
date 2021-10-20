import pygame as pg
from pygame.locals import *  
from setting import *
from get_stage_data import *
from player import *
from stage_data import *
from enemy import *
from spot_light import Spot_light


#メインゲームクラス
class Game():
    def __init__(self):
        pg.init()      

        #各クラスのインスタンス化
        self.stage = Stage(stage_data)
        self.spot_light = Spot_light()
        self.keys = 5

    def draw(self):
        #ステージを描画
        self.stage.draw(SCREEN)
        #ゴールを描画
        self.stage.goalSprite.draw(SCREEN)
        #敵を描画
        self.stage.enemySprite.draw(SCREEN)
        #鍵を描画
        self.stage.keySprite.draw(SCREEN)
        
        #プレイヤーを描画
        self.stage.playerSprite.draw(SCREEN)

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

            #画面全体を灰色に塗る
            SCREEN.fill(GRAY)
            
            self.draw()
            
            # playerとenemyの衝突判定
            for enemy in self.stage.enemySprite:
                if pg.sprite.collide_circle(enemy,self.stage.player):
                    self.stage.player.kill()
            # playerとkeyの衝突判定        
            for key in self.stage.keySprite:
                if pg.sprite.collide_circle(key,self.stage.player):
                    key.kill()
                    self.keys -= 1

            #全てのカギを取得した時の処理
            if self.keys == 0:
                self.stage.key.get_all_keys = True
            #ゴールの画像を切り替える
            if self.stage.key.get_all_keys:
                self.stage.goalSprite.update()

            #playerのupdateメソッド呼び出し
            self.stage.playerSprite.update(self.stage.tile_list)

            #enemyのupdateメソッド呼び出し
            self.stage.enemySprite.update(self.stage.tile_list)

            #spot_lightのupdateメソッド呼び出し
            self.spot_light.update(self.stage.player.rect)

            
            #playerとgoalの接触判定
            if pg.sprite.collide_circle(self.stage.player,self.stage.goal):
                if self.keys == 0:
                    self.stage.player.goal = True
                

            #ゴール時の処理（テキスト描画）
            if self.stage.player.goal:
                draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), BLUE)
            pg.draw.rect(self.stage.player.image,WHITE,self.stage.player.rect)    
            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()