import unittest

from String.q383_ransom_note import Solution


class TestRansomNote(unittest.TestCase):
    """Test q383_ransom_note.py"""

    def test_ransom_note(self):
        s = Solution()

        self.assertEqual(False, s.canConstruct('a', 'b'))
        self.assertEqual(False, s.canConstruct('aa', 'ab'))
        self.assertEqual(True, s.canConstruct('aa', 'aab'))


if __name__ == '__main__':
    unittest.main()
