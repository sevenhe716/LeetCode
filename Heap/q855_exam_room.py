# Time:  seat O(n) leave O(log(n))
# Space: O(n)

# 解题思路：
# 多次调用，需要维护当前座位信息的数据结构，当数据稀疏时，维护座位索引即可
# 对于相邻的座位i,j，离相邻学习的最大距离为d = (j-i)//2，新的位置为i+d，但需要保证i+1<j,或者说保证存在座位，则不会取到这种情况（我的计算方式太复杂）
# 特殊情况：左右两端需要单独判断，d = seat_index[0], d = self.N-1-seat_index[-1]，从左至右选择第一个满足条件的解
# O(n)并非效率最高的解法，用最大堆或者优先队列来维护下一个最优位置，可以把seat的时间复杂度降为O(log(n))，但是维护成本变高

import bisect
import heapq
from heapq import heappop, heappush


class ExamRoom:
    @staticmethod
    def call(methods, params):
        room = None
        rets = [0] * len(methods)

        for i, method in enumerate(methods):
            if method == 'ExamRoom':
                room = ExamRoom(params[i][0])
                rets[i] = None
            elif method == 'seat':
                rets[i] = room.seat()
            elif method == 'leave':
                room.leave(params[i][0])
                rets[i] = None

        return rets

    def __init__(self, N):
        """
        :type N: int
        """

        self.seats = [0] * N
        self.dp = [i + 1 for i in range(N)]
        self.N = N

        # print(self.seats)
        # print(self.dp)
        # print()

    def seat(self):
        """
        :rtype: int
        """
        seat_pos = self.find_seat_pos1()
        self.seats[seat_pos] = 1
        self.adjust_seat_seat(seat_pos)

        # print(self.seats)
        # print(self.dp)
        # print(seat_pos)
        # print()

        # if seat_pos >= 0:
        #     self.seats[seat_pos] = 1

        return seat_pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats[p] = 0
        self.adjust_seat_leave(p)

        # print('leave')
        # print(self.seats)
        # print(self.dp)
        # print(p)
        # print()

    def adjust_seat_seat(self, p):
        self.dp[p] = 0
        count = 1
        for i in range(p + 1, self.N):
            if self.seats[i]:
                return
            else:
                self.dp[i] = count
                count += 1

        begin = -1
        for i in range(p)[::-1]:
            if self.seats[i]:
                begin = i
                break

        count = 1
        for i in range(begin + 1, p):
            self.dp[i] = count
            count += 1

    def adjust_seat_leave(self, p):
        begin = -1
        for i in range(p)[::-1]:
            if self.seats[i]:
                begin = i
                break

        end = self.N
        for i in range(p + 1, self.N):
            if self.seats[i]:
                end = i
                break

        count = 1
        for i in range(begin + 1, end):
            self.dp[i] = count
            count += 1

    def find_seat_pos1(self):
        longest = 0
        cur = -1
        for i in range(self.N):
            # 单独讨论两端的情况
            if i == self.N - 1:
                if self.dp[i] << 1 > longest and ((self.dp[i] << 1) - 1) >> 1 > (longest - 1) >> 1:
                    longest = self.dp[i] << 1
                    cur = i
            elif i == self.dp[i] - 1:
                longest = self.dp[i] << 1
                cur = i
            else:
                if self.dp[i] > longest and (self.dp[i] - 1) >> 1 > (longest - 1) >> 1:
                    longest = self.dp[i]
                    cur = i

        # print(cur)
        # print('l={}, c={}'.format(longest, cur))
        # if cur == 7:
        #     print('here')

        if longest >> 1 == self.N:
            return 0
        elif cur == self.N - 1:
            return cur
        elif cur == (longest >> 1) - 1:
            return 0

        cur_seat = cur - longest + 1 + ((longest - 1) >> 1)
        return cur_seat

    # def find_seat_pos(self):
    #     longest = 0
    #     cur = 0
    #     cur_seat = -1
    #
    #     for i, seat in enumerate(self.seats):
    #         if seat:
    #             if i == cur:  # 单独处理头部为0的情况
    #                 if cur > longest >> 1:
    #                     longest = cur << 1
    #                     cur_seat = 0
    #             else:
    #                 # if (cur + 1) >> 1 > longest >> 1 or (longest == 0 and (cur + 1) >> 1 >= longest >> 1):
    #                 if (cur + 1) >> 1 > longest >> 1 and (cur - 1) >> 1 > (longest - 1) >> 1:
    #                     longest = cur
    #                     cur_seat = i - cur + ((cur - 1) >> 1)
    #
    #             cur = 0
    #         else:
    #             cur += 1
    #
    #     if cur > 0:  # 单独处理尾部为0的情况
    #         if cur << 1 > longest:
    #
    #             if cur == len(self.seats):
    #                 cur_seat = 0
    #             else:
    #                 cur_seat = len(self.seats) - 1
    #
    #     return cur_seat


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


class ExamRoom1:
    @staticmethod
    def call(methods, params):
        room = None
        rets = [0] * len(methods)

        for i, method in enumerate(methods):
            if method == 'ExamRoom':
                room = ExamRoom1(params[i][0])
                rets[i] = None
            elif method == 'seat':
                rets[i] = room.seat()
            elif method == 'leave':
                room.leave(params[i][0])
                rets[i] = None

        return rets

    # 这个数据结构维护了区间，同时记录了区间的长度
    # 还可以只维护1的索引，然后每次用1来减

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seat_index = []

    def seat(self):
        """
        :rtype: int
        """
        seat_pos = self.find_seat_pos()
        self.adjust_seat_seat(seat_pos)
        return seat_pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.adjust_seat_leave(p)

    def adjust_seat_seat(self, p):
        import bisect
        bisect.insort(self.seat_index, p)

    def adjust_seat_leave(self, p):
        import bisect
        self.seat_index.pop(bisect.bisect_left(self.seat_index, p))

    def find_seat_pos(self):
        longest = 0
        cur = -1

        if not self.seat_index:
            return 0

        for i in range(len(self.seat_index) - 1):
            zero_count = self.seat_index[i + 1] - self.seat_index[i] - 1
            if zero_count > longest and (zero_count - 1) >> 1 > (longest - 1) >> 1:
                longest = zero_count
                cur = i

        # 单独讨论两端的情况
        zero_count = self.N - self.seat_index[-1] - 1
        if self.seat_index[0] << 1 >= longest and self.seat_index[0] << 1 > 0 and self.seat_index[0] >= zero_count:
            return 0
        if zero_count << 1 > longest and ((zero_count << 1) - 1) >> 1 > (longest - 1) >> 1:
            return self.N - 1

        return self.seat_index[cur] + 1 + ((longest - 1) >> 1)


class ExamRoom2:
    # 最大堆 interval value为离相邻位置的最大距离，还需要一个dict索引左边界 右边界对应的区间，保证可以O(1)时间找到对应区间
    # 添加时，先pop出当前区间，然后将此区间分裂成两个区间即可，删除时，需要找到这个点对应的左右区间，并且删除，合并一个新的区间
    # left+1=right的区间是否要添加
    class Interval:
        def __init__(self, left, right, N):
            self.left = left
            self.right = right
            self.N = N
            self.available = True

        def __lt__(self, other):
            d1 = self.dist()
            d2 = other.dist()

            if d1 == d2:
                return self.left <= other.left        # 相等时选择坐标小的那个
            else:
                return d1 > d2

        def dist(self):
            # 左右边界单独处理
            if self.left == 0 or self.right == self.N:
                return self.right - self.left

            return (self.right - self.left + 1) // 2

        def __str__(self):
            return '({}, {})'.format(self.left, self.right)

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.priority_intervals = []
        self.left_interval_dict = {}
        self.right_interval_dict = {}
        self.add_interval(self.Interval(0, N, N))

    def print_intervals(self):
        print('left ', end='')
        for k, v in self.left_interval_dict.items():
            if v.available:
                print('{}:{} '.format(k, v), end='')
        print()

        print('right ', end='')
        for k, v in self.right_interval_dict.items():
            if v.available:
                print('{}:{} '.format(k, v), end='')
        print()
        print()

    def add_interval(self, interval):
        heapq.heappush(self.priority_intervals, interval)
        self.left_interval_dict[interval.left] = interval
        self.right_interval_dict[interval.right] = interval

    def add_seat(self, p, interval):
        # if interval.left < p:
        #     li = self.Interval(interval.left, p, self.N)
        #     self.add_interval(li)
        #
        # if p + 1 < interval.right:
        #     ri = self.Interval(p + 1, interval.right, self.N)
        #     self.add_interval(ri)
        li = self.Interval(interval.left, p, self.N)
        self.add_interval(li)

        ri = self.Interval(p + 1, interval.right, self.N)
        self.add_interval(ri)

    def pop_seat(self):
        interval = heapq.heappop(self.priority_intervals)

        while not interval.available:
            interval = heapq.heappop(self.priority_intervals)

        self.left_interval_dict.pop(interval.left)
        self.right_interval_dict.pop(interval.right)

        return interval

    # 无法删除heapq中的指定元素，因此使用标记的方式
    def remove_seat(self, p):
        # 暂时默认删除的元素必然存在
        self.add_interval(self.Interval(self.right_interval_dict[p].left, self.left_interval_dict[p+1].right, self.N))
        self.left_interval_dict.pop(p + 1).available = False
        self.right_interval_dict.pop(p).available = False

    def seat(self):
        """
        :rtype: int
        """
        interval = self.pop_seat()

        # 若是两端则取0, n-1，若是中段则(left+right)//2
        if interval.left == 0:
            seat_pos = 0
        elif interval.right == self.N:
            seat_pos = self.N - 1
        else:
            seat_pos = (interval.left + interval.right - 1) // 2

        # print('pos=', seat_pos)

        self.add_seat(seat_pos, interval)
        # self.print_intervals()
        return seat_pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.remove_seat(p)
        # self.print_intervals()

    @staticmethod
    def call(methods, params):
        room = None
        rets = [0] * len(methods)

        for i, method in enumerate(methods):
            if method == 'ExamRoom':
                room = ExamRoom2(params[i][0])
                rets[i] = None
            elif method == 'seat':
                rets[i] = room.seat()
            elif method == 'leave':
                room.leave(params[i][0])
                rets[i] = None

        return rets


class ExamRoom3(object):
    @staticmethod
    def call(methods, params):
        room = None
        rets = [0] * len(methods)

        for i, method in enumerate(methods):
            if method == 'ExamRoom':
                room = ExamRoom3(params[i][0])
                rets[i] = None
            elif method == 'seat':
                rets[i] = room.seat()
            elif method == 'leave':
                room.leave(params[i][0])
                rets[i] = None

        return rets

    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i - 1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.pop(bisect.bisect(self.students, p))


class ExamRoom4:
    @staticmethod
    def call(methods, params):
        room = None
        rets = [0] * len(methods)

        for i, method in enumerate(methods):
            if method == 'ExamRoom':
                room = ExamRoom4(params[i][0])
                rets[i] = None
            elif method == 'seat':
                rets[i] = room.seat()
            elif method == 'leave':
                room.leave(params[i][0])
                rets[i] = None

        return rets

    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L:
            L.append(0)
            return 0
        d = max(L[0], N - 1 - L[-1])
        for a, b in zip(L, L[1:]): d = max(d, (b - a) // 2)  # 这么写很cool，zip并未生成拷贝，也是iter

        if L[0] == d:
            L.insert(0, 0)
            return 0
        for i in range(len(L) - 1):
            if (L[i + 1] - L[i]) / 2 == d:
                L.insert(i + 1, (L[i + 1] + L[i]) // 2)
                return L[i + 1]
        L.append(N - 1)
        return N - 1

    def leave(self, p):
        self.L.remove(p)


# https://leetcode.com/problems/exam-room/discuss/139941/Python-O(log-n)-time-for-both-seat()-and-leave()-with-heapq-and-dicts-Detailed-explanation


class ExamRoom5(object):
    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.heap = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.N - 1)

    def put_segment(self, first, last):

        if first == 0 or last == self.N - 1:
            priority = last - first
        else:
            priority = (last - first) // 2

        segment = [-priority, first, last, True]        # 未使用class，而是把排序值也放进了heap中

        self.avail_first[first] = segment
        self.avail_last[last] = segment

        heappush(self.heap, segment)

    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, first, last, is_valid = heappop(self.heap)

            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break

        if first == 0:
            ret = 0
            if first != last:
                self.put_segment(first + 1, last)

        elif last == self.N - 1:
            ret = last
            if first != last:
                self.put_segment(first, last - 1)

        else:
            ret = first + (last - first) // 2

            if ret > first:
                self.put_segment(first, ret - 1)

            if ret < last:
                self.put_segment(ret + 1, last)

        return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        first = p
        last = p

        left = p - 1
        right = p + 1

        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]

        if right < self.N and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2]

        self.put_segment(first, last)
