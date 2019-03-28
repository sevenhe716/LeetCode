# Time:  O(n)
# Space: O(1)

# 解题思路：
# dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs
    def countUnivalSubtrees(self, root: 'TreeNode') -> int:
        if not root:
            return 0
        res = 0

        def dfs(root):
            nonlocal res
            unique = True
            if root.left:
                check, left_val = dfs(root.left)
                if not check or root.val != left_val:
                    unique = False
            if root.right:
                check, right_val = dfs(root.right)
                if not check or root.val != right_val:
                    unique = False
            if unique:
                res += 1
            return unique, root.val
        dfs(root)
        return res


class Solution1:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val
