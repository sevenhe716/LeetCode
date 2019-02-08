import unittest

from LinkedList.q234_palindrome_linked_list import Solution1
from common import ListNode


class TestPalindromeLinkedList(unittest.TestCase):
    """Test q234_palindrome_linked_list.py"""

    def test_palindrome_linked_list(self):
        s = Solution1()

        # self.assertEqual(True, s.isPalindrome(ListNode.generate([])))
        # self.assertEqual(True, s.isPalindrome(ListNode.generate([1])))
        # self.assertEqual(False, s.isPalindrome(ListNode.generate([1, 2])))
        self.assertEqual(True, s.isPalindrome(ListNode.generate([1, 2, 2, 1])))


if __name__ == '__main__':
    unittest.main()
