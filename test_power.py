import unittest
from calculator import power
class _TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(4,2), 16)

if __name__ == '__main__':
    unittest.main()