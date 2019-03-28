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
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        paths, cur_path = [], []

        def dfs(cur):
            if cur:
                cur_path.append(str(cur.val))
                if not cur.left and not cur.right:
                    # join函数
                    # path_str = ''
                    # for node in cur_path:
                    #     path_str += str(node) + '->'
                    # paths.append(path_str[:-2])
                    paths.append('->'.join(cur_path))
                else:
                    dfs(cur.left)
                    dfs(cur.right)
                cur_path.pop()

        dfs(root)
        return paths


class Solution1:
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        cur_paths = []

        # cur_path用参数传递，利用函数堆栈则可以省去push pop
        def dfs(node, cur_path):
            if node.left:
                dfs(node.left, cur_path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, cur_path + "->" + str(node.right.val))

            if not node.left and not node.right:
                cur_paths.append(cur_path)

        if root:
            dfs(root, str(root.val))
        return cur_paths

