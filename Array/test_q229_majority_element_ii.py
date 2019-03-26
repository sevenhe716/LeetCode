import unittest

from Array.q229_majority_element_ii import Solution


class TestMajorityElementIi(unittest.TestCase):
    """Test q229_majority_element_ii.py"""

    def test_majority_element_ii(self):
        s = Solution()

        self.assertEqual([3], s.majorityElement([3, 2, 3]))
        self.assertEqual([1, 2], s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
