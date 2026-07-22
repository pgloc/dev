import pygame

from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez obcych."""

    def __init__(self, ai_game, alien):
        """Utworzenie obiektu pocisku w aktualnym położeniu obcego."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Utworzenie prostokąta pocisku w punkcie (0, 0), a następnie zdefiniowanie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = alien.rect.midbottom

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej.
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku.
        self.y += self.settings.alien_bullet_speed
        # Uaktualnienie położenia prostokąta pocisku.
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)