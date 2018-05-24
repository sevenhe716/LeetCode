import unittest

from Tree.q493_reverse_pairs import Solution


class TestReversePairs(unittest.TestCase):
    """Test q493_reverse_pairs.py"""

    def test_reverse_pairs(self):
        s = Solution()
        self.assertEqual(0, s.reversePairs([]))
        self.assertEqual(0, s.reversePairs([1]))
        self.assertEqual(0, s.reversePairs([1, 3]))
        self.assertEqual(1, s.reversePairs([3, 1]))
        self.assertEqual(2, s.reversePairs([1, 3, 2, 3, 1]))
        self.assertEqual(3, s.reversePairs([2, 4, 3, 5, 1]))
        self.assertEqual(1, s.reversePairs([-5, -5]))


if __name__ == '__main__':
    unittest.main()
