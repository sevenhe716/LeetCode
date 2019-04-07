import unittest

from BackTracking.q017_letter_combinations import Solution


class TestLetterCombinations(unittest.TestCase):
    """Test q017_letter_combinations.py"""

    def test_letter_combinations(self):
        s = Solution()

        self.assertEqual(sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]), sorted(s.letterCombinations("23")))
        self.assertEqual([], s.letterCombinations(""))



if __name__ == '__main__':
    unittest.main()
