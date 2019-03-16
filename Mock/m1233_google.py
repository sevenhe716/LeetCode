# Time:  O(nlogn)
# Space: O(1)

# Ideas:
# sort and merge it


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: (x.start, x.end))
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1].end >= interval.start:
                if res[-1].end < interval.end:
                    res[-1].end = interval.end
            else:
                res.append(interval)

        return res
