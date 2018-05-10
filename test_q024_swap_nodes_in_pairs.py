import unittest

from q024_swap_nodes_in_pairs import Solution
from common import ListNode


class TestSwapNodesInPairs(unittest.TestCase):
    """Test q024_swap_nodes_in_pairs.py"""

    def test_swap_nodes_in_pairs(self):
        s = Solution()

        self.assertEqual(ListNode.generate([]), s.swapPairs(ListNode.generate([])))
        self.assertEqual(ListNode.generate([1]), s.swapPairs(ListNode.generate([1])))
        self.assertEqual(ListNode.generate([2, 1]), s.swapPairs(ListNode.generate([1, 2])))
        self.assertEqual(ListNode.generate([2, 1, 3]), s.swapPairs(ListNode.generate([1, 2, 3])))
        self.assertEqual(ListNode.generate([2, 1, 4, 3]), s.swapPairs(ListNode.generate([1, 2, 3, 4])))
        self.assertEqual(ListNode.generate([2, 1, 4, 3, 5]), s.swapPairs(ListNode.generate([1, 2, 3, 4, 5])))


if __name__ == '__main__':
    unittest.main()
