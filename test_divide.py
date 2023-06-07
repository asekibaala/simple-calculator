import unittest
from calculator import divide
class _TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

if __name__ == '__main__':
    unittest.main()