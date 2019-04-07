# Time:  O(n)
# Space: O(m)

# 解题思路：
# Hash生成字符串的指纹，hash满足交换率，当总hash相等时，再进一步检查每三个的hash值是否相等
# 疑问：words that are all of the same length，为什么第二个测试用例就不等长了？？
# 优化思路：
# 其实直接用hashtable，string作key即可，无需再自己生成hash值，然后需要注意的是words可能会重复，所以需要用counter来计数
# 利用滑动窗口算法，遍历word长度次，用counter和left指针来维护当前滑动窗口的位置和进度
from collections import Counter


class Solution:
    def findSubstring1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or not words:
            return []

        m = len(words)
        n = len(words[0])

        words_hash = []

        def cal_hash(word, begin, count):
            hash = 0
            bit = 0
            for i in range(count):
                c = word[begin + i]
                if c.islower():
                    hash += (ord(c) - ord('a')) << bit
                else:
                    hash += (ord(c) - ord('A')) << (bit + 1)
                bit += 6
            return hash

        for w in words:
            words_hash.append(cal_hash(w, 0, n))

        words_hash.sort()
        total_hash = sum(words_hash)

        ans = []

        for i in range(len(s) - m * n + 1):
            start = i
            cur_words_hash = []

            for j in range(m):
                cur_words_hash.append(cal_hash(s, start, n))
                start += n

            if sum(cur_words_hash) == total_hash and sorted(cur_words_hash) == words_hash:
                ans.append(i)

        return ans

    def findSubstring(self, s: str, words: 'List[str]') -> 'List[int]':
        if not words:
            return []

        word_len, res = len(words[0]), []

        # start offset from 0 to word_len, and step is word_len
        for i in range(word_len):
            # reset state every epoch
            counter = Counter(words)
            start, end, count = i, i, len(words)
            while end < len(s):
                cur_word = s[end:end + word_len]
                # check is not necessary here, just for performance
                if cur_word in counter:
                    counter[cur_word] -= 1
                    if counter[cur_word] >= 0:
                        count -= 1
                end += word_len

                if count == 0:
                    res.append(start)

                # ensure consecutive words
                if end - start == word_len * len(words):
                    cur_word = s[start:start + word_len]
                    if cur_word in counter:
                        counter[cur_word] += 1
                        if counter[cur_word] > 0:
                            count += 1
                    start += word_len

        # the order is not necessary here
        return res

class Solution1:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections

        if not s or not words:
            return []

        m = len(words)
        n = len(words[0])

        words_counter = collections.Counter(words)  # 需要考虑重复的情况
        ans = []

        for i in range(n):
            left = i
            count = 0
            cur_counter = collections.defaultdict(int)

            for j in range(i, len(s) - n + 1, n):
                cur_str = s[j:j + n]

                if cur_str in words_counter:
                    if cur_counter[cur_str] < words_counter[cur_str]:
                        cur_counter[cur_str] += 1
                        count += 1
                    else:
                        # 从left开始遍历，移除word直到为cur_str
                        left_str = s[left:left+n]
                        # while left_str != cur_str or (left_str == cur_str and cur_counter[left_str] >= words_counter[left_str]):
                        while left_str != cur_str:
                            cur_counter[left_str] -= 1
                            count -= 1
                            left += n
                            left_str = s[left:left+n]

                        left += n

                    if count == m:
                        ans.append(left)
                        cur_counter[s[left:left+n]] -= 1
                        count -= 1
                        left += n

                else:
                    cur_counter.clear()
                    left = j + n
                    count = 0

        return ans

    # variation with complex match policy
    def findSubstring2(self, s: str, words: 'List[str]') -> 'List[int]':
        if not words:
            return []

        word_len, res = len(words[0]), []

        # start offset from 0 to word_len, and step is word_len
        for i in range(word_len):
            # reset state every epoch
            counter = Counter(words)
            start, end, count = i, i, len(words)
            while end < len(s):
                cur_word = s[end:end + word_len]
                # check is not necessary here, just for performance
                if cur_word in counter:
                    counter[cur_word] -= 1
                    if counter[cur_word] >= 0:
                        count -= 1
                end += word_len

                if count == 0:
                    res.append(start)

                # ensure consecutive words
                if end - start == word_len * len(words):
                    cur_word = s[start:start + word_len]
                    if cur_word in counter:
                        counter[cur_word] += 1
                        if counter[cur_word] > 0:
                            count += 1
                    start += word_len

        # the order is not necessary here
        return res
