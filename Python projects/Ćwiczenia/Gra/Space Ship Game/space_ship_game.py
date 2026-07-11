import sys
from time import sleep
import pygame

from space_ship_settings import Settings
from space_ship_stats import GameStats
from space_ship import SpaceShip
from space_ship_bullet import SpaceShipBullet
from space_ship_ufo import Ufo

class SpaceShipGame:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        # Fullscreen.
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Statek kosmiczny")

        # Utworzenie egzemplarza przechowującego dane statystyczne dotyczące gry.
        self.space_ship_stats = GameStats(self)

        self.space_ship = SpaceShip(self)
        self.space_ship_bullets = pygame.sprite.Group()
        self.space_ship_ufos = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()

            if self.space_ship_stats.game_active:
                self.space_ship.update()
                self._update_bullets()
                self._update_ufos()

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
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_UP:
            self.space_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_UP:
            self.space_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.space_ship.moving_down = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.space_ship_bullets) < 3:
            new_bullet = SpaceShipBullet(self)
            self.space_ship_bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        # Uaktualnienie położenia pocisków.
        self.space_ship_bullets.update()

        # Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.space_ship_bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.space_ship_bullets.remove(bullet)
                
        collisions = pygame.sprite.groupcollide(self.space_ship_bullets, self.space_ship_ufos, True, True)

        if not self.space_ship_ufos:
            # Pozbycie się istniejących pocisków i utworzenie nowej floty.
            self.space_ship_bullets.empty()
            self._create_fleet()

    def _update_ufos(self):
        """Sprawdzenie, czy flota obcych znajduje się przy krawędzi, a następnie uaktualnienie położenia wszystkich obcych we flocie."""
        for ufo in self.space_ship_ufos.copy():
            if ufo.check_edges():
                self.space_ship_ufos.remove(ufo)
        self.space_ship_ufos.update()

        # Wykrywanie kolizji między obcym i statkiem.
        if pygame.sprite.spritecollideany(self.space_ship, self.space_ship_ufos):
            self._ship_hit()
    
    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        # Utworzenie pełnej floty obcych.
        for ufo_number in range(self.settings.alien_limit):
            self._create_ufo(ufo_number)
            
    def _create_ufo(self, ufo_number):
        """Utworzenie obcego i umieszczenie go w rzędzie."""
        ufo = Ufo(self)
        self.space_ship_ufos.add(ufo)

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek."""
        if self.space_ship_stats.ships_left > 0:
            # Zmniejszenie wartości przechowywanej w ships_left.
            self.space_ship_stats.ships_left -= 1

            # Usunięcie zawartości list aliens i bullets.
            self.space_ship_ufos.empty()
            self.space_ship_bullets.empty()

            # Utworzenie nowej floty i wyśrodkowanie statku.
            self._create_fleet()
            self.space_ship.center_ship()

            # Pauza.
            sleep(0.5)

        else:
            self.space_ship_stats.game_active = False

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.space_ship.blitme()
        for bullet in self.space_ship_bullets.sprites():
            bullet.draw_bullet()
        self.space_ship_ufos.draw(self.screen)

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = SpaceShipGame()
    ai.run_game()