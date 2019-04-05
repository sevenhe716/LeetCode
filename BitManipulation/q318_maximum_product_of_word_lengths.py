# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def maxProduct(self, words: 'List[str]') -> int:
        max_len = 0
        word_bits = []
        for word in words:
            word_bit = 0
            for c in word:
                word_bit |= 1 << ord(c) - ord('a')

            for i, cur_bit in enumerate(word_bits):
                if cur_bit & word_bit == 0:
                    max_len = max(max_len, len(words[i]) * len(word))

            word_bits.append(word_bit)
        return max_len
