# Time:  O(n)
# Space: O(1)

# 解题思路：
# 跟求开根号一样，用二分查找是一个不错的思路


class Solution:
    def isPerfectSquare1(self, num: 'int') -> 'bool':
        for i in range(1, int(num ** 0.5) + 1):
            if i * i == num:
                return True
        return False

    def isPerfectSquare(self, num: 'int') -> 'bool':
        # 假设high能取到
        low, high = 1, num // 2
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
