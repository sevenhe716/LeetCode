import unittest

from BinarySearch.q374_guess_number_higher_or_lower import Solution1
from BinarySearch import q374_guess_number_higher_or_lower


class TestGuessNumberHigherOrLower(unittest.TestCase):
    """Test q374_guess_number_higher_or_lower.py"""

    def test_guess_number_higher_or_lower(self):
        s = Solution1()
        q374_guess_number_higher_or_lower.pick = 6
        self.assertEqual(6, s.guessNumber(10))


if __name__ == '__main__':
    unittest.main()
