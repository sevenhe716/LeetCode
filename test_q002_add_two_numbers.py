import unittest

from q002_add_two_numbers import Solution
from common import ListNode


class TestAddTwoNum(unittest.TestCase):
    """Test q002_add_two_numbers.py"""

    def test_addTwoNumbers(self):
        s = Solution()

        # self.assertEqual(ListNode.generate([7, 0, 8]), ListNode.generate([7, 0, 8]))
        # self.assertEqual(ListNode.generate([7, 0, 8]),
        #                  s.addTwoNumbers(ListNode.generate([2, 4, 3]), ListNode.generate([5, 6, 4])))
        self.assertEqual(ListNode.generate([7, 0, 2, 1]),
                         s.addTwoNumbers(ListNode.generate([2, 4, 3]), ListNode.generate([5, 6, 8])))
        self.assertEqual(ListNode.generate([7, 0, 8, 1]),
                         s.addTwoNumbers(ListNode.generate([2, 4, 3, 1]), ListNode.generate([5, 6, 4])))
        self.assertEqual(ListNode.generate([7, 0, 0, 0, 0, 1]),
                         s.addTwoNumbers(ListNode.generate([2, 4, 3]), ListNode.generate([5, 6, 6, 9, 9])))
        self.assertEqual(None, s.addTwoNumbers(None, None))
        self.assertEqual(ListNode.generate([1, 2, 3]), s.addTwoNumbers(ListNode.generate([1, 2, 3]), ListNode.generate([0])))
        self.assertEqual(ListNode.generate([1, 2, 3]), s.addTwoNumbers(ListNode.generate([1, 2, 3]), None))


if __name__ == '__main__':
    unittest.main()
