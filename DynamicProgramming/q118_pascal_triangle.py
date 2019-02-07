# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[] for _ in range(numRows)]
        ret[0] = [1]
        for i in range(1, numRows):
            ret[i] = [1] * (i + 1)
            for j in range(len(ret[i-1])-1):
                ret[i][j+1] = ret[i-1][j] + ret[i-1][j+1]
        return ret
