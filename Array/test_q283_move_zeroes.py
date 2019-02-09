import unittest

from Array.q283_move_zeroes import Solution


class TestMoveZeroes(unittest.TestCase):
    """Test q283_move_zeroes.py"""

    def test_move_zeroes(self):
        s = Solution()

        nums = [0, 1, 0, 3, 12]
        s.moveZeroes(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)


if __name__ == '__main__':
    unittest.main()
