import unittest

from Mock.m1312_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1312_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(True, s.areSentencesSimilarTwo(words1=["great", "acting", "skills"],
                                                        words2=["fine", "drama", "talent"],
                                                        pairs=[["great", "good"], ["fine", "good"], ["acting", "drama"],
                                                               ["skills", "talent"]]))

        self.assertEqual(True, s.areSentencesSimilarTwo(["a", "very", "delicious", "meal"],
                                                        ["one", "really", "delicious", "dinner"],
                                                        [["great", "good"], ["extraordinary", "good"], ["well", "good"],
                                                         ["wonderful", "good"], ["excellent", "good"],
                                                         ["fine", "good"], ["nice", "good"], ["any", "one"],
                                                         ["some", "one"], ["unique", "one"], ["the", "one"],
                                                         ["an", "one"], ["single", "one"], ["a", "one"],
                                                         ["truck", "car"], ["wagon", "car"], ["automobile", "car"],
                                                         ["auto", "car"], ["vehicle", "car"], ["entertain", "have"],
                                                         ["drink", "have"], ["eat", "have"], ["take", "have"],
                                                         ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"],
                                                         ["food", "meal"], ["dinner", "meal"],
                                                         ["super", "meal"], ["lunch", "meal"], ["possess", "own"],
                                                         ["keep", "own"], ["have", "own"], ["extremely", "very"],
                                                         ["actually", "very"], ["really", "very"], ["super", "very"]]))

if __name__ == '__main__':
    unittest.main()
