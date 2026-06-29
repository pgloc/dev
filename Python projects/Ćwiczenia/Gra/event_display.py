import sys
import pygame

class EventDisplay:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        # Fullscreen.
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Klawisze")
        self.font = pygame.font.Font(None, 36)
        self.key_text = "Naciśnij klawisz"

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.key_text = f"event.key = {event.key}"
                self._update_screen()
            
            # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.bg_color)
        text = self.font.render(self.key_text, True, (255, 255, 255))
        self.screen.blit(text, (20, 20))

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = EventDisplay()
    ai.run_game()