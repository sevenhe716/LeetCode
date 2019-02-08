# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一个比较常见的思维方式是利用一个map来维护映射关系，如果map出现冲突则返回False
# 不能映射到同一个字符，即一一映射关系
# 优化思路：由于映射空间是确定的，可以用数组来代替map提高索引和存储效率（貌似未限定是大小写字母）

class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        # 先进行长度校验，提高检测效率
        if len(s) != len(t):
            return False

        char_dict = {}
        for c1, c2 in zip(s, t):
            if c1 in char_dict:
                if char_dict[c1] != c2:
                    return False
            else:
                if c2 in char_dict.values():
                    return False
                else:
                    char_dict[c1] = c2
        return True


# elegant solution
class Solution1:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))