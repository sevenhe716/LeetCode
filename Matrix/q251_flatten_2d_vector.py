# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一种做法是遍历时改变二维索引，一种做法是预处理时展平数组，预处理有额外的空间开销，而且如果没遍历完，预处理的开销也是浪费掉的

class Vector2D:
    def __init__(self, v: 'List[List[int]]'):
        self.v = [_v for _v in v if _v]
        self.i, self.j = 0, 0

    def next(self) -> int:
        res = self.v[self.i][self.j]
        self.j += 1
        if self.j == len(self.v[self.i]):
            self.i, self.j = self.i + 1, 0
        return res

    def hasNext(self) -> bool:
        return self.i < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Vector2D1:
    def __init__(self, v: 'List[List[int]]'):
        self.iter = 0
        self.vec = [v[i][j] for i in range(len(v)) for j in range(len(v[i]))]

    def next(self) -> 'int':
        val = self.vec[self.iter]
        self.iter += 1
        return val

    def hasNext(self) -> 'bool':
        if self.iter < len(self.vec):
            return True
        return False


class Vector2D2:
    def __init__(self, a):
        def it():
            for line in a:
                for val in line:
                    self.size -= 1
                    yield val

        self.it = it()
        self.size = sum(len(line) for line in a)

    def next(self):
        return next(self.it)

    def hasNext(self):
        return self.size