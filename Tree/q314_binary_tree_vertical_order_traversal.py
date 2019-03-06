# Time:  O(n)
# Space: O(1)

# 解题思路：
# dfs的遍历顺序不正确，需要从上往下，从左往右，只能使用层序遍历，层序遍历需要额外记录index


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from collections import deque


class Solution:
    # dfs遍历顺序不正确
    def verticalOrder1(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return
        res = defaultdict(list)

        def dfs(root, index):
            res[index].append(root.val)
            if root.left:
                dfs(root.left, index - 1)
            if root.right:
                dfs(root.right, index + 1)

        dfs(root, 0)

        ans = []
        for i in sorted(res.keys()):
            ans.append(res[i])
        return ans

    # BFS
    def verticalOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        res = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            cur, index = queue.popleft()
            res[index].append(cur.val)
            if cur.left:
                queue.append((cur.left, index - 1))
            if cur.right:
                queue.append((cur.right, index + 1))

        ans = []
        for i in sorted(res.keys()):
            ans.append(res[i])
        return ans
