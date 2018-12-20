# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings 
from ship import Ship 
import game_functions as gf

def run_game():

	alien_setting = Settings()
	screen = pygame.display.set_mode((alien_setting.screen_width,alien_setting.screen_height)) 
	ship = Ship(screen,alien_setting)
	pygame.display.set_caption("Alien Invasion")
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(alien_setting,screen,ship)

run_game()