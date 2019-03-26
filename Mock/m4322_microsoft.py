# Time:  O(n)
# Space: O(1)

# Ideas:
#


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        # find candidate
        candidate = 0
        find = True
        while find:
            find = False
            for j in range(candidate+1, n):
                if knows(candidate, j):
                    candidate = j
                    find = True
                    break

        for i in range(candidate):
            if i != candidate and knows(candidate, i):
                return -1

        for i in range(n):
            if not knows(i, candidate):
                return -1
        return candidate
