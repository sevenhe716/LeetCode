# Time:  O(n)
# Space: O(1)

# 解题思路：
# 从后往前对比，当出现#号时继续往前直到非#号个数抵消#号为止
# 更简单但效率较低的做法是，生成最终的字符串并对比，但是有生成字符串的开销


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        si = len(S) - 1
        ti = len(T) - 1
        sb = 0
        tb = 0

        while si >= 0 and ti >= 0:
            if S[si] != '#' and T[ti] != '#':
                if S[si] == T[ti]:
                    si -= 1
                    ti -= 1
                else:
                    return False
            else:
                if S[si] == '#':
                    sb += 1
                    si -= 1
                    while si >= 0 and sb > 0:
                        if S[si] == '#':
                            sb += 1
                            si -= 1
                        else:
                            sb -= 1
                            si -= 1

                if T[ti] == '#':
                    tb += 1
                    ti -= 1
                    while ti >= 0 and tb > 0:
                        if T[ti] == '#':
                            tb += 1
                            ti -= 1
                        else:
                            tb -= 1
                            ti -= 1

        if si >= 0:
            while si >= 0 and S[si] == '#':
                sb += 1
                si -= 1
                while si >= 0 and sb > 0:
                    if S[si] == '#':
                        sb += 1
                        si -= 1
                    else:
                        sb -= 1
                        si -= 1

        if si >= 0:
            return False

        if ti >= 0:
            while ti >= 0 and T[ti] == '#':
                tb += 1
                ti -= 1
                while ti >= 0 and tb > 0:
                    if T[ti] == '#':
                        tb += 1
                        ti -= 1
                    else:
                        tb -= 1
                        ti -= 1

        if ti >= 0:
            return False

        return True


# Build String
class Solution1(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


# 跟我的思路相同，但是比我简洁很多，构造遍历器
class Solution2(object):
    def backspaceCompare(self, S, T):
        import itertools
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x     # 借鉴：yield构造迭代器

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))        # 借鉴：zip_longest，构造对比的元组
