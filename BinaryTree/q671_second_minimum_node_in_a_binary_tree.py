# Time:  O(n)
# Space: O(1)

# 解题思路：
# dfs遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> int:
        if not root:
            return -1

        def find_sec_min(root, min_val):
            if root.val > min_val:
                return root.val
            if root.left:
                left = find_sec_min(root.left, min_val)
                right = find_sec_min(root.right, min_val)
                if left == min_val:
                    return right
                elif right == min_val:
                    return left
                else:
                    return min(left, right)
            return root.val

        sec_min_val = find_sec_min(root, root.val)
        return sec_min_val if sec_min_val != root.val else -1


class Solution1:
    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1