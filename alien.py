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
        self.image = pygame.image.load('Assets/images/enemyRed1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.settings = ai_game.settings

        self.exploding = False
        self.explosion_timer = 0


    def update(self):
        """ Updates alien position on screen while alive, shows explosion animation if hit. """
        if self.exploding:
            self.explosion_timer += 1

            if self.explosion_timer > 10:
                self.kill()

        else:
            self.rect.x += self.settings.alien_speed * self.settings.fleet_direction


    def check_edges(self):
        """ Returns True if alien is at edge of screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    

    def explode(self):
        self.image = pygame.image.load("Assets/images/explosion.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.exploding = True
        