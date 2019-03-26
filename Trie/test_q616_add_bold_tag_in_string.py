import unittest

from Trie.q616_add_bold_tag_in_string import Solution


class TestAddBoldTagInString(unittest.TestCase):
    """Test q616_add_bold_tag_in_string.py"""

    def test_add_bold_tag_in_string(self):
        s = Solution()

        self.assertEqual("<b>abc</b>xyz<b>123</b>", s.addBoldTag("abcxyz123", ["abc", "123"]))
        self.assertEqual("<b>aaabbc</b>c", s.addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))


if __name__ == '__main__':
    unittest.main()
