#!/usr/bin/env python3
"""
贪吃蛇游戏 - Snake Game
支持键盘方向键控制，空格键暂停，Q键退出
"""

import curses
import random
import time

# 游戏配置
WIDTH = 40
HEIGHT = 20
SPEED = 0.15  # 移动速度（秒）

def main(stdscr):
    # 初始化 curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    # 颜色初始化
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # 蛇
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # 食物
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # 墙壁
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # 文字
    
    # 游戏状态
    snake = [(HEIGHT//2, WIDTH//2), (HEIGHT//2, WIDTH//2-1), (HEIGHT//2, WIDTH//2-2)]
    direction = curses.KEY_RIGHT
    food = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
    score = 0
    game_over = False
    paused = False
    
    while not game_over:
        # 绘制游戏界面
        stdscr.clear()
        
        # 绘制边界
        for x in range(WIDTH + 2):
            stdscr.addch(0, x, '#', curses.color_pair(3))
            stdscr.addch(HEIGHT + 1, x, '#', curses.color_pair(3))
        for y in range(HEIGHT + 2):
            stdscr.addch(y, 0, '#', curses.color_pair(3))
            stdscr.addch(y, WIDTH + 1, '#', curses.color_pair(3))
        
        # 绘制食物
        stdscr.addch(food[0] + 1, food[1] + 1, '@', curses.color_pair(2))
        
        # 绘制蛇
        for i, (y, x) in enumerate(snake):
            if i == 0:
                stdscr.addch(y + 1, x + 1, 'O', curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addch(y + 1, x + 1, 'o', curses.color_pair(1))
        
        # 显示分数
        stdscr.addstr(HEIGHT + 3, 2, f"Score: {score}", curses.color_pair(4))
        stdscr.addstr(HEIGHT + 4, 2, "Controls: Arrow keys to move, Space to pause, Q to quit", curses.color_pair(4))
        
        if paused:
            stdscr.addstr(HEIGHT//2, WIDTH//2 - 5, "PAUSED", curses.color_pair(4) | curses.A_BOLD)
        
        stdscr.refresh()
        
        # 获取按键
        key = stdscr.getch()
        
        if key == ord('q') or key == ord('Q'):
            break
        elif key == ord(' '):
            paused = not paused
        elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            # 防止反向移动
            if key == curses.KEY_UP and direction != curses.KEY_DOWN:
                direction = key
            elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
                direction = key
            elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
                direction = key
            elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
                direction = key
        
        if not paused:
            # 计算新蛇头位置
            head = snake[0]
            if direction == curses.KEY_UP:
                new_head = (head[0] - 1, head[1])
            elif direction == curses.KEY_DOWN:
                new_head = (head[0] + 1, head[1])
            elif direction == curses.KEY_LEFT:
                new_head = (head[0], head[1] - 1)
            elif direction == curses.KEY_RIGHT:
                new_head = (head[0], head[1] + 1)
            
            # 碰撞检测
            if (new_head[0] <= 0 or new_head[0] >= HEIGHT + 1 or
                new_head[1] <= 0 or new_head[1] >= WIDTH + 1 or
                new_head in snake):
                game_over = True
                break
            
            # 移动蛇
            snake.insert(0, new_head)
            
            # 吃到食物
            if new_head == food:
                score += 10
                # 生成新食物
                while True:
                    food = (random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2))
                    if food not in snake:
                        break
            else:
                snake.pop()
            
            time.sleep(SPEED)
    
    # 游戏结束界面
    stdscr.clear()
    msg = f"GAME OVER! Score: {score}"
    stdscr.addstr(HEIGHT//2, (WIDTH - len(msg))//2, msg, curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(HEIGHT//2 + 2, WIDTH//2 - 10, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
