# Time:  O(n)
# Space: O(1)

# 解题思路：
# 维护cur_char char_count，遍历一遍字符串即可
# 需要注意的是，退出循环后，最后一段的特殊处理
# 优化思路：Two-Pointers思路更清晰


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        if not S or len(S) < 3:
            return []

        count = 0
        char = S[0]
        result = []

        for index in range(len(S)):
            if S[index] == char:
                count += 1
            else:
                if count >= 3:
                    result.append([index - count, index - 1])
                char = S[index]
                count = 1

        if count >= 3:
            result.append([index - count + 1, index])

        return result


# 无需存char，直接比较S[j]与S[j + 1]，count也可以用start指针来代替
class Solution1(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    result.append([i, j])
                i = j + 1
        return result


# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.


