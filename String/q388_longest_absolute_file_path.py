# Time:  O(n)
# Space: O(n)

# 解题思路：
# 首先是字符串解析，然后记录嵌套关系和长度，区分是文件还是路径，只统计到file的最长路径
# 数据结构使用stack


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        # splitlines is better
        max_len, cur_len = 0, 0
        for dir in input.split('\n'):
            # count \t的个数，且去除
            depth = dir.count('\t')
            length = len(dir) - depth
            while depth < len(stack) and stack:
                cur_len -= stack.pop()
            if '.' in dir:
                # is file，计算长度
                max_len = max(max_len, cur_len + length)
            else:
                # is dir, 压栈，需要加1
                stack.append(length + 1)
                cur_len += length + 1
        return max_len


class Solution1:
    # use dict, for each depth I store the current path length. more faster
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            # lstrip is better here
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen