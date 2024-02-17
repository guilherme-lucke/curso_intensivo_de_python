import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = get_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile.')
    
    def test_city_country_population(self):
        formatted = get_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted, 'Santiago, Chile - população 5000000.')


unittest.main()
