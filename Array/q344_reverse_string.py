# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        # ~的妙用，索引到水平镜像位置
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]

    def reverseString1(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()