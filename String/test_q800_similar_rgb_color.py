import unittest

from String.q800_similar_rgb_color import Solution


class TestSimilarRgbColor(unittest.TestCase):
    """Test q800_similar_rgb_color.py"""

    def test_similar_rgb_color(self):
        s = Solution()

        self.assertEqual("#11ee66", s.similarRGB("#09f166"))
        self.assertEqual("#00ee66", s.similarRGB("#02f166"))


if __name__ == '__main__':
    unittest.main()
