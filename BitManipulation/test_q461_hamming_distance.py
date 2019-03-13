import unittest

from BitManipulation.q461_hamming_distance import Solution


class TestHammingDistance(unittest.TestCase):
    """Test q461_hamming_distance.py"""

    def test_hamming_distance(self):
        s = Solution()

        self.assertEqual(2, s.hammingDistance(1, 4))
        # self.assertEqual(31, s.hammingDistance(1, -1))


if __name__ == '__main__':
    unittest.main()
