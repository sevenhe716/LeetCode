# Time:  O(n)
# Space: O(1)

# 解题思路：
# 实际就是发现邻接矩阵中，一行只有自己是1其余为0，一列全为1
# 可以这个关系想像成小于的关系


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return True

class Solution:
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            for j in range(n):
                # 如果i认识任何一个人，或者任何一个人不认识i，则不是名人
                if i != j and (knows(i, j) or not knows(j, i)):
                    break
            else:
                return i
        return -1


# The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
# After the first loop, x is the only candidate.
# The second and third loop is to verify x is actually a celebrity by definition.
#
# The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison, if a knows b then a < b, if a does not know b, a > b. Then if there is a celebrity, he/she must be the "maximum" of the n people.
#
# However, the "maximum" may not be the celebrity in the case of no celebrity at all. Thus we need the second and third loop to check if x is actually celebrity by definition.
#
# The total calls of knows is thus 3n at most. One small improvement is that in the second loop we only need to check i in the range [0, x). You can figure that out yourself easily.
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # if there is a celebrity, he/she must be the "maximum" of the n people
        # 找到唯一可能的候选者
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # candidate以后的关系已经在上一个循环中检测过了
        for i in range(candidate):
            if knows(candidate, i):
                return -1

        if i in range(n):
            if not knows(i, candidate):
                return -1

        return candidate
