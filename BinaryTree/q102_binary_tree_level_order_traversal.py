# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用队列实现迭代版本的层序遍历（BFS）


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level, ans = 0, []
        while queue:
            ans.append([])
            # 边遍历边修改
            for _ in range(len(queue)):
                cur = queue.popleft()
                ans[level].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return ans


class Solution1:
    # 将level也打包加入队列，可以一次遍历完成
    # pythonic way:python for支持边遍历边修改
    def levelOrder(self, root):
        res = []
        queue = [(root, 0)]
        for node, level in queue:
            if node:
                if level >= len(res):
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res
