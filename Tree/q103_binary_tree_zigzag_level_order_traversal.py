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


class Solution1(object):
    # 层序遍历的递归版本，DFS
    def zigzagLevelOrder(self, root):
        def dfs(level, direction, root):
            if root:
                if level >= len(res):
                    res.append([])
                if direction == 0:
                    res[level].append(root.val)
                if direction == 1:
                    res[level].insert(0,root.val)
                if root.left:
                    dfs(level+1, (direction+1)%2, root.left)
                if root.right:
                    dfs(level+1, (direction+1)%2, root.right)
        res = []
        dfs(0,0,root)
        return res