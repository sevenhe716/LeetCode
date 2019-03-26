# Time:  O(n)
# Space: O(1)

# Ideas:
# dfs is too slow, exclude start with zero
# operator priority, stack to implement
# mark
from functools import reduce


class Solution:
    def addOperators(self, num: str, target: int) -> 'List[str]':
        if not num:
            return []
        oper_funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

        def calc(num, oper):
            start = 0
            numbers = []
            for i, op in enumerate(oper):
                if op != '':
                    num_str = num[start:i+1]
                    if num_str.startswith('0') and num_str != '0':
                        return
                    numbers.append(int(num_str))
                    start = i + 1
            num_str = num[start:]
            if num_str.startswith('0') and num_str != '0':
                return
            numbers.append(int(num_str))

            # print(numbers)
            cur_oper = ['+', numbers[0]]
            result = 0
            for n, o in zip(numbers[1:], filter(None, oper)):
                if o != '*':
                    result = oper_funcs[cur_oper[0]](result, cur_oper[1])
                    cur_oper = [o, n]
                else:
                    cur_oper[1] = oper_funcs[o](cur_oper[1], n)
            result = oper_funcs[cur_oper[0]](result, cur_oper[1])

            # print(result)
            return result

        opers = [[]]
        for i in range(len(num) - 1):
            opers = [op + [o] for op in opers for o in ('', '*', '+', '-')]

        res = []
        for op in opers:
            if calc(num, op) == target:
                res.append(reduce(lambda x, y: x + y[1] + y[0], zip(num[1:], op), num[0]))

        return res


class Solution1:
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)