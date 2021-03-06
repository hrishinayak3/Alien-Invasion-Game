import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ A class to manage ship"""

    def __init__(self,ai_game):
        """Initialize ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start new ship at bottom center of the screen
        self.x = float(self.rect.x)

        self.rect.midbottom = self.screen_rect.midbottom
        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flag"""
        # update ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw ships current loction"""
        self.screen.blit(self.image, self.rect)

    def centre_ship(self):
        """Centre the shiop on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

