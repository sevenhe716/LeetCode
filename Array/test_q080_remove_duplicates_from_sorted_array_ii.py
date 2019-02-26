import unittest

from Array.q080_remove_duplicates_from_sorted_array_ii import Solution


class TestRemoveDuplicatesFromSortedArrayIi(unittest.TestCase):
    """Test q080_remove_duplicates_from_sorted_array_ii.py"""

    def test_remove_duplicates_from_sorted_array_ii(self):
        s = Solution()

        arr = [1, 1, 1, 2, 2, 3]
        self.assertEqual(5, s.removeDuplicates(arr))
        self.assertEqual([1, 1, 2, 2, 3], arr[:5])
        arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.assertEqual(7, s.removeDuplicates(arr))
        self.assertEqual([0, 0, 1, 1, 2, 3, 3], arr[:7])


if __name__ == '__main__':
    unittest.main()
