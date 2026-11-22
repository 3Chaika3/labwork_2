import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_regular(self):
        """Проверка площади квадрата с целым положительным числом"""
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_zero(self):
        """Проверка площади квадрата с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        """Проверка площади квадрата с вещественной стороной"""
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_perimeter_regular(self):
        """Проверка периметра квадрата со стандартной стороной"""
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        """Проверка периметра квадрата с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        """Проверка периметра квадрата с вещественным значением"""
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14.0)


if __name__ == '__main__':
    unittest.main()