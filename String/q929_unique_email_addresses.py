# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> int:
        res = set()
        for email in emails:
            # 可以考虑用split
            at_index = email.find('@')
            # domain include @
            local, domain = email[:at_index].replace('.', ''), email[at_index:]
            index = local.find('+')
            if index != -1:
                local = local[:index]
            res.add(local + domain)
        return len(res)


class Solution1:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        def identify_email_id(email) -> str:
            at_idx = email.find('@')
            local_name, domain_name = email[:at_idx], email[at_idx:]
            plus_idx = local_name.find('+')
            if plus_idx != -1:
                local_name = local_name[:plus_idx]
            return local_name.replace('.', '') + domain_name

        return len(set(map(identify_email_id, emails)))

