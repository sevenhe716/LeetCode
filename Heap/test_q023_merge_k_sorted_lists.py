import unittest

from Heap.q023_merge_k_sorted_lists import Solution
from common import ListNode


class TestMergeKSortedLists(unittest.TestCase):
    """Test q023_merge_k_sorted_lists.py"""

    def test_merge_k_sorted_lists(self):
        s = Solution()

        self.assertEqual(ListNode.generate([1, 1, 2, 3, 4, 4, 5, 6]), s.mergeKLists(
            [ListNode.generate([1, 4, 5]), ListNode.generate([1, 3, 4]), ListNode.generate([2, 6])]))
        self.assertEqual(ListNode.generate([1, 1, 3, 4, 4, 5]), s.mergeKLists(
            [ListNode.generate([1, 4, 5]), ListNode.generate([1, 3, 4]), ListNode.generate([])]))
        self.assertEqual(ListNode.generate([]), s.mergeKLists(
            [ListNode.generate([]), ListNode.generate([]), ListNode.generate([])]))
        self.assertEqual(ListNode.generate([2]), s.mergeKLists(
            [ListNode.generate([]), ListNode.generate([2]), ListNode.generate([])]))
        self.assertEqual(ListNode.generate([1, 2, 4, 5]), s.mergeKLists(
            [ListNode.generate([5]), ListNode.generate([1, 2, 4]), ListNode.generate([])]))


if __name__ == '__main__':
    unittest.main()
