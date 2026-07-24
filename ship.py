""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class
24-July-2026 """

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Handles logic for player's ship sprites in game. """
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.center_ship()
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ Updates ship position every frame. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed


    def blitme(self):
        """ Draws ship to scrren. """
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """ Centers ship at bottom of screen. """
        self.rect.midbottom = self.screen_rect.midbottom