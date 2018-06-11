# Time:  O(n)
# Space: O(1)

# 解题思路：
# interval起始部分满足cur.end >= new.start，新的起始点为min(cur.start, new.start)，
# 结束部分满足cur.start <= new.end，新的起始点为max(cur.end, new.end)
# 还需要单独考虑，与所有interval都不相交的情况

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from common import Interval


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        ans = []
        i = 0

        while i < len(intervals) and intervals[i].end < newInterval.start:
            ans.append([intervals[i].start, intervals[i].end])
            i += 1

        if i == len(intervals):
            ans.append([newInterval.start, newInterval.end])
            return ans

        # 不与任何一个interval相交
        if intervals[i].start > newInterval.end:
            ans.append([newInterval.start, newInterval.end])
            while i < len(intervals):
                ans.append([intervals[i].start, intervals[i].end])
                i += 1

            return ans

        start = min(intervals[i].start, newInterval.start)

        while i < len(intervals) and intervals[i].start <= newInterval.end:
            i += 1

        end = max(intervals[i-1].end, newInterval.end)

        ans.append([start, end])

        if i == len(intervals):
            return ans

        while i < len(intervals):
            ans.append([intervals[i].start, intervals[i].end])
            i += 1

        return ans


# 左右分别找到边界，然后合并区间
class SolutionF:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start, end = newInterval.start, newInterval.end
        left = [i for i in intervals if start > i.end]
        right = [i for i in intervals if end < i.start]
        if left + right != intervals:       # 这种方式比较是否有区间重叠，很精髓
            start = min(start, intervals[len(left)].start)
            end = max(end, intervals[~len(right)].end)      # 借鉴取反的写法，a[~i]即a[-i-1]
        return left + [Interval(start, end)] + right

