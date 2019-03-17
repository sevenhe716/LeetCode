import unittest

from Mock.m2111_facebook import Solution
from common import ListNode


class TestFacebook(unittest.TestCase):
    """Test m2111_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(ListNode.generate([1, 1, 2, 3, 4, 4]),
                         s.mergeTwoLists(ListNode.generate([1, 2, 4]), ListNode.generate([1, 3, 4])))


if __name__ == '__main__':
    unittest.main()
