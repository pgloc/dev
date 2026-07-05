import sys
import pygame

from random import randint
from star import Star

class StarrySky:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (0, 0, 204)

        pygame.display.set_caption("Gwiezdna noc")
        self.stars = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self._update_screen()
            
            # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_sky(self):
        """Utworzenie pełnego nieba z gwiazdami."""
        # Utworzenie gwiazdy i ustalenie liczby gwiazd, które zmieszczą się w rzędzie.
        # Odległość między poszczególnymi gwiazdami jest równa szerokości gwiazdy.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_rect.width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Ustalenie, ile rzędów gwiazd zmieści się na ekranie.
        available_space_y = self.screen_rect.height - star_height
        number_rows = available_space_y // (2 * star_height)

        # Utworzenie pełnego nieba z gwiazdami.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Utworzenie gwiazdy i umieszczenie jej w rzędzie."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = randint(0, self.screen_rect.width - star_width)
        star.rect.x = star.x
        star.rect.y = randint(0, self.screen_rect.height - star_height)
        self.stars.add(star)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = StarrySky()
    ai.run_game()