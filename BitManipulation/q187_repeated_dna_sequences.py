# Time:  O(n)
# Space: O(1)

# Ideas:
#
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> 'List[str]':
        if len(s) <= 10:
            return []
        dna2bit = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        bit2dna = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        dna_bit = 0
        for c in s:
            dna_bit <<= 2
            dna_bit += dna2bit[c]

        dna_seq = defaultdict(int)
        mask = (1 << 20) - 1
        mask2 = 3
        dna_seq[dna_bit & mask] = 1
        res = []
        for _ in range(len(s) - 10):
            dna_bit >>= 2
            cur_bit = dna_bit & mask
            dna_seq[cur_bit] += 1

            if dna_seq[cur_bit] == 2:
                s = ''
                for _ in range(10):
                    s = bit2dna[cur_bit & mask2] + s
                    cur_bit >>= 2
                res.append(s)
        return res


class Solution1:
    def findRepeatedDnaSequences(self, s):
        res = []
        dic = {"A":1, "C":2, "G":3, "T":4}
        dicDNA = {}
        num = 1
        for i in range(len(s)):
            num = (num*4 + dic[s[i]]) & 0XFFFFF
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            elif dicDNA[num] == 1:
                res.append(s[i-9:i+1])
                dicDNA[num] = 2
        return res

    def findRepeatedDnaSequences1(self, s):
        res, dic = [], {}
        for i in range(len(s) - 9):
            if s[i:i + 10] not in dic:
                dic[s[i:i + 10]] = 1
            elif dic[s[i:i + 10]] == 1:
                res.append(s[i:i + 10])
                dic[s[i:i + 10]] = 2
        return res

