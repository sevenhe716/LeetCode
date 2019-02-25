# Time:  O(n)
# Space: O(1)

# 解题思路：
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level, ans = 0, []
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                cur = queue.popleft()
                ans[level].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        for i in range(len(ans))[1::2]:
            ans[i].reverse()
        return ans
