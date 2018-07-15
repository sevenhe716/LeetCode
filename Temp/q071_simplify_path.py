# Time:  O(n)
# Space: O(1)

# 解题思路：
# 规则：移除最右的/，//->/，a/../抵消，/../特殊情况


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
