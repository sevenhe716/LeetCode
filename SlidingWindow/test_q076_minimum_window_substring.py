import unittest

from SlidingWindow.q076_minimum_window_substring import Solution


class TestMinimumWindowSubstring(unittest.TestCase):
    """Test q076_minimum_window_substring.py"""

    def test_minimum_window_substring(self):
        s = Solution()

        self.assertEqual("", s.minWindow("ADOBECODEBANC", "ABCF"))
        self.assertEqual("", s.minWindow("", "ABC"))
        self.assertEqual("A", s.minWindow("A", "A"))
        self.assertEqual("", s.minWindow("A", "AA"))
        self.assertEqual("B", s.minWindow("AB", "B"))
        self.assertEqual("BANC", s.minWindow("ADOBECODEBANC", "ABC"))


if __name__ == '__main__':
    unittest.main()
