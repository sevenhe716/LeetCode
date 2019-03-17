# Time:  O(n)
# Space: O(1)

# Ideas:
# mark

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import TreeNode


class Solution:
    def trimBST(self, root: 'TreeNode', L: int, R: int) -> 'TreeNode':

        dummy = TreeNode(float('inf'))
        dummy.left = root

        print(root)

        # default: cur is valid
        def dfs(cur):
            if not cur:
                return
            while cur.right and cur.right.val > R:
                cur.right = cur.right.left

            while cur.right and cur.right.val < L:
                cur.right = cur.right.right

            while cur.left and cur.left.val > R:
                cur.left = cur.left.left

            while cur.left and cur.left.val < L:
                cur.left = cur.left.right

            dfs(cur.left)
            dfs(cur.right)

        dfs(dummy)
        return dummy.left

    # def trimBST(self, root: 'TreeNode', L: int, R: int) -> 'TreeNode':
    #     # for R, if R is left child records all left parents, remove right child of all
    #     cur = root
    #     parents = []
    #     while cur:
    #         if cur.val == R:
    #             parents.append(cur)
    #             break
    #         elif cur.val < R:
    #             parents.clear()
    #             cur = cur.right
    #         else:
    #             parents.append(cur)
    #             cur = cur.left
    #
    #     for p in parents:
    #         p.right = None
    #
    #     # for L, find the node who left than L, replace by its left node,
    #     # and right node add to left node's right most, if no left node, replace by right node
    #     def dfs():
    #
    #
    #     cur = root
    #     while cur:
    #         if cur.val < L:



