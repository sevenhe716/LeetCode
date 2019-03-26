import unittest

from Matrix.q675_cut_off_trees_for_golf_event import Solution


class TestCutOffTreesForGolfEvent(unittest.TestCase):
    """Test q675_cut_off_trees_for_golf_event.py"""

    def test_cut_off_trees_for_golf_event(self):
        s = Solution()

        self.assertEqual(6, s.cutOffTree([
            [1, 2, 3],
            [0, 0, 4],
            [7, 6, 5]
        ]))
        self.assertEqual(-1, s.cutOffTree([
            [1, 2, 3],
            [0, 0, 0],
            [7, 6, 5]
        ]))
        self.assertEqual(6, s.cutOffTree([
            [2, 3, 4],
            [0, 0, 5],
            [8, 7, 6]
        ]))


if __name__ == '__main__':
    unittest.main()
