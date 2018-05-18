import unittest

from Contests.c083 import Solution


class TestC083(unittest.TestCase):
    """Test test_c083.py"""

    def test_c083(self):
        s = Solution()

        self.assertEqual([], s.largeGroupPositions(''))
        self.assertEqual([], s.largeGroupPositions(None))
        self.assertEqual([[3, 6]], s.largeGroupPositions('abbxxxxzzy'))
        self.assertEqual([], s.largeGroupPositions("abc"))
        self.assertEqual([[2, 6]], s.largeGroupPositions("abccccc"))
        self.assertEqual([[3, 5], [6, 9], [12, 14]], s.largeGroupPositions("abcdddeeeeaabbbcd"))

        self.assertEqual("l*****e@leetcode.com", s.maskPII("LeetCode@LeetCode.com"))
        self.assertEqual("a*****b@qq.com", s.maskPII("AB@qq.com"))
        self.assertEqual("***-***-7890", s.maskPII("1(234)567-890"))
        self.assertEqual("+**-***-***-5678", s.maskPII("86-(10)12345678"))

        self.assertEqual(1, s.consecutiveNumbersSum(1))
        self.assertEqual(2, s.consecutiveNumbersSum(5))
        self.assertEqual(3, s.consecutiveNumbersSum(9))
        self.assertEqual(4, s.consecutiveNumbersSum(15))
        self.assertEqual(2, s.consecutiveNumbersSum(3))

        self.assertEqual(10, s.uniqueLetterString('ABC'))
        self.assertEqual(8, s.uniqueLetterString('ABA'))
        self.assertEqual(1, s.uniqueLetterString('A'))
        self.assertEqual(0, s.uniqueLetterString(''))


if __name__ == '__main__':
    unittest.main()
