import unittest

from q019_remove_nth_from_end import Solution
from common import ListNode


class TestRemoveNthFromEnd(unittest.TestCase):
    """Test q019_remove_nth_from_end.py"""

    def test_remove_nth_from_end(self):
        s = Solution()

        self.assertEqual(ListNode.generate([2, 3, 4, 5]), s.removeNthFromEnd(ListNode.generate([1, 2, 3, 4, 5]), 5))
        self.assertEqual(ListNode.generate([1, 2, 3, 5]), s.removeNthFromEnd(ListNode.generate([1, 2, 3, 4, 5]), 2))
        self.assertEqual(ListNode.generate([1, 2, 3, 4]), s.removeNthFromEnd(ListNode.generate([1, 2, 3, 4, 5]), 1))
        self.assertEqual(ListNode.generate([]), s.removeNthFromEnd(ListNode.generate([1]), 1))


if __name__ == '__main__':
    unittest.main()
