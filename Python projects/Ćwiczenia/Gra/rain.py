import sys
import pygame

from raindrop import Raindrop

class Rain:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (0, 0, 204)

        pygame.display.set_caption("Deszcz")
        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self._update_rain()
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

    def _update_rain(self):
        """Sprawdzenie, czy krople znajdują się przy krawędzi, a następnie uaktualnienie położenia wszystkich kropli."""
        self._check_rain_edges()
        self.raindrops.update()

    def _create_rain(self):
        """Utworzenie deszczu."""
        # Utworzenie kropli i ustalenie liczby kropli, które zmieszczą się w rzędzie.
        # Odległość między poszczególnymi kroplami jest równa szerokości kropli.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_rect.width - (2 * raindrop_width)
        number_drops_x = available_space_x // (2 * raindrop_width)

        # Ustalenie, ile rzędów kropli zmieści się na ekranie.
        available_space_y = self.screen_rect.height - (4 * raindrop_height)
        number_rows = available_space_y // (2 * raindrop_height)

        # Utworzenie pełnego nieba z kroplami.
        for row_number in range(number_rows):
            for drops_number in range(number_drops_x):
                self._create_raindrop(drops_number, row_number)

    def _create_raindrop(self, drops_number, row_number):
        """Utworzenie kropli i umieszczenie jej w rzędzie."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * drops_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop_height + 2 * raindrop_height * row_number
        self.raindrops.add(raindrop)

    def _check_rain_edges(self):
        """Odpowiednia reakcja, gdy kropla dotrze do krawędzi ekranu."""
        i = 0
        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)
                self._create_raindrop(i, 0)
                i += 1

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = Rain()
    ai.run_game()