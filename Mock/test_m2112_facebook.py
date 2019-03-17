import unittest

from Mock.m2112_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2112_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(4, s.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
        self.assertEqual(2, s.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))


if __name__ == '__main__':
    unittest.main()
