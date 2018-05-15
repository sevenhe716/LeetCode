import unittest

from Stack.q020_valid_parenthese import Solution


class TestValidParenthese(unittest.TestCase):
    """Test q020_valid_parenthese.py"""

    def test_valid_parenthese(self):
        s = Solution()

        self.assertEqual(True, s.isValid("()"))
        self.assertEqual(True, s.isValid("()[]{}"))
        self.assertEqual(False, s.isValid("(]"))
        self.assertEqual(False, s.isValid("([)]"))
        self.assertEqual(True, s.isValid("{[]}"))
        self.assertEqual(True, s.isValid(""))
        self.assertEqual(False, s.isValid("a"))
        self.assertEqual(False, s.isValid("[b]"))
        self.assertEqual(False, s.isValid("["))


if __name__ == '__main__':
    unittest.main()
