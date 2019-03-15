# Time:  O(n)
# Space: O(1)

# 解题思路：
# 按高度来分组输出


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeaves(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []

        def dfs(root):
            if not root:
                return -1
            height = max(dfs(root.left), dfs(root.right)) + 1
            # height如果大于等于len(res)，实际上就是等于len(res)，只需要向尾部添加一个即可
            if height >= len(res):
                res.append([])
            res[height].append(root.val)
            return height
        dfs(root)
        return res


class Solution1:
    def findLeaves(self, root):
        if not root: return []
        kids = list(map(self.findLeaves, (root.left, root.right)))
        return list(map(lambda l, r: (l or []) + (r or []), *kids)) + [[root.val]]

