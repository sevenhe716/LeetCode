import unittest

from DFS.q851_loud_and_rich import Solution


class TestLoudAndRich(unittest.TestCase):
    """Test q851_loud_and_rich.py"""

    def test_loud_and_rich(self):
        s = Solution()

        self.assertEqual([5, 5, 2, 5, 4, 5, 6, 7],
                         s.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                                       [3, 2, 5, 4, 6, 1, 7, 0]))


if __name__ == '__main__':
    unittest.main()
