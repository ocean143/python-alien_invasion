import pygame
from pygame.sprite import Sprite
# 子弹类
class Bullet(Sprite):
	
	def __init__(self,ai_settings,screen,ship):
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.bullet_speed = ai_settings.bullet_speed

	def update(self):
		# 子弹不断上移
		self.y -= self.bullet_speed
		# 更新子弹的位置
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
