# Time:  O(vn) O(vlog(n))
# Space: O(1)

# 解题思路：
# 一种比较简单的思路是一个个的添加，但是有可能会TLE
# 每次添加会先向左到递减序列的最小值，当左侧值中大于该值之前都没有比其小的时，再同理往右找，最后放在中间
from heapq import *


class Solution:
    def pourWater(self, heights: 'List[int]', V: int, K: int) -> 'List[int]':
        def find_lowest(terrain_range, direct):
            find, find_idx = False, -1
            for i in terrain_range:
                if heights[i] > heights[i + direct]:
                    if find:
                        heights[find_idx] += 1
                    return find
                elif heights[i] < heights[i + direct]:
                    find, find_idx = True, i
            # 边界条件处理
            if find:
                heights[find_idx] += 1
            return find

        for _ in range(V):
            if find_lowest(range(K)[::-1], 1) or find_lowest(range(K + 1, len(heights)), -1):
                continue
            heights[K] += 1
        return heights


class Solution1:
    # 跟我的思路一样，但写法上更简单，遍历也可以一起完成，无需使用函数指针
    def pourWater1(self, heights: 'List[int]', V: int, K: int) -> 'List[int]':
        for _ in range(V):
            for d in (-1, 1):
                i = best = K
                while 0 <= i + d < len(heights) and heights[i + d] <= heights[i]:
                    if heights[i + d] < heights[i]:
                        best = i + d
                    i += d
                if best != K:
                    heights[best] += 1
                    break
            else:
                heights[K] += 1
        return heights

    # 堆（优先队列），时间复杂度从O(vn)降至O(vlogn)
    def pourWater(self, heights: 'List[int]', V: int, K: int) -> 'List[int]':
        n = len(heights)
        left_heap = []
        right_heap = []

        def move_left(l):
            while l > 0 and heights[l] >= heights[l - 1]:
                l -= 1
                # 取负的目的是，当高度相等时，会取到更靠近中间的索引
                heappush(left_heap, (heights[l], -l))
            return l

        def move_right(r):
            while r < n - 1 and heights[r] >= heights[r + 1]:
                r += 1
                heappush(right_heap, (heights[r], r))
            return r

        left = move_left(K)
        right = move_right(K)

        for _ in range(V):
            if left_heap and left_heap[0][0] < heights[K]:
                height, idx = heappop(left_heap)
                idx = abs(idx)
                heights[idx] += 1
                heappush(left_heap, (heights[idx], -idx))
                if idx == left:
                    left = move_left(left)
            elif right_heap and right_heap[0][0] < heights[K]:
                height, idx = heappop(right_heap)
                heights[idx] += 1
                heappush(right_heap, (heights[idx], idx))
                if idx == right:
                    right = move_right(right)
            else:
                heights[K] += 1
                if left == K:
                    left = move_left(left)
                if right == K:
                    right = move_right(right)
        return heights