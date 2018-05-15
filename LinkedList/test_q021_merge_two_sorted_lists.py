import unittest

from LinkedList.q021_merge_two_sorted_lists import Solution
from common import ListNode


class TestMergeTwoSortedLists(unittest.TestCase):
    """Test q021_merge_two_sorted_lists.py"""

    def test_merge_two_sorted_lists(self):
        s = Solution()

        self.assertEqual(ListNode.generate([1, 1, 2, 3, 4, 4]),
                         s.mergeTwoLists(ListNode.generate([1, 2, 4]), ListNode.generate([1, 3, 4])))
        self.assertEqual(ListNode.generate([1, 3, 4]),
                         s.mergeTwoLists(ListNode.generate([]), ListNode.generate([1, 3, 4])))
        self.assertEqual(ListNode.generate([1, 2, 4]),
                         s.mergeTwoLists(ListNode.generate([1, 2, 4]), ListNode.generate([])))
        self.assertEqual(ListNode.generate([]),
                         s.mergeTwoLists(ListNode.generate([]), ListNode.generate([])))
        self.assertEqual(ListNode.generate([1, 2, 3, 4]),
                         s.mergeTwoLists(ListNode.generate([1, 2]), ListNode.generate([3, 4])))
        self.assertEqual(ListNode.generate([1, 2, 3, 4]),
                         s.mergeTwoLists(ListNode.generate([3, 4]), ListNode.generate([1, 2])))


if __name__ == '__main__':
    unittest.main()
