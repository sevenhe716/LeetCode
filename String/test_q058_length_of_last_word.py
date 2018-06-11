import unittest

from String.q058_length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    """Test q058_length_of_last_word.py"""

    def test_length_of_last_word(self):
        s = Solution()

        self.assertEqual(5, s.lengthOfLastWord("Hello World"))
        self.assertEqual(0, s.lengthOfLastWord("     "))
        self.assertEqual(4, s.lengthOfLastWord("  fjewl fewj   "))
        self.assertEqual(3, s.lengthOfLastWord("abc     "))
        self.assertEqual(3, s.lengthOfLastWord("     abc"))
        self.assertEqual(0, s.lengthOfLastWord(""))


if __name__ == '__main__':
    unittest.main()
