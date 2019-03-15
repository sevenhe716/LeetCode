import unittest

from String.q271_encode_and_decode_strings import Codec


class TestEncodeAndDecodeStrings(unittest.TestCase):
    """Test q271_encode_and_decode_strings.py"""

    def test_encode_and_decode_strings(self):
        s = Codec()

        self.assertEqual(["Hello", "World"], s.decode(s.encode(["Hello", "World"])))


if __name__ == '__main__':
    unittest.main()
