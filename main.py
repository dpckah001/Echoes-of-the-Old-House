"""
《回响老屋》 游戏开发
"""

# 启动游戏
import time
import pygame
# buttons files
from buttons import GameStartButton
from buttons import SettingButton



pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("《回响老屋》")

# SET COLOR

WHITE = (255, 255, 255)
DARK_RED = (128, 0, 0)
BROWN = (128, 64, 0)
DARK_BROWN = (64, 32, 0)
BLACK = (0, 0, 0)

game_running = True
game_clock = pygame.time.Clock()

def start_web():
    # 创建START按钮实例
	Start_new_game_button = GameStartButton(250, 70, "New Game")
	Load_old_gam_button = GameStartButton(250, 70, "Load Game")

	# settings button
	setting_button = SettingButton(80, 80)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False 

    # 渲染游戏
    screen.fill(BLACK)

    # 绘制按钮
    button.draw(screen)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    game_clock.tick(60)  # 60fps

pygame.quit()