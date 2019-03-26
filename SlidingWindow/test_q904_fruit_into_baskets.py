import unittest

from SlidingWindow.q904_fruit_into_baskets import Solution


class TestFruitIntoBaskets(unittest.TestCase):
    """Test q904_fruit_into_baskets.py"""

    def test_fruit_into_baskets(self):
        s = Solution()

        self.assertEqual(3, s.totalFruit([1, 2, 1]))
        self.assertEqual(3, s.totalFruit([0, 1, 2, 2]))
        self.assertEqual(4, s.totalFruit([1, 2, 3, 2, 2]))
        self.assertEqual(5, s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))


if __name__ == '__main__':
    unittest.main()
