# Time:  O(n)
# Space: O(1)

# 解题思路：
# 优化思路：左右两端可以寻找第一个1到两端的距离即可


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        longest = 0
        cur = 0
        # end = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                if i == cur:        # 单独处理头部为0的情况
                    longest = max(longest, cur * 2)
                else:
                    longest = max(longest, cur)
                # if cur > longest:
                #
                #     longest = cur
                #     end = i
                cur = 0
            else:
                cur += 1

        if cur > 0:     # 单独处理尾部为0的情况
            longest = max(longest, cur * 2)

        # if cur >= longest:
        #     longest = cur
        #     end = len(seats)

        # if end == len(seats) or end - longest == 0:
        #     return longest
        # else:
        return (longest + 1) // 2


class Solution1:
    # left right数组维护离左和右边人的距离，二者的最小值则是实际距离，注意如果是两端则为N
    # 这个算法的缺点是，有2N的空间复杂度
    def maxDistToClosest1(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:     # 排除i==0的情况
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                right[i] = right[i + 1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)     # 当座位为空时


    # 双指针维护左右两人的坐标
    def maxDistToClosest2(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev       # 不能用if not，因为有0的可能性
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans


    # 跟我的思路类似(k+1) // 2，优化的点在于itertools.groupby寻找0的区间，以及用index处理双端0的情况
    def maxDistToClosest3(self, seats):
        import itertools
        ans = 0
        for seat, group in itertools.groupby(seats):        # groupby
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) // 2)

        return max(ans, seats.index(1), seats[::-1].index(1))   # 左右两端可以寻找第一个1到两端的距离即可
