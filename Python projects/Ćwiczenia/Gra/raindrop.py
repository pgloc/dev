import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Klasa przedstawiająca kroplę deszczu."""

    def __init__(self, ai_game):
        """Inicjalizacja kropli i zdefiniowanie jej położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu kropli i zdefiniowanie jej atrybutu rect.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Umieszczenie nowej kropli w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomu położenia kropli.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Zwraca wartość True, jeśli kropla znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        
    def update(self):
        """Przesunięcie kropli w dół."""
        self.y += 1.5
        self.rect.y = self.y