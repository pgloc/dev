import pygame

from pygame.sprite import Sprite

class SpaceShipBullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek."""

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku."""
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)

        # Utworzenie prostokąta pocisku w punkcie (0, 0), a następnie zdefiniowanie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midleft = ai_game.space_ship.rect.midright

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej.
        self.x = float(self.rect.x)

    def update(self):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku.
        self.x += 1.5
        # Uaktualnienie położenia prostokąta pocisku.
        self.rect.x = self.x

    def draw_bullet(self):
        """Wyświetlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)