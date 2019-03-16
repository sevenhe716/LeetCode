import unittest

from Mock.q1131_google import Solution


class TestInterview31(unittest.TestCase):
    """Test q1131_google.py"""

    def test_interview_3_1(self):
        s = Solution()

        self.assertEqual("19:39", s.nextClosestTime("19:34"))
        self.assertEqual("22:22", s.nextClosestTime("23:59"))
        self.assertEqual("15:11", s.nextClosestTime("13:55"))



if __name__ == '__main__':
    unittest.main()
