import unittest

from String.q014_longest_common_prefix import SolutionF


class TestLongestCommonPrefix(unittest.TestCase):
    """Test q014_longest_common_prefix.py"""

    def test_longest_common_prefix(self):
        s = SolutionF()

        self.assertEqual('fl', s.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual('', s.longestCommonPrefix(["flower", "flow", ""]))
        self.assertEqual('f', s.longestCommonPrefix(["flower", "flow", "f"]))
        self.assertEqual('', s.longestCommonPrefix(["dog", "racecar", "car"]))
        self.assertEqual('', s.longestCommonPrefix([]))


if __name__ == '__main__':
    unittest.main()
