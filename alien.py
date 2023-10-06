import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class of alien."""
    def __init__(self, ai_game):
        """ Init alien and take his start position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Getting image of alien and setting his attribute rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x

