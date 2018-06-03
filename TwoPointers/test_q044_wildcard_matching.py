import unittest

from TwoPointers.q044_wildcard_matching import Solution1


class TestWildcardMatching(unittest.TestCase):
    """Test q044_wildcard_matching.py"""

    def test_wildcard_matching(self):
        s = Solution1()

        self.assertEqual(False, s.isMatch('aa', 'a'))
        self.assertEqual(True, s.isMatch('aa', '*'))
        self.assertEqual(False, s.isMatch('cb', '?a'))
        self.assertEqual(True, s.isMatch('adceb', 'a*b'))
        self.assertEqual(False, s.isMatch('acdcb', 'a*c?b'))
        self.assertEqual(True, s.isMatch('adceb', '*a*b'))
        self.assertEqual(True, s.isMatch('ho', 'ho**'))
        self.assertEqual(True, s.isMatch('abecwjb', 'a*********************************b'))
        self.assertEqual(True, s.isMatch('aa', 'a*'))


if __name__ == '__main__':
    unittest.main()
