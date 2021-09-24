class Settings:
    """A Class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)


        #snip settings
        self.ship_speed = 1.5
        self.ship_limit = 3


        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 9

        #how quickly the game speeds up
        self.speedup_scale = 1.0

        #how quickly can alien value increase
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.9
  
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int (self.alien_points* self.score_scale)

