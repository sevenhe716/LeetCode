import unittest

from LinkedList.q206_reverse_linked_list import Solution
from common import ListNode


class TestReverseLinkedList(unittest.TestCase):
    """Test q206_reverse_linked_list.py"""

    def test_reverse_linked_list(self):
        s = Solution()

        self.assertEqual(ListNode.generate([]), s.reverseList(ListNode.generate([])))
        self.assertEqual(ListNode.generate([5]), s.reverseList(ListNode.generate([5])))
        self.assertEqual(ListNode.generate([5, 1]), s.reverseList(ListNode.generate([1, 5])))
        self.assertEqual(ListNode.generate([3, 2, 1]), s.reverseList(ListNode.generate([1, 2, 3])))
        self.assertEqual(ListNode.generate([5, 4, 3, 2, 1]), s.reverseList(ListNode.generate([1, 2, 3, 4, 5])))

if __name__ == '__main__':
    unittest.main()
