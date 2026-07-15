import pygame
from pygame.sprite import Sprite
from random import randint

class Target(Sprite):
    """Klasa przedstawiająca pojedynczy cel."""

    def __init__(self, ai_game):
        """Inicjalizacja celu i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.target_color

        # Utworzenie prostokąta celu w punkcie (0, 0), a następnie zdefiniowanie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)

        # Umieszczenie nowego celu przy prawej krawędzi ekranu.
        self.rect.x = self.screen.get_rect().right - self.rect.width
        self.rect.y = randint(0, self.screen.get_rect().height - self.rect.height)

        # Przechowywanie dokładnego poziomu położenia celu.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Zwraca wartość True, jeśli cel znajduje się przy dolnej lub górnej krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
        
    def update(self):
        """Przesunięcie celu w górę i w dół."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y
        
    def draw_target(self):
        """Wyświetlenie celu na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)