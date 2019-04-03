# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 双指针，滑动窗口，维护左右括号的数量，记录最长的substring
# 动态规划，必定存在基本单元()，从()出发往外规划


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        longest_count = 0
        # left = 0
        left_count = 0
        right_count = 0
        for i, c in enumerate(s):
            if c == '(':
                left_count += 1
            else:
                if right_count < left_count:
                    right_count += 1
                else:
                    longest_count = max(longest_count, left_count)
                    left_count = 0
                    right_count = 0
                    # left = i + 1

        # 处理余下的数组，这本身就是一个原问题
        return max(longest_count, self.longestValidParentheses1(s[len(s) - left_count - right_count:len(s)]))
        # if left_count > right_count:
        #     i -= (right_count << 1)
        #     for j in range(left_count - right_count):
        #         # s[i] =
        #         i -= 1
        #
        # return longest_count << 1

    # dp
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [0 for _ in range(n)]  # 右边界通过个数就能计算出

        i = 0
        has_pair = False

        dp_dict = {}

        while i < n - 1:
            if s[i + 1] == ')':
                if s[i] == '(':
                    dp[i] = 2
                    has_pair = True
                    dp_dict[i] = 2
                i += 2  # 可以直接跳过下一个节点
            else:
                i += 1

        if not has_pair:
            return 0
        #
        # changed = True
        # while changed:
        #     changed = False

        i = 0
        # 从左向右，扩充节点直到与其它节点合并
        while i < n - 1:
            if dp[i] == 0:
                i += 1
                continue

            changed = True
            while changed:
                changed = False

                # 以[i,i+1]为核心扩充节点到最大值
                pre_i = i
                left, right = i - 1, i + dp[i]
                while left >= 0 and right < n and s[left] == '(' and s[right] == ')':
                    dp[left] = dp[i] + 2
                    i -= 1
                    left, right = i - 1, i + dp[i]
                    changed = True

                if pre_i != i:
                    dp_dict.pop(pre_i)
                    dp_dict[i] = dp[i]

                # 判断是否能与其它节点合并，需要考虑左合并
                j = i + dp[i]  # 右合并，是否需要考虑左合并？暂时先不考虑，在最后统一进行一次合并
                while j < n and dp[j] > 0:
                    dp[i] += dp[j]
                    dp_dict.pop(j)
                    j = i + dp[i]
                    changed = True

                dp_dict[i] = dp[i]

                # 左合并，遍历dp_dict，至多只有一个满足条件
                for k, v in dp_dict.items():
                    if k + v == i:
                        dp[k] += dp[i]
                        changed = True
                        dp_dict.pop(i)
                        i = k
                        break

            # # i跳过当前最大的节点
            i += dp[i]

        return max(dp)


# https://leetcode.com/problems/longest-valid-parentheses/solution/
# 解题思路：
# 1. dp: longest valid substring ending at iith index, '()'dp[i]=dp[i-2]+2 '))' dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
# 2. stack: 索引压栈，距离则为长度，起始压-1
# 3. 和我的思路很像，但是我卡在最后未完成的字符串不知道如何处理，解题思路是从右到左再遍历一次，这样就能解决最后一段字符串的问题

class Solution1:
    def longestValidParentheses(self, s):
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)
