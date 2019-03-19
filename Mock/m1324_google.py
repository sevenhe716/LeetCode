# Time:  O(n)
# Space: O(1)

# Ideas:
# mark
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: 'List[int]', wage: 'List[int]', K: int) -> float:
        n = len(quality)
        # for i in range(len(wage)):
        #     print([max((wage[i] / quality[i]) * q, 0) for q, w in zip(quality, wage)])

        sorted_pay = sorted([(wage[i] * quality[i], i) for i in range(n)], reverse=True)
        wage_per_quality = sorted([(wage[i] / quality[i], i) for i in range(n)], reverse=True)

        wage_per_quality = []
        for i in range(K):
            _, idx = sorted_pay[i]
            wage_per_quality.append((wage[idx] / quality[idx], idx))

        wage_per_quality.sort(reverse=True)

        print(sorted_pay)
        print(wage_per_quality)

        # for i in range(n):
        #     # wage_per_quality[i]
        #     for j in range(i, n):
        #         pass
        #         # wage_per_quality[i] * quality[j]
        #     heapq.nsmallest(K, wage_per_quality[i:])



