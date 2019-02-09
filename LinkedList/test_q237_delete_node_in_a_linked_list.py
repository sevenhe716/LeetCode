import unittest

from LinkedList.q237_delete_node_in_a_linked_list import Solution
from common import ListNode


class TestDeleteNodeInALinkedList(unittest.TestCase):
    """Test q237_delete_node_in_a_linked_list.py"""

    def test_delete_node_in_a_linked_list(self):
        s = Solution()

        head1 = ListNode.generate([4, 5, 1, 9])
        s.deleteNode(head1.find_by_val(5))
        self.assertEqual(ListNode.generate([4, 1, 9]), head1)

        head2 = ListNode.generate([4, 5, 1, 9])
        s.deleteNode(head2.find_by_val(4))
        self.assertEqual(ListNode.generate([5, 1, 9]), head2)

        head3 = ListNode.generate([4, 5, 1, 9])
        s.deleteNode(head3.find_by_val(1))
        self.assertEqual(ListNode.generate([4, 5, 9]), head3)


if __name__ == '__main__':
    unittest.main()
