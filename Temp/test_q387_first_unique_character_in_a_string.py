import unittest

from Temp.q387_first_unique_character_in_a_string import Solution


class TestFirstUniqueCharacterInAString(unittest.TestCase):
    """Test q387_first_unique_character_in_a_string.py"""

    def test_first_unique_character_in_a_string(self):
        s = Solution()

        self.assertEqual(0, s.firstUniqChar('leetcode'))
        self.assertEqual(2, s.firstUniqChar('loveleetcode'))
        self.assertEqual(-1, s.firstUniqChar('leoetctlocdde'))


if __name__ == '__main__':
    unittest.main()
