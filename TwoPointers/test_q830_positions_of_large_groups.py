import unittest

from TwoPointers.q830_positions_of_large_groups import Solution


class TestPositionsOfLargeGroups(unittest.TestCase):
    """Test q830_positions_of_large_groups.py"""

    def test_positions_of_large_groups(self):
        s = Solution()

        self.assertEqual([], s.largeGroupPositions(''))
        self.assertEqual([], s.largeGroupPositions(None))
        self.assertEqual([[3, 6]], s.largeGroupPositions('abbxxxxzzy'))
        self.assertEqual([], s.largeGroupPositions("abc"))
        self.assertEqual([[2, 6]], s.largeGroupPositions("abccccc"))
        self.assertEqual([[3, 5], [6, 9], [12, 14]], s.largeGroupPositions("abcdddeeeeaabbbcd"))


if __name__ == '__main__':
    unittest.main()
