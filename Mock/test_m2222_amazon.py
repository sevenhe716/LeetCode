import unittest

from Mock.m2222_amazon import Solution
from common import ListNode


class TestAmazon(unittest.TestCase):
    """Test m2222_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual(ListNode.generate([5, 4, 3, 2, 1]), s.reverseList(ListNode.generate([1, 2, 3, 4, 5])))
        self.assertEqual(ListNode.generate([1]), s.reverseList(ListNode.generate([1])))
        self.assertEqual(ListNode.generate([]), s.reverseList(ListNode.generate([])))


if __name__ == '__main__':
    unittest.main()
