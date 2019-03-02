import unittest

from HashTable.q266_palindrome_permutation import Solution1


class TestPalindromePermutation(unittest.TestCase):
    """Test q266_palindrome_permutation.py"""

    def test_palindrome_permutation(self):
        s = Solution1()

        self.assertEqual(False, s.canPermutePalindrome('code'))
        self.assertEqual(True, s.canPermutePalindrome('aab'))
        self.assertEqual(True, s.canPermutePalindrome('carerac'))


if __name__ == '__main__':
    unittest.main()
