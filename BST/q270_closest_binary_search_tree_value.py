# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# dfs 将当前最小的差值和节点作为参数传递，如果当前值比目标值小，则不需要再遍历左子树，右子树同理进行剪枝


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recusively
    def closestValue1(self, root: 'TreeNode', target: float) -> int:
        def dfs(root, diff, closest):
            if abs(target - root.val) < diff:
                diff = abs(target - root.val)
                closest = root.val
            if root.val > target and root.left:
                return dfs(root.left, diff, closest)
            elif root.val < target and root.right:
                return dfs(root.right, diff, closest)
            return closest

        return dfs(root, float('inf'), None)

    # iteratively
    def closestValue(self, root: 'TreeNode', target: float) -> int:
        diff, closest = float('inf'), None
        while root:
            if abs(target - root.val) < diff:
                diff = abs(target - root.val)
                closest = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return closest

