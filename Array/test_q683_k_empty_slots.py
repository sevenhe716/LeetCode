import unittest

from Array.q683_k_empty_slots import Solution


class TestKEmptySlots(unittest.TestCase):
    """Test q683_k_empty_slots.py"""

    def test_k_empty_slots(self):
        s = Solution()

        self.assertEqual(2, s.kEmptySlots([1, 3, 2], 1))
        self.assertEqual(-1, s.kEmptySlots([1, 2, 3], 1))


if __name__ == '__main__':
    unittest.main()
