# Time:  O(n)
# Space: O(1)

# 解题思路：
# 规则：移除最右的/，//->/，a/../抵消，/../特殊情况


class Solution:
    # 用栈维护所有的路径，若上一级则回退
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)
