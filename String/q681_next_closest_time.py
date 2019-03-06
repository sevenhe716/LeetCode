# Time:  O(4)
# Space: O(1)

# 解题思路：
# 按秒累加时间，但效率太低，很有可能TLE，因此可以尝试用这些数字来递增组合，并验证有效性
# 还有个问题需要确定的是，在字符串上操作，还是在int上操作，由于前面需要补0，使用str比较好
# corner case: 00:00 11:11 22:22
# 可以看作是特殊的加法进位运算
# Time Complexity Analysis:
# Traversing by minutes: O(24 * 60) possible times
# Traversing by allowed digits: O(4^4) possible times
# Find next valid time: at most O(4) possible times
import datetime


class Solution:
    def nextClosestTime1(self, time: str) -> str:
        words = sorted(list(set(time[:2] + time[3:])))
        next_map = {w1: w2 for w1, w2 in zip(words[:-1], words[1:])}
        next_map[words[-1]] = words[0]
        res = list(time[:2] + time[3:])
        idx, carry = len(res) - 1, 1
        while carry and idx >= 0:
            condition, carry = True, 0
            while condition:
                if res[idx] > next_map[res[idx]]:
                    carry = 1
                res[idx] = next_map[res[idx]]
                hour, minute = divmod(int(''.join(res)), 100)
                condition = hour > 23 or minute > 59
                # condition = int(''.join(res[:2])) > 23 or int(''.join(res[2:])) > 59
            idx -= 1
        return ''.join(res[:2]) + ':' + ''.join(res[2:])

    # 不用map
    def nextClosestTime2(self, time: str) -> str:
        words = sorted(list(set(time[:2] + time[3:])))
        res = list(time[:2] + time[3:])
        idx, carry = len(res) - 1, 1

        while carry and idx >= 0:
            condition, carry = True, 0
            while condition:
                next_idx = words.index(res[idx]) + 1
                if next_idx == len(words):
                    next_idx, carry = 0, 1
                res[idx] = words[next_idx]
                hour, minute = divmod(int(''.join(res)), 100)
                condition = hour > 23 or minute > 59
            idx -= 1
        return ''.join(res[:2]) + ':' + ''.join(res[2:])

    # 尝试用int
    def nextClosestTime3(self, time: str) -> str:
        words = sorted(list({int(i) for i in time if i.isdigit()}))
        res = int(time[:2] + time[3:])
        carry, base = 1, 1

        while carry and base <= 1000:

            condition, carry = True, 0
            while condition:
                # 取得当前这一位的数字
                reminder = (res // base) % 10
                next_idx = words.index(reminder) + 1
                if next_idx == len(words):
                    next_idx, carry = 0, 1
                res = res + (words[next_idx] - reminder) * base
                hour, minute = divmod(res, 100)
                condition = hour > 23 or minute > 59
            base *= 10
        q, r = divmod(res, 100)
        return str(q).zfill(2) + ':' + str(r).zfill(2)

    # str version
    def nextClosestTime(self, time: str) -> str:
        words = sorted(list(set(time[:2] + time[3:])))
        res = list(time[:2] + time[3:])
        for idx in range(4)[::-1]:
            next_idx = words.index(res[idx]) + 1
            if next_idx < len(words):
                # change to the next digit
                res[idx] = words[next_idx]
                hour, minute = divmod(int(''.join(res)), 100)
                # if it is valid time and not carry on, return it
                if hour < 24 and minute < 60:
                    return ''.join(res[:2]) + ':' + ''.join(res[2:])
            # back to the first digit, and carry on to high-pos digit
            res[idx] = words[0]
        return ''.join(res[:2]) + ':' + ''.join(res[2:])

    # int version
    def nextClosestTime(self, time: str) -> str:
        words = sorted(list({int(i) for i in time if i.isdigit()}))
        res = int(time[:2] + time[3:])
        base = 1
        while base <= 1000:
            reminder = (res // base) % 10
            next_idx = words.index(reminder) + 1
            if next_idx < len(words):
                res = res + (words[next_idx] - reminder) * base
                hour, minute = divmod(res, 100)
                if hour < 24 and minute < 60:
                    q, r = divmod(res, 100)
                    return str(q).zfill(2) + ':' + str(r).zfill(2)
            res = res + (words[0] - (res // base) % 10) * base
            base *= 10
        q, r = divmod(res, 100)
        return str(q).zfill(2) + ':' + str(r).zfill(2)


class Solution1(object):
    def nextClosestTime1(self, time):
        digits = set(time)
        while True:
            time = (datetime.strptime(time, '%H:%M') + datetime.timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:
                return time

    def nextClosestTime2(self, time):
        # 利用字符本身的有序性，以及集合的包含关系
        return min((t <= time, t)
                   for i in range(24 * 60)
                   for t in ['%02d:%02d' % divmod(i, 60)]
                   if set(t) <= set(time))[1]

    # dfs
    def nextClosestTime3(self, time):
        res = []
        t = ""
        for i in time:
            if i != ":":
                t += i
        if t[0] * 4 == t:
            return time
        self.helper(res, t, 0, "")
        ans = 2400
        dif = 2400
        for i in res:
            if i > t and dif > abs(int(i) - int(t)):
                ans = i
                dif = abs(int(i) - int(t))
            elif t > i and dif > 2400 - int(t) + int(i):
                ans = i
                dif = 2400 - int(t) + int(i)
        return ans[:2] + ":" + ans[2:]

    def helper(self, res, time, idx, path):
        if len(path) == 4:
            res.append(path)
            return

        for i in range(idx, 4):
            if len(path) == 0 and int(time[i]) > 2:
                continue
            elif len(path) == 1 and int(path) > 1 and int(time[i]) > 4:
                continue
            elif len(path) == 2 and int(time[i]) > 5:
                continue

        self.helper(res, time, idx, path + time[i])


# fastest
class Solution:
    # 跟我思路一样，不使用brute-force遍历，而是直接找到下一个合法的时间，因为他的逻辑条件处理分得更细，所以这种解法效率更高
    def nextClosestTime(self, time: 'str') -> 'str':
        H, M = time.split(':')

        n = set()
        n.add(time[0])
        n.add(time[1])
        n.add(time[3])
        n.add(time[4])

        min_n = min(n)
        m_tmrw = h_tmrw = min_n + min_n
        m_today = h_today = None

        # attempt to find next minute today
        one = self.find_next(n, M[1], '0', '9')
        if one:
            m_today = M[0] + one
        else:
            ten = self.find_next(n, M[0], '0', '5')
            if ten:
                m_today = ten + min_n

        # attempt to find next hour today
        if not m_today:
            if H[0] < '2':
                one = self.find_next(n, H[1], '0', '9')
            else:
                one = self.find_next(n, H[1], '0', '4')
            if one:
                h_today = H[0] + one
            else:
                ten = self.find_next(n, H[0], '0', '2')
                if ten:
                    h_today = ten + min_n

        if m_today:
            # if there is a later minute today
            return H + ':' + m_today
        elif h_today:
            # if there is a later hour today
            return h_today + ':' + m_tmrw
        else:
            # otherwise, return the minimum hour and minute tomorrow
            return h_tmrw + ':' + m_tmrw

    def find_next(self, n, t, min_i, max_i):
        return min([i for i in n if i > t and min_i <= i and i <= max_i], default=None)