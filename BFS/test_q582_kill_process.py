import unittest

from BFS.q582_kill_process import Solution


class TestKillProcess(unittest.TestCase):
    """Test q582_kill_process.py"""

    def test_kill_process(self):
        s = Solution()

        self.assertEqual(sorted([5, 10]), sorted(s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)))


if __name__ == '__main__':
    unittest.main()
