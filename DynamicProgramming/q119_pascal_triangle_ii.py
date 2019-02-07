# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1] * (rowIndex + 1)
        for i in range(rowIndex+1):
            cur = ret[0]
            for j in range(i-1):
                ret[j+1], cur = ret[j+1] + cur, ret[j+1]
        return ret

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 加了这句，就快了很多，呵呵，LeetCode trick
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        ret = [1] * (rowIndex + 1)
        for i in range(rowIndex+1):
            cur = ret[0]
            for j in range(i-1):
                ret[j+1], cur = ret[j+1] + cur, ret[j+1]
        return ret
