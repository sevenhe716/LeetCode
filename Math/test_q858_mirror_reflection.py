import unittest

from Math.q858_mirror_reflection import Solution


class TestMirrorReflection(unittest.TestCase):
    """Test q858_mirror_reflection.py"""

    def test_mirror_reflection(self):
        s = Solution()

        self.assertEqual(2, s.mirrorReflection(2, 1))
        self.assertEqual(0, s.mirrorReflection(3, 2))


if __name__ == '__main__':
    unittest.main()
