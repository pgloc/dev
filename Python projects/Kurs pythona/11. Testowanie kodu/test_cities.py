import unittest
from city_functions import get_formatted_text

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'."""

    def test_city_country(self):
        """Czy dane w postaci 'Santiago, Chile' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_text('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Czy dane w postaci 'Santiago, Chile - populacja 5000000' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_text('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - populacja 5000000')

if __name__ == '__main__':
    unittest.main()