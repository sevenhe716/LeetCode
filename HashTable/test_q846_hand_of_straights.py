import unittest

from HashTable.q846_hand_of_straights import Solution


class TestHandOfStraights(unittest.TestCase):
    """Test q846_hand_of_straights.py"""

    def test_hand_of_straights(self):
        s = Solution()

        self.assertEqual(False, s.isNStraightHand([1], 3))
        self.assertEqual(True, s.isNStraightHand([1], 1))
        self.assertEqual(True, s.isNStraightHand([5, 1], 1))
        self.assertEqual(True, s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
        self.assertEqual(True, s.isNStraightHand([1, 2, 2, 2, 3, 3, 3, 4, 4], 3))
        self.assertEqual(False, s.isNStraightHand([1, 2, 2, 2, 3, 2, 3, 4, 4], 3))
        self.assertEqual(False, s.isNStraightHand([1, 2, 3, 4, 5], 4))
        self.assertEqual(True, s.isNStraightHand([1, 2, 3, 4], 4))


if __name__ == '__main__':
    unittest.main()
