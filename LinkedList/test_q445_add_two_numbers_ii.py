import unittest

from LinkedList.q445_add_two_numbers_ii import Solution
from common import ListNode


class TestAddTwoNumbersIi(unittest.TestCase):
    """Test q445_add_two_numbers_ii.py"""

    def test_add_two_numbers_ii(self):
        s = Solution()

        self.assertEqual(ListNode.generate([7, 8, 0, 7]),
                         s.addTwoNumbers(ListNode.generate([7, 2, 4, 3]), ListNode.generate([5, 6, 4])))
        self.assertEqual(ListNode.generate([0]),
                         s.addTwoNumbers(ListNode.generate([0]), ListNode.generate([0])))


if __name__ == '__main__':
    unittest.main()
