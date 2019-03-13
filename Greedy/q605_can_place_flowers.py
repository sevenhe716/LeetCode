# Time:  O(n)
# Space: O(1)

# 解题思路：
# 比较直观的方法是用flag标记是否能种花，然后当n已经为0时，提前终止循环
# 如果用数学方法直接分割出0的序列，然后统计0的个数，这个解法有个缺陷是需要单独讨论左右两端，或者说可以在左右两端加0
# 可以改变原数组，使用贪心算法


class Solution:
    def canPlaceFlowers1(self, flowerbed: 'List[int]', n: int) -> bool:
        if n == 0:
            return True
        can = True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                can = False
            else:
                if can and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
                    n -= 1
                    if n == 0:
                        return True
                    can = False
                else:
                    can = True
        return False

    def canPlaceFlowers(self, flowerbed: 'List[int]', n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        zero_cnt = 0
        for fb in flowerbed:
            if fb == 0:
                zero_cnt += 1
            else:
                n -= max((zero_cnt - 1) // 2, 0)
                zero_cnt = 0
                if n <= 0:
                    return True
        n -= max((zero_cnt - 1) // 2, 0)
        return n <= 0


class Solution1:
    # 我的解法的优化版，不管是计算量还是简洁度上都更佳
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return True
        return False

    # 贪心算法
    def canPlaceFlowers(self, A, N):
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0)
                    and (i == len(A)-1 or A[i+1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0