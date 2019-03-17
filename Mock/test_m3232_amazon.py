import unittest

from Mock.m3232_amazon import Solution
from common import ListNode


class TestAmazon(unittest.TestCase):
    """Test m3232_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual(ListNode.generate([7, 0, 8]), s.addTwoNumbers(ListNode.generate([2, 4, 3]), ListNode.generate([5, 6, 4])))


if __name__ == '__main__':
    unittest.main()
