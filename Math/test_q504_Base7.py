import unittest

from Math.q504_Base7 import Solution


class TestBase7(unittest.TestCase):
    """Test q504_Base7.py"""

    def test_base7(self):
        s = Solution()

        self.assertEqual('202', s.convertToBase7(100))
        self.assertEqual('-10', s.convertToBase7(-7))
        self.assertEqual('0', s.convertToBase7(0))


if __name__ == '__main__':
    unittest.main()