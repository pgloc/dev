class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku.
        self.ship_limit = 2

        # Ustawienia dotyczące pocisku.
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        # Ustawienia dotyczące celu.
        self.target_color = (255, 0, 0)
        self.target_width = 10
        self.target_height = 50

        # Łatwa zmiana szybkości gry.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed = 1.0
        self.bullet_speed = 1.0
        self.target_speed = 0.2
        
        # Wratość target_direction wynosząca 1 oznacza dół, natomiast -1 górę.
        self.target_direction = 1

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale