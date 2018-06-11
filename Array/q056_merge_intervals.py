# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# 先排序，排序后，arr1[1] >= arr2[0] 则二者相交，进行合并，然后再继续进行比较


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        cur = [intervals[0].start, intervals[0].end]

        ans = []
        for i in range(1, len(intervals)):
            if cur[1] >= intervals[i].start:
                cur = [cur[0], max(cur[1], intervals[i].end)]
            else:
                ans.append(cur)
                cur = [intervals[i].start, intervals[i].end]

        ans.append(cur)
        return ans


# 思路类似，但这个解法不需要cur，直接放入尾部，然后进行比较和更改
class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged