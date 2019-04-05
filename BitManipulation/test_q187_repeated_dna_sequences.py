import unittest

from BitManipulation.q187_repeated_dna_sequences import Solution


class TestRepeatedDnaSequences(unittest.TestCase):
    """Test q187_repeated_dna_sequences.py"""

    def test_repeated_dna_sequences(self):
        s = Solution()

        self.assertEqual(sorted(["AAAAACCCCC", "CCCCCAAAAA"]), sorted(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))


if __name__ == '__main__':
    unittest.main()
