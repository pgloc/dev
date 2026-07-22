import pygame
from pygame.sprite import Sprite

class SpaceShip(Sprite):
    """Klasa przeznaczona do zarządzania statkiem."""

    def __init__(self, ai_game):
        """Inicjalizacja statku i jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku i pobranie jego prostokąta.
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()

        # Każdy nowy statek pojawia się na środku ekranu.
        self.rect.midleft = self.screen_rect.midleft

        # Położenie statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.y = float(self.rect.y)

        # Opcje wskazujące na poruszanie się statkiem.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 

        # Uaktualnienie obiektu rect na podstawie wartości self.y.
        self.rect.y = self.y

    def blitme(self):
        """Wyświetlenie statku w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na środku przy lewej krawędzi ekranu."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)