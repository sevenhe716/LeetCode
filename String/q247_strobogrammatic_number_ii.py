# Time:  O(n)
# Space: O(1)

# 解题思路：
# 由strob_map中的数组成n位数字，实际上只有n//2+1个数能确定，其他数是由map生成
# 有一些约束条件：0不能作为开头，单个的字符不能是6，9


class Solution:
    def findStrobogrammatic(self, n: int) -> 'List[str]':
        strob_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = ['']

        for i in range(n // 2):
            # 0不能作为开头
            res = [r + k for r in res for k in strob_map.keys() if i > 0 or (i == 0 and k != '0')]
        # 中间的单个字符只能为018
        if n % 2 == 1:
            res = [r + k for r in res for k in '018']
        # 翻转数组
        for i, r in enumerate(res):
            # 如果是奇数位，需排除中间那个元素
            res[i] = r + ''.join(strob_map[k] for k in (r[-2::-1] if n % 2 else r[::-1]))

        return res


class Solution1:
    # pythnic
    def findStrobogrammatic(self, n):
        nums = n % 2 * list('018') or ['']
        while n > 1:
            n -= 2
            # n < 2 真的是genius，神来之笔，保证最外面的那个数不取到0
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n < 2:] for num in nums]
        return nums

    def findStrobogrammatic1(self, n):
        numbers = ['0', '1', '8'] if n % 2 else ['']
        for _ in range(n // 2):
            numbers = [head + s + tail for head, tail in [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
                       for s in numbers]
        # 先加0，再筛选一次
        return [s for s in numbers if s and (s[0] != '0' or len(s) == 1)]
