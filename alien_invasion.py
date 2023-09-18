import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """ Инициалищирует игру и созает русурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    
    def run_game(self):
        """ Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """ Wait key events."""
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """ Update screen."""
        # Get background.
        self.screen.fill(self.settings.bg_color)
        # Get spaceship.
        self.ship.blitme()
        # Отображение последнего прорисованного экрана.

        pygame.display.flip()
    

    


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
