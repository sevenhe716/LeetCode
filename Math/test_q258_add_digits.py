import unittest

from Math.q258_add_digits import Solution


class TestAddDigits(unittest.TestCase):
    """Test q258_add_digits.py"""

    def test_add_digits(self):
        s = Solution()

        self.assertEqual(2, s.addDigits(38))


if __name__ == '__main__':
    unittest.main()
