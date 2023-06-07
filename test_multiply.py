import unittest
from calculator import multiply
class _TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(6, 2), 12)

if __name__ == '__main__':
    unittest.main()