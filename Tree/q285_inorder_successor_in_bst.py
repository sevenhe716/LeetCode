# Time:  O(n)
# Space: O(1)

# 解题思路：
# 如果当前节点有右节点，则后继节点是右节点中的最左侧的节子叶点，用于这种情况下的加速
# 如果当前节点没有右节点，则需要从root遍历来找到


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iteratively
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            stack, find = [], False
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if find:
                    return root
                if root == p:
                    find = True
                root = root.right
        if find:
            return None


class Solution1:
    # recursively
    def inorderSuccessor(self, root, p):
        self.res = None
        self.dfs(root, p)
        return self.res

    def dfs(self, root, p):
        if not root: return
        if p.val < root.val:
            self.res = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)

