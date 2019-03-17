# Time:  O(logn)
# Space: O(1)

# Ideas:
# inorder traverse is ok, but not fast enough


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            # if p has right child, left-most leaf
            if not p:
                return None
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            parent = None
            # if it from left, return parent, if from right, find last
            while p.val != root.val:
                if p.val < root.val:
                    parent = root
                    root = root.left
                else:
                    root = root.right
            return parent


