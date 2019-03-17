import unittest

from Mock.m4132_microsoft import Solution
from common import ListNode


class TestMicrosoft(unittest.TestCase):
    """Test m4132_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(ListNode.generate([7, 8, 0, 7]),
                         s.addTwoNumbers(ListNode.generate([7, 2, 4, 3]), ListNode.generate([5, 6, 4])))
        self.assertEqual(ListNode.generate([0]),
                         s.addTwoNumbers(ListNode.generate([0]), ListNode.generate([0])))


if __name__ == '__main__':
    unittest.main()
