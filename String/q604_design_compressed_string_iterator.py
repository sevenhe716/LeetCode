# Time:  O(n)
# Space: O(1)

# 解题思路：
# 如何高效的切分字符串，如果用yield构造generator不能同时支持next hasNext两个api
# 切分方法可以用正则表达式，或者两次split，或者自己遍历完成
# 优化：可以不进行预处理和额外的空间存储，直接在原字符串上迭代，省去了预处理时间以及额外的空间开销 Demand-Computation vs. Pre-Computation
import re


class StringIterator:
    def __init__(self, compressedString: str):
        self.cs, char, n = [], None, ''
        for c in compressedString:
            if c.isalpha():
                if n != '':
                    self.cs.append((char, int(n)))
                char, n = c, ''
            else:
                n += c
        # 注意这里处理尾部的边界情况
        self.cs.append((char, int(n)))
        self.idx1, self.idx2 = 0, 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        res = self.cs[self.idx1][0]
        self.idx2 += 1
        if self.idx2 == self.cs[self.idx1][1]:
            self.idx1, self.idx2 = self.idx1 + 1, 0
        return res

    def hasNext(self) -> bool:
        return self.idx1 < len(self.cs)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class StringIterator1:
    def __init__(self, compressedString):
        self.tokens = []
        # 正则表达式，字符串处理效率更高
        self.tokens = [(token[0], int(token[1:])) for token in re.findall('\\D\\d+', compressedString)][::-1]

    def next(self):
        if not self.tokens: return ' '
        t, n = self.tokens.pop()
        if n > 1:
            self.tokens.append((t, n - 1))
        return t

    def hasNext(self):
        return bool(self.tokens)

class StringIterator2:
    # 两次re.split
    def __init__(self, compressedString):
        self.values = re.split('[a-zA-Z]+', compressedString)[1:][::-1]
        self.letter = re.split('[0-9]+', compressedString)[0:-1][::-1]

    def next(self):
        if self.hasNext():
            value = self.values.pop()
            letter = self.letter.pop()
            if int(value) > 1:
                self.values.append(str(int(value)-1))
                self.letter.append(letter)
            return letter
        return ' '

    def hasNext(self):
        return not (len(self.values) == 0)


# Python solution with Lazy initializer
class StringIterator3:
    def __init__(self, compressedString):
        self.data = compressedString
        self.idx = -1
        self.decodeNext()

    def decodeNext(self):
        self.idx += 1
        if self.idx + 1 < len(self.data):
            self.cur = self.data[self.idx]
            end = self.idx + 1
            while end < len(self.data) and self.data[end].isdigit():
                end += 1
            self.num = int(self.data[self.idx + 1:end])
            self.idx = end - 1

    def next(self):
        if self.hasNext():
            ret = self.cur
            self.num -= 1
            if self.num <= 0:
                self.decodeNext()
            return ret
        return " "

    def hasNext(self):
        return self.idx < len(self.data) and self.num > 0


# Demand-Computation
class StringIterator4:
    def __init__(self, compressedString: str):
        self.s, self.n = compressedString, len(compressedString)
        self.char = self.count = self.total = self.end = 0

    def counter(self):
        i = start = self.char + 1
        while i < self.n and self.s[i].isdigit():
            i += 1
        self.total = int(self.s[start:i])
        return i

    def next(self) -> str:
        if self.char >= self.n:
            return " "
        if self.count == 0:
            self.end = self.counter()
        c = self.s[self.char]
        self.count += 1
        if self.count == self.total:
            self.char = self.end
            self.count = 0
        return c

    def hasNext(self) -> bool:
        return self.char < self.n
