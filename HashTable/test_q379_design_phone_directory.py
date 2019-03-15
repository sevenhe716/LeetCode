import unittest

from common import test_by_reflect


class TestDesignPhoneDirectory(unittest.TestCase):
    """Test q379_design_phone_directory.py"""

    def test_design_phone_directory(self):
        commands = ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
        params = [[3], [], [], [2], [], [2], [2], [2]]
        res = [None, 0, 1, True, 2, False, None, True]

        test_by_reflect(self, 'q379_design_phone_directory', commands, params, res)


if __name__ == '__main__':
    unittest.main()
