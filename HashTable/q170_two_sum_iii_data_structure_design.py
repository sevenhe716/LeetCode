# Time:  O(n)
# Space: O(n^2)

# 解题思路：
# 没有删除功能，因此加速方式是可以缓存求和的结果，可以将find降为O(1)，但add的时间复杂度为O(n)
# 如果add的时间复杂度要求更高，那可以用dict，这样add的时间复杂度为O(1)，find为O(n)

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.sums = set()

    # O(n)
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # 如果允许有重复的元素存在的话，实际上相同的元素至多存两个即可
        for n in self.nums:
            self.sums.add(n + number)
        self.nums.append(number)

    # O(1)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.sums


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


# set解法的key point处理重复元素的问题，因为dict不支持重复，而如果允许有重复的元素存在的话，实际上相同的元素至多存两个即可，
# 因此我们可以再用一个set来存储重复的元素
class TwoSum1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        self.dup_nums = set()

    # O(1)
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.nums:
            self.nums.add(number)
        elif number not in self.dup_nums:
            self.dup_nums.add(number)

    # O(n)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self.dup_nums:
            if number << 1 == value:
                return True
        for number in self.nums:
            # 需先排除掉匹配自身的情况
            if number << 1 != value and value - number in self.nums:
                return True

        return False


# 最快的解法相对于我的解法有几处地方加速：
# 1. 用dict来整合两个set
# 2. 和我第一种解法一样，用sum缓存加速，但是他是边遍历边缓存，没有在add时缓存，使得add的开销不会特别大，find的开销也实现了均摊
# 3. 另外还使用了边界值作为额外的预处理加速
class TwoSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.sum = set()
        self.max = float('-inf')
        self.min = float('inf')

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1
        self.max = max(self.max, number)
        self.min = min(self.min, number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value > 2 * self.max or value < 2 * self.min:
            return False
        if value in self.sum:
            return True
        for k in self.data.keys():
            if (value - k != k and value - k in self.data) or (value - k == k and self.data[k] > 1):
                self.sum.add(value)
                return True
        return False
