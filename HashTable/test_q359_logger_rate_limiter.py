import unittest

from common import test_by_reflect


class TestLoggerRateLimiter(unittest.TestCase):
    """Test q359_logger_rate_limiter.py"""

    def test_logger_rate_limiter(self):
        commands = ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
                    "shouldPrintMessage", "shouldPrintMessage"]
        params = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
        res = [None, True, True, False, False, False, True]

        test_by_reflect(self, 'q359_logger_rate_limiter', commands, params, res)

    if __name__ == '__main__':
        unittest.main()
