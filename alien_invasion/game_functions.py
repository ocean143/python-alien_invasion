import pygame
import sys
from bullet import Bullet

def check_events(alien_setting,screen,ship,bullets): 
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# 按下按键的时候	
			check_events_down(alien_setting,screen,ship,event,bullets)
			# 松开按键的时候 
			check_events_up(ship,event)

# 监听按键按下
def check_events_down(alien_setting,screen,ship,event,bullets):
	if event.type == pygame.KEYDOWN:
		# 按键为右键的时候
		if event.key == pygame.K_RIGHT:
			ship.movright = True
		# 按键为左键的时候
		if event.key == pygame.K_LEFT:
			ship.movleft = True
		# 按键为上键的时候
		if event.key == pygame.K_UP:
			ship.movtop = True
		# 按键为下键的时候
		if event.key == pygame.K_DOWN:
			ship.movdown = True
		# 按下空格键
		if event.key == pygame.K_SPACE:
			fire_bullets(alien_setting,screen,ship,bullets)
			

# 检查按键松开
def check_events_up(ship,event):
	if event.type == pygame.KEYUP:	
		ship.movleft = False	
		ship.movtop = False
		ship.movright = False	
		ship.movdown = False

# 更新飞船的位置
def update_screen(alien_setting,screen,ship,bullets):
	screen.fill(alien_setting.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	pygame.display.flip()

# 发射子弹
def fire_bullets(alien_setting,screen,ship,bullets):
	if len(bullets) < alien_setting.bullet_maxnum:
		new_bullet = Bullet(alien_setting,screen,ship)
		bullets.add(new_bullet)
	else: 
		print("超过最大子弹数目")

# 更新子弹的位置
def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))








