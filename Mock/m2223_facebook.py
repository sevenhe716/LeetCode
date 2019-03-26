# Time:  O(n)
# Space: O(1)

# Ideas:
# BFS, DFS has wrong order in same vertical_index (not top to bottom)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def verticalOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        vertical_dict = defaultdict(list)
        queue = [(root, 0)]

        for root, vertical_idx in queue:
            vertical_dict[vertical_idx].append(root.val)
            if root.left:
                queue.append((root.left, vertical_idx-1))
            if root.right:
                queue.append((root.right, vertical_idx+1))

        res = []
        for key in sorted(vertical_dict.keys()):
            res += [vertical_dict[key]]

        return res