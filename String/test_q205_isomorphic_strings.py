import unittest

from String.q205_isomorphic_strings import Solution


class TestIsomorphicStrings(unittest.TestCase):
    """Test q205_isomorphic_strings.py"""

    def test_isomorphic_strings(self):
        s = Solution()

        self.assertEqual(True, s.isIsomorphic('egg', 'add'))
        self.assertEqual(False, s.isIsomorphic('foo', 'bar'))
        self.assertEqual(True, s.isIsomorphic('paper', 'title'))
        self.assertEqual(False, s.isIsomorphic('ab', 'aa'))


if __name__ == '__main__':
    unittest.main()
