import unittest

from BackTracking.q010_regular_expression_matching import Solution


class TestRegularExpressionMatching(unittest.TestCase):
    """Test q010_regular_expression_matching.py"""

    def test_regular_expression_matching(self):
        s = Solution()

        self.assertEqual(False, s.isMatch('aa', 'a'))
        self.assertEqual(True, s.isMatch('aa', 'a*'))
        self.assertEqual(True, s.isMatch('ab', '.*'))
        self.assertEqual(True, s.isMatch('aab', 'c*a*b'))
        self.assertEqual(False, s.isMatch('mississippi', 'mis*is*p*'))
        self.assertEqual(True, s.isMatch('', '.*'))
        self.assertEqual(False, s.isMatch('', '.'))
        self.assertEqual(False, s.isMatch('aaaaaaaaaaaaab', 'a*a*a*ba*a*a*aaa*a*a*a*c'))
        self.assertEqual(False, s.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))
        self.assertEqual(True, s.isMatch('aaaaaaaaaaaaab', 'a*a*a*ab*a*a*a*a*a*a*'))
        self.assertEqual(True, s.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*b'))
        self.assertEqual(True, s.isMatch('acfjeiwojabfiejfjeibewfejiabbbcaaaaa', 'ab*cd*e*.*e*abe*w*.*a*.*t*..bew.*abb*b*bbcaaaaa'))
        self.assertEqual(False, s.isMatch('acfjeiwojabfiejfjeibewfejiabbcaaaaa', 'ab*cd*e*.*e*abe*w*.*a*.*t*..bew.*abb*b*bbcaaaaa'))
        self.assertEqual(True, s.isMatch('aaabbccddeee', 'a*b*c*d*e*'))
        self.assertEqual(True, s.isMatch('abcde', 'a*b*c*d*e*'))
        self.assertEqual(False, s.isMatch('a', '.*..a*'))
        self.assertEqual(True, s.isMatch('abeefwaaaa', '.*.*.*.*.*.*..a*'))
        self.assertEqual(True, s.isMatch('aefaaaa', '.*.*.*.*.*.*..a*'))
        self.assertEqual(False, s.isMatch('a', '.*...*.*....*.*.*.*...a*'))
        self.assertEqual(False, s.isMatch('acaabbaccbbacaabbbb', 'a*.*b*.*a*aa*a*'))


if __name__ == '__main__':
    unittest.main()
