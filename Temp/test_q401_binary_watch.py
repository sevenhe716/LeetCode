import unittest

from Temp.q401_binary_watch import Solution


class TestBinaryWatch(unittest.TestCase):
    """Test q401_binary_watch.py"""

    def test_binary_watch(self):
        s = Solution()

        self.assertEqual(sorted(["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]), sorted(s.readBinaryWatch(1)))


if __name__ == '__main__':
    unittest.main()
