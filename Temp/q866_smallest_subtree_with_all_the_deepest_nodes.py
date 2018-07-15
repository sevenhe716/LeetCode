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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        parents = {}
        parents[root.val] = None

        def init(cur):
            if cur.left:
                parents[cur.left.val] = cur

                init(cur.left)
            if cur.right:
                parents[cur.right.val] = cur

                init(cur.right)

        init(root)
        stack = [root]

        # bfs
        new_stack = []
        last_stack = []
        while stack:
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)

            last_stack = stack
            stack = new_stack

        print(last_stack)

        values = set([node.val for node in last_stack])

        while len(values) > 1:
            new_values = set()
            for v in values:
                new_values.add(parents[v])
            values = new_values

        # find target
        def find_target(cur, val):
            if cur.val == val:
                return cur
            else:
                if cur.left:
                    t1 = find_target(cur.left, val)
                    if t1:
                        return t1
                if cur.right:
                    t2 = find_target(cur.right, val)
                    if t2:
                        return t2

            return None

        values.po
        return find_target(root, values[0])

