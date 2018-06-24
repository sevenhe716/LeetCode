import unittest

from Stack.q856_score_of_parentheses import Solution


class TestScoreOfParentheses(unittest.TestCase):
    """Test q856_score_of_parentheses.py"""

    def test_score_of_parentheses(self):
        s = Solution()

        self.assertEqual(1, s.scoreOfParentheses('()'))
        self.assertEqual(2, s.scoreOfParentheses('(())'))
        self.assertEqual(2, s.scoreOfParentheses('()()'))
        self.assertEqual(6, s.scoreOfParentheses('(()(()))'))
        self.assertEqual(3, s.scoreOfParentheses('()(())'))


if __name__ == '__main__':
    unittest.main()
