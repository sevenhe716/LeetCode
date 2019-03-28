# Time:  O(n)
# Space: O(1)

# 解题思路：
# 直接递归比较父子节点是不正确的，需要传递最小值和最大值
# 也可以使用中序遍历，判断是否是严格递增


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 直接递归比较父子节点是不正确的，需要传递最小值和最大值
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     if not root:
    #         return True
    #     if root.left and root.left.val >= root.val:
    #             return False
    #     if root.right and root.right.val <= root.val:
    #             return False
    #     return self.isValidBST(root.left) and self.isValidBST(root.right)

    # 中序遍历，缓存并比较上一个节点的值
    def isValidBST1(self, root: 'TreeNode') -> 'bool':
        last_val = float('-inf')

        def inorder(root):
            nonlocal last_val
            if not root:
                return True

            if not inorder(root.left):
                return False
            if root.val <= last_val:
                return False
            else:
                last_val = root.val
            if not inorder(root.right):
                return False
            return True
        return inorder(root)

    # 返回值传递最小值和最大值
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def dfs(root):
            if not root.left and not root.right:
                return True, root.val, root.val
            if root.left:
                left_res, left_min, left_max = dfs(root.left)
                if not left_res or root.val <= left_max:
                    return False, 0, 0
            else:
                left_min = root.val

            if root.right:
                right_res, right_min, right_max = dfs(root.right)
                if not right_res or root.val >= right_min:
                    return False, 0, 0
            else:
                right_max = root.val
            return True, left_min, right_max
        if not root:
            return True
        res, _, _ = dfs(root)
        return res


class Solution1:
    # DFS，使用参数传递
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 参数传递，我使用的是返回值传递
        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and upper_limit <= node.val:
                return False

            left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
            if left:
                right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
                return right
            else:
                return False

        return isBSTHelper(root, None, None)

    # BFS
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, None, None), ]
        while stack:
            root, lower_limit, upper_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True

    # 迭代版本的中序遍历
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
