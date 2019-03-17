import unittest

from Mock.m4324_microsoft import Solution
from common import ListNode


class TestMicrosoft(unittest.TestCase):
    """Test m4324_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(ListNode.generate([2, 1, 4, 3, 5]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5]), 2))
        # self.assertEqual(ListNode.generate([3, 2, 1, 4, 5]), s.reverseKGroup(ListNode.generate([1, 2, 3, 4, 5]), 3))


if __name__ == '__main__':
    unittest.main()
