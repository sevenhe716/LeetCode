import unittest

from Mock.m2132_facebook import Solution
from common import ListNode


class TestFacebook(unittest.TestCase):
    """Test m2132_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(ListNode.generate([7, 0, 8]),
                         s.addTwoNumbers(ListNode.generate([2, 4, 3]), ListNode.generate([5, 6, 4])))


if __name__ == '__main__':
    unittest.main()
