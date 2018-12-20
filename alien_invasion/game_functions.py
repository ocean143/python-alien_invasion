import pygame
import sys

def check_events(ship): 
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# 按下按键的时候	
			check_events_down(ship,event)
			# 松开按键的时候 
			check_events_up(ship,event)

def check_events_down(ship,event):
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

def check_events_up(ship,event):
	if event.type == pygame.KEYUP:	
		ship.movleft = False	
		ship.movtop = False
		ship.movright = False	
		ship.movdown = False

def update_screen(alien_setting,screen,ship):
	screen.fill(alien_setting.bg_color)
	ship.blitme()
	pygame.display.flip()
