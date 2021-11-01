import pygame as pg
from pygame.locals import *  
from setting import *
from get_stage_data import *
from player import *
from stage_data import *
from enemy import Enemy
from spot_light import Spot_light
from title_screen import *


#メインゲームクラス
class Game():
    def __init__(self):
        pg.init()

           
        #Title/GameOver画面の表示切り替えフラグ
        self.title = True
        self.game_over = False

        #画面切り替えのタイミング
        self.init_count = 200
        self.timing_counter = self.init_count

    def main_set(self):
        #画面全体を灰色に塗る（通路の色）
        SCREEN.fill(GRAY)
        
        #まとめたdrawメソッドの呼び出し
        self.draw()
        
        # playerとenemyの衝突判定
        for enemy in self.stage.enemySprite:
            if pg.sprite.collide_circle(enemy,self.stage.player):
                self.stage.player.kill()
                self.game_over = True
        
        #game_overの時のテキスト
        if self.game_over:
            draw_text(f'Failed..', 100, WIDTH / 2, int(HEIGHT * 0.45), RED)
            draw_text(f'press [t]key to return Title', 40, WIDTH / 2, int(HEIGHT * 0.60), RED)
            if pg.key.get_pressed()[K_t]:
                self.game_over = False
                self.title = True

        # playerとkeyの衝突判定        
        for key in self.stage.keySprite:
            if pg.sprite.collide_circle(key,self.stage.player):
                key.kill()
                self.get_keys += 1
        
        #keyの数のテキスト
        if not self.stage.key.get_all_keys:
            draw_text(f'Keys: {self.get_keys}', 35, 55, 6, YELLOW)  
        else:
            draw_text(f'Door is open', 35, 80, 6, YELLOW)
        
        #全てのカギを取得した時の処理
        if self.get_keys == self.set_keys:
            self.stage.key.get_all_keys = True

        #doorの画像を切り替える
        if self.stage.key.get_all_keys:
            self.stage.goalSprite.update()
        
        #playerとgoalの接触判定
        if pg.sprite.collide_circle(self.stage.player,self.stage.goal):
            if self.get_keys == self.set_keys:
                self.stage.player.goal = True
        
        #ゴール時の処理（テキスト描画）
        if self.stage.player.goal:
            draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), WHITE)
            self.timing_counter -= 1
            if self.timing_counter < 0:
                self.title = True
                self.timing_counter = self.init_count

        #まとめたupdateメソッドの呼び出し
        self.update()


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

    #それぞれのclassのupdateメソッドをまとめて関数化しておく
    def update(self):
        #playerのupdateメソッド呼び出し
        self.stage.playerSprite.update(self.stage.tile_list)
        #enemyのupdateメソッド呼び出し
        self.stage.enemySprite.update(self.stage.tile_list)
        #spot_lightのupdateメソッド呼び出し
        if not self.game_over:
            self.spot_light.update(self.stage.player.rect)

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

            #マウスカーソルの消去
            pg.mouse.set_visible(False)

            #titleがFalseならメソッドを実行,trueならtitle画面をインスタンス化
            if not self.title:
                self.main_set()

            else:
                self.title_screen = Title()
                if pg.key.get_pressed()[K_RETURN]:
                    self.title = False
                    self.game_over = False
                    self.stage = Stage(create_data())
                    self.spot_light = Spot_light()
                    #鍵の設定
                    self.set_keys = number_of_keys
                    self.get_keys = 0 

            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()