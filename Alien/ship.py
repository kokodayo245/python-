import pygame


class Ship(object):

    def __init__(self, ai_settings, screen):

        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.moving_up = False
        self.moving_down = False

    def update(self):
        # 根据移动标志调整飞船位置
        # 限制飞船移动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.vertical

    def center_ship(self):
        # 让飞船回到初始位置
        self.center = self.screen_rect.centerx
        self.vertical = self.screen_rect.bottom - self.rect.height / 2
        print(self.rect.bottom, self.screen_rect.bottom)

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

