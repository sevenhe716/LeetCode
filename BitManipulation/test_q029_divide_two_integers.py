import unittest

from BitManipulation.q029_divide_two_integers import Solution


class TestDivideTwoIntegers(unittest.TestCase):
    """Test q029_divide_two_integers.py"""

    def test_divide_two_integers(self):
        s = Solution()

        self.assertEqual(3, s.divide(10, 3))
        self.assertEqual(1, s.divide(1, 1))
        self.assertEqual(3, s.divide(9, 3))
        self.assertEqual(2, s.divide(8, 3))
        self.assertEqual(-2, s.divide(7, -3))
        self.assertEqual(0, s.divide(0, -3))
        self.assertEqual(0, s.divide(0, 2))
        self.assertEqual(2147483647, s.divide(-2147483648, -1))


if __name__ == '__main__':
    unittest.main()
