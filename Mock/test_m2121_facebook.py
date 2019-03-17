import unittest

from Mock.m2121_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2121_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
