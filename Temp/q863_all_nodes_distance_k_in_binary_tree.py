# Time:  O(n)
# Space: O(1)

# 解题思路：
#

from common import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    class TreeNode1:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def distanceK1(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """

        if not root:
            return []

        troot = Solution.TreeNode1(root[0])
        stack = []
        stack.append(troot)
        troot.visit = True
        # BFS方式来建树
        index = 1

        while index < len(root):
            parent = stack.pop(0)

            if root[index] or root[index] == 0:
                parent.left = Solution.TreeNode1(root[index])
                parent.left.visit = True
                parent.left.parent = parent
                stack.append(parent.left)
            else:
                stack.append(None)

            index += 1
            if index >= len(root):
                break

            if root[index] or root[index] == 0:
                parent.right = Solution.TreeNode1(root[index])
                parent.right.visit = True
                parent.right.parent = parent
                stack.append(parent.right)
            else:
                stack.append(None)

            index += 1

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

        cur = find_target(troot, target)

        cur.visit = True
        stack = [cur]
        # BFS
        for _ in range(K):
            new_stack = []
            for node in stack:
                if node.left and not node.left.visit:
                    node.left.visit = True
                    new_stack.append(node.left)
                if node.right and not node.right.visit:
                    node.right.visit = True
                    new_stack.append(node.right)
                if node.parent and not node.parent.visit:
                    node.parent.visit = True
                    new_stack.append(node.parent)

            stack = new_stack
            print([node.val for node in stack])

        return [node.val for node in stack]

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """

        if not root:
            return []

        visits, parents = {}, {}
        visits[root.val] = False
        parents[root.val] = None

        def init(cur):
            if cur.left:
                visits[cur.left.val] = False
                parents[cur.left.val] = cur

                init(cur.left)
            if cur.right:
                visits[cur.right.val] = False
                parents[cur.right.val] = cur

                init(cur.right)

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

        cur = find_target(root, target)

        visits[cur.val] = True
        stack = [cur]
        # BFS
        for _ in range(K):
            new_stack = []
            for node in stack:
                if node.left and not visits[node.left.val]:
                    visits[node.left.val] = True
                    new_stack.append(node.left)
                if node.right and not visits[node.right.val]:
                    visits[node.right.val] = True
                    new_stack.append(node.right)
                parent = parents[node.v]
                if parent and not visits[parent.val]:
                    visits[parent.val] = True
                    new_stack.append(parent)

            stack = new_stack
            print([node.val for node in stack])

        return [node.val for node in stack]