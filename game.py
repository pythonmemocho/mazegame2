import pygame as pg
from _create_stage import create_data, number_of_keys
from _draw_stage import *
from spot_light import Spot_light
from title_screen import *

from _functions import draw_text, image_load_and_scale_func

#メインゲームクラス
class Game:
    key_img = image_load_and_scale_func('img/key.png',CHIP_SIZE,CHIP_SIZE)
    door_open_img = image_load_and_scale_func('img/door_open.png',CHIP_SIZE,CHIP_SIZE)
    
    def __init__(self):
        pg.init()
        self.reset()
        
        self.stage = Stage(create_data())
        self.spot_light = Spot_light()
        #画面切り替え用のタイミング
        self.init_count = 200
        self.timing_counter = self.init_count
    
    def reset(self):
        ''' call this method when start or restart '''
        self.title = True
        self.game_over = False
        self.goal_open = False
        self.goal_arrive = False

        self.get_keys = 0
        self.set_keys = number_of_keys
        

    def game_loop(self):
        ''' call this method when game start '''
        SCREEN.fill(GRAY)
        self.draw()

        # playerとenemyの衝突判定
        if self.check_collision(self.stage.enemySprite, self.stage.player):
            self.stage.player.kill()
            print(self.stage.playerSprite)
            self.game_over = True

        # playerとkeyの衝突判定        
        for key in self.stage.keySprite:
            if pg.sprite.collide_circle(key,self.stage.player):
                key.kill()
                self.get_keys += 1

        #全てのカギを取得した時の処理
        if self.get_keys == self.set_keys:
            # self.stage.key.get_all_keys = True
            self.goal_open = True

        #doorの画像を切り替える
        #playerとgoalの接触判定
        if self.goal_open:
            self.stage.goalSprite.update()
            if pg.sprite.collide_circle(self.stage.player,self.stage.goal):
                self.goal_arrive = True
                self.stage.player.kill()
                print(self.stage.player)
                draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), WHITE)
                self.timing_counter -= 1
                if self.timing_counter < 0:
                    self.title = True
                    self.timing_counter = self.init_count
                
        self.update()

        #keyの数のテキスト
        if not self.goal_open:
            draw_text(f'{self.get_keys}', 35, 55, 6, (255, 215, 0))  
            SCREEN.blit(self.key_img, (0,0))
        else:
            draw_text(f'OPEN', 35, 80, 6, (255, 215, 0))
            SCREEN.blit(self.door_open_img, (0,0))
            
        #game_overの時のテキスト
        if self.game_over:
            draw_text(f'Failed..', 100, WIDTH / 2, int(HEIGHT * 0.45), RED)
            draw_text(f'press [ R ]key to return Title', 40, WIDTH / 2, int(HEIGHT * 0.60), WHITE)
            if pg.key.get_pressed()[K_r]:
                self.game_over = False
                self.title = True

        # if self.goal_arrive:
        #     draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), WHITE)
        #     self.timing_counter -= 1
        #     if self.timing_counter < 0:
        #         self.title = True
        #         self.timing_counter = self.init_count

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
        #spot_lightのdrawメソッド呼び出し
        if not self.game_over or not self.goal_arrive:
            self.spot_light.draw(self.stage.player.rect)

    #それぞれのclassのupdateメソッドをまとめて関数化しておく
    def update(self):
        #playerのupdateメソッド呼び出し
        self.stage.playerSprite.update(self.stage.tile_list)
        #enemyのupdateメソッド呼び出し
        self.stage.enemySprite.update(self.stage.tile_list)
       

    def check_collision(self, obj_list:list, player):
        for obj in obj_list:
            if pg.sprite.collide_circle(obj,player):
                return True

    # def timing_func(num):
    #     flag = True
    #     now = pg.time.get_ticks()
    #     while flag:
    #         if pg.time.get_ticks() - now > num:
    #             flag = False
    #     return True