import unittest

from TwoPointers.q075_sort_colors import Solution


class TestSortColors(unittest.TestCase):
    """Test q075_sort_colors.py"""

    def test_sort_colors(self):
        s = Solution()

        arr = [2, 0, 2, 1, 1, 0]
        s.sortColors(arr)
        self.assertEqual([0, 0, 1, 1, 2, 2], arr)

        # arr = []
        # s.sortColors(arr)
        # self.assertEqual([], arr)
        #
        # arr = [0]
        # s.sortColors(arr)
        # self.assertEqual([0], arr)
        #
        # arr = [2, 0, 1]
        # s.sortColors(arr)
        # self.assertEqual([0, 1, 2], arr)
if __name__ == '__main__':
    unittest.main()
