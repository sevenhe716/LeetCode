import unittest

from Mock.m2223_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m2223_amazon.py"""

    def test_amazon(self):
        s = Solution()

        # self.assertEqual(4, s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
        # self.assertEqual(-1, s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
        # self.assertEqual(0, s.search(nums=[5, 1, 3], target=5))
        # self.assertEqual(4, s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8))
        self.assertEqual(1, s.search(nums=[3, 1], target=1))


if __name__ == '__main__':
    unittest.main()
