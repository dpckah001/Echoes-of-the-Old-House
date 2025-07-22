import pygame

class GameStartButton():
    def __init__(self,width,height,text,x=0,y=0):
        self.width = width
        self.height = height
        self.text = text
        self.x = x
        self.y = y

    def draw(self, screen):
        # 定义矩形区域
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        DARK_RED = (128, 0, 0)
        # 绘制矩形按钮，这里假设颜色为黑红色
        pygame.draw.rect(screen, DARK_RED, rect)
        # 渲染文本
        font = pygame.font.Font("fonts/game_regular.ttf", 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        # 计算文本居中位置
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        # 绘制文本
        screen.blit(text_surface, (text_x, text_y))

# Setting button 
class SettingButton():
    def __init__(self, width, height,radius,color):
        self.width = width
        self.height = height
        self.radius = radius
        self.color = color 
        # import image
        self.setting_button_image = pygame.image.load("/image/setting_button.png").convert_alpha()
        self.setting_button_image = pygame.transform.scale(self.setting_button_image, (radius * 2, radius * 2))
        
        
    def draw(self,screen):
        # draw the png
        screen.bilt(self.setting_button_image, (self.x - self.radius, self.y - self.radius))
    
    # press the button and then tell the page file
    def the_set_press_down(self, mousepos):
        if self.is