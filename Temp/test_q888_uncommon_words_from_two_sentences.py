import unittest

from Temp.q888_uncommon_words_from_two_sentences import Solution


class TestUncommonWordsFromTwoSentences(unittest.TestCase):
    """Test q888_uncommon_words_from_two_sentences.py"""

    def test_uncommon_words_from_two_sentences(self):
        s = Solution()

        self.assertEqual(["sweet", "sour"], s.uncommonFromSentences("this apple is sweet", "this apple is sour"))
        self.assertEqual(["banana"], s.uncommonFromSentences("apple apple", "banana"))


if __name__ == '__main__':
    unittest.main()
