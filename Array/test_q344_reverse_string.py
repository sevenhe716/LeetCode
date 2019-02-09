import unittest

from Array.q344_reverse_string import Solution


class TestReverseString(unittest.TestCase):
    """Test q344_reverse_string.py"""

    def test_reverse_string(self):
        s = Solution()
        str1 = ["h", "e", "l", "l", "o"]
        s.reverseString(str1)
        self.assertEqual(["o", "l", "l", "e", "h"], str1)

        str2 = ["H", "a", "n", "n", "a", "h"]
        s.reverseString(str2)
        self.assertEqual(["h", "a", "n", "n", "a", "H"], str2)


if __name__ == '__main__':
    unittest.main()
