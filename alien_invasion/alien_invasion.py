# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings 
from ship import Ship 
import game_functions as gf
from pygame.sprite import Group

def run_game():

	alien_setting = Settings()
	screen = pygame.display.set_mode((alien_setting.screen_width,alien_setting.screen_height)) 
	ship = Ship(screen,alien_setting)
	pygame.display.set_caption("Alien Invasion")

	bullets = Group()

	while True:
		gf.check_events(alien_setting,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(alien_setting,screen,ship,bullets)

run_game()