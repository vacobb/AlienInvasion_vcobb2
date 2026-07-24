""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class
24-July-2026 """

import sys
from time import sleep

import pygame

from alien import Alien
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """ Game engine. """
    def __init__(self):
        pygame.init()

        self.game_active = False

        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion - Track 2")

        self.bg_color = self.settings.bg_color
        self.bg_image = pygame.image.load('Assets/images/Starbasesnow.png').convert_alpha()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.play_button = Button(self, "Play")

        self._create_fleet()

    
    def run_game(self):
        """ Establishes main game loop. """
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()     
            self.clock.tick(60)     # 60 fps


    def _update_bullets(self):
        """ Checks for bullets on screen and helps despawn them. """
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        

    def _check_bullet_alien_collisions(self):
        """ Checks for bullets collisions with aliens and initiates resulting logic. """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            self.stats.score += self.settings.alien_points
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()

    
    def _check_events(self):
        """ Checks for keyboard and mouse inputs. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """ Controls what happens when 'Play' button is pressed. """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._reset_game()

            
    def _reset_game(self):
        """ Resets game back to default after game over. """
        self.stats.reset_stats()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_ships()
        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)  # Hide mouse during gameplay
        self.settings.initialize_dynamic_settings()
            

    def _check_keydown_events(self, event):
        """ Controls have happens on key down events. """
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            sys.exit()


    def _check_keyup_events(self, event):
        """ Controls what happens on key up events. """
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False
    
    
    def _fire_bullet(self):
        """ Fires a bullet. """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    
    def _update_screen(self):
        """ Redraws screen, updating with what has changed since last frame. """
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.scoreboard.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()   # We draw to a display behind what is shown. Flip switches between themm.


    def _create_fleet(self):
        """ Creates the fleet of aliens at start of level. """
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height - 3 * alien_height):    # Start with y for a spreadsheet. 
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            current_y += 2 * alien_height
            current_x = alien_width

    
    def _create_alien(self, x_position, y_position):
        """ Creates new alien ships to be places in fleet. """
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)   


    def _update_aliens(self):
        """ Controls movement of alien fleet. """
        self._check_fleet_edges()
        self.aliens.update()

        # Has an alien ship collieded with the hero ship?
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()
    

    def _ship_hit(self):
        """ Determins whether player ship has been hit. """
        if self.stats.ships_remaining > 0:
            self.stats.ships_remaining -= 1
            self.scoreboard.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_fleet_edges(self):
        """ Checks fleet position to determind if direction change is needed. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    

    def _change_fleet_direction(self):
        """ Changes movement direction of alien ships. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """ Checks to see if alien ships hit bottom of screen. """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
