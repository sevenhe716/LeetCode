import unittest

from String.q681_next_closest_time import Solution


class TestNextClosestTime(unittest.TestCase):
    """Test q681_next_closest_time.py"""

    def test_next_closest_time(self):
        s = Solution()

        self.assertEqual("22:22", s.nextClosestTime("22:22"))
        self.assertEqual("00:00", s.nextClosestTime("00:00"))
        self.assertEqual("19:39", s.nextClosestTime("19:34"))
        self.assertEqual("22:22", s.nextClosestTime("23:59"))


if __name__ == '__main__':
    unittest.main()
