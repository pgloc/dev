class GameStats:
    """Monitorowanie danych statystycznych w grze 'Inwazja obcych'."""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Uruchomienie gry 'Inwazja obcych' w stanie nieaktywnym.
        self.game_active = False

        # Sprawdzenie, czy użytkownik nacisnął przycisk Gra.
        self.play_clicked = False

        # Najlepszy wynik niegdy nie powinien zostać wyzerowany.
        self.save_score = 'save_score.txt'
        with open(self.save_score) as file_object:
            self.high_score = int(file_object.read())

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1