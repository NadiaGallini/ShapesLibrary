import unittest
from shapes.circle import Circle
import math

class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

if __name__ == '__main__':
    unittest.main()
