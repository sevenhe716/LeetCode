# Time:  O(n)
# Space: O(1)

# 解题思路：
# 难点是如何在N个人中选出K个最优解，需满足K个人能力所占的比例与工资比例最接近，且总工资最少
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141820/Python-Priority-Queue-with-explanation-O(N-log(K))
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)


class Solution:
    # brute
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """

class Solution1:
    def mincostToHireWorkers(self, quality, wage, K):
        import heapq
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        import queue as Q
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(wage)
        leet = sorted([[float(wage[i]) / quality[i], -quality[i], wage[i]] for i in range(n)])
        J = Q.PriorityQueue()
        temp, ans = 0, float("inf")

        # Start building the queue and find how much to pay to workers #1-#K-1 if we hire worker #K.
        for i in range(K - 1):
            J.put([leet[i][1], leet[i][2]])
            temp += -leet[i][1] * leet[K - 1][0]

        for i in range(K - 1, len(leet)):
            # Update the best answer.
            ans = min(ans, temp + leet[i][2])
            # If we got to the last worker, return the best answer.
            if i == len(leet) - 1:
                return ans
            # Add the new worker to the priority queue.
            J.put([leet[i][1], leet[i][2]])
            # Remove the worker with the highest quality from the priority queue.
            x = J.get()
            # Update the money we need to pay temp. Do not forget to scale by the ratio of the qualities.
            temp += x[0] * leet[i][0] + leet[i][2]
            temp *= leet[i + 1][0] / leet[i][0]

