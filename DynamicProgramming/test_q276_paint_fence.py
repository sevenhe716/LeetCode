import unittest

from DynamicProgramming.q276_paint_fence import Solution


class TestPaintFence(unittest.TestCase):
    """Test q276_paint_fence.py"""

    def test_paint_fence(self):
        s = Solution()

        self.assertEqual(6, s.numWays(3, 2))
        self.assertEqual(0, s.numWays(0, 3))
        self.assertEqual(3, s.numWays(1, 3))
        self.assertEqual(9, s.numWays(2, 3))
        self.assertEqual(24, s.numWays(3, 3))
        self.assertEqual(66, s.numWays(4, 3))
        self.assertEqual(180, s.numWays(5, 3))
        self.assertEqual(492, s.numWays(6, 3))


if __name__ == '__main__':
    unittest.main()
