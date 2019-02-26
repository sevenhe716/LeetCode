# Time:  O(n)
# Space: O(1)

# 解题思路：
# 找到前序遍历的节点在中序的位置，以此作为分割做为左右子树，再递归即可


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import TreeNode


class Solution:
    # 递归版本较慢，无效调用次数过多，虽然看起来很简洁
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder:
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root


class Solution1(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        stack = [head]
        i, j = 1, 0

        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1

        return head