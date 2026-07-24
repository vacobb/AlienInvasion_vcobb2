""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class
24-July-2026 """

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Handles logic for bullet sprites in game. """
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        
        self.rect.midtop = ai_game.ship.rect.midtop


    def update(self):
        """ Updates bullet location. """
        self.rect.y -= self.settings.bullet_speed

    
    def draw_bullet(self):
        """ Creates bullet asset on screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
