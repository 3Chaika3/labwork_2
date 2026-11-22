import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_regular(self):
        """Проверка площади треугольника со стандартными параметрами"""
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_zero_side(self):
        """Проверка площади треугольника при нулевой стороне"""
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        """Проверка площади треугольника при нулевой высоте"""
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        """Проверка площади треугольника с вещественными числами"""
        res = area(3.5, 4.2)
        self.assertAlmostEqual(res, 7.35)

    def test_perimeter_regular(self):
        """Проверка периметра произвольного треугольника"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_equilateral(self):
        """Проверка периметра равностороннего треугольника"""
        res = perimeter(7, 7, 7)
        self.assertEqual(res, 21)

    def test_perimeter_float(self):
        """Проверка периметра треугольника с вещественными сторонами"""
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)


if __name__ == '__main__':
    unittest.main()