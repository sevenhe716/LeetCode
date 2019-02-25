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
    # recursively
    def inorderTraversal1(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # iteratively
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        stack, ans = [root], []
        visited = set()
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
