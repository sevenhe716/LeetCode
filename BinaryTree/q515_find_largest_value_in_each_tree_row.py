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

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        max_values = []
        self.largestValuesR(root, 1, max_values)

        return max_values

    def largestValuesR(self, root, depth, max_values):
        if len(max_values) == depth - 1:
            max_values.append(root.val)
        else:
            if root.val > max_values[depth - 1]:
                max_values[depth - 1] = root.val

        if root.left:
            self.largestValuesR(root.left, depth + 1, max_values)

        if root.right:
            self.largestValuesR(root.right, depth + 1, max_values)


# iterative
class SolutionF:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = [root]
        r = []
        while q:
            r.append(max([i.val for i in q]))
            q = [i for node in q for i in [node.left, node.right] if i]
        return r