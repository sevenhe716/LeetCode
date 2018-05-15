import unittest

from HashTable.q001_two_sum import Solution


class TestTwoSum(unittest.TestCase):
    """Test q001_two_sum.py"""

    def test_twoSum(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], s.twoSum([2, 4, 4, 11, 15], 8))
        self.assertEqual([1, 2], s.twoSum([2, 4, 4], 8))
        self.assertEqual([0, 3], s.twoSum([2, 7, 11, 15], 17))
        self.assertEqual([0, 2], s.twoSum([3, 2, 3], 6))


if __name__ == '__main__':
    unittest.main()
