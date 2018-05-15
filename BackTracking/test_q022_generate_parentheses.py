import unittest

from BackTracking.q022_generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    """Test q022_generate_parentheses.py"""

    def test_generate_parentheses(self):
        s = Solution()

        self.assertEqual([
            "()",
        ], s.generateParenthesis(1))
        self.assertEqual(sorted([
            "(())",
            "()()",
        ]), sorted(s.generateParenthesis(2)))
        self.assertEqual(sorted([
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]), sorted(s.generateParenthesis(3)))


if __name__ == '__main__':
    unittest.main()
