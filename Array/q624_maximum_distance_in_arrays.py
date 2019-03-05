# Time:  O(nlogn)
# Space: O(n)

# 解题思路：
# 统计每个数组的最值，然后找到差值最大的，由于不能是同一个数组，则可以比较最小值，次最小值，最大值和次最大值，但需要考虑并列的情况
# 当最小值和最大值其中一个存在多个时，差值最大的依然最大值减最小值，只有当最大值和最小值只有一个，且来自同一个数组时
# 才需要找次最小值和次最大值，然后比较最大值-次最小值，次最大值-最小值
# 优化：事实上不需要排序，而是记录最值和次最值即可
# 优化：数组是已排序的


class Solution:
    def maxDistance1(self, arrays: 'List[List[int]]') -> int:
        min_idxs = sorted([(v, i) for i, v in enumerate(map(min, arrays))])
        max_idxs = sorted([(v, i) for i, v in enumerate(map(max, arrays))], reverse=True)

        # 当最大值和最小值只有一个，没有并列，且来自同一个数组时
        if min_idxs[0][0] != min_idxs[1][0] and max_idxs[0][0] != max_idxs[1][0] and min_idxs[0][1] == max_idxs[0][1]:
            return max(max_idxs[0][0] - min_idxs[1][0], max_idxs[1][0] - min_idxs[0][0])
        else:
            return max_idxs[0][0] - min_idxs[0][0]

    # largest two，可以考虑用堆，但是时间复杂更高
    def maxDistance2(self, arrays: 'List[List[int]]') -> int:
        min_idxs = [(v, i) for i, v in enumerate(map(min, arrays))]
        max_idxs = [(v, i) for i, v in enumerate(map(max, arrays))]
        min_idx1, min_idx2, max_idx1, max_idx2 = [float('inf'), -1], [float('inf'), -1], [float('-inf'), -1], [
            float('-inf'), -1]
        for min_idx, max_idx in zip(min_idxs, max_idxs):
            if min_idx[0] <= min_idx1[0]:
                min_idx2 = min_idx1
                min_idx1 = min_idx
            elif min_idx[0] <= min_idx2[0]:
                min_idx2 = min_idx
            if max_idx[0] >= max_idx1[0]:
                max_idx2 = max_idx1
                max_idx1 = max_idx
            elif max_idx[0] >= max_idx2[0]:
                max_idx2 = max_idx

        if min_idx1[0] != min_idx2[0] and max_idx1[0] != max_idx2[0] and min_idx1[1] == max_idx1[1]:
            return max(max_idx1[0] - min_idx2[0], max_idx2[0] - min_idx1[0])
        else:
            return max_idx1[0] - min_idx1[0]

    # 比较次数更少
    def maxDistance(self, arrays: 'List[List[int]]') -> int:
        min_idx1, min_idx2, max_idx1, max_idx2 = (float('inf'), -1), (float('inf'), -1), (float('-inf'), -1), (
        float('-inf'), -1)
        for i in range(len(arrays)):
            min_idx, max_idx = (arrays[i][0], i), (arrays[i][-1], i)
            if min_idx[0] <= min_idx1[0]:
                min_idx2 = min_idx1
                min_idx1 = min_idx
            elif min_idx[0] <= min_idx2[0]:
                min_idx2 = min_idx
            if max_idx[0] >= max_idx1[0]:
                max_idx2 = max_idx1
                max_idx1 = max_idx
            elif max_idx[0] >= max_idx2[0]:
                max_idx2 = max_idx

        if min_idx1[0] != min_idx2[0] and max_idx1[0] != max_idx2[0] and min_idx1[1] == max_idx1[1]:
            return max(max_idx1[0] - min_idx2[0], max_idx2[0] - min_idx1[0])
        else:
            return max_idx1[0] - min_idx1[0]


class Solution1:
    def maxDistance1(self, arrays: 'List[List[int]]') -> int:
        res, min_val, max_val = 0, arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - min_val, max_val - arrays[i][0])
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return res

    # 效率不高
    def maxDistance2(self, arrays):
        arrays.sort(key=lambda x: x[0])
        d1 = max(arr[-1] for arr in arrays[1:]) - arrays[0][0]
        arrays.sort(key=lambda x: x[-1])
        d2 = arrays[-1][-1] - min(arr[0] for arr in arrays[:-1])
        return max(d1, d2)
