import unittest

from Contests.c019 import Solution1
from Contests.c019 import Solution


class TestC019(unittest.TestCase):
    """Test test_c019.py"""

    def test_c019(self):
        s = Solution1()

        self.assertEqual('202', s.convertToBase7(100))
        self.assertEqual('-10', s.convertToBase7(-7))
        self.assertEqual('0', s.convertToBase7(0))

        s = Solution()
        self.assertEqual(0, s.reversePairs([]))
        self.assertEqual(0, s.reversePairs([1]))
        self.assertEqual(0, s.reversePairs([1, 3]))
        self.assertEqual(1, s.reversePairs([3, 1]))
        self.assertEqual(2, s.reversePairs([1, 3, 2, 3, 1]))
        self.assertEqual(3, s.reversePairs([2, 4, 3, 5, 1]))


if __name__ == '__main__':
    unittest.main()
