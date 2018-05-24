# Time:  O(2^n)
# Space: O(n)

# 解题思路：
# 递归的方式枚举所有的子串，并且用map来维护当前的字符及个数


class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        M = 1000000007

        counts = 0
        for i in range(len(S)):
            counts += self.calcLetters(S, i, 1, 0, 0, {})

        return counts % M

    def calcLetters(self, S, start, length, counts, count, nums_count):
        new_num = S[start + length - 1]

        num_count = nums_count.setdefault(new_num, 0)
        if num_count == 0:
            count += 1
        elif num_count == 1:
            count -= 1

        nums_count[new_num] = num_count + 1
        counts += count

        if start + length + 1 <= len(S):
            counts = self.calcLetters(S, start, length + 1, counts, count, nums_count)

        return counts


class Solution1(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        import string

        M = 10**9 + 7
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        result = 0
        for i, c in enumerate(S):
            k, j = index[c]
            result += (i-j) * (j-k)         # 关键，但为何？
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            result += (len(S)-j) * (j-k)
        return result % M


# F(0)=∑c∈Aindex[c][1]−index[c][0]
class Solution2(object):
    def uniqueLetterString(self, S):
        import collections

        N = len(S)
        index = collections.defaultdict(list)
        peek = collections.defaultdict(int)
        for i, c in enumerate(S):
            index[c].append(i)
        for c in index:
            index[c].extend([N, N])     # 辅助用于尾节点边界判断

        def get(c):
            return index[c][peek[c] + 1] - index[c][peek[c]]

        ans = 0
        cur = sum(get(c) for c in index)

        for i, c in enumerate(S):
            ans += cur
            oldv = get(c)
            peek[c] += 1
            cur += get(c) - oldv
        return ans % (10**9 + 7)


class Solution3:
    def uniqueLetterString(self, S):
        import collections
        indexs = collections.defaultdict(list)
        for i, c in enumerate(S):
            indexs[c].append(i)

        ans = 0
        for A in indexs.values():
            A = [-1] + A + [len(S)]     # bound
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i - 1]) * (A[i + 1] - A[i])

        return ans % 1000000007


class SolutionF:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        m = {}
        res = 0
        for i, j in enumerate(S):
            if j in m:
                b = i - m[j][0] - 1
                res += m[j][1] + b + b * m[j][1] + 1
                m[j] = [i, b]
            else:
                m[j] = [i, i]
        n = len(S)
        for i in m:
            b = n - m[i][0] - 1
            res += m[i][1] + b + b * m[i][1] + 1
        return res

# A character is unique in string S if it occurs exactly once in it.
#
# For example, in string S = "LETTER", the only unique characters are "L" and "R".
#
# Let's define UNIQ(S) as the number of unique characters in string S.
#
# For example, UNIQ("LETTER") =  2.
#
# Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.
#
# If there are two or more equal substrings at different positions in S, we consider them different.
#
# Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.

# Example 1:
#
# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# Example 2:
#
# Input: "ABA"
# Output: 8
# Explanation: The same as example 1, except uni("ABA") = 1.
