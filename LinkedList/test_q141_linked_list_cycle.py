import unittest

from LinkedList.q141_linked_list_cycle import Solution
from common import ListNode


class TestLinkedListCycle(unittest.TestCase):
    """Test q141_linked_list_cycle.py"""

    def test_linked_list_cycle(self):
        def addCycle(node, num):
            if num == -1 and not node:
                return
            i = 0
            cur_node = None
            while node.next:
                if i == num:
                    cur_node = node
                i = i + 1
                node = node.next
            node.next = cur_node

        s = Solution()

        # 重载了equal，因此有环时==有问题
        node1 = ListNode.generate([3, 2, 0, -4])
        addCycle(node1, 1)
        self.assertEqual(True, s.hasCycle(node1))

        node2 = ListNode.generate([1, 2])
        addCycle(node2, 0)
        self.assertEqual(True, s.hasCycle(node2))

        node3 = ListNode.generate([1])
        addCycle(node3, -1)
        self.assertEqual(False, s.hasCycle(node3))


if __name__ == '__main__':
    unittest.main()
