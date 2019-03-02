import unittest

from Array.q252_meeting_rooms import Solution
from Array.q252_meeting_rooms import Interval


class TestMeetingRooms(unittest.TestCase):
    """Test q252_meeting_rooms.py"""

    def test_meeting_rooms(self):
        s = Solution()

        self.assertEqual(True, s.canAttendMeetings([Interval(7, 10)]))
        self.assertEqual(True, s.canAttendMeetings([]))
        self.assertEqual(False, s.canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(True, s.canAttendMeetings([Interval(7, 10), Interval(2, 4)]))


if __name__ == '__main__':
    unittest.main()
