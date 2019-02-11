import unittest

from BinarySearch.q367_valid_perfect_square import Solution


class TestValidPerfectSquare(unittest.TestCase):
    """Test q367_valid_perfect_square.py"""

    def test_valid_perfect_square(self):
        s = Solution()

        self.assertEqual(True, s.isPerfectSquare(16))
        self.assertEqual(False, s.isPerfectSquare(14))


if __name__ == '__main__':
    unittest.main()
