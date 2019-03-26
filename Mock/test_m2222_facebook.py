import unittest

from Mock.m2222_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2222_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(2, s.subarraySum([1, 1, 1], 2))


if __name__ == '__main__':
    unittest.main()
