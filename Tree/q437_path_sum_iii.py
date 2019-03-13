# Time:  O(n)
# Space: O(n)

# 解题思路：
# dfs记录子路径和，然后相减可以得到任意一段路径和，头节点上添加0来包含头节点的用例


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def pathSum(self, root: 'TreeNode', sum: int) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(root, path):
            for i in range(len(path)-1):
                if sum == path[-1] - path[i]:
                    self.res += 1
            if root.left:
                path.append(path[-1] + root.left.val)
                dfs(root.left, path)
                path.pop()
            if root.right:
                path.append(path[-1] + root.right.val)
                dfs(root.right, path)
                path.pop()
        dfs(root, [0, root.val])
        return self.res


class Solution1:
    # dict counter
    def pathSum1(self, root, target):
        self.count = 0
        preDict = {0: 1}

        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, target, 0, preDict)
        return self.count

    def pathSum2(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t - node.val: hit += 1  # count if sum == target
        targets = [t - node.val for t in targets] + [origin]  # update the targets
        return hit + self.helper(node.left, origin, targets) + self.helper(node.right, origin, targets)

    # counter
    def pathSum3(self, root, target):
        def findSum(root, totSum):
            if not root: return
            totSum += root.val
            res[0] += partSums[totSum - target]
            partSums[totSum] += 1
            findSum(root.left, totSum)
            findSum(root.right, totSum)
            partSums[totSum] -= 1

        res = [0]
        partSums = collections.Counter([0])
        findSum(root, 0)
        return res[0]
