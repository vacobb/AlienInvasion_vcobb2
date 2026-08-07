""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class - taken from Python Crash Course.
24-July-2026 """

import pygame
from pathlib import Path

class Settings:
    """ Handles game's setting details. """

    def __init__(self):
        """ Initialize attributes of game settings. """

        # Window settings
        self.screen_width = 1200
        self.screen_height = 800
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

        # HUD settings
        BASE_DIR = Path(__file__).resolve().parent
        IMAGE_DIR = BASE_DIR / "Assets" / "images"
        self.hud_height = 100
        self.hud_image = pygame.image.load(IMAGE_DIR / "HUD_background.png")

        # Ship settings
        self.player_lives = 3

        # Bullet settings
        self.bullets_allowed = 5.0

        # Aliens' settings
        self.fleet_drop_speed = 10.0

        # Difficulty increase settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """ Provides starting poingt for the dynamic settings that evolve throughout gameplay. """
        self.ship_speed = 3.0
        self.alien_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_points = 50

        self.fleet_direction = 1


    def increase_level(self):
        """ Increases difficulty of game as levels increase. """
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
