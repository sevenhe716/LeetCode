import unittest

from TwoPointers.q026_remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    """Test q026_remove_duplicates_from_sorted_array.py"""

    def test_remove_duplicates_from_sorted_array(self):
        s = Solution()

        a1 = [1, 1, 2]
        self.assertEqual(2, s.removeDuplicates(a1))
        self.assertEqual([1, 2], a1[:2])
        a2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, s.removeDuplicates(a2))
        self.assertEqual([0, 1, 2, 3, 4], a2[:5])
        a3 = []
        self.assertEqual(0, s.removeDuplicates(a3))
        self.assertEqual([], a3[:0])
        a4 = [1]
        self.assertEqual(1, s.removeDuplicates(a4))
        self.assertEqual([1], a4[:1])


if __name__ == '__main__':
    unittest.main()
