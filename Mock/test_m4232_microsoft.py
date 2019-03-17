import unittest

from Mock.m4232_microsoft import Solution
from common import ListNode


class TestMicrosoft(unittest.TestCase):
    """Test m4232_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(ListNode.generate([2, 1, 4, 3]), s.swapPairs(ListNode.generate([1, 2, 3, 4])))


if __name__ == '__main__':
    unittest.main()
