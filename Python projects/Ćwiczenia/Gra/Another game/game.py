import sys
from time import sleep
import pygame

from settings import Settings
from stats import GameStats
from ship import Ship
from target import Target
from bullet import Bullet
from button import Button

class Game:
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
        pygame.display.set_caption("Gra")

        # Utworzenie egzemplarza przechowującego dane statystyczne dotyczące gry.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Utworzenie przycisku Gra.
        self.play_button = Button(self, "Gra")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
                
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry po kliknięciu przycisku Gra przez użytkownika."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Wyzerowanie ustawień dotyczących gry.
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_g:
            self._start_game()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _start_game(self):
        """Rozpoczęcie nowej gry."""
        # Wyzerowanie danych statystycznych gry.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Usunięcie zawartości listy bullets.
        self.bullets.empty()
        self.ship.center_ship()

        # Ukrycie kursora myszy.
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        # Uaktualnienie położenia pocisków.
        self.bullets.update()

        # Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self._miss()

        self._check_bullet_target_collisions()

    def _check_bullet_target_collisions(self):
        """Reakcja na kolizję między pociskiem i celem."""
        # Usunięcie wszystkich pocisków i celów, między którymi doszło do kolizji.
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            self.bullets.empty()
            sleep(0.5)
            self.settings.increase_speed()

    def _update_target(self):
        """Uaktualnienie położenia celu."""
        self.target.update()
        self._check_target_edges()

    def _check_target_edges(self):
        """Odpowiednia reakcja, gdy cel dotrze do krawędzi ekranu."""
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        """Zmiana kierunku ruchu celu."""
        self.settings.target_direction *= -1

    def _miss(self):
        """Reakcja na chybienie celu."""
        if self.stats.ships_left > 0:
            # Zmniejszenie wartości przechowywanej w ships_left.
            self.stats.ships_left -= 1

            # Usunięcie zawartości listy bullets.
            self.bullets.empty()

            # Wyśrodkowanie statku.
            self.ship.center_ship()

            # Pauza.
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()

        # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = Game()
    ai.run_game()