from _setting import *
import random

#ステージの設定
SIZE_W = int(WIDTH / CHIP_SIZE)
SIZE_H = int(HEIGHT / CHIP_SIZE)

#keyの個数
number_of_keys = 1
#敵の数
number_of_enemies = 1

def create_data():
    stage_data = []
    #始めにステージ全てを[0]にする
    for y in range(SIZE_H):
        stage_data.append([0]*SIZE_W)
    #周りの壁のみを[1]にする
    for x in range(SIZE_W):
        stage_data[0][x] = 1
        stage_data[SIZE_H-1][x] = 1
    for y in range(SIZE_H):
        stage_data[y][0] = 1
        stage_data[y][SIZE_W-1] = 1
        
    #壁から2列毎に柱を立てる
    for y in range(2, SIZE_W - 2, 2):
        for x in range(2, SIZE_H - 2, 2):
            stage_data[y][x] = 1

    #柱から上下左右にランダムに柱を立てる。入れない通路ができないように
    xp = [0, 1, 0, -1]
    yp = [-1, 0, 1, 0]
    for y in range(2, SIZE_H - 2, 2):
        for x in range(2, SIZE_W - 2, 2):
            d = random.randint(0, 3)
            if x > 2:
                d = random.randint(0, 2)
            stage_data[y + yp[d]][x + xp[d]] = 1

    #GOALの初期位置をセット
    goal_pos_set = False
    while not goal_pos_set:
        if init_position_set(2,SIZE_W-1,2,SIZE_H-2,stage_data,'G'):
            goal_pos_set = True

    #keyの初期位置をセット
    key_pos_set = False
    key_count = number_of_keys
    while not key_pos_set:
        if init_position_set(1,SIZE_W-1,2,SIZE_H-2,stage_data,"K"):
            key_count -= 1
        if key_count <= 0:
            key_pos_set = True

    #敵の初期位置をセット
    enemy_pos_set = False
    enemy_count = number_of_enemies
    while not enemy_pos_set:
        if init_position_set(4,SIZE_W-1,4,SIZE_H-2,stage_data,"E"):
            enemy_count -= 1
        if enemy_count <= 0:
            enemy_pos_set = True

    #プレイヤー開始位置セット
    if stage_data[1][1] == 0:
        stage_data[1][1] = "P"

    #ステージの配列を確認したい場合にコメントアウトを外す
    # for  stage in stage_data:
    #    print(stage)

    return stage_data

def init_position_set(a,b,c,d,data,target):
        x = random.randint(a,b)
        y = random.randint(c,d)
        if data[y][x] == 0:
            data[y][x] = target
            return True