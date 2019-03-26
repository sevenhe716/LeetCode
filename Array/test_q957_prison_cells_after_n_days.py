import unittest

from Array.q957_prison_cells_after_n_days import Solution


class TestPrisonCellsAfterNDays(unittest.TestCase):
    """Test q957_prison_cells_after_n_days.py"""

    def test_prison_cells_after_n_days(self):
        s = Solution()

        self.assertEqual([0, 0, 1, 1, 0, 0, 0, 0], s.prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7))
        self.assertEqual([0, 0, 1, 1, 1, 1, 1, 0], s.prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))


if __name__ == '__main__':
    unittest.main()
