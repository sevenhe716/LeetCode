# Time:  O(n)
# Space: O(1)

# 解题思路：
# 先对pattern作预处理，防止'..****..'的情况出现，会导致遍历分支指数级增加，考虑使用回溯


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ls, lp = len(s), len(p)

        # 递归方法，且不用slice，而是用索引下标
        def isMatchR(s_i, p_i):
            if p_i == lp:
                if s_i < ls:
                    return False
                else:
                    return True

            # lp > 0
            if s_i == ls:
                if all([c == '*' for c in p[p_i:]]):
                    return True
                else:
                    return False

            # ls > 0 and lp > 0
            if p[p_i] == '?':
                return isMatchR(s_i + 1, p_i + 1)
            elif p[p_i] == '*':  # util not * 直接跳过多个*
                while p_i + 1 < lp and p[p_i] == '*':
                    p_i += 1

                if p[p_i - 1] == '*':
                    p_i -= 1
                return isMatchR(s_i + 1, p_i) or isMatchR(s_i, p_i + 1)
            else:
                if p[p_i] != s[s_i]:
                    return False
                else:
                    return isMatchR(s_i + 1, p_i + 1)

        return isMatchR(0, 0)


# Two pointer O(n)
class Solution1:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''维护两个下标，逐个比较，如果pj为*，则记录*的位置，将*后一个元素与si进行比较，如果不相等，则将i从记录的位置+1，重新比较'''
        s_cur, p_cur, match, star = 0, 0, 0, -1

        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            elif star != -1:
                p_cur = star + 1
                match += 1
                s_cur = match
            else:
                return False
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1

        if p_cur == len(p):
            return True
        else:
            return False
