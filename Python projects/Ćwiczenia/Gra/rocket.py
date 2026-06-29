import pygame

class Rocket:
    """Klasa przeznaczona do zarządzania rakietą."""

    def __init__(self, ai_game):
        """Inicjalizacja rakiety i jej położenia początkowego."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu rakiety i pobranie jej prostokąta.
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # Każda nowa rakieta pojawia się na środku ekranu.
        self.rect.center = self.screen_rect.center

        # Położenie rakiety jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Opcje wskazujące na poruszanie się rakiety.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Uaktualnienie położenia rakiety na podstawie opcji wskazującej na jej ruch."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

        # Uaktualnienie obiektu rect na podstawie wartości self.x i self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Wyświetlenie rakiety w jej aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)