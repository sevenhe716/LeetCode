# Time:  O(n)
# Space: O(1)

# 解题思路：
# 正则表达式匹配并替换即可


class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """

        index = S.find('@')

        if index != -1:
            # return S[0].lower() + "*****" + S[index - 1:].lower()           # format更好
            return "{}*****{}".format(S[0].lower(), S[index - 1:].lower())
        else:
            S = S.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')

            if len(S) == 10:
                return '***-***-{}'.format(S[-4:])
            elif len(S) > 10:
                return '+{}-***-***-{}'.format('*' * (len(S) - 10), S[-4:])


class Solution1(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            first, after = S.split('@')
            return "{}*****{}@{}".format(first[0], first[-1], after).lower()    # str concat format的写法

        digits = filter(lambda x: x.isdigit(), S)
        local = "***-***-{}".format(digits[-4:])
        if len(digits) == 10:
            return local
        return "+{}-{}".format('*' * (len(digits) - 10), local)


class SolutionF:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        import re

        if '@' in S:
            s = S.lower()
            s1 = re.findall(r".*(.@.*)", s)
            s = str(s[:1]) + "*****" + "".join(s1)
        else:
            s = [x for x in S if x.isdigit()]       # isdigit better than replace
            cmj = []
            if len(s) > 10:
                cmj = ['+'] + ['*'] * (len(s) - 10) + ['-']
            s1 = "".join(cmj)
            s1 = s1 + "***-***-"
            s1 = s1 + "".join(s[-4:])
            s = s1
        return s

# We are given a personal information string S, which may represent either an email address or a phone number.
#
# We would like to mask this personal information according to the following rules:
#
# 1. Email address:
#
# We define a name to be a string of length ≥ 2 consisting of only lowercase letters a-z or uppercase letters A-Z.
#
# An email address starts with a name, followed by the symbol '@', followed by a name, followed by the dot '.' and followed by a name.
#
# All email addresses are guaranteed to be valid and in the format of "name1@name2.name3".
#
# To mask an email, all names must be converted to lowercase and all letters between the first and last letter of the first name must be replaced by 5 asterisks '*'.
#
# 2. Phone number:
#
# A phone number is a string consisting of only the digits 0-9 or the characters from the set {'+', '-', '(', ')', ' '}. You may assume a phone number contains 10 to 13 digits.
#
# The last 10 digits make up the local number, while the digits before those make up the country code. Note that the country code is optional. We want to expose only the last 4 digits and mask all other digits.
#
# The local number should be formatted and masked as "***-***-1111", where 1 represents the exposed digits.
#
# To mask a phone number with country code like "+111 111 111 1111", we write it in the form "+***-***-***-1111".  The '+' sign and the first '-' sign before the local number should only exist if there is a country code.  For example, a 12 digit phone number mask should start with "+**-".
#
# Note that extraneous characters like "(", ")", " ", as well as extra dashes or plus signs not part of the above formatting scheme should be removed.
#
# Return the correct "mask" of the information provided.
