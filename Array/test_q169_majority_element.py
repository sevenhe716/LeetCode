import unittest

from Array.q169_majority_element import Solution2


class TestMajorityElement(unittest.TestCase):
    """Test q169_majority_element.py"""

    def test_majority_element(self):
        s = Solution2()

        self.assertEqual(4, s.majorityElement([4, 4, 4, 1, 3]))
        self.assertEqual(3, s.majorityElement([3, 2, 3]))
        self.assertEqual(2, s.majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
