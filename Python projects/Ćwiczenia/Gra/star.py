import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Klasa przedstawiająca gwiazdę."""

    def __init__(self, ai_game):
        """Inicjalizacja gwiazzdy i zdefiniowanie jej położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu gwiazdy i zdefiniowanie jej atrybutu rect.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Umieszczenie nowej gwiazdy w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomu położenia gwiazdy.
        self.x = float(self.rect.x)