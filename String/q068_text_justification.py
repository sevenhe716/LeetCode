# Time:  O(n)
# Space: O(1)

# 解题思路：
# 首先计算出每行的单词，然后再做对齐操作
# 两端对齐的，则是求出平均空白数，然后优先前面的多一个空格，如果只有一个单词则左对齐，最后一行也是左对齐


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        row, i = 0, 0
        cur_width = -1
        ans, output = [], []

        while True:         # 可以在一个循环内完成，不需要先统计word
            ans.append([])
            while i < len(words) and len(words[i]) + cur_width + 1 <= maxWidth:     # 这种写法会多做2n次加法
                cur_width += len(words[i]) + 1
                ans[row].append(words[i])
                i += 1

            row += 1
            cur_width = -1
            if i >= len(words):
                break

        for i in range(len(ans) - 1):
            count = len(ans[i])

            if count == 1:          # 可以划归成添加' '，无需单独讨论
                output.append(ans[i][0].ljust(maxWidth))
                continue

            blank_num = maxWidth - sum([len(s) for s in ans[i]])    # 统计长度也可以在前面遍历的循环内一次完成

            aver_blank = blank_num // (count - 1)
            extra_blank = blank_num - aver_blank * (count - 1)

            for j in range(count - 1):      # 取模依次分配即可
                if extra_blank > 0:
                    ans[i].insert(1 + (j << 1), ' ' * (aver_blank + 1))
                    extra_blank -= 1
                else:
                    ans[i].insert(1 + (j << 1), ' ' * aver_blank)

            output.append(''.join(ans[i]))

        output.append((' '.join(ans[-1])).ljust(maxWidth))

        return output


# 简洁，值得借鉴
class Solution1:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:       # len(cur)即当前空格数
                for i in range(maxWidth - num_of_letters):
                    # 取模的方式依次在word后面添加空格 len(cur)-1 最后一个不添加
                    # 不要太担心str concat的效率问题
                    # len(cur)-1 or 1 当len=1时，也可以归为此类，无需用ljust
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
