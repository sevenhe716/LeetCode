import unittest

from TwoPointers.q088_merge_sorted_array import Solution


class TestMergeSortedArray(unittest.TestCase):
    """Test q088_merge_sorted_array.py"""

    def test_merge_sorted_array(self):
        s = Solution()

        a = [1, 2, 3, 0, 0, 0]
        s.merge(a, 3, [2, 5, 6], 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], a)

        a = [4, 5, 6, 0, 0, 0]
        s.merge(a, 3, [1, 2, 6], 3)
        self.assertEqual([1, 2, 4, 5, 6, 6], a)

        a = [0, 0, 0]
        s.merge(a, 0, [1, 2, 3], 3)
        self.assertEqual([1, 2, 3], a)

        a = [1, 2, 3]
        s.merge(a, 3, [], 0)
        self.assertEqual([1, 2, 3], a)

        a = []
        s.merge(a, 0, [], 0)
        self.assertEqual([], a)

        a = None
        s.merge(a, 0, None, 0)
        self.assertEqual(None, a)

if __name__ == '__main__':
    unittest.main()
