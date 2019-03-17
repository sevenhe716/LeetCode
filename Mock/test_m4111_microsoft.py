import unittest

from Mock.m4111_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4111_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(True, s.rotateString(A='abcde', B='cdeab'))
        self.assertEqual(False, s.rotateString(A='abcde', B='abced'))
        self.assertEqual(True, s.rotateString(A='', B=''))


if __name__ == '__main__':
    unittest.main()
