# -*- coding: utf-8 -*-
import pygame

class Ship():
	# 传入屏幕
	def __init__(self,screen,alien_setting):
		self.screen = screen;
		self.alien_setting = alien_setting
		# 飞船图片
		self.image = pygame.image.load('images/ship.bmp')
		# 飞船所处的区域
		self.rect = self.image.get_rect()
		# 屏幕所处的区域
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.movleft = False
		self.movtop = False
		self.movright = False
		self.movdown = False

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.movright:
			self.rect.centerx += self.alien_setting.ship_move_speed
			# 移动到最右边就不移动了 
			if self.rect.right>=self.screen_rect.right:
				self.rect.right = self.screen_rect.right

		if self.movleft:
			self.rect.centerx -= self.alien_setting.ship_move_speed
			# 移动到最左边就不移动了 
			if self.rect.left <=self.screen_rect.left:
				self.rect.left = self.screen_rect.left

		if self.movtop:
			self.rect.top -= self.alien_setting.ship_move_speed
			# 移动到最上边就不移动了 
			if self.rect.top <=self.screen_rect.top:
				self.rect.top = self.screen_rect.top

		if self.movdown:
			self.rect.bottom += self.alien_setting.ship_move_speed
			# 移动到最下边就不移动了 
			if self.rect.bottom >=self.screen_rect.bottom:
				self.rect.bottom = self.screen_rect.bottom


			
