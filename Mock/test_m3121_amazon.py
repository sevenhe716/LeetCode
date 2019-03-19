import unittest

from Mock.m3121_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3121_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual('ball', s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                                                  banned=["hit"]))
        self.assertEqual('b', s.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c",
                                               banned=["a"]))


if __name__ == '__main__':
    unittest.main()
