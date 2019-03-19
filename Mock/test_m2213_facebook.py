import unittest

from Mock.m2213_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2213_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(sorted([]), sorted(s.addOperators(num="", target=5)))
        self.assertEqual(sorted(["1+2+3", "1*2*3"]), sorted(s.addOperators(num="123", target=6)))
        self.assertEqual(sorted(["2*3+2", "2+3*2"]), sorted(s.addOperators(num="232", target=8)))
        self.assertEqual(sorted(["1*0+5", "10-5"]), sorted(s.addOperators(num="105", target=5)))
        self.assertEqual(sorted(["0+0", "0-0", "0*0"]), sorted(s.addOperators(num="00", target=0)))
        self.assertEqual([], s.addOperators(num="3456237490", target=9191))


if __name__ == '__main__':
    unittest.main()
