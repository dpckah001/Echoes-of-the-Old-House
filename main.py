"""
《回响老屋》 游戏开发
"""

# 启动游戏
import time
import pygame

pygame.init()

width,height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("《回响老屋》")

# SET COLOR

WHITE = (255,255,255)
DARK_RED = (128,0,0)
BROWN = (128,64,0)
DARK_BROWN = (64,32,0)
BLACK = (0,0,0)

game_running = True
game_clock = pygame.time.Clock()




while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    # 渲染游戏
    screen.fill(BLACK)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    game_clock.tick(60) # 60fps
