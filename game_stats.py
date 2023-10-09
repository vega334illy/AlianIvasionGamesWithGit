""" Tracking statistics for the game 'Alien Invasion'."""

class GameStats():
    """ Tracking statistics for the game 'Alien Invasion'."""

    def __init__(self, ai_game):
        """ Initilaze statistics."""
        self.settings = ai_game.settings
        self.reset_status()

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
