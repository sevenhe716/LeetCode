import unittest

from Matrix.q463_island_perimeter import Solution


class TestIslandPerimeter(unittest.TestCase):
    """Test q463_island_perimeter.py"""

    def test_island_perimeter(self):
        s = Solution()

        self.assertEqual(16, s.islandPerimeter([[0, 1, 0, 0],
                                                [1, 1, 1, 0],
                                                [0, 1, 0, 0],
                                                [1, 1, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
