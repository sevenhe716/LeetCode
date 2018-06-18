# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# 到终点之前追上为一个车队
# p1>=p2 and t1>=t2


class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)

        if not n:
            return 0

        # time = [float(target - p) / s for p, s in sorted(zip(position, speed))] 用zip更好
        time = [(target-position[i]) / speed[i] for i in range(n)]
        a = sorted(list(zip(position, time)), reverse=True)     # 这里zip之后转成list有性能损失

        count = 1
        cur = a[0][1]
        for i in range(1, n):
            # if a[i][1] < a[i+1][1]:
            if a[i][1] > cur:
                count += 1
                cur = a[i][1]

        return count

    # 思路相同，优化之后的写法
    def carFleet1(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
