import unittest

from Mock.m3111_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3111_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual([0, 1], s.twoSum(nums=[2, 7, 11, 15], target=9))


if __name__ == '__main__':
    unittest.main()
