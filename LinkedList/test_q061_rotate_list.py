import unittest

from LinkedList.q061_rotate_list import Solution
from common import ListNode


class TestRotateList(unittest.TestCase):
    """Test q061_rotate_list.py"""

    def test_rotate_list(self):
        s = Solution()

        self.assertEqual(ListNode.generate([4, 5, 1, 2, 3]), s.rotateRight(ListNode.generate([1, 2, 3, 4, 5]), 2))
        self.assertEqual(ListNode.generate([1, 2, 3, 4, 5]), s.rotateRight(ListNode.generate([1, 2, 3, 4, 5]), 0))
        self.assertEqual(ListNode.generate([2, 0, 1]), s.rotateRight(ListNode.generate([0, 1, 2]), 4))
        self.assertEqual(None, s.rotateRight(None, 4))


if __name__ == '__main__':
    unittest.main()
