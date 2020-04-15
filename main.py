# -*- coding=utf-8 -*-
import pygame
import time
pygame.init()

flag = 1 # 黑棋为单，白棋为偶
chess_white_arr = [] # 每一个棋子的位置
chess_black_arr = [] 
WHITE = (255,255,255)
BLACK = (0,0,0)
space = 60 # 四周留下的边距
cell_size = 40  # 每个格子大小
cell_num = 15   # 每行每列可以下的点数
grid_size = cell_size * (cell_num - 1) + space * 2 # 棋盘大小
screencaption = pygame.display.set_caption('FIR')
screen = pygame.display.set_mode((grid_size,grid_size)) # 设置窗口大小

def chess_win(xi,yi,chess_arr):
    mark = False
    count = 1
    x = xi
    # 对行进行判断
    for i in range(0,5):
        x = x-1
        if (x,yi) in chess_arr:
            count += 1
            
        else:
            break
    x = xi
    for i in range(0,5):
        x = x+1
        if (x,yi) in chess_arr:
            count += 1
        else:
            break

# 对列进行判断
    if count < 5:
        count = 1
        y = yi
        for i in range(0,5):
            y -= 1
            if (xi,y) in chess_arr:
                count += 1
            else:
                break
        y = yi
        for i in range(0,5):
            y += 1
            if (xi,y) in chess_arr:
                count += 1
            else:
                break
    
        
# 对\斜边进行判断
    if count < 5:
        count = 1
        x = xi
        y = yi
        for i in range(0,5):
            x -= 1
            y -= 1
            if (x,y) in chess_arr:
                count += 1
            else:
                break
        x = xi
        y = yi
        for i in range(0,5):
            x += 1
            y += 1 
            if (x,y) in chess_arr:
                count += 1
            else:
                break
# 对/斜边进行判断
    if count < 5:
        count = 1
        x = xi
        y = yi
        for i in range(0,5):
            x += 1
            y -= 1
            if (x,y) in chess_arr:
                count += 1
            else:
                break
        x = xi
        y = yi
        for i in range(0,5):
            x -= 1
            y += 1 
            if (x,y) in chess_arr:
                count += 1
            else:
                break


    if count >= 5:
        mark = True
    
    return mark

while True:
    over = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:  # 鼠标松开事件
            x, y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            if xi >= 0 and yi >= 0 and xi <= cell_num-1 and yi <= cell_num-1 and (not (xi,yi) in chess_white_arr) and (not (xi,yi) in chess_black_arr):
                if flag%2 == 0:
                    chess_white_arr.append((xi, yi))
                    if chess_win(xi,yi,chess_white_arr):
                        print('白棋胜利')
                        over = True
                else:
                    chess_black_arr.append((xi, yi))
                    if chess_win(xi,yi,chess_black_arr):
                        print('黑棋胜利')
                        over = True
                flag += 1
                
                
    screen.fill((0,0,150)) # 将界面设置为蓝色


    # 列，利用for循环将每一点的坐标都显示出来了
    for x in range(0,cell_size*cell_num,cell_size):
        pygame.draw.line(screen,(200,200,200),(x+space,0+space),(x+space,cell_size*(cell_num-1)+space),1) # 显示的窗口，颜色，起始点，终止点，线条宽度
    # 行
    for y in range(0,cell_size*cell_num,cell_size):
        pygame.draw.line(screen,(200,200,200),(0+space,y+space),(cell_size*(cell_num-1)+space,y+space),1)
    for x, y in chess_white_arr:
        pygame.draw.circle(screen,WHITE,(x*cell_size+space,y*cell_size+space),16,16) # 白棋，圆心坐标，半径，线条宽度
    for x, y in chess_black_arr:
        pygame.draw.circle(screen,BLACK,(x*cell_size+space,y*cell_size+space),16,16) # 白棋，圆心坐标，半径，线条宽度

    if over:
        break
    pygame.display.update() 

