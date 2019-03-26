# Time:  O(n^4)
# Space: O(1)

# 解题思路：
# 建立坐标到1的map，将问题从二维化归到一维，并且减少了0值的判断，计算两个map所有元素对的差值，寻找差值最多即可
# 这种解法需要确定的一点是，差值最多的是否是最大解
# 优化思路：如果1值比较多时，应该使用0值作为索引，所以可以在之前先统计一下1值的个数，选择个数较少的作为索引值（不成立，题目要求的是1）


class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        import collections

        N = len(A)

        # count = sum([A[i][j] + B[i][j] for i in range(N) for j in range(N)])
        # flag = 1 if count < N * N << 1 else 0

        LA = [(i, j) for i in range(N) for j in range(N) if A[i][j]]    # flag ^ A[i][j]
        LB = [(i, j) for i in range(N) for j in range(N) if B[i][j]]

        counter = collections.defaultdict(int)      # defaultdict比counter快
        for (i1, j1) in LA:
            for (i2, j2) in LB:
                counter[(i1-i2, j1-j2)] += 1

        return max(counter.values() or [0])

    def largestOverlap1(self, A, B):
        import collections
        N = len(A)
        LA = [i / N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
        LB = [i / N * 100 + i % N for i in range(N * N) if B[i // N][i % N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])
