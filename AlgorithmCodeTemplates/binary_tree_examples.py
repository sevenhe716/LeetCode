from collections import defaultdict
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# [101] https://leetcode.com/problems/symmetric-tree/
# check whether it is a mirror of itself
def isSymmetric(root):
    def isSymmetricR(left, right):
        if left and right:
            return left.val == right.val and isSymmetricR(left.left, right.right) and isSymmetricR(
                left.right, right.left)
        return left is right

    return isSymmetricR(root, root)


# [105] https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# construct tree from preorder and inorder
def buildTree(preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
    if not preorder:
        return
    index = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:index + 1], inorder[0:index])
    root.right = buildTree(preorder[index + 1:], inorder[index + 1:])
    return root


# [110] https://leetcode.com/problems/balanced-binary-tree/
# determine if it is height-balanced
def isBalanced(root):
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        return 1 + max(left, right)

    if not root:
        return True
    return dfs(root) != -1


# [314] https://leetcode.com/problems/binary-tree-vertical-order-traversal
# output vertical order
# BFS
def verticalOrder(root: 'TreeNode') -> 'List[List[int]]':
    if not root:
        return []

    vertical_dict = defaultdict(list)
    queue = [(root, 0)]

    for root, vertical_idx in queue:
        vertical_dict[vertical_idx].append(root.val)
        if root.left:
            queue.append((root.left, vertical_idx - 1))
        if root.right:
            queue.append((root.right, vertical_idx + 1))

    res = []
    for key in sorted(vertical_dict.keys()):
        res += [vertical_dict[key]]

    return res


# [116] https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# populate each next pointer to point to its next right node
def connect(root: 'Node') -> 'Node':
    # connect left child to right child, and cross connect left right child to right left child in recursion
    def connect_inner(l, r):
        if not l.left or not r.right:
            return
        l.left.right = l.right
        l.right.next = r.left
        r.left.next = r.right

        connect_inner(l.left, l.right)
        connect_inner(l.right, r.left)
        connect_inner(r.left, r.right)

    if not root or root.left:
        return root
    root.left.next = root.right
    connect_inner(root.left, root.right)
    return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# invert binary tree
# recursively
def invertTree1(root):
    if root:
        root.left, root.right = invertTree1(root.right), invertTree1(root.left)
        return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# BFS
def invertTree2(root: 'TreeNode') -> 'TreeNode':
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            # accept add None node to queue, in order to deal with edge case together
            queue.append(node.left)
            queue.append(node.right)
    return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# DFS
def invertTree3(root: 'TreeNode') -> 'TreeNode':
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            # accept push None node to stack, in order to deal with edge case together
            stack.append(node.left)
            stack.append(node.right)
    return root


# [236] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# find the lowest common ancestor (LCA) of two given nodes in binary tree
# recursively
def lowestCommonAncestor1(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right


# [236] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# iteratively, use common path
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


# [545] https://leetcode.com/problems/boundary-of-binary-tree
# get the boundary of binary tree
def boundaryOfBinaryTree(root):
    res = []

    def preorder(node, is_left, is_right):
        if not node:
            return
        is_leaf_or_left = (not node.left and not node.right) or is_left
        # append leaf or leftboundary
        if is_leaf_or_left:
            res.append(node.val)
        # preorder traversal
        if not node.left and not node.right:
            return
        elif not node.right:
            preorder(node.left, is_left, is_right and not is_left)
        elif not node.left:
            preorder(node.right, is_left and not is_right, is_right)
        else:
            preorder(node.left, is_left, False)
            preorder(node.right, False, is_right)
        # append right boundary, in backtrack so don't need reverse order
        if is_right and not is_leaf_or_left:
            res.append(node.val)

    preorder(root, True, True)
    return res
