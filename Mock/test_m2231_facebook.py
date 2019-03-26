import unittest

from Mock.m2231_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2231_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual([
            [-1, 0, 1],
            [-1, -1, 2]
        ], s.threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    unittest.main()
