import unittest

from DynamicProgramming.q032_longest_valid_parentheses import Solution


class TestLongestValidParentheses(unittest.TestCase):
    """Test q032_longest_valid_parentheses.py"""

    def test_longest_valid_parentheses(self):
        s = Solution()

        self.assertEqual(2, s.longestValidParentheses("(()"))
        self.assertEqual(4, s.longestValidParentheses(")()())"))
        self.assertEqual(0, s.longestValidParentheses("))(("))
        self.assertEqual(0, s.longestValidParentheses(""))
        self.assertEqual(6, s.longestValidParentheses("(()())"))
        self.assertEqual(6, s.longestValidParentheses("()(())"))
        self.assertEqual(22, s.longestValidParentheses(")(((((()())()()))()(()))("))

        # )(  ((((()())()()))()  (())) (


if __name__ == '__main__':
    unittest.main()
