import pygame

class Ship():
    
    """ Class to manage space airplane."""
    def __init__(self, ai_game):
        """ Initilaize space ship and set starts position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Make and Get space ship image
        self.image = pygame.image.load("images/ship_left_side.bmp")
        # Make and Get space ship rectangle
        self.rect = self.image.get_rect()
        # Set space ship window midbottom
        self.rect.midleft = self.screen_rect.midleft
        # Make and Save center of space ship rectangle
        self.y = float(self.rect.y)
        
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update ship position."""
        # Update x, not rect
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        # Update rect on base self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

