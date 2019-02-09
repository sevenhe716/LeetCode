import unittest

from String.q345_reverse_vowels_of_a_string import Solution


class TestReverseVowelsOfAString(unittest.TestCase):
    """Test q345_reverse_vowels_of_a_string.py"""

    def test_reverse_vowels_of_a_string(self):
        s = Solution()

        self.assertEqual('', s.reverseVowels(''))
        self.assertEqual('a', s.reverseVowels('a'))
        self.assertEqual('ea', s.reverseVowels('ae'))
        self.assertEqual('b', s.reverseVowels('b'))
        self.assertEqual('holle', s.reverseVowels('hello'))
        self.assertEqual('leotcede', s.reverseVowels('leetcode'))


if __name__ == '__main__':
    unittest.main()
