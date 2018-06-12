import unittest

from Math.q067_add_binary import Solution


class TestAddBinary(unittest.TestCase):
    """Test q067_add_binary.py"""

    def test_add_binary(self):
        s = Solution()

        self.assertEqual("100", s.addBinary("11", "1"))
        self.assertEqual("10101", s.addBinary("1010", "1011"))


if __name__ == '__main__':
    unittest.main()
