import unittest

from Mock.m2233_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m2233_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual([24, 12, 8, 6], s.productExceptSelf([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
