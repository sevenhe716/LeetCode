import unittest

from Greedy.q605_can_place_flowers import Solution


class TestCanPlaceFlowers(unittest.TestCase):
    """Test q605_can_place_flowers.py"""

    def test_can_place_flowers(self):
        s = Solution()

        self.assertEqual(True, s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertEqual(False, s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertEqual(True, s.canPlaceFlowers([0, 0, 1, 0, 1], 1))
        self.assertEqual(False, s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
        self.assertEqual(True, s.canPlaceFlowers([1, 0, 0, 0, 0], 2))
        self.assertEqual(True, s.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0))


if __name__ == '__main__':
    unittest.main()
