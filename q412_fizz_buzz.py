# Time:  O(n)
# Space: O(1)

# 解题思路：
# 两种做法，一种是遍历每个数都做取模运算，另一种是先生成再按步长覆盖


class Solution:
    def fizzBuzz1(self, n: 'int') -> 'List[str]':
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans

    def fizzBuzz(self, n: 'int') -> 'List[str]':
        ans = [str(i) for i in range(1, n+1)]
        for i in range(2, n+1, 3):
            ans[i] = 'Fizz'
        for i in range(4, n+1, 5):
            ans[i] = 'Buzz'
        for i in range(14, n+1, 15):
            ans[i] = 'FizzBuzz'
        return ans