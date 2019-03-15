# Time:  O(n)
# Space: O(1)

# 解题思路：
# 选择一个分隔符，并且把该字符在原字符串中进行转义


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """

        return ''.join(s.replace('|', '||') + ' | ' for s in strs)


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))