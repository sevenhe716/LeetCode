import unittest

from Mock.m2213_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m2213_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual([
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ], s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    unittest.main()
