import unittest
from calculator import add
class _TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 6)

if __name__ == '__main__':
    unittest.main()