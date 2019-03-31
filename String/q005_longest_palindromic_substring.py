# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 有个显而易见的思路是，模式匹配，以每个元素为中点，往两侧寻找回文的最大长度（需要分奇偶讨论），时间复杂度介于O(n)~O(n^2)
# 更好的思路是，翻转字符串，可以把问题化归为求两个字符串的最大公共子串问题
# 但有额外的O(n)空间复杂度，题目注明不超过1000，这部分开销可以忽略不计（其实无需O(n)的开销，返向遍历字符串即可）
# 最大公共子串问题可以用动态规划求解，优化过后的时间复杂度是O(m*n)，空间复杂度是O(m)
# 我思考的解法是如果不用动态规划，而是坐标偏移的方式进行两个字符串的比对
# 时间复杂度同样是O((m+n)*min(m+n))即O(2n^2)（但每个循环执行的计算更少），但空间复杂度是O(1)，是否为更好的解法？
# 最大公共子串问题参考资料：
# https://blog.csdn.net/u012102306/article/details/53184446
# https://www.cnblogs.com/ider/p/longest-common-substring-problem-optimization.html
# https://blog.csdn.net/hackbuteer1/article/details/6686931
# 优化一：逆字符串先比较，这样能保证返回第一个匹配的子字符串
# 优化二：无需创建逆字符串，反向遍历即可
# 优化三：还需要保证是同一个子字符串，通过索引位置来判断（正序的起始位置等于逆序的结束位置）


class Solution:
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        start1, start2 = 0, n - 1

        cur_len, max_len, end_index = 0, 0, 0

        while start1 <= n - 1 or start2 > 0:
            count = min(n - start1, n - start2)

            for i in range(count):
                if s[start1 + i] == s[-1 - start2 - i]:
                    cur_len += 1
                else:
                    if cur_len > max_len and start1 + i - cur_len == n - start2 - i:     # 保证是同一位置
                        max_len = cur_len
                        end_index = start1 + i
                    cur_len = 0
            i += 1                          # 退出循环时i不会加1

            if cur_len > 0:                 # 当遍历完成时，也需要检查一遍是否是最大子串
                if cur_len > max_len and start1 + i - cur_len == n - start2 - i:
                    max_len = cur_len
                    end_index = start1 + i
                cur_len = 0

            if start2 > 0:
                start2 -= 1
            else:
                start1 += 1

        return s[end_index-max_len:end_index]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T += ['#', c]
            T += ['#', '$']
            return T

        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in range(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) // 2
        return s[start: start + P[max_i]]

