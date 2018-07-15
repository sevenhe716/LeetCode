import unittest

from Temp.q072_edit_distance import Solution


class TestEditDistance(unittest.TestCase):
    """Test q072_edit_distance.py"""

    def test_edit_distance(self):
        s = Solution()

        self.assertEqual(3, s.minDistance('horse', 'ros'))
        self.assertEqual(5, s.minDistance('intention', 'execution'))
        self.assertEqual(30, s.minDistance('pneumonoultramicroscopicsilicovolcanoconiosis', 'stereomicroscopically'))


if __name__ == '__main__':
    unittest.main()
