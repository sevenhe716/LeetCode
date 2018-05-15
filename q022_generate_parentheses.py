# Time:  O(2^n)
# Space: O(1)

# 解题思路：
# 递归或迭代的方式，维护左右括号的个数
# 还有一种思路是从1开始，往已有的序列中插入括号


class Solution:
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateParentheseR(left_count, count, results):
            if count == n + n:
                return results

            new_results = []

            if left_count < n:      # 没有必要维护中间结果的集合，可以结束时再添加，通过参数值传递来维护
                new_results += generateParentheseR(left_count + 1, count + 1, [result + '(' for result in results])

            if count - left_count < left_count:
                new_results += generateParentheseR(left_count, count + 1, [result + ')' for result in results])

            return new_results

        return generateParentheseR(0, 0, [''])

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        # 没有必要维护中间结果的集合，可以结束时再添加，通过参数值传递来维护
        # P.S. 事实证明，前一种方法更快？？
        def generateParentheseR(left_count, count, s):
            if count == n << 1:
                results.append(s)
                return

            if left_count < n:
                generateParentheseR(left_count + 1, count + 1, s + '(')

            if count - left_count < left_count:
                generateParentheseR(left_count, count + 1, s + ')')

        generateParentheseR(0, 0, '')

        return results

    # 迭代的算法比递归慢很多，是不知道是否是因为slice拼接的原因，已优化为在结束时整体删除
    def generateParenthesis3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = [[]]
        counts = [0]

        for i in range(n + n):
            last_len = len(results)
            for j in range(last_len)[::-1]:
                s = results[j]
                # left_count = s.count('(')  # 优化：count效率太低，不如用一个变量来维护
                left_count = counts[j]
                # results = results[:j] + results[j + 1:]
                # counts = counts[:j] + counts[j + 1:]
                if left_count < n:
                    results.append(s + ['('])
                    counts.append(left_count + 1)
                if i - left_count < left_count:
                    results.append(s + [')'])
                    counts.append(left_count)

            results = results[last_len:]
            counts = counts[last_len:]

        return [''.join(r) for r in results]


# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
class Solution1:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)


class SolutionF:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        left = right = n  # 从n到0，无需再传n
        result = []
        self.generate(left, right, result, '')
        return result

    def generate(self, left, right, result, string):  # string来保存结果，无需用中间的list来存
        if left == 0 and right == 0:  # 递归结束时再添加元素
            result.append(string)
            return
        if left:
            self.generate(left - 1, right, result, string + '(')
        if left < right:
            self.generate(left, right - 1, result, string + ')')

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
