# Time:  O(n)
# Space: O(1)

# 解题思路：
# the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor


# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        pre = dummy = Node(0, None, None)
        cur, stack = root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            pre.right, cur.left, pre = cur, pre, cur
            cur = cur.right
        pre.right, dummy.right.left = dummy.right, pre
        return dummy.right


# Python in-place DFS solution
class Solution1:
    def treeToDoublyList(self, root):
        head, tail = [None], [None]
        def dfs(node, pre):
            if not node:
                return
            l = dfs(node.left, pre)
            new = Node(node.val, l or pre, None)
            if pre and not l:
                pre.right = new
            elif l:
                l.right = new
            if not pre and not l:
                head[0] = new
            if not tail[0] or node.val > tail[0].val:
                tail[0] = new
            r = dfs(node.right, new)
            return r if r else new
        dfs(root, None)
        if head[0]:
            head[0].left = tail[0]
            tail[0].right = head[0]
        return head[0]
