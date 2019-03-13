# Time:  O(n)
# Space: O(k)

# 解题思路：
# 借鉴字符串匹配的优化思维，用p长度的窗口滑动扫描，当第i个字符出现不在p中时，可以直接跳到i+1，当字符k在p中，但已经用完时，
# 可以跳过到窗口中字符k的第一个位置之后，否则当匹配完成时，+1，然后右移，右移时，更新元素的计数。
# 从后往前扫描，效率更高
# 这种解法虽然比逐个扫描跳过了很多元素，但是counter的重赋值本身的开销也和逐个扫描差不多，除非p很长或包含了大量重复的元素
# The keypoint of this solution: speed up scan process by skip letters as much as possible, it is faster than one-step scanning when p is long.
# Instead of scaning letters one by one, when match failed I try to skip letters as many as possible like KMP algorithm (at this point).
#
# Same as other solution, we maintain start and end two pointers and a hashmap counter. And scan forward and scan backward alternately.
# First we scan backward, because if we find a invalid word, we can jump all the words before it.
#
# scan_backfoward(end):
# Scan from end to start
#
# If counter[s[i]] == 0, jump all the words before it, and scan forward start from i + 1: scan_foward(i + 1, end)
# If all the letters matched, jump to match_success(end)
# scan_forward(start, end):
# Now we have matched from start to end, and need continue to match from end to start+len(p):
#
# If mismatched jump to match_failed(start, i)
# If all mached jump to match_success(start+len(p))
# match_success(end):
# First add start index to results, and check if s[start] == s[end]. If matched, also add start+1 to results , move pointers one step and repeat this process. when not matched, jump to match_failed(start, end)
#
# match_failed(start, end):
# There are two situations:
#
# If letter s[i] not in p, We skip all the words before it and scan backward start from i+1: scan_backward(i + 1 + len(p))
# If letter s[i] in p but use out, We find the first letter equal to it and scan forward start from this index+1: scan_foward(index + 1, end + 1)
from collections import Counter


class Solution:
    def findAnagrams1(self, s: str, p: str) -> 'List[int]':
        p_counter = Counter(p)
        n, k, self.res = len(s), len(p), []
        if k > n: return []

        def scan_backward(end):
            # reach the end
            if end > n:
                return
            # reset the counter
            self.counter = Counter(p_counter)
            # scan from end to start
            for i in range(end - k, end)[::-1]:
                # if not matched, skip all the words before i to speed up
                if self.counter[s[i]] == 0:
                    scan_forward(i + 1, end)
                    return
                else:
                    self.counter[s[i]] -= 1
                # jump to match_success
            match_success(end)

        def scan_forward(start, end):
            # reach the end
            if start + k > n:
                return
            # now we have matched from start to end, and need continue to match from end to start+len(p):
            for i in range(end, start + k):
                # if not in p or use out, jump to match_failed
                if self.counter[s[i]] == 0:
                    match_failed(start, i)
                    return
                else:
                    self.counter[s[i]] -= 1
            # jump to match_sucess
            match_success(start + k)

        def match_success(end):
            # add start index to results
            self.res.append(end - k)
            # if s[stat] == s[end], also add to results and move on, continue this process
            while end < len(s) and s[end] == s[end - k]:
                end += 1
                self.res.append(end - k)
            # reach the end
            if end == len(s):
                return
            # s[start] != s[end], jump to match_failed
            match_failed(end - k, end)

        def match_failed(start, end):
            # if s[i] not in p, we skip all the words before it and scan backward start from i+1
            if s[end] not in p_counter:
                scan_backward(end + k + 1)
            # letter s[i] in p but use out, we find the first letter equal to it and scan forward start from this index+1
            else:
                for i in range(start, end):
                    if s[i] != s[end]:
                        self.counter[s[i]] += 1
                    else:
                        scan_forward(i + 1, end + 1)
                        return

        scan_backward(k)
        return self.res

    # substring template
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []
        counter = Counter(p)
        count, start, end, res = len_p, 0, 0, []

        while end < len_s:
            # 只有当p中的字符匹配时，计数器才减1
            if counter[s[end]] >= 1:
                count -= 1
            counter[s[end]] -= 1
            end += 1

            if count == 0:
                res.append(start)

            if end - start == len_p:
                # 排除掉p以外的字符，p以外的字符为负
                if counter[s[start]] >= 0:
                    count += 1
                counter[s[start]] += 1
                start += 1
        return res


# 最快的方法，直接利用哈希值
class Solution1:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        len_p = len(p)
        if not s or len(s) < len_p:
            return []
        ans = []
        hs, hp = 0, 0
        for i in range(len_p):
            hs += hash(s[i])
            hp += hash(p[i])
        if hs == hp:
            ans.append(0)
        for right in range(len_p, len(s)):
            left = right - len_p
            hs += hash(s[right]) - hash(s[left])
            if hs == hp:
                ans.append(left + 1)
        return ans
