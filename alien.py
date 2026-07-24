""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class
24-July-2026 """

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Handles logic for alien sprites in game. """
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.settings = ai_game.settings


    def update(self):
        """ Updates alien position on screen. """
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction


    def check_edges(self):
        """ Returns True if alien is at edge of screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
