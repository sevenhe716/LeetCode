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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # 这种方式只连接了兄弟节点，而未连通整层
        if root.left:
            root.left.next = root.right
            self.connect(root.left)
            self.connect(root.right)
        return root

    # 先用递归实现层序遍历：
    # 带上前一个节点即可实现连接，需要区分层级
    # 迭代版本使用队列，而递归是栈，用递归来实现是否就相当于用双栈模拟队列？
