import unittest

from Mock.m4212_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4212_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(45, s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))


if __name__ == '__main__':
    unittest.main()
