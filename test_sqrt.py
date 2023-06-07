import unittest
from calculator import sqrt
class _TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)

if __name__ == '__main__':
    unittest.main()