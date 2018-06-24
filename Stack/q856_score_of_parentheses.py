# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def scoreOfParentheses1(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(S):
            if S[i] == '(':
                stack.append(-1)
            else:
                top = stack.pop()
                if top == -1:
                    if stack and stack[-1] > 0:
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else:
                    x = stack.pop()
                    while x > 0:
                        top += x
                        x = stack.pop()
                    stack.append(top*2)
            i += 1

        return sum(stack)

    # def scoreOfParentheses(self, S):
    #     """
    #     :type S: str
    #     :rtype: int
    #     """
    #     stack = []
    #
    #     i = 0
    #
    #     cur = 0
    #
    #     while i < len(S):
    #         if S[i] == '(':
    #             if cur != 0:
    #                 stack.append(('+', cur))
    #                 cur = 0
    #             stack.append(('*', 2))
    #         else:
    #             oper = stack.pop()
    #             cur = 1
    #             if oper ==
    #
    #             pass
    #
    #         i += 1
    #
    #
    # def scoreOfParentheses(self, S):
    #     """
    #     :type S: str
    #     :rtype: int
    #     """
    #     def scoreR():
    #         return

class Solution1:
    # use stack or array
    # O(N) time and O(N) space
    def scoreOfParentheses1(self, S):
        res, i = [0] * 30, 0
        for c in S:
            i += 1 if c == '(' else -1
            res[i] = res[i] + max(res[i + 1] * 2, 1) if c == ')' else 0
        return res[0]

    # Count layers and add score when meet "()"
    def scoreOfParentheses2(self, S):
        res = layers = 0
        for a, b in zip(S, S[1:]):
            layers += 1 if a == '(' else -1
            if a + b == '()': res += 2 ** (layers - 1)
        return res

    # stack
    def scoreOfParentheses(self, S):
        stack, res = [], 0
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                add = last and 2 * last or 1    # 2 * last or 1??
                if stack:
                    stack[-1] += add
                else:
                    res += add
        return res
