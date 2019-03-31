# Time:  O(n)
# Space: O(1)

# 解题思路：
# 寻找最长子序列
# 一种思路是找到所有的匹配索引start和end，然后合并排序后得到合并区间位置
# 另一种思路是边遍历边匹配并合并区间
# 用mask标记所有匹配的字符，然后再统一修改
# Trie树


class Solution:
    def boldWords(self, words: 'List[str]', S: str) -> str:
        res = S
        idxs = []
        for word in words:
            word_len = len(word)
            idx = S.find(word, 0)
            while idx != -1:
                idxs += [(idx, 0), (idx + word_len, 1)]
                idx = S.find(word, idx + 1)
        idxs.sort(reverse=True)
        count = 0
        for idx in idxs:
            if idx[1] == 0:
                count -= 1
                if count == 0:
                    res = res[:idx[0]] + '<b>' + res[idx[0]:]
            else:
                count += 1
                if count == 1:
                    res = res[:idx[0]] + '</b>' + res[idx[0]:]
        return res


class Solution1:
    # 区间合并解法，边遍历边合并，比我的解法空间占有率更小
    def boldWords(self, words: 'List[str]', S: str) -> str:
        intervals = []

        def add_interval(interval):
            # 区间合并
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # 逐个字符匹配，时间复杂度O(mn)
        for pos in range(len(S)):
            # 如果有多个匹配时只添加最长区间
            matched_words = list(filter(lambda x: S[pos:].startswith(x), words))
            if matched_words:
                add_interval([pos, pos + len(max(matched_words, key=lambda x: len(x)))])

        ans, prev_end = "", 0
        for start, end in intervals:
            ans += S[prev_end:start] + '<b>' + S[start:end] + "</b>"
            prev_end = end
        ans += S[prev_end:]
        return ans


class Solution2:
    def boldWords(self, words: 'List[str]', S: str) -> str:
        trie, n, mask, res = {}, len(S), set(), ""
        for w in words:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            # 无需将word存入终止符的set中
            cur["#"] = cur.get("#", set()) | {w}
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                # 这里可以优化：只需要寻找到最长的子串并mask即可，而不需要每次匹配都添加，前面必定是重复的
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"
        return res


class Solution3:
    def boldWords(self, words: 'List[str]', S: str) -> str:
        trie, n, intervals, res = {}, len(S), [], ""

        # create trie tree
        for w in words:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 0

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, j, max_end = trie, i, None
            for j in range(i, n):
                if S[j] not in cur:
                    break
                cur = cur[S[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += S[prev_end:start] + '<b>' + S[start:end] + "</b>"
            prev_end = end
        return res + S[prev_end:]
