import unittest

from Math.q204_count_primes import Solution


class TestCountPrimes(unittest.TestCase):
    """Test q204_count_primes.py"""

    def test_count_primes(self):
        s = Solution()

        self.assertEqual(4, s.countPrimes(10))


if __name__ == '__main__':
    unittest.main()
