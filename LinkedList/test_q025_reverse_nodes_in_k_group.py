import unittest

from LinkedList.q025_reverse_nodes_in_k_group import Solution
from common import ListNode


class TestReverseNodesInKGroup(unittest.TestCase):
    """Test q025_reverse_nodes_in_k_group.py"""

    def test_reverse_nodes_in_k_group(self):
        s = Solution()

        self.assertEqual(ListNode.generate([]), s.reverseKGroup(ListNode.generate([]), 2))
        self.assertEqual(ListNode.generate([1]), s.reverseKGroup(ListNode.generate([1]), 2))
        self.assertEqual(ListNode.generate([1, 2]), s.reverseKGroup(ListNode.generate([1, 2]), 3))
        self.assertEqual(ListNode.generate([1, 2, 3, 4, 5]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5]), 1))
        self.assertEqual(ListNode.generate([2, 1, 4, 3, 5]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5]), 2))
        self.assertEqual(ListNode.generate([3, 2, 1, 4, 5]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5]), 3))
        self.assertEqual(ListNode.generate([3, 2, 1, 6, 5, 4]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5, 6]), 3))
        self.assertEqual(ListNode.generate([3, 2, 1, 4]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4]), 3))


if __name__ == '__main__':
    unittest.main()
