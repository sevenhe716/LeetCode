import unittest

from Mock.m2122_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2122_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual([24, 12, 8, 6], s.productExceptSelf([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
