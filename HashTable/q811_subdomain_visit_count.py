# Time:  O(n)
# Space: O(1)

# 解题思路：
# 计数器
from collections import defaultdict


class Solution:
    # either 1 or 2 '.'
    def subdomainVisits(self, cpdomains: 'List[str]') -> 'List[str]':
        res = defaultdict(int)
        for cp in cpdomains:
            cnt_str, domain = cp.split(' ')
            count = int(cnt_str)
            res[domain] += count
            index = domain.find('.')
            res[domain[index + 1:]] += count
            index = domain.find('.', index+1)
            if index != -1:
                res[domain[index + 1:]] += count
        return ['{} {}'.format(cnt, domain) for domain, cnt in res.items()]


class Solution1(object):
    def subdomainVisits(self, cpdomains):
        ans = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                # 借鉴这种写法，扩展性更强
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]