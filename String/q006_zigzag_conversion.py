# Time:  O(n)
# Space: O(1)

# 解题思路：
# 找到基本循环单元(row+row-2)，从原字符串中依次索引相应的元素即可
# 特殊情况处理：
# 1. 最后一个zigzag可能不完整
# 2. row=0, 1, 2的边界条件


class Solution:
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        n = len(s)
        str_list = []

        if numRows <= 1:        # 边界条件判断
            return s

        zig_size = numRows * 2 - 2
        zig_count = n // zig_size      # 完整的zig个数，实际可能会再多一个

        for i in range(numRows):
            if i == 0 or i == numRows - 1:      # 当为头尾两行时
                for j in range(zig_count + 1):  # 把最后一个不完整的zig归在一起写法上更简洁，但是每次都需要判断是否越界
                    index = j * zig_size + i
                    if index < n:
                        str_list.append(s[index])
            else:
                for j in range(zig_count + 1):
                    index = j * zig_size + i
                    if index < n:
                        str_list.append(s[index])
                    index = (j + 1) * zig_size - i
                    if index < n:
                        str_list.append(s[index])

        return ''.join(str_list)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step, zigzag = 2 * numRows - 2, ''                  # 字符串累加的写法，不太苟同，效率应该不如list
        for i in range(numRows):
            for j in range(i, len(s), step):                # step长度的遍历，借鉴这种写法
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):   # 非两端的行数再做额外添加即可
                    zigzag += s[j + step - 2 * i]
        return zigzag


# 按行建string，step在行之间走Z字形，用空间换时间，时间复杂度同样是O(n)只是运算量小一些
class SolutionF:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        r = ['']*numRows
        k = 0
        step = 1
        for i in s:
            r[k] += i
            if k == 0:
                step = 1
            elif k == numRows - 1:
                step = -1
            k += step
        return ''.join(r)


# 额外思考：关于python str concat与join的对比：
# https://stackoverflow.com/questions/19926089/python-equivalent-of-java-stringbuffer
# its main statement that the naive concatenation is far slower than joining is not valid anymore,
# because this part has been optimized in CPython

