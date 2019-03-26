# Time:  O(kn)
# Space: O(k)

# Ideas:
# trie tree + interval merge
# mark


class Solution:
    def addBoldTag(self, s: str, dict: 'List[str]') -> str:
        trie, n, intervals, res = {}, len(s), [], ""

        # create trie tree
        for w in dict:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = 1

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, max_end = trie, None
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += s[prev_end:start] + '<b>' + s[start:end] + "</b>"
            prev_end = end
        return res + s[prev_end:]


# 简单的find and mask
class Solution1:
    def addBoldTag(self, s: 'str', dict: 'List[str]') -> 'str':
        if not len(s): return ''
        if not dict or not len(dict): return s
        #mark all chars within s to be bolded
        bolded = [False]*len(s)
        for word in dict:
            index = -1
            while True:
                #need to identify overlapping occurrences as well
                index = s.find(word, index+1)
                if index != -1:
                    bolded[index:index+len(word)] = [True]*len(word)
                else: break
        answer = []
        for index in range(len(bolded)):
            if bolded[index] and (index == 0 or not bolded[index-1]):
                answer.append('<b>')
            answer.append(s[index])
            if bolded[index] and (index == len(bolded)-1 or not bolded[index+1]):
                answer.append('</b>')
        return ''.join(answer)