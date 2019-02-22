import unittest

from Math.q400_nth_digit import Solution


class TestNthDigit(unittest.TestCase):
    """Test q400_nth_digit.py"""

    def test_nth_digit(self):
        s = Solution()

        self.assertEqual(1, s.findNthDigit(10))
        self.assertEqual(3, s.findNthDigit(3))
        self.assertEqual(0, s.findNthDigit(11))
        self.assertEqual(1, s.findNthDigit(12))
        self.assertEqual(1, s.findNthDigit(190))


if __name__ == '__main__':
    unittest.main()
