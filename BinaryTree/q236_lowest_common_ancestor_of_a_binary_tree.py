# Time:  O(n)
# Space: O(n)

# Ideas:
# dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(root):
            find_p, find_q = False, False

            if root == p:
                find_p = True
            if root == q:
                find_q = True

            if root.left:
                left_find_p, left_find_q = dfs(root.left)
                find_p = find_p or left_find_p
                find_q = find_q or left_find_q
            if root.right:
                right_find_p, right_find_q = dfs(root.right)
                find_p = find_p or right_find_p
                find_q = find_q or right_find_q
            if find_p and find_q and not self.res:
                self.res = root
            return find_p, find_q

        dfs(root)
        return self.res


class Solution1:
    def lowestCommonAncestor1(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor2(self, root, p, q):
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()

        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)

    # fastest
    def lowestCommonAncestor3(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q