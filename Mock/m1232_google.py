# Time:  O(nlogn)
# Space: O(n)

# Ideas:
# do indexes in order? I will treat it as in order, test case tell me not
# Replace S from right to left


class Solution:
    def findReplaceString(self, S: str, indexes: 'List[int]', sources: 'List[str]', targets: 'List[str]') -> str:
        offset = 0
        for idx, src, tar in sorted(zip(indexes, sources, targets), key=lambda x:x[0]):
            start = idx + offset
            if S.startswith(src, start):
                # replace
                S = S[:start] + tar + S[len(src) + start:]
                offset += len(tar) - len(src)
        return S


class Solution1:
    def findReplaceString(self, S, indexes, sources, targets):
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S