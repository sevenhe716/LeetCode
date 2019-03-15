import unittest

from BFS.q286_walls_and_gates import Solution


class TestWallsAndGates(unittest.TestCase):
    """Test q286_walls_and_gates.py"""

    def test_walls_and_gates(self):
        s = Solution()

        rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
                 [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
        s.wallsAndGates(rooms)
        self.assertEqual([[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]], rooms)


if __name__ == '__main__':
    unittest.main()
