# Time:  O(nlog(n))
# Space: O(n)

# 解题思路：
# 有一个思路，左右区间一同排序，遍历整个数组，左右计数器之差的最大值即位于同一个区间的最大区间数
import heapq


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> int:
        # sort start and end times together
        sorted_intervals = []
        for i in intervals:
            sorted_intervals.append((i.start, True))
            sorted_intervals.append((i.end, False))
        sorted_intervals.sort()

        # count how many rooms are in a meeting currently
        count, max_count = 0, 0
        for t, is_start in sorted_intervals:
            count += 1 if is_start else -1
            max_count = max(max_count, count)
        return max_count


class Solution1:
    # 优先级队列
    def minMeetingRooms(self, intervals: 'List[Interval]') -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

    # 双指针维护开始和结束时间，继而得出当前的房间数
    def minMeetingRooms1(self, intervals: 'List[Interval]') -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i.start for i in intervals])
        end_timings = sorted(i.end for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms
