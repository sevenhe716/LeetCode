# Time:  O(n)
# Space: O(1)

# 解题思路：
# 若除数为奇数且能整除，若除数为偶数且不能整除，如果余数为除数的一半，则再验证中位数跟长度的一半之差是否大于0（头元素是否大于0）
# 遍历次数需要O(N/2)


class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = set()
        if N == 1:
            return 1

        for i in range(1, int(N / 2 + 1) + 1):
            div, remain = divmod(N, i)

            if remain == 0 and i % 2 == 1 or remain == i // 2 and i % 2 == 0:
                mid = (i + 1) // 2
                if div - mid >= 0:
                    result.add(i)
        return len(result)


class Solution1:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # x + x+1 + x+2 + ... + x+l-1 = N = 2^k * M, where M is odd
        # => l*x + (l-1)*l/2 = 2^k * M
        # => x = (2^k * M -(l-1)*l/2)/l= 2^k * M/l - (l-1)/2 is integer
        # => l could be 2 or any odd factor of M (excluding M)
        #    s.t. x = 2^k * M/l - (l-1)/2 is integer, and also unique
        # => the answer is the number of all odd factors of M
        # if prime factorization of N is 2^k * p1^a * p2^b * ..
        # => answer is the number of all odd factors = (a+1) * (b+1) * ...
        result = 1
        while N % 2 == 0:
            N /= 2
        i = 3
        while i*i <= N:
            count = 0
            while N % i == 0:
                N /= i
                count += 1
            result *= count+1
            i += 2
        if N > 1:
            result *= 2
        return result


# 思路跟我一样，唯一区别是步长在增加，i += j，j += 1
class SolutionF:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        i = 1
        res = 1
        j = 2
        while N > i:
            if j & 1:       # 奇数更简洁的表达
                if N % j == 0:
                    res += 1
            else:
                if N % j == j >> 1:
                    res += 1
            i += j
            j += 1
        return res


# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:
#
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:
#
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
