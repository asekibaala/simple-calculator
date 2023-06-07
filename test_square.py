import unittest
from calculator import square
class _TestSqaure(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

if __name__ == '__main__':
    unittest.main()