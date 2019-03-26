# Time:  O(nlogn)
# Space: O(n)

# 解题思路：
# TreeMap是最适合的结构，这里使用二分查找和二分插入
import bisect
from collections import deque


class Solution:
    # O(n^2)
    def kEmptySlots(self, flowers: 'List[int]', k: int) -> int:
        blooms = []
        for i, f in enumerate(flowers):
            idx = bisect.bisect_left(blooms, f)
            if idx > 0:
                if f - blooms[idx - 1] - 1 == k:
                    return i + 1
            if idx < len(blooms):
                if blooms[idx] - f - 1 == k:
                    return i + 1
            # 这里不需要再次使用bisect，会有两次二分查找的开销，直接insert
            # bisect.insort_left(blooms, f)
            blooms.insert(idx, f)

        return -1


class Solution1:
    # another similar solution, different in detail
    def kEmptySlots1(self, flowers, k):
        active = []
        # 末尾添加1，整合末尾的情况
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            # 处理i=0的情况
            for neighbor in active[i - (i > 0):i + 1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

    # min stack
    def kEmptySlots2(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i - k] < window.min() > days[i + 1]:
                    ans = min(ans, max(days[i - k], days[i + 1]))

        return ans if ans <= len(days) else -1

    # sliding windows
    def kEmptySlots3(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        return ans if ans < float('inf') else -1


class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]