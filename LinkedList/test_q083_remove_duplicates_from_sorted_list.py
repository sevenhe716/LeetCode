import unittest

from LinkedList.q083_remove_duplicates_from_sorted_list import Solution
from common import ListNode

class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    """Test q083_remove_duplicates_from_sorted_list.py"""

    def test_remove_duplicates_from_sorted_list(self):
        s = Solution()

        self.assertEqual(ListNode.generate([1, 2]), s.deleteDuplicates(ListNode.generate([1, 1, 2])))
        self.assertEqual(ListNode.generate([1, 2, 3]), s.deleteDuplicates(ListNode.generate([1, 1, 2, 3, 3])))

if __name__ == '__main__':
    unittest.main()
