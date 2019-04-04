import unittest

from common import test_by_reflect


class TestMovingAverageFromDataStream(unittest.TestCase):
    """Test q346_moving_average_from_data_stream.py"""

    def test_moving_average_from_data_stream(self):
        commands = ["MovingAverage", "next", "next", "next", "next"]
        params = [[3], [1], [10], [3], [5]]
        res = [None, 1.0, 5.5, 4.666666666666667, 6.0]
        test_by_reflect(self, 'q346_moving_average_from_data_stream', commands, params, res)

    if __name__ == '__main__':
        unittest.main()
