# Time:  O(nlog(k))
# Space: O(k)

# 解题思路：
# K个最小值，考虑使用大顶堆
# 借鉴快排的思路，但对于前K个元素不再需要排序
import heapq
import random


class Solution:
    # 更简洁的写法
    def kClosest1(self, points: 'List[List[int]]', K: int) -> 'List[List[int]]':
        return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])

    # without using nsmallest
    def kClosest(self, points: 'List[List[int]]', K: int) -> 'List[List[int]]':
        heap = [(-p[0] * p[0] - p[1] * p[1], p) for p in points[:K]]
        heapq.heapify(heap)

        for p in points[K:]:
            # score = -p[0] * p[0] - p[1] * p[1]
            # if score > heap[0][0]:
            #     heapq.heapreplace(heap, (score, p))
            # 直接使用heappushpop
            heapq.heappushpop(heap, (-p[0] * p[0] - p[1] * p[1], p))
        return [h[1] for h in heap]


# Divide and Conquer, thoughts from quick sort
class Solution1:
    def kClosest(self, points, K):
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
