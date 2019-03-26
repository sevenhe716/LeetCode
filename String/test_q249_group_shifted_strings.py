import unittest

from String.q249_group_shifted_strings import Solution


class TestGroupShiftedStrings(unittest.TestCase):
    """Test q249_group_shifted_strings.py"""

    def test_group_shifted_strings(self):
        s = Solution()

        self.assertEqual(sorted([
            ["abc", "bcd", "xyz"],
            ["az", "ba"],
            ["acef"],
            ["a", "z"]
        ]), sorted(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])))


if __name__ == '__main__':
    unittest.main()
