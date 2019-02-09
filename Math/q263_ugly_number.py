# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一个思路是一直用2，3，5来除，直到为1


class Solution:
    # 优化思路，可以先把2除完，再除3，除5，无需一直遍历
    def isUgly(self, num: 'int') -> 'bool':
        if num <= 0:
            return False
        factors = [2, 3, 5]
        while num > 1:
            # for else的应用场景
            for factor in factors:
                if num % factor == 0:
                    num //= factor
                    break
            else:
                return False
        return True


class Solution1:
    def isUgly(self, num: 'int') -> 'bool':
        if num <= 0:
            return False
        if num != 0:
            for n in [2, 3, 5]:
                while num % n == 0:
                    num //= n

        return num == 1
