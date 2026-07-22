import sys
from time import sleep
import pygame
import pygame.mixer
import random

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from bullet import Bullet
from alien_bullet import AlienBullet
from button import Button

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Fullscreen.
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        # Utworzenie egzemplarza przechowującego dane statystyczne dotyczące gry oraz utworzenie egzemplarza klasy Scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()

        self._create_fleet()

        # Utworzenie przycisku Gra.
        self.play_button = Button(self, "Gra")

        # Utworzenie przycisków dotyczących poziomu trudności.
        self.easy_button = Button(self, "Łatwy")
        self.medium_button = Button(self, "Średni")
        self.hard_button = Button(self, "Trudny")

        # Zaczytanie muzyki w tle.
        pygame.mixer.music.load("sounds/background.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullet()

                current_time = pygame.time.get_ticks()

                if current_time - self.settings.last_alien_shot > self.settings.alien_shot_delay:
                    self._alien_fire()
                    self.settings.last_alien_shot = current_time
                
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
                self._check_mode_buttons(mouse_pos)
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry po kliknięciu przycisku Gra przez użytkownika."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active and not self.stats.play_clicked:
            # Wyzerowanie ustawień dotyczących gry.
            self._mode_buttons_show()

    def _check_mode_buttons(self, mouse_pos):
        """Rozpoczęcie nowej gry po wybraniu poziomu trudności przez użytkownika."""
        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if not self.stats.game_active and self.stats.play_clicked:
            if easy_clicked:
                self._start_game()
            if medium_clicked:
                self._set_medium_mode()
                self._start_game()
            if hard_clicked:
                self._set_hard_mode()
                self._start_game()

    def _set_medium_mode(self):
        """Średni poziom trudności."""
        self.settings.alien_speed = 0.5
        self.settings.bullet_speed = 1.5
        self.settings.ship_speed = 1.5
        self.settings.alien_points = 100
        self.settings.alien_bullet_speed = 0.5
        self.settings.alien_shot_delay = 800

    def _set_hard_mode(self):
        """Trudny poziom trudności."""
        self.settings.alien_speed = 1
        self.settings.bullet_speed = 2
        self.settings.ship_speed = 2
        self.settings.alien_points = 200
        self.settings.alien_bullet_speed = 1
        self.settings.alien_shot_delay = 500

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            with open(self.stats.save_score, 'w') as file_object:
                file_object.write(str(self.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_g:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self._mode_buttons_show()

    def _mode_buttons_show(self):
        """Pokazanie i pozycjonowanie przycisków dotyczących poziomu trudności."""
        self.settings.initialize_dynamic_settings()
        self.stats.play_clicked = True
        self.easy_button.rect.y = self.medium_button.rect.y - self.medium_button.height * 2
        self.easy_button.msg_image_rect.center = self.easy_button.rect.center
        self.hard_button.rect.y = self.medium_button.rect.y + self.medium_button.height * 2
        self.hard_button.msg_image_rect.center = self.hard_button.rect.center

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _start_game(self):
        """Rozpoczęcie nowej gry."""
        # Wyzerowanie danych statystycznych gry.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()

        # Usunięcie zawartości list aliens i bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Utworzenie nowej floty i wyśrodkowanie statku.
        self._create_fleet()
        self.ship.center_ship()

        # Ukrycie kursora myszy.
        pygame.mouse.set_visible(False)

    def _start_new_level(self):
        """Rozpoczęcie nowego poziomu."""
        # Pozbycie się istniejących pocisków i utworzenie nowej floty.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Inkrementacja numeru poziomu.
        self.stats.level += 1
        self.sb.prep_level()

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.shoot_sound.play()

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        # Uaktualnienie położenia pocisków.
        self.bullets.update()

        # Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reakcja na kolizję między pociskiem i obcym."""
        # Usunięcie wszystkich pocisków i obcych, między którymi doszło do kolizji.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.settings.explosion_sound.play()

        if not self.aliens:
            self._start_new_level()

    def _update_aliens(self):
        """Sprawdzenie, czy flota obcych znajduje się przy krawędzi, a następnie uaktualnienie położenia wszystkich obcych we flocie."""
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między obcym i statkiem.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Wykrywanie obcych docierających do dolnej krawędzi ekranu.
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszcząsię w rzędzie.
        # Odległość między poszczególnymi obcymi jest równa szerokości obcego.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Ustalenie, ile rzędów obcych zmieści się na ekranie.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Utworzenie pełnej floty obcych.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzędzie."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona porusza."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Sprawdzenie, czy którykolwiek obcy dotarł do dolnej krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Tak samo jak w przypadku zderzenia statku z obcym.
                self._ship_hit()
                break

    def _alien_fire(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.aliens) == 0:
            return

        # Losowy wybór istniejącego obcego.
        alien = random.choice(self.aliens.sprites())

        bullet = AlienBullet(self, alien)
        self.alien_bullets.add(bullet)

    def _update_alien_bullet(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        # Uaktualnienie położenia pocisków.
        self.alien_bullets.update()

        # Usunięcie pocisków, które znajdują się poza ekranem.
        for alien_bullet in self.alien_bullets.copy():
            if alien_bullet.rect.top >= self.screen.get_rect().height:
                self.alien_bullets.remove(alien_bullet)

        self._check_alien_bullet_ship_collision()

    def _check_alien_bullet_ship_collision(self):
        """Sprawdzenie, czy jakiś pocisk obcego trafił statek."""
        # Wykrywanie kolizji między pociskiem i statkiem.
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek."""
        if self.stats.ships_left > 0:
            # Zmniejszenie wartości przechowywanej w ships_left i uaktualnienie tablicy wyników.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Usunięcie zawartości list aliens i bullets.
            self.aliens.empty()
            self.bullets.empty()
            self.alien_bullets.empty()

            # Utworzenie nowej floty i wyśrodkowanie statku.
            self._create_fleet()
            self.ship.center_ship()

            self.settings.explosion_sound.play()

            # Pauza.
            sleep(0.5)

        else:
            self.stats.game_active = False
            self.stats.play_clicked = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        for alien_bullet in self.alien_bullets.sprites():
            alien_bullet.draw_bullet()

        # Wyświetlenie informacji o punktacji.
        self.sb.show_score()

        # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
        if not self.stats.game_active:
            if not self.stats.play_clicked:
                self.play_button.draw_button()
            else:
                self.easy_button.draw_button()
                self.medium_button.draw_button()
                self.hard_button.draw_button()

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()