class Settings:
    def __init__(self):
        # Window settings
        self.screen_width = 1200
        self.screen_height = 800
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.player_lives = 3   # ship_limit in tutorial

        # Bullet settings
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5.0

        # Aliens settings
        self.fleet_drop_speed = 10.0


        # Difficulty increase settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.alien_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_points = 50

        self.fleet_direction = 1


    def increase_speed(self):   # increase_level might be a better name
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
