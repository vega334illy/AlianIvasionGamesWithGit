#! /bin/python3 
""" Module for spaceship bullet."""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from  the spaceship."""
    def __init__(self, ai_game):
        """ Create a bullet object at the ship's curren position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        #
        self.x = float(self.rect.x)

    def update(self):
        """ Move bullet up the screen."""
        # Update the decimall position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """ Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


