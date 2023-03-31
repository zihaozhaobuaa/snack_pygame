import pygame
import random

# 初始化 Pygame
pygame.init()

# 游戏窗口大小
window_width = 400
window_height = 400

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# 创建游戏窗口
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake')

# 设置游戏时钟
clock = pygame.time.Clock()

# 蛇方块尺寸
block_size = 10

# 蛇移动速度
speed = 10

# 定义字体
font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [window_width / 6, window_height / 2])


def game_loop():
    # 准备游戏数据
    game_exit = False
    game_over = False

    lead_x = window_width / 2
    lead_y = window_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # 生成初始食物位置
    food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    while not game_exit:
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game over!", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # 检查蛇是否越界
        if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
            game_over = True

        # 更新蛇的位置
        lead_x += lead_x_change
        lead_y += lead_y_change

        # 游戏胜利
        if snake_length == 50:
            game_over = True
            message_to_screen("you win!", green)

        # 画出食物和蛇
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_list:
            pygame.draw.rect(game_display, black, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # 检查蛇是否吃到食物
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # 设置游戏时钟速度
        clock.tick(speed)

    pygame.quit()
    quit()


# 运行游戏循环
game_loop()
