# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """

        n = len(group)

        total = 2 ** n - 1

        profit1 = [p for p in profit if p < P].sort()
        

