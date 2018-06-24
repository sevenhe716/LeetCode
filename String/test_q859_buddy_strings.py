import unittest

from String.q859_buddy_strings import Solution


class TestBuddyStrings(unittest.TestCase):
    """Test q859_buddy_strings.py"""

    def test_buddy_strings(self):
        s = Solution()

        self.assertEqual(True, s.buddyStrings('ab', 'ba'))
        self.assertEqual(False, s.buddyStrings('ab', 'ab'))
        self.assertEqual(True, s.buddyStrings('aa', 'aa'))
        self.assertEqual(True, s.buddyStrings('aaaaaaabc', 'aaaaaaacb'))
        self.assertEqual(False, s.buddyStrings('', 'aa'))


if __name__ == '__main__':
    unittest.main()
