import unittest

from DFS.q351_android_unlock_patterns import Solution


class TestAndroidUnlockPatterns(unittest.TestCase):
    """Test q351_android_unlock_patterns.py"""

    def test_android_unlock_patterns(self):
        s = Solution()

        self.assertEqual(9, s.numberOfPatterns(1, 1))


if __name__ == '__main__':
    unittest.main()
