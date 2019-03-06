# Time:  O(n)
# Space: O(1)

# 解题思路：
# 先得到最大深度，然后再dfs


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: 'List[NestedInteger]') -> int:
        def get_depth(nestedList):
            max_depth = 1
            for ni in nestedList:
                if not ni.isInteger():
                    max_depth = max(max_depth, get_depth(ni.getList()) + 1)
            return max_depth

        res = 0

        def dfs(nestedList, depth):
            nonlocal res
            for ni in nestedList:
                if not ni.isInteger():
                    dfs(ni.getList(), depth - 1)

            for ni in nestedList:
                if ni.isInteger():
                    res += depth * ni.getInteger()

        dfs(nestedList, get_depth(nestedList))
        return res
