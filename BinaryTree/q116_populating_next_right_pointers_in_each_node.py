# Time:  O(n)
# Space: O(1)

# 解题思路：
# 只能使用常数空间，可以使用递归，递归栈不计入空间复杂度
# 实际就是层序遍历，并进行连接


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return None
    #     # 这种方式只连接了兄弟节点，而未连通整层
    #     if root.left:
    #         root.left.next = root.right
    #         self.connect(root.left)
    #         self.connect(root.right)
    #     return root

    # 符合常数空间复杂度，但是遍历次数大大增多，每一层分别遍历
    def connect(self, root: 'Node') -> 'Node':
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))

        def dfs(root, level):
            nonlocal last
            if level == 0:
                if last:
                    last.next = root
                last = root
                return
            if root.left:
                dfs(root.left, level - 1)
            if root.right:
                dfs(root.right, level - 1)

        for i in range(getDepth(root)):
            last = None
            dfs(root, i)

    # 先用递归实现层序遍历：
    # 带上前一个节点即可实现连接，需要区分层级，需要用log(n)的空间


class Solution1:
    # 递归实现跨节点连接，这才是符合题意的正解
    def connect(self, root: 'Node') -> 'Node':
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
