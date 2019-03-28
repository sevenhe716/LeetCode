# Time:  O(n)
# Space: O(1)

# 解题思路：
# 反中序遍历，然后用当前值加上累加值


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursively
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        accumulate = 0

        def anti_inorder(root):
            nonlocal accumulate
            if not root:
                return
            anti_inorder(root.right)
            accumulate += root.val
            root.val = accumulate
            anti_inorder(root.left)
        anti_inorder(root)
        return root


class Solution1:
    # iteratively
    def convertBST1(self, root):
        total = 0

        node = root
        stack = []
        while stack or node:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root

    # O(1)空间复杂度，利用空指针来存储后继节点
    # https://leetcode.com/problems/convert-bst-to-greater-tree/solution/
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root