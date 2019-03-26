# Time:  O(nlogn)
# Space: O(n)

# 解题思路：
# TreeMap是最适合的结构，这里使用二分查找和二分插入
import bisect


class Solution:
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