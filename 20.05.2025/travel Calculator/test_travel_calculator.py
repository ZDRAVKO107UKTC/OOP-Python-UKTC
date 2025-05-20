import unittest
from travel_calculator import get_distance_between_cities, calculate_travel_cost

class TestTravelCalculator(unittest.TestCase):

    def test_known_distances(self):
        self.assertEqual(get_distance_between_cities("София", "Пловдив"), 145)
        self.assertEqual(get_distance_between_cities("Пловдив", "София"), 145)
        self.assertEqual(get_distance_between_cities("Русе", "Варна"), 195)

    def test_unknown_distance(self):
        self.assertIsNone(get_distance_between_cities("София", "Лондон"))

    def test_calculate_cost_success(self):
        result = calculate_travel_cost("София", "Бургас", price_per_km=0.30)
        self.assertIn("Разстоянието между София и Бургас е 390 км", result)
        self.assertIn("117.00 лв", result)

    def test_calculate_cost_failure(self):
        result = calculate_travel_cost("София", "Париж")
        self.assertIn("Нямаме данни", result)

if __name__ == '__main__':
    unittest.main()
