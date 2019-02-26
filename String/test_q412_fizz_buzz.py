import unittest

from String.q412_fizz_buzz import Solution


class TestFizzBuzz(unittest.TestCase):
    """Test q412_fizz_buzz.py"""

    def test_fizz_buzz(self):
        s = Solution()

        self.assertEqual([
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
        ], s.fizzBuzz(5))

        self.assertEqual([
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
], s.fizzBuzz(15))


if __name__ == '__main__':
    unittest.main()
