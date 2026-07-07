import pygame
from pygame.sprite import Sprite
from random import randint

class Ufo(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""

    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego za prawą krawędzią ekranu.
        self.rect.x = self.screen.get_rect().right + self.rect.width
        self.rect.y = randint(0, self.screen.get_rect().height - self.rect.height)

        # Przechowywanie dokładnego poziomu położenia obcego.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0:
            return True
        
    def update(self):
        """Przesunięcie obcego w prawo."""
        self.x -= 0.5
        self.rect.x = self.x