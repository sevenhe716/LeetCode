import unittest

from Mock.m4331_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4331_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual("A", s.convertToTitle(1))
        self.assertEqual("AB", s.convertToTitle(28))
        self.assertEqual("ZY", s.convertToTitle(701))


if __name__ == '__main__':
    unittest.main()
