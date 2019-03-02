import unittest

from PriorityQueue.q253_meeting_rooms_ii import Solution
from PriorityQueue.q253_meeting_rooms_ii import Interval


class TestMeetingRoomsIi(unittest.TestCase):
    """Test q253_meeting_rooms_ii.py"""

    def test_meeting_rooms_ii(self):
        s = Solution()

        self.assertEqual(2, s.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(1, s.minMeetingRooms([Interval(7, 10), Interval(2, 4)]))
        self.assertEqual(1, s.minMeetingRooms([Interval(7, 10)]))
        self.assertEqual(0, s.minMeetingRooms([]))


if __name__ == '__main__':
    unittest.main()
