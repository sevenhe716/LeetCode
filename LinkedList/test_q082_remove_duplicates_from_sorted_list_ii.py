import unittest

from LinkedList.q082_remove_duplicates_from_sorted_list_ii import Solution
from common import ListNode


class TestRemoveDuplicatesFromSortedListIi(unittest.TestCase):
    """Test q082_remove_duplicates_from_sorted_list_ii.py"""

    def test_remove_duplicates_from_sorted_list_ii(self):
        s = Solution()

        self.assertEqual(ListNode.generate([]), s.deleteDuplicates(ListNode.generate([])))
        self.assertEqual(ListNode.generate([1]), s.deleteDuplicates(ListNode.generate([1])))
        self.assertEqual(ListNode.generate([]), s.deleteDuplicates(ListNode.generate([1, 1])))
        self.assertEqual(ListNode.generate([1, 2, 5]), s.deleteDuplicates(ListNode.generate([1, 2, 3, 3, 4, 4, 5])))
        self.assertEqual(ListNode.generate([2, 3]), s.deleteDuplicates(ListNode.generate([1, 1, 1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
