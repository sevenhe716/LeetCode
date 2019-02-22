import unittest

from Array.q077_combinations import Solution1


class TestCombinations(unittest.TestCase):
    """Test q077_combinations.py"""

    def test_combinations(self):
        s = Solution1()

        self.assertEqual(sorted([
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]), sorted(s.combine(4, 2)))

if __name__ == '__main__':
    unittest.main()
