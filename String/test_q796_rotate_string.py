import unittest

from String.q796_rotate_string import Solution


class TestRotateString(unittest.TestCase):
    """Test q796_rotate_string.py"""

    def test_rotate_string(self):
        s = Solution()

        self.assertEqual(True, s.rotateString(A='abcde', B='cdeab'))
        self.assertEqual(False, s.rotateString(A='abcde', B='abced'))
        self.assertEqual(True, s.rotateString(A='', B=''))


if __name__ == '__main__':
    unittest.main()
