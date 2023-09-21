import pygame

class Ship():
    
    """ Class to manage space airplane."""
    def __init__(self, ai_game):
        """ Initilaize space ship and set starts position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Make and Get space ship image
        self.image = pygame.image.load("images/ship.bmp")
        # Make and Get space ship rectangle
        self.rect = self.image.get_rect()
        # Set space ship window midbottom
        self.rect.midbottom = self.screen_rect.midbottom
        # Make and Save center of space ship rectangle
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update ship position."""
        # Update x, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect on base self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

