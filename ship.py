import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen    # Do not recommend to pass game engine through classes
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.center_ship()
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom