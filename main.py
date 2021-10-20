import pygame as pg
from pygame.locals import *  
from setting import *
from get_stage_data import *
from player import *
from stage_data import *
from enemy import Enemy
from spot_light import Spot_light


#メインゲームクラス
class Game():
    def __init__(self):
        pg.init()      

        #各クラスのインスタンス化
        self.stage = Stage(stage_data)
        self.spot_light = Spot_light()
        
        #鍵の設定
        self.set_keys = number_of_keys
        self.get_keys = 0

    #それぞれのclassのdrawメソッドをまとめて関数化しておく
    def draw(self):
        #ステージを描画
        self.stage.draw(SCREEN)
        #ゴールを描画
        self.stage.goalSprite.draw(SCREEN)
        #鍵を描画
        self.stage.keySprite.draw(SCREEN)
        #敵を描画
        self.stage.enemySprite.draw(SCREEN)
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

            #画面全体を灰色に塗る（通路の色）
            SCREEN.fill(GRAY)
            
            #まとめたdrawメソッドの呼び出し
            self.draw()
            
            # playerとenemyの衝突判定
            for enemy in self.stage.enemySprite:
                if pg.sprite.collide_circle(enemy,self.stage.player):
                    self.stage.player.kill()
                    self.stage.player.dead = True
            # playerとkeyの衝突判定        
            for key in self.stage.keySprite:
                if pg.sprite.collide_circle(key,self.stage.player):
                    key.kill()
                    self.get_keys += 1

            #全てのカギを取得した時の処理
            if self.get_keys == self.set_keys:
                self.stage.key.get_all_keys = True

            #doorの画像を切り替える
            if self.stage.key.get_all_keys:
                self.stage.goalSprite.update()

            #playerのupdateメソッド呼び出し
            self.stage.playerSprite.update(self.stage.tile_list)

            #enemyのupdateメソッド呼び出し
            self.stage.enemySprite.update(self.stage.tile_list)

            #spot_lightのupdateメソッド呼び出し
            if not self.stage.player.dead:
                self.spot_light.update(self.stage.player.rect)


            #playerとgoalの接触判定
            if pg.sprite.collide_circle(self.stage.player,self.stage.goal):
                if self.get_keys == self.set_keys:
                    self.stage.player.goal = True

            #keyの数のテキスト
            if not self.stage.key.get_all_keys:
                draw_text(f'Keys: {self.get_keys}', 35, 55, 6, ORANGE)  
            else:
                draw_text(f'Door is open', 35, 80, 6, ORANGE)  

            if self.stage.player.dead:
                draw_text(f'Failed..', 100, WIDTH / 2, int(HEIGHT * 0.45), RED)  

            #ゴール時の処理（テキスト描画）
            if self.stage.player.goal:
                draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), WHITE)

            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()