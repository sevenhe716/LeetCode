import unittest

from TwoPointers.q027_remove_element import Solution


class TestRemoveElement(unittest.TestCase):
    """Test q027_remove_element.py"""

    def test_remove_element(self):
        s = Solution()

        a1 = [3, 2, 2, 3]
        self.assertEqual(2, s.removeElement(a1, 3))
        self.assertEqual([2, 2], a1[:2])
        a2 = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(5, s.removeElement(a2, 2))
        self.assertEqual(sorted([0, 1, 3, 0, 4]), sorted(a2[:5]))
        a3 = []
        self.assertEqual(0, s.removeElement(a3, 2))
        self.assertEqual([], a3[:0])
        a4 = [1]
        self.assertEqual(1, s.removeElement(a4, 2))
        self.assertEqual([1], a4[:1])
        a5 = [3, 2, 3, 3, 3, 3, 2, 3]
        self.assertEqual(2, s.removeElement(a5, 3))
        self.assertEqual([2, 2], a5[:2])
        a6 = [1, 1]
        self.assertEqual(0, s.removeElement(a6, 1))
        self.assertEqual([], a6[:0])
        a7 = [1]
        self.assertEqual(0, s.removeElement(a7, 1))
        self.assertEqual([], a7[:0])
        a8 = [4, 5]
        self.assertEqual(1, s.removeElement(a8, 4))
        self.assertEqual([5], a8[:1])
        a9 = [1, 1, 1]
        self.assertEqual(0, s.removeElement(a9, 1))
        self.assertEqual([], a9[:0])
        a10 = [1, 2, 1, 1]
        self.assertEqual(1, s.removeElement(a10, 1))
        self.assertEqual([2], a10[:1])
        a11 = [2, 2, 3]
        self.assertEqual(1, s.removeElement(a11, 2))
        self.assertEqual([3], a11[:1])


if __name__ == '__main__':
    unittest.main()
