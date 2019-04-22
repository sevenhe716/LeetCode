# Time:  O(n)
# Space: O(1)

# 解题思路：
# 根节点需要访问两次，因此需要额外记录是否访问过
# 优化：其实可以不用访问两次，每次添加根节点之前先把左节点添加到底即可


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root.left:
            self.inorderTraversal(root.left)

        yield root

        if root.right:
            self.inorderTraversal(root.right)

    # recursively
    def inorderTraversal1(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # iteratively
    def inorderTraversal2(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            node = stack[-1]
            # if node not in visited:
            # 对原有结构具有破坏性
            if not hasattr(node, 'visited'):
                if node.left:
                    stack.append(node.left)
                # visited.add(node)
                node.visited = True
            else:
                ans.append(node.val)
                stack.pop()
                # visited.remove(node)
                del node.visited
                if node.right:
                    stack.append(node.right)
        return ans

    # iteratively
    def inorderTraversal3(self, root: 'TreeNode') -> 'List[int]':
        stack, ans = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

    # 顺带用栈实现了前序和后序的迭代遍历
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return ans

    def postorderTraversal1(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            root = stack[-1]
            if not hasattr(root, 'visited'):
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
                root.visited = True
            else:
                ans.append(root.val)
                stack.pop()
                del root.visited
        return ans

    # 另一种思路是将值插入到头位置
    # 因为出栈顺序为“根右左”，所以需要每次将元素插入list开头
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            root = stack.pop()
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
            ans.insert(0, root.val)
        return ans