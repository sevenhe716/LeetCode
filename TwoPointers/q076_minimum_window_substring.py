# Time:  O(n)
# Space: O(1)

# 解题思路：
# O(n)的时间复杂度，线性扫描
# 记录索引位置？动态规划？滑动窗口？
# 一个思路是：标记出T中字符的所有索引位置
# 另一个思路是双指针滑动窗口
# 优化思路：每次比较完整的计数器效率太低，可以只记录变化时，当计数器相等时+1，小于时-1，时间复杂度从m1*n减少n (m1代表t中不重复的元素个数)
# 优化思路：过滤掉T中不存在的元素，保留key和index的键值对


from collections import Counter
from collections import defaultdict


class Solution:
    # 标记所有的索引位置，利用有序字典排序，每次取最小的索引，然后加入最小字母的下一个索引
    # 还需要得知当前的最小最大值，但维护此结构的开销过大
    # def minWindow(self, s: 'str', t: 'str') -> 'str':
    #     index = {c: [] for c in t}
    #     for i, c in enumerate(s):
    #         if c in t:
    #             index[c].append(i)
    #
    #     if any(not v for v in index.values()):
    #         return ''
    #
    #     window = {c: c[0] for c in index}
    #
    #     min_dist =
    #     c = min(window.keys(), key=window.get)

    def minWindow1(self, s: 'str', t: 'str') -> 'str':
        cnt_t = Counter(t)
        cnt = {c: 0 for c in t}
        n = len(s)
        min_dist, min_left, min_right = 2147483647, 0, 0

        # find first
        for i, c in enumerate(s):
            if c in cnt_t:
                left, right = i, i + 1
                cnt[c] += 1
                break
        else:
            return ''

        while right <= n:
            # 右侧延伸到合法的窗口区间
            # 优化：这种比较效率非常低，每次都要遍历整个字典，可以用一个计数器维护临界条件即可
            while any(v < cnt_t[k] for k, v in cnt.items()):
                if right >= n:
                    return s[min_left:min_right]
                if s[right] in cnt:
                    cnt[s[right]] += 1
                right += 1

            # 比较当前窗口是否是最小窗口
            if right - left < min_dist:
                min_dist = right - left
                min_left, min_right = left, right

            cnt[s[left]] -= 1
            left += 1
            if left >= right:
                return s[min_left:min_right]

            # 移除最左侧的字符
            while s[left] not in cnt:
                left += 1
                if left >= right:
                    return s[min_left:min_right]

        return s[min_left:min_right]

    def minWindow(self, s: 'str', t: 'str') -> 'str':
        if not t or not s:
            return ""

        cnt_t = Counter(t)
        cnt = {c: 0 for c in t}
        left, right, formed, required = 0, 0, 0, len(cnt_t)
        # python的动态类型
        ans = float('inf'), None, None

        # 过滤掉无用元素，减少遍历成本，空间换时间
        filter_s = []
        for i, c in enumerate(s):
            if c in cnt_t:
                filter_s.append((i, c))

        while right < len(filter_s):
            # 结束位置向右延展一步
            char = filter_s[right][1]
            cnt[char] += 1
            if cnt[char] == cnt_t[char]:
                formed += 1

            # 起始位置向右直到不满足窗口条件
            while left <= right and formed == required:
                char = filter_s[left][1]

                start, end = filter_s[left][0], filter_s[right][0]
                # 记录当前最小窗口
                if end - start + 1 < ans[0]:
                    ans = end - start + 1, start, end
                cnt[char] -= 1
                if cnt[char] < cnt_t[char]:
                    formed -= 1
                left += 1
            right += 1

        return s[ans[1]:ans[2] + 1] if ans[0] != float('inf') else ''


class Solution1:
    # 用mem统一处理在t中和不在t中的字符，通过mem跟0比较以及t_len来判断，非常巧妙的做法
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        mem = defaultdict(int)
        for c in t:
            mem[c] += 1
        t_len = len(t)

        minL, minR = 0, float('inf')
        l = 0

        for i, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1

            mem[c] -= 1

            # 当成为合法窗口时，移动左指针
            if t_len == 0:
                # 移动左指针，直到得到最小的窗口
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1

                if i - l < minR - minL:
                    minR, minL = i, l

                # 左指针再移动一格，让右指针再次寻找合法的窗口
                mem[s[l]] += 1
                t_len += 1
                l += 1
        return '' if minR == float('inf') else s[minL:minR + 1]
