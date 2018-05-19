import unittest

from String.q028_implement_strstr import Solution


class TestImplementStrStr(unittest.TestCase):
    """Test q028_implement_strstr.py"""

    def test_implement_strstr(self):
        s = Solution()

        self.assertEqual(2, s.strStr('hello', 'll'))
        self.assertEqual(-1, s.strStr('aaaaa', 'bba'))
        self.assertEqual(0, s.strStr('aaaaa', ''))


if __name__ == '__main__':
    unittest.main()
