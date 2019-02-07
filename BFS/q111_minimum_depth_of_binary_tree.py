# Time:  O(n)
# Space: O(1)

# 解题思路：
# 我的思路被maxdepth限制住了，其实使用BFS逐层扫描，找到的第一个叶子节点即是结果


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return 1

        left_depth = self.minDepth(root.left) if root.left else 2147483647
        right_depth = self.minDepth(root.right) if root.right else 2147483647

        return 1 + min(left_depth, right_depth)


class Solution1:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case. Covers when the tree is empty or the root we're looking at doesn't exist.
        if not root:
            return 0

        # Using BFS, implement a queue.
        queue = [[1, root]]
        while queue:
            # When you pop the node [1, root] comes out. Height = 1, node = root.
            height, node = queue.pop(0)
            if not node.left and not node.right:
                return height
            if node.left:
                queue.append((height + 1, node.left))
            if node.right:
                queue.append((height + 1, node.right))

