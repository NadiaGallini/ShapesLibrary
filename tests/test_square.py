import unittest
from shapes.square import Square

class TestSquare(unittest.TestCase):
    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

if __name__ == '__main__':
    unittest.main()