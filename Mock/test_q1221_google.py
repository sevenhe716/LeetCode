import unittest

from Mock.q1221_google import Solution


class TestGoogle(unittest.TestCase):
    """Test q1221_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(True, s.backspaceCompare("ab#c", "ad#c"))
        self.assertEqual(True, s.backspaceCompare("ab##", "c#d#"))
        self.assertEqual(True, s.backspaceCompare("a##c", "#a#c"))
        self.assertEqual(False, s.backspaceCompare("a#c", "b"))


if __name__ == '__main__':
    unittest.main()
