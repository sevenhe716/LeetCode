# Time:  O(n)
# Space: O(1)

# Ideas:
# 按ratio排序，维护最小的K个quality
import heapq


class Solution:
    # TLE
    def mincostToHireWorkers(self, quality: 'List[int]', wage: 'List[int]', K: int) -> float:
        res = float('inf')
        for q1, w1 in zip(quality, wage):
            wages = [w1 / q1 * q2 for q2, w2 in zip(quality, wage) if w1 / q1 * q2 >= w2]
            if len(wages) >= K:
                res = min(res, sum(heapq.nsmallest(K, wages)))
        return res


class Solution1:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res
