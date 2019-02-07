import unittest

from Math.q172_factorial_trailing_zeroes import Solution


class TestFactorialTrailingZeroes(unittest.TestCase):
    """Test q172_factorial_trailing_zeroes.py"""

    def test_factorial_trailing_zeroes(self):
        s = Solution()

        self.assertEqual(0, s.trailingZeroes(3))
        self.assertEqual(1, s.trailingZeroes(5))
        self.assertEqual(7, s.trailingZeroes(30))
        self.assertEqual(452137076, s.trailingZeroes(1808548329))


if __name__ == '__main__':
    unittest.main()
