# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            idx = local.find('+')
            if idx != -1:
                local = local[:idx]
            res.add(local + '@' + domain)
        return len(res)
