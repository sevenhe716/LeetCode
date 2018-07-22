import unittest

from BinarySearch.q875_koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    """Test q875_koko_eating_bananas.py"""

    def test_koko_eating_bananas(self):
        s = Solution()

        self.assertEqual(4, s.minEatingSpeed([3, 6, 7, 11], 8))
        self.assertEqual(30, s.minEatingSpeed([30, 11, 23, 4, 20], 5))
        self.assertEqual(23, s.minEatingSpeed([30, 11, 23, 4, 20], 6))


if __name__ == '__main__':
    unittest.main()
