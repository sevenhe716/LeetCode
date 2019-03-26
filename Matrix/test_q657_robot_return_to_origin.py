import unittest

from Matrix.q657_robot_return_to_origin import Solution


class TestRobotReturnToOrigin(unittest.TestCase):
    """Test q657_robot_return_to_origin.py"""

    def test_robot_return_to_origin(self):
        s = Solution()

        self.assertEqual(True, s.judgeCircle("UD"))
        self.assertEqual(False, s.judgeCircle("LL"))


if __name__ == '__main__':
    unittest.main()
