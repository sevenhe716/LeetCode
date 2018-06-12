import unittest

from String.q068_text_justification import Solution1


class TestTextJustification(unittest.TestCase):
    """Test q068_text_justification.py"""

    def test_text_justification(self):
        s = Solution1()

        self.assertEqual([
            "This  ",
            "is    ",
        ], s.fullJustify(["This", "is"], 6))

        self.assertEqual([
            "This    is    an",
            "example  of text",
            "justification.  "
        ], s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

        self.assertEqual([
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ], s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))

        self.assertEqual([
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ], s.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                          "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))


if __name__ == '__main__':
    unittest.main()
