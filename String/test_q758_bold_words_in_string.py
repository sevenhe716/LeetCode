import unittest

from String.q758_bold_words_in_string import Solution3


class TestBoldWordsInString(unittest.TestCase):
    """Test q758_bold_words_in_string.py"""

    def test_bold_words_in_string(self):
        s = Solution3()

        # self.assertEqual('a<b>abc</b>d', s.boldWords(["ab", "bc"], 'aabcd'))
        # self.assertEqual('<b>c</b>e<b>bc</b>e<b>cc</b>e<b>ab</b>',
        #                  s.boldWords(["b", "dee", "a", "ee", "c"], 'cebcecceab'))
        # self.assertEqual("cb<b>ccceee</b>ad", s.boldWords(["e", "cab", "de", "cc", "db"], "cbccceeead"))
        self.assertEqual("<b>ad</b>c<b>ad</b>d<b>ece</b>d", s.boldWords(["e", "ad", "ce", "a", "b"], "adcaddeced"))


if __name__ == '__main__':
    unittest.main()
