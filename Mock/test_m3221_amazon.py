import unittest

from Mock.m3221_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3221_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual(0, s.firstUniqChar("leetcode"))
        self.assertEqual(2, s.firstUniqChar("loveleetcode"))


if __name__ == '__main__':
    unittest.main()
