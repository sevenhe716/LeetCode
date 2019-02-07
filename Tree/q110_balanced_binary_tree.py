# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一个比较容易想到的思路是，利用多返回值，自底向上统计每个节点的深度，以及是否平衡，再向上传递即可


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBalancedR(root):
            if not root:
                return 0, True

            left_depth, left_balance = isBalancedR(root.left)
            right_depth, right_balance = isBalancedR(root.right)

            depth = 1 + max(left_depth, right_depth)
            if left_balance and right_balance:
                if abs(right_depth - left_depth) > 1:
                    return depth, False
                else:
                    return depth, True
            else:
                return depth, False

        _, ret = isBalancedR(root)
        return ret


# 思路跟我类似，比较有技巧的地方是利用特殊值-1代表not balance，合并了多返回值
class Solution1:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        return 1 + max(left, right)