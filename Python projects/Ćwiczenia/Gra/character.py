import pygame

class Character:
    """Klasa przeznaczona do zarządzania postacią."""

    def __init__(self, ai_game):
        """Inicjalizacja postaci i jej położenie początkowe."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu postaci i pobranie jego prostokąta.
        self.image = pygame.image.load('images/pirate.png')
        self.rect = self.image.get_rect()

        # Każda nowa postać pojawia się na środku ekranu.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Wyświetlenie postaci w jej aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)