# Time:  O(n)
# Space: O(1)

# 解题思路：
# 第一种思路是BFS，但需要考虑空节点的问题
# 第二种思路是按照中轴翻转，然后比较是否与原树相等
# 第三种思路是计算出对称的位置，然后对对称的位置进行对比，如果是原构造数组则用这种方式比较好

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSymmetricR(left, right):
            if left and right:
                return left.val == right.val and isSymmetricR(left.left, right.right) and isSymmetricR(
                    left.right, right.left)
            return left is right

        return isSymmetricR(root, root)


# iteratively way, BFS的思想
class Solution1:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True

        dq = collections.deque([(root.left, root.right)])
        while dq:
            node1, node2 = dq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            # node1.left and node2.right are symmetric nodes in structure
            # node1.right and node2.left are symmetric nodes in structure
            dq.append((node1.left, node2.right))
            dq.append((node1.right, node2.left))
        return True
