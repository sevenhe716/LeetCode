# Time:  O(n)
# Space: O(n)

# Ideas:
# stack


class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(b_map[c])
            elif not stack or c != stack.pop():
                    return False
        return len(stack) == 0
