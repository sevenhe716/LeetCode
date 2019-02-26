import unittest

from LinkedList.q086_partition_list import Solution
from common import ListNode


class TestPartitionList(unittest.TestCase):
    """Test q086_partition_list.py"""

    def test_partition_list(self):
        s = Solution()

        # self.assertEqual(ListNode.generate([1, 2, 2, 4, 3, 5]), s.partition(ListNode.generate([1, 4, 3, 2, 5, 2]), 3))
        # self.assertEqual(ListNode.generate([1, 4]), s.partition(ListNode.generate([4, 1]), 3))
        # self.assertEqual(ListNode.generate([]), s.partition(ListNode.generate([]), 3))
        # self.assertEqual(ListNode.generate([1, 2, 3]), s.partition(ListNode.generate([2, 1, 3]), 2))
        # self.assertEqual(ListNode.generate([1]), s.partition(ListNode.generate([1]), 2))
        # self.assertEqual(ListNode.generate([1]), s.partition(ListNode.generate([1]), 0))
        self.assertEqual(ListNode.generate([1, 2, 3]), s.partition(ListNode.generate([3, 1, 2]), 3))


if __name__ == '__main__':
    unittest.main()
