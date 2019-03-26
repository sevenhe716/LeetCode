# Time:  O(n)
# Space: O(1)

# Ideas:
# heap?
import heapq


class Solution:
    def kClosest(self, points: 'List[List[int]]', K: int) -> 'List[List[int]]':
        # use key in nsmallest
        # return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])
        return [point for dist, point in heapq.nsmallest(K, ((p[0] * p[0] + p[1] * p[1], p) for p in points))]

