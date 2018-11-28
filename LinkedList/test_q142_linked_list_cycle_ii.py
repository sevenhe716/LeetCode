import unittest

from LinkedList.q142_linked_list_cycle_ii import Solution
from common import ListNode


class TestLinkedListCycleIi(unittest.TestCase):
    """Test q142_linked_list_cycle_ii.py"""

    def test_linked_list_cycle_ii(self):
        s = Solution()

        list1 = ListNode.generate([1, 2, 3, 4, 5, 6])
        cycle_start = list1.find_by_value(3)
        list1.find_by_value(6).next = cycle_start

        self.assertTrue(cycle_start is s.detectCycle(list1))
        self.assertEqual(None, s.detectCycle(ListNode.generate([1, 2, 3, 4, 5, 6])))
        self.assertEqual(None, s.detectCycle(ListNode.generate([1])))
        self.assertEqual(None, s.detectCycle(ListNode.generate([])))

if __name__ == '__main__':
    unittest.main()
