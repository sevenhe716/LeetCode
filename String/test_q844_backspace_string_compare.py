import unittest

from String.q844_backspace_string_compare import Solution


class TestBackspaceStringCompare(unittest.TestCase):
    """Test q844_backspace_string_compare.py"""

    def test_backspace_string_compare(self):
        s = Solution()

        self.assertEqual(True, s.backspaceCompare("ab#c", "ad#c"))
        self.assertEqual(True, s.backspaceCompare("ab##", "c#d#"))
        self.assertEqual(True, s.backspaceCompare("a##c", "#a#c"))
        self.assertEqual(False, s.backspaceCompare("a#c", "b"))
        self.assertEqual(True, s.backspaceCompare("du###vu##v#fbtu", "du###vu##v##fbtu"))


if __name__ == '__main__':
    unittest.main()
