import unittest

from Array.q031_next_permutation import Solution


class TestNextPermutation(unittest.TestCase):
    """Test q031_next_permutation.py"""

    def test_next_permutation(self):
        s = Solution()

        self.assertEqual([1, 1], s.nextPermutation([1, 1]))
        self.assertEqual([2, 0, 1, 2], s.nextPermutation([1, 2, 2, 0]))
        self.assertEqual([1, 0, 1], s.nextPermutation([0, 1, 1]))
        self.assertEqual([1], s.nextPermutation([1]))
        self.assertEqual([], s.nextPermutation([]))
        self.assertEqual([1, 3, 2], s.nextPermutation([1, 2, 3]))
        self.assertEqual([1, 2, 3], s.nextPermutation([3, 2, 1]))
        self.assertEqual([1, 5, 1], s.nextPermutation([1, 1, 5]))
        self.assertEqual([1, 2, 3, 4, 5], s.nextPermutation([5, 4, 3, 2, 1]))
        self.assertEqual([1, 3, 1, 2, 2, 5], s.nextPermutation([1, 2, 5, 3, 2, 1]))
        self.assertEqual([3, 1, 3, 3, 3, 3], s.nextPermutation([1, 3, 3, 3, 3, 3]))


if __name__ == '__main__':
    unittest.main()
