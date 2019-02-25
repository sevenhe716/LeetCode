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
                results += [cur for cur in cur_results if cur < max_num]
            else:
                for i in range(cur_num, bit_count):
                    generate_nums(n - 1, max_num, bit_count, i + 1, [cur + 1 << i for cur in cur_results], results)

        ans = []
        for hour_num in range(num + 1):
            hours, minutes = [], []
            generate_nums(hour_num, 11, 4, 0, [0], hours)
            generate_nums(num - hour_num, 59, 6, 0, [0], minutes)
            ans += [str(hour) + ':' + str(minute).zfill(2) for hour in hours for minute in minutes]
        return ans
