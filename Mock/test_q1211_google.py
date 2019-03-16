import unittest

from common import test_by_reflect


class TestGoogle(unittest.TestCase):
    """Test q1211_google.py"""

    def test_google(self):
        commands = ["MovingAverage", "next", "next", "next", "next"]
        params = [[3], [1], [10], [3], [5]]
        res = [None, 1, (1 + 10) / 2, (1 + 10 + 3) / 3, (10 + 3 + 5) / 3]
        test_by_reflect(self, 'q1211_google', commands, params, res)


if __name__ == '__main__':
    unittest.main()
