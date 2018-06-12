import unittest

from BinarySearch.q069_sqrt import Solution


class TestSqrt(unittest.TestCase):
    """Test q069_sqrt.py"""

    def test_sqrt(self):
        s = Solution()

        self.assertEqual(1, s.mySqrt(3))
        self.assertEqual(2, s.mySqrt(4))
        self.assertEqual(2, s.mySqrt(8))
        self.assertEqual(0, s.mySqrt(0))
        self.assertEqual(1, s.mySqrt(1))
        self.assertEqual(1, s.mySqrt(2))
        self.assertEqual(34611, s.mySqrt(1197958592))


if __name__ == '__main__':
    unittest.main()
