# Time:  O(n)
# Space: O(n)

# 解题思路：
# 需要注意的是，如果root的左子树不存在，则root为left boundary，如果存在，则left boundary为从root到left-most的路径，右侧同理
# left_bounary阶段和叶子节点阶段可以用dfs，再额外添加right boundary阶段
# 优化：三个阶段都可以在一个dfs中完成，标记flag，分开存储路径即可


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        self.res, self.left_most = [], True

        # 如果没有左子树，则root为左boundary
        if not root.left:
            self.left_most = False
            # 如果root不是叶子节点
            if root.right:
                self.res.append(root.val)

        def dfs(root):
            if not root:
                return
            # left boundary阶段, 在找到第一个叶子节点之前，路径里的所有节点都添加
            if self.left_most:
                self.res.append(root.val)
                # 如果到达叶子节点，切换到leaf阶段
                if not root.left and not root.right:
                    self.left_most = False
            # leaf阶段 如果是叶子节点，则添加
            elif not root.left and not root.right:
                self.res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        # find right most, 不添加头节点
        cur, right_most_path = root, []

        # 如果右子树存在，再执行right-boundary阶段
        if root.right:
            while cur.left or cur.right:
                if cur.right:
                    cur = cur.right
                    right_most_path.append(cur.val)
                else:
                    cur = cur.left
                    right_most_path.append(cur.val)

        # 去掉叶子节点
        if right_most_path:
            right_most_path = right_most_path[:-1]

        return self.res + right_most_path[::-1]


class Solution1:
    def boundaryOfBinaryTree(self, root: 'TreeNode') -> 'List[int]':
        if root == None:
            return []
        leaf = []
        left = [root.val]
        right = []

        def inOrder(node, flag):
            if node == None:
                return
            if flag == 0:
                left.append(node.val)
            elif flag == 1:
                right.append(node.val)
            elif node.left == None and node.right == None:
                leaf.append(node.val)
            if flag == 2:
                l_flag, r_flag = 2, 2
            elif flag == 0:
                l_flag, r_flag = 0, 2
                if node.left == None:
                    r_flag = 0
            elif flag == 1:
                l_flag, r_flag = 2, 1
                if node.right == None:
                    l_flag = 1

            inOrder(node.left, l_flag)
            inOrder(node.right, r_flag)

        inOrder(root.left, 0)
        inOrder(root.right, 1)
        right.reverse()
        return left + leaf + right


# 这个解法很棒，简洁优美
class Solution1:
    def boundaryOfBinaryTree(self, root):
        res = []
        self.preorder(root, res, True, True)
        return res

    def preorder(self, node, res, isLeft, isRight):
        if not node: return
        isLeafOrLeft = (not node.left and not node.right) or isLeft
        # append leaf or leftboundary
        if isLeafOrLeft: res.append(node.val)
        # preorder traversal
        if not node.left and not node.right:
            return
        elif not node.right:
            self.preorder(node.left, res, isLeft, isRight and not isLeft)
        elif not node.left:
            self.preorder(node.right, res, isLeft and not isRight, isRight)
        else:
            self.preorder(node.left, res, isLeft, False)
            self.preorder(node.right, res, False, isRight)
        # append right boundary，返回的路径中添加，不需要反序
        if isRight and not isLeafOrLeft: res.append(node.val)