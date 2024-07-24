import unittest
from shapes.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
    
    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
    
    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())
        
        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right_angle())
        
        triangle = Triangle(6, 8, 10)
        self.assertTrue(triangle.is_right_angle())
        
        triangle = Triangle(3, 3, 3)
        self.assertFalse(triangle.is_right_angle())

if __name__ == '__main__':
    unittest.main()
