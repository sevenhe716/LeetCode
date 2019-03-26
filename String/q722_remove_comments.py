# Time:  O(n)
# Space: O(1)

# Ideas:
# 一个难点在于，块注释需要把跨行的内容合并到一行
import re


class Solution:
    def removeComments(self, source: 'List[str]') -> 'List[str]':
        res = [''] * len(source)
        in_block_comment, block_comment_start_line = False, 0

        for line_num, line in enumerate(source):
            in_line_comment = False
            start, i, line_res = 0, 0, ''
            line_to_write = line_num
            while i < len(line):
                if not in_block_comment:
                    if line.startswith('//', i):
                        line_res += line[start:i]
                        in_line_comment = True
                        break
                    if line.startswith('/*', i):
                        in_block_comment = True
                        block_comment_start_line = line_num
                        line_res += line[start:i]
                        i += 2
                        continue
                # only to find */
                else:
                    if line.startswith('*/', i):
                        line_to_write = block_comment_start_line
                        in_block_comment = False
                        i += 2
                        start = i
                        continue

                i += 1

            if not in_line_comment and not in_block_comment:
                line_res += line[start:]

            res[line_to_write] += line_res

        return list(filter(None, res))


class Solution1:
    # regex, 将注释内容替换为空，之前需要先将source合为一行
    def removeComments(self, source):
        return list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))