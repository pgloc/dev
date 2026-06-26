import sys
import pygame

from character import Character

class Cwiczenie:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Ćwiczenie")

        self.character = Character(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()
            
            # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = Cwiczenie()
    ai.run_game()