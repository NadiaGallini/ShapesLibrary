import unittest
from shapes.shape import calculate_area
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.square import Square
import math

class TestShape(unittest.TestCase):
    def test_calculate_area(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        square = Square(4)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 25)
        self.assertAlmostEqual(calculate_area(triangle), 6)
        self.assertEqual(calculate_area(square), 16)

if __name__ == '__main__':
    unittest.main()
