""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class - taken from Python Crash Course.
24-July-2026 """

import pygame
from pygame.sprite import Sprite
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "Assets" / "images"

class Bullet(Sprite):
    """ Handles logic for bullet sprites in game. """

    def __init__(self, ai_game):
        """ Initialize attributes of the bullet. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load(IMAGE_DIR / 'laserBlue01.png').convert_alpha()

        self.rect = self.image.get_rect()
        
        self.rect.midtop = ai_game.ship.rect.midtop


    def update(self):
        """ Updates bullet location. """
        self.rect.y -= self.settings.bullet_speed

    
    def draw_bullet(self):
        """ Creates bullet asset on screen. """
        self.screen.blit(self.image, self.rect)
