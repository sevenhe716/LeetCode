# Time:  O(logn)
# Space: O(1)

# 解题思路：
# 一个差强人意的思路是利用python动态属性，添加子节点到父节点的指针，然后转化为两个链表求交点的问题，没注意是二叉搜索树
# 如果是二叉搜索树，可以dfs比较值大小即可


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p > q:
            p, q = q, p

        def dfs(cur):
            if p <= cur.val <= q:
                return cur
            return dfs(cur.left) if cur.val > q else dfs(cur.right)

        return dfs(root)
