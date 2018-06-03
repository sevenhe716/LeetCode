import unittest

from Array.q845_longest_mountain_in_array import Solution


class TestLongestMountainInArray(unittest.TestCase):
    """Test q845_longest_mountain_in_array.py"""

    def test_longest_mountain_in_array(self):
        s = Solution()

        self.assertEqual(5, s.longestMountain([2, 1, 4, 7, 3, 2, 5]))
        self.assertEqual(0, s.longestMountain([2, 2, 2]))
        self.assertEqual(0, s.longestMountain([]))
        self.assertEqual(11, s.longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))
        self.assertEqual(3, s.longestMountain([0, 2, 1]))


if __name__ == '__main__':
    unittest.main()
