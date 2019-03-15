import unittest

from common import test_by_reflect


class TestDesignLogStorageSystem(unittest.TestCase):
    """Test q635_design_log_storage_system.py"""

    def test_design_log_storage_system(self):
        commands = ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
        params = [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"],
                  ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"],
                  ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
        res = [None, None, None, None, [3, 1, 2], [1, 2]]
        test_by_reflect(self, 'q635_design_log_storage_system', commands, params, res)


if __name__ == '__main__':
    unittest.main()
