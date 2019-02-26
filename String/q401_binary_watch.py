# Time:  O(n)
# Space: O(1)

# 解题思路：
# 拼成一个数字10位2进制数，然后获取所有的可能性，然后时分分别转换为有效的字符串，再进行拼接即可
# 效率更高的方式是，先验证有效性再生成数字，时针和分针先后生成合法的组合
# 优化：对于有限的组合方式，可以提前生成缓存起来，以预处理时间和空间来换取执行时间，逻辑上也更简单
from collections import defaultdict


class Solution:
    def generate_nums(self):
        hours, minutes = defaultdict(list), defaultdict(list)
        for i in range(12):
            hours[bin(i)[2:].count('1')].append(i)
        for j in range(60):
            minutes[bin(j)[2:].count('1')].append(j)
        return hours, minutes

    def __init__(self):
        self.hours, self.minutes = self.generate_nums()

    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        ans = []
        for hour_num in range(num + 1):
            hours = self.hours[hour_num]
            minutes = self.minutes[num - hour_num]
            ans += [str(hour) + ':' + str(minute).zfill(2) for hour in hours for minute in minutes]
        return ans

    def readBinaryWatch1(self, num: 'int') -> 'List[str]':
        # 生成方式，位运算或者用字符串拼接
        def generate_nums(n, max_num, bit_count, cur_num, cur_results, results):
            if n == 0:
                # results += [cur for cur in cur_results if cur < max_num]
                if cur_results < max_num:
                    results.append(cur_results)
            else:
                for i in range(cur_num, bit_count):
                    # cur_results不是集合，而是单个数
                    generate_nums(n - 1, max_num, bit_count, i + 1, cur_results + (1 << i), results)
                    # generate_nums(n - 1, max_num, bit_count, i + 1, [cur + (1 << i) for cur in cur_results], results)

        ans = []
        for hour_num in range(num + 1):
            hours, minutes = [], []
            generate_nums(hour_num, 12, 4, 0, 0, hours)
            generate_nums(num - hour_num, 60, 6, 0, 0, minutes)
            ans += [str(hour) + ':' + str(minute).zfill(2) for hour in hours for minute in minutes]
        return ans


class Solution1:
    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        def dfs(nums, count, start, s, paths):
            if count == 0:
                paths.append(s)
                return
            for i in range(start, len(nums)):
                dfs(nums, count-1, i+1, s+nums[i], paths)

        res = []
        nums1, nums2 = [8,4,2,1], [32,16,8,4,2,1]
        for i in range(num+1):
            paths1, paths2 = [], []
            dfs(nums1, i, 0, 0, paths1)
            dfs(nums2, num-i, 0, 0, paths2)
            for n1 in paths1:
                if n1 >= 12:
                    continue
                for n2 in paths2:
                    if n2 >= 60:
                        continue
                    if n2 < 10:
                        res.append(str(n1) + ":0" + str(n2))
                    else:
                        res.append(str(n1) + ":" + str(n2))
        return res

    # 简单粗暴，遍历的开销比较大
    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        return ["%d:%02d" % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]