# Time:  O(nlogn)
# Space: O(n)

# Ideas:
# do indexes in order? I will treat it as in order, test case tell me not


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

    # first flag all index to replace
    # def findReplaceString(self, S: str, indexes: 'List[int]', sources: 'List[str]', targets: 'List[str]') -> str:
    #     idxs = []
    #     for i, idx in enumerate(indexes):
    #         if S.startswith(sources[i], idx):
    #             idxs.append(i)
    #
    #     idxs.sort()
    #     offset = 0
    #     for i in idxs:
    #         S = S[:indexes[i]] + targets[i] + S[indexes[i]:]
    #         offset += len(targets)
    #
    #     return S
